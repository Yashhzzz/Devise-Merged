"""Shared HTTP client module for Devise Desktop Agent.

Provides a centralized HTTP client with authentication and retry logic
for backend communication (tamper alerts, gap events, etc.).
"""

import logging
from typing import Optional, Dict, Any

import httpx


logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10.0
DEFAULT_BACKOFF = [30, 60, 120, 300]
MAX_RETRIES = 4


class HttpClient:
    """Shared async HTTP client with auth and retry support."""

    def __init__(
        self,
        base_url: str = "",
        api_key: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT,
        backoff_intervals: Optional[list] = None,
    ):
        """Initialize HTTP client.

        Args:
            base_url: Base URL for requests
            api_key: API key for authorization header
            timeout: Request timeout in seconds
            backoff_intervals: Custom backoff intervals for retries
        """
        self._base_url = base_url.rstrip("/") if base_url else ""
        self._api_key = api_key
        self._timeout = timeout
        self._backoff = backoff_intervals or DEFAULT_BACKOFF
        self._client: Optional[httpx.AsyncClient] = None

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self._client is None:
            headers = {"Content-Type": "application/json"}
            if self._api_key:
                headers["Authorization"] = f"Bearer {self._api_key}"
            self._client = httpx.AsyncClient(
                timeout=self._timeout,
                headers=headers,
            )
        return self._client

    async def post(
        self,
        endpoint: str,
        payload: Dict[str, Any],
        require_success: bool = True,
    ) -> Optional[httpx.Response]:
        """Send POST request with retry logic.

        Args:
            endpoint: API endpoint path (appended to base_url)
            payload: JSON payload
            require_success: If True, return None on failure

        Returns:
            Response object if successful (or if require_success=False), None on failure
        """
        url = (
            f"{self._base_url}{endpoint}"
            if endpoint.startswith("/")
            else f"{self._base_url}/{endpoint}"
        )
        client = await self._get_client()

        for attempt in range(MAX_RETRIES + 1):
            try:
                response = await client.post(url, json=payload)

                if response.status_code == 401:
                    logger.warning("Got 401, attempting to refresh auth...")
                    if attempt < MAX_RETRIES:
                        continue

                if require_success:
                    response.raise_for_status()

                logger.debug(f"POST {url} -> {response.status_code}")
                return response

            except httpx.HTTPStatusError as e:
                if (
                    400 <= e.response.status_code < 500
                    and e.response.status_code != 401
                ):
                    logger.warning(
                        f"Client error {e.response.status_code}: {e.response.text[:200]}"
                    )
                    return None
                logger.warning(
                    f"Server error (attempt {attempt + 1}): {e.response.status_code}"
                )
            except httpx.RequestError as e:
                logger.warning(f"Network error (attempt {attempt + 1}): {e}")
            except Exception as e:
                logger.warning(f"Unexpected error (attempt {attempt + 1}): {e}")

            if attempt < MAX_RETRIES:
                backoff = self._backoff[attempt]
                logger.info(f"Retrying in {backoff}s...")
                import asyncio

                await asyncio.sleep(backoff)

        return None

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None


def create_http_client(
    base_url: str = "",
    api_key: Optional[str] = None,
    timeout: float = DEFAULT_TIMEOUT,
) -> HttpClient:
    """Create an HTTP client instance.

    Args:
        base_url: Base URL for requests
        api_key: API key for authorization
        timeout: Request timeout

    Returns:
        HttpClient instance
    """
    return HttpClient(base_url=base_url, api_key=api_key, timeout=timeout)
