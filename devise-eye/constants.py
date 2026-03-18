"""Constants module for Devise Desktop Agent.

Centralizes all magic numbers and configuration constants.
"""

# Detection defaults
DEFAULT_POLL_INTERVAL = 30  # seconds between detection cycles
DEFAULT_DEDUP_WINDOW = 300  # seconds before connection key expires

# Scheduling intervals (in poll intervals)
HEARTBEAT_INTERVAL_COUNT = 10  # ~5 minutes (10 * 30s)
CONFIG_CHECK_INTERVAL_COUNT = 10  # ~5 minutes (10 * 30s)

# Retry configuration
MAX_RETRIES = 4
BACKOFF_INTERVALS = [30, 60, 120, 300]  # seconds

# Firestore configuration
FIRESTORE_BASE_URL = "https://firestore.googleapis.com/v1"
FIRESTORE_TIMEOUT = 10.0
FIRESTORE_BATCH_SIZE = 100

# Default paths
DEFAULT_SERVICE_ACCOUNT_PATH = r"C:\ProgramData\Devise\service_account.json"
DEFAULT_FALLBACK_PROJECT_ID = "dev-project"
DEFAULT_FALLBACK_ORG_ID = "local-org"

# Queue configuration
DEFAULT_QUEUE_ENCRYPTION = True

# Frequency thresholds
HIGH_FREQUENCY_THRESHOLD = 10  # connections per 5 minutes
