"""HTTP reporter module for Devise Desktop Agent.

Writes events directly to Firestore REST API using Google service account
OAuth2 credentials. Falls back to offline queue on failure.
"""

import asyncio
import json
import logging
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

import httpx


logger = logging.getLogger(__name__)

# Backoff intervals in seconds
BACKOFF_INTERVALS = [30, 60, 120, 300]
MAX_RETRIES = 4
BATCH_SIZE = 100


def dict_to_firestore_fields(d: dict) -> dict:
    """Convert a Python dict to Firestore REST typed fields format."""
    fields = {}
    for key, value in d.items():
        if value is None:
            fields[key] = {"nullValue": None}
        elif isinstance(value, bool):
            fields[key] = {"booleanValue": value}
        elif isinstance(value, int):
            fields[key] = {"integerValue": str(value)}
        elif isinstance(value, float):
            fields[key] = {"doubleValue": value}
        elif isinstance(value, str):
            fields[key] = {"stringValue": value}
        elif isinstance(value, dict):
            fields[key] = {"mapValue": {"fields": dict_to_firestore_fields(value)}}
        elif isinstance(value, list):
            arr_values = []
            for item in value:
                if item is None:
                    arr_values.append({"nullValue": None})
                elif isinstance(item, bool):
                    arr_values.append({"booleanValue": item})
                elif isinstance(item, int):
                    arr_values.append({"integerValue": str(item)})
                elif isinstance(item, float):
                    arr_values.append({"doubleValue": item})
                elif isinstance(item, str):
                    arr_values.append({"stringValue": item})
            fields[key] = {"arrayValue": {"values": arr_values}}
        elif hasattr(value, 'isoformat'):
            ts_str = value.strftime("%Y-%m-%dT%H:%M:%S") + ".%03dZ" % (value.microsecond // 1000)
            fields[key] = {"timestampValue": ts_str}
        else:
            fields[key] = {"stringValue": str(value)}
    return fields


class FirestoreReporter:
    """Reports events to Firestore REST API via service account auth."""

    FIRESTORE_BASE = "https://firestore.googleapis.com/v1"
    OAUTH_SCOPE = "https://www.googleapis.com/auth/datastore"

    def __init__(
        self,
        project_id: str,
        service_account_path: str,
        timeout: float = 10.0,
        queue=None,
    ):
        self._project_id = project_id
        self._service_account_path = service_account_path
        self._timeout = timeout
        self._queue = queue
        self._client: Optional[httpx.AsyncClient] = None
        self._credentials = None

    def _load_credentials(self):
        """Load and cache Google service account credentials."""
        if self._credentials is not None:
            return
        try:
            from google.oauth2 import service_account
            self._credentials = service_account.Credentials.from_service_account_file(
                self._service_account_path,
                scopes=[self.OAUTH_SCOPE],
            )
            logger.info("Service account credentials loaded successfully")
        except ImportError:
            raise RuntimeError("google-auth not installed. Run: pip install google-auth")
        except FileNotFoundError:
            raise RuntimeError(f"Service account file not found: {self._service_account_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to load service account: {e}")

    def _get_access_token(self) -> str:
        """Get a valid OAuth2 access token, refreshing if expired."""
        self._load_credentials()
        now = datetime.utcnow().replace(tzinfo=None)
        creds = self._credentials
        if (
            creds.token is not None
            and creds.expiry is not None
            and creds.expiry.replace(tzinfo=None) > now
        ):
            return creds.token

        import google.auth.transport.requests
        import requests as google_requests
        request = google.auth.transport.requests.Request(session=google_requests.Session())
        creds.refresh(request)
        logger.debug("OAuth2 access token refreshed")
        return creds.token

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create async HTTP client with current auth token."""
        token = self._get_access_token()
        if self._client is not None:
            await self._client.aclose()
        self._client = httpx.AsyncClient(
            timeout=self._timeout,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        return self._client

    def _build_collection_url(self, collection: str) -> str:
        return (
            f"{self.FIRESTORE_BASE}/projects/{self._project_id}"
            f"/databases/(default)/documents/{collection}"
        )

    async def _write_to_firestore(self, event: Dict[str, Any], collection: str = "detection_events") -> bool:
        url = self._build_collection_url(collection)
        body = {"fields": dict_to_firestore_fields(event)}

        for attempt in range(MAX_RETRIES + 1):
            try:
                client = await self._get_client()
                response = await client.post(url, json=body)

                if response.status_code == 401:
                    logger.warning("Firestore auth 401, refreshing token...")
                    self._credentials.token = None
                    if attempt < MAX_RETRIES:
                        continue

                response.raise_for_status()
                logger.debug(f"Firestore write OK: {response.status_code}")
                return True

            except httpx.HTTPStatusError as e:
                if 400 <= e.response.status_code < 500 and e.response.status_code != 401:
                    logger.warning(f"Firestore client error {e.response.status_code}: {e.response.text[:200]}")
                    return False
                logger.warning(f"Firestore server error (attempt {attempt + 1}): {e.response.status_code}")
            except httpx.RequestError as e:
                logger.warning(f"Network error (attempt {attempt + 1}): {e}")
            except Exception as e:
                logger.warning(f"Unexpected error (attempt {attempt + 1}): {e}")

            if attempt < MAX_RETRIES:
                backoff = BACKOFF_INTERVALS[attempt]
                logger.info(f"Retrying in {backoff}s...")
                await asyncio.sleep(backoff)

        return False

    def set_queue(self, queue) -> None:
        self._queue = queue

    async def report_event(self, event: Dict[str, Any], collection: str = "detection_events") -> bool:
        success = await self._write_to_firestore(event, collection)
        if not success:
            if self._queue:
                logger.info("Firestore write failed — queueing event for later")
                self._queue.enqueue(event)
            else:
                logger.warning("Firestore write failed and no queue configured")
            return False
        return True

    async def report_events(self, events: List[Dict[str, Any]]) -> Dict[str, int]:
        results = {"success": 0, "failure": 0}
        for event in events:
            if await self.report_event(event):
                results["success"] += 1
            else:
                results["failure"] += 1
        return results

    async def flush_queue(self) -> Dict[str, int]:
        if not self._queue:
            return {"success": 0, "failure": 0, "skipped": 0}
        results = {"success": 0, "failure": 0, "skipped": 0}
        pending = self._queue.get_pending(limit=BATCH_SIZE)
        if not pending:
            return results
        logger.info(f"Flushing {len(pending)} queued events to Firestore")
        success_ids, failed_ids = [], []
        for event in pending:
            queue_id = event.get("_queue_id")
            if await self.report_event(event):
                if queue_id: success_ids.append(queue_id)
                results["success"] += 1
            else:
                if queue_id: failed_ids.append(queue_id)
                results["failure"] += 1
        if success_ids: self._queue.mark_success(success_ids)
        if failed_ids: self._queue.mark_failed(failed_ids)
        return results

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "FirestoreReporter":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()


# Alias for compatibility
Reporter = FirestoreReporter


def create_reporter(
    endpoint: str = "",
    timeout: float = 10.0,
    queue=None,
    # Keep legacy and new args flexible
    api_key: str = "",
    project_id: str = "",
    service_account_path: str = "",
) -> FirestoreReporter:
    """Create a Firestore reporter instance."""
    return FirestoreReporter(
        project_id=project_id,
        service_account_path=service_account_path,
        timeout=timeout,
        queue=queue,
    )
