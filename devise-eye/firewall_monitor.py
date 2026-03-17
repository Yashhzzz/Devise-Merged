"""Firewall monitor for filtering blocklisted connections.

Polls Firestore for organization firewall rules and ensures blocklisted
domains/IPs are rejected locally via Windows Filtering Platform (WFP)
or simply drops events before processing.
"""

import logging
import threading
import time
from typing import Dict, Any, Optional
import google.auth
from google.auth.transport.requests import Request as GoogleAuthRequest
import httpx


logger = logging.getLogger(__name__)


class FirewallMonitor:
    """Monitors and enforces organization firewall rules."""

    def __init__(self, project_id: str, org_id: str, service_account_path: str, poll_interval: int = 300):
        """Initialize FirewallMonitor.
        
        Args:
            project_id: Firebase project ID
            org_id: Organization ID
            service_account_path: Path to service account JSON
            poll_interval: How often to poll Firestore for rule changes (seconds)
        """
        self._project_id = project_id
        self._org_id = org_id
        self._service_account_path = service_account_path
        self._poll_interval = poll_interval
        
        # Firestore REST API base URL
        self._base_url = f"https://firestore.googleapis.com/v1/projects/{self._project_id}/databases/(default)/documents"
        self._auth_req = GoogleAuthRequest()
        self._credentials = self._load_credentials()
        self._access_token = None
        self._token_expiry = 0
        
        self._rules: Dict[str, str] = {}  # domain -> "allow" | "block"
        
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def _load_credentials(self):
        """Load Google service account credentials."""
        try:
            creds, _ = google.auth.load_credentials_from_file(
                self._service_account_path,
                scopes=["https://www.googleapis.com/auth/datastore"]
            )
            return creds
        except Exception as e:
            logger.error(f"Failed to load credentials for firewall monitor: {e}")
            return None

    def _get_access_token(self) -> Optional[str]:
        """Get or refresh OAuth2 token."""
        if not self._credentials:
            return None

        current_time = time.time()
        # Refresh if token is missing or expires in less than 5 minutes (300 seconds)
        if not self._access_token or (self._token_expiry - current_time) < 300:
            try:
                self._credentials.refresh(self._auth_req)
                self._access_token = self._credentials.token
                # Google tokens usually live for 1 hour
                self._token_expiry = current_time + 3600
                logger.debug("Refreshed OAuth2 token for firewall monitor.")
            except Exception as e:
                logger.error(f"Failed to refresh OAuth2 token: {e}")
                return None
        return self._access_token

    def _poll_rules(self):
        """Fetch firewall rules from Firestore."""
        token = self._get_access_token()
        if not token:
            logger.warning("No auth token available, skipping firewall rule poll.")
            return

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # We query the `org_settings/{orgId}/firewall_rules` collection
        url = f"{self._base_url}/org_settings/{self._org_id}/firewall_rules"
        
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    new_rules = {}
                    
                    documents = data.get("documents", [])
                    for doc in documents:
                        # doc["name"] format: projects/PID/databases/(default)/documents/org_settings/ORGID/firewall_rules/RULE_ID
                        # Assuming documents contain fields `domain` (string) and `action` (string "allow" or "block")
                        fields = doc.get("fields", {})
                        domain = fields.get("domain", {}).get("stringValue")
                        action = fields.get("action", {}).get("stringValue")
                        
                        if domain and action:
                            new_rules[domain.lower()] = action.lower()
                            
                    self._rules = new_rules
                    logger.info(f"Updated local firewall rules: {len(self._rules)} rules loaded.")
                elif response.status_code == 404:
                     logger.debug("No firewall rules collection found. Starting with empty ruleset.")
                     self._rules = {}
                else:
                    logger.error(f"Failed to fetch firewall rules: {response.status_code} - {response.text}")
                    
        except Exception as e:
             logger.error(f"Exception while polling firewall rules: {e}")

    def _monitor_loop(self):
        """Main loop for polling rules."""
        logger.info("Firewall monitor started.")
        # Perform initial poll immediately
        self._poll_rules()

        while not self._stop_event.is_set():
            # Wait with interruptable sleep
            if self._stop_event.wait(self._poll_interval):
                break
            self._poll_rules()
            
        logger.info("Firewall monitor stopped.")

    def start(self):
        """Start the monitor thread."""
        if self._thread and self._thread.is_alive():
            return
            
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the monitor thread."""
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=5.0)

    def is_blocked(self, domain: str) -> bool:
        """Check if a domain is blocklisted.
        
        Args:
            domain: The domain to check
            
        Returns:
            True if the domain is explicitly blocked, False otherwise.
        """
        if not domain:
            return False
            
        # Optional: Implement sub-domain wildcards (e.g. *.chatgpt.com)
        domain = domain.lower()
        
        # Explicit block wins
        if self._rules.get(domain) == "block":
            return True
            
        # Check for wildcard matches (if rule is "chatgpt.com", block "api.chatgpt.com")
        for rule_domain, action in self._rules.items():
            if action == "block" and (domain.endswith(f".{rule_domain}") or domain == rule_domain):
                 return True
                 
        return False


def create_firewall_monitor(project_id: str, org_id: str, service_account_path: str, poll_interval: int = 300) -> FirewallMonitor:
    """Create a firewall monitor instance.
    
    Args:
        project_id: Firebase project ID
        org_id: Organization ID
        service_account_path: Path to service account JSON
        poll_interval: Seconds between polls
        
    Returns:
        FirewallMonitor instance
    """
    return FirewallMonitor(project_id, org_id, service_account_path, poll_interval)
