# COMPREHENSIVE CODEBASE DUMP FOR CURSOR

## 1. Directory Structure

### devise-eye/
├── .gitignore
├── __init__.py
├── build-arm64.spec
├── build-x86_64.spec
├── build.spec
├── config.py
├── context.md
├── data
│   ├── ai_tools_registry.json
│   ├── binary_hash.txt
│   └── cdn_ip_ranges.json
├── debug_orgs.py
├── deduplicator.py
├── detector.py
├── diag_event.py
├── dns_resolver.py
├── doh_resolver.py
├── event_builder.py
├── event_queue.py
├── fetch_latest_data.py
├── firewall_monitor.py
├── frequency_tracker.py
├── generate_traffic.py
├── generate_traffic_fast.py
├── heartbeat.py
├── identity.py
├── implementation_context.md
├── installers
│   ├── linux
│   │   ├── devise-agent.service
│   │   └── install.sh
│   ├── macos
│   │   └── com.devise.agent.plist
│   └── windows
│       ├── install-service.ps1
│       └── uninstall-service.ps1
├── list_all_profiles.py
├── liveness_monitor.py
├── main.py
├── process_resolver.py
├── registry.py
├── reporter.py
├── requirements.txt
├── scripts
│   └── create_config.py
├── sensitivity_monitor.py
└── tamper_guard.py

### devise-iris/


## 2. File Contents


### File: devise-eye\.gitignore
```gitignore
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.mypy_cache/
.pytest_cache/
.coverage
htmlcov/

```


### File: devise-eye\build-arm64.spec
```spec
# -*- mode: python ; coding: utf-8 -*-
# Build spec for arm64 (Apple Silicon / ARM 64-bit) architecture

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/ai_tools_registry.json', 'data'),
        ('data/binary_hash.txt', 'data'),
        ('installers/linux', 'installers/linux'),
    ],
    hiddenimports=[
        'psutil',
        'dnspython',
        'httpx',
        'APScheduler',
        'keyring',
        'keyring.backends',
        'keyring.backends.SecretService',
        'keyring.backends.Windows',
        'keyring.backends.macOS',
        'pysqlcipher3',
        'doh_resolver',
        'frequency_tracker',
        'tamper_guard',
        'liveness_monitor',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='devise-agent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
)

```


### File: devise-eye\build-x86_64.spec
```spec
# -*- mode: python ; coding: utf-8 -*-
# Build spec for x86_64 (Intel/AMD 64-bit) architecture

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/ai_tools_registry.json', 'data'),
        ('data/binary_hash.txt', 'data'),
        ('installers/linux', 'installers/linux'),
    ],
    hiddenimports=[
        'psutil',
        'dnspython',
        'httpx',
        'APScheduler',
        'keyring',
        'keyring.backends',
        'keyring.backends.SecretService',
        'keyring.backends.Windows',
        'keyring.backends.macOS',
        'pysqlcipher3',
        'doh_resolver',
        'frequency_tracker',
        'tamper_guard',
        'liveness_monitor',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='devise-agent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='x86_64',
    codesign_identity=None,
    entitlements_file=None,
)

```


### File: devise-eye\build.spec
```spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/ai_tools_registry.json', 'data'),
    ],
    hiddenimports=[
        'psutil',
        'dnspython',
        'httpx',
        'APScheduler',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DeviseEye',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

```


### File: devise-eye\config.py
```py
"""Configuration management for Devise Desktop Agent.

Provides local and remote configuration with polling.
"""

import json
import logging
import os
import platform
from pathlib import Path
from typing import Any, Dict, Optional


logger = logging.getLogger(__name__)


class Config:
    """Configuration manager for Devise Agent with remote config support."""

    DEFAULT_CONFIG_LOCATIONS = {
        "Windows": r"C:\ProgramData\Devise\config.json",
        "Darwin": "/Library/Application Support/Devise/config.json",
        "Linux": "/etc/devise/config.json",
    }

    DEFAULT_BACKEND_URL = "https://api.devise.example.com"
    DEFAULT_POLL_INTERVAL = 30  # seconds
    DEFAULT_CONFIG_POLL_INTERVAL = 1800  # 30 minutes
    DEFAULT_HEARTBEAT_INTERVAL = 300  # 5 minutes

    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration.

        Args:
            config_path: Optional custom config file path
        """
        self._config: Dict[str, Any] = {}
        self._config_path = config_path or self._get_default_config_path()
        self._remote_config: Dict[str, Any] = {}
        self._load_config()

    def _get_default_config_path(self) -> str:
        """Get platform-specific default config path."""
        system = platform.system()
        return self.DEFAULT_CONFIG_LOCATIONS.get(system, "/etc/devise/config.json")

    def _load_config(self) -> None:
        """Load configuration from file."""
        if os.path.exists(self._config_path):
            try:
                with open(self._config_path, "r") as f:
                    self._config = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._config = {}
        else:
            self._config = {}

    def _get(self, key: str, default: Any = None) -> Any:
        """Get config value, checking remote config first.

        Args:
            key: Config key
            default: Default value if not found

        Returns:
            Config value
        """
        # Check remote config first (has priority)
        if key in self._remote_config:
            return self._remote_config[key]

        # Fall back to local config
        return self._config.get(key, default)

    def update_remote_config(self, remote_config: Dict[str, Any]) -> None:
        """Update remote configuration.

        Args:
            remote_config: Remote configuration dict
        """
        old_config = self._remote_config.copy()
        self._remote_config = remote_config

        # Log changes
        for key, value in remote_config.items():
            if old_config.get(key) != value:
                logger.info(f"Remote config updated: {key} = {value}")

    @property
    def api_key(self) -> Optional[str]:
        """Get device API key from config."""
        return self._get("api_key")

    @property
    def firebase_project_id(self) -> Optional[str]:
        """Get Firebase project ID."""
        return self._get("firebase_project_id")

    @property
    def firebase_api_key(self) -> Optional[str]:
        """Get Firebase web API key."""
        return self._get("firebase_api_key")

    @property
    def service_account_path(self) -> Optional[str]:
        """Get path to the service account JSON file."""
        return self._get("service_account_path")

    @property
    def org_id(self) -> Optional[str]:
        """Get organization ID."""
        return self._get("org_id")

    @property
    def backend_url(self) -> str:
        """Get backend URL."""
        return self._get("backend_url", self.DEFAULT_BACKEND_URL)

    @property
    def event_endpoint(self) -> str:
        """Get full event API endpoint URL."""
        return f"{self.backend_url}/api/event"

    @property
    def registry_update_url(self) -> Optional[str]:
        """Get registry update endpoint URL."""
        return self._get("registry_update_url")

    @property
    def config_endpoint(self) -> Optional[str]:
        """Get remote config endpoint URL."""
        return self._get("config_endpoint")

    @property
    def device_id(self) -> Optional[str]:
        """Get device ID."""
        return self._get("device_id")

    @property
    def identity_config(self) -> Dict[str, Any]:
        """Get identity configuration."""
        return self._get("identity", {})

    @property
    def poll_interval(self) -> int:
        """Get polling interval in seconds."""
        return self._get("poll_interval", self.DEFAULT_POLL_INTERVAL)

    @property
    def config_poll_interval(self) -> int:
        """Get remote config polling interval in seconds."""
        return self._get("config_poll_interval", self.DEFAULT_CONFIG_POLL_INTERVAL)

    @property
    def heartbeat_interval(self) -> int:
        """Get heartbeat interval in seconds."""
        return self._get("heartbeat_interval", self.DEFAULT_HEARTBEAT_INTERVAL)

    @property
    def deduplication_window(self) -> int:
        """Get deduplication window in seconds."""
        return self._get("deduplication_window", 300)

    @property
    def debug_mode(self) -> bool:
        """Get debug mode flag."""
        return self._get("debug", False)

    @property
    def agent_version(self) -> str:
        """Get agent version."""
        return self._get("agent_version", "1.0.0")

    @property
    def remote_config_enabled(self) -> bool:
        """Check if remote config is enabled."""
        return self.config_endpoint is not None

    @property
    def doh_enabled(self) -> bool:
        """Check if DNS-over-HTTPS is enabled (default: True)."""
        return self._get("doh_enabled", True)

    def reload(self) -> None:
        """Reload configuration from disk."""
        self._load_config()


class ConfigPoller:
    """Polls remote configuration periodically."""

    def __init__(self, config: Config, device_id: str):
        """Initialize config poller.

        Args:
            config: Config instance
            device_id: Device ID for config endpoint
        """
        self._config = config
        self._device_id = device_id
        self._running = False
        self._last_config: Dict[str, Any] = {}
        self._last_fetch_time: Optional[float] = None

    async def start(self) -> None:
        """Start polling remote config."""
        if not self._config.remote_config_enabled:
            logger.debug("Remote config disabled")
            return

        self._running = True

        # Fetch initial config
        await self.fetch_config()

    async def stop(self) -> None:
        """Stop polling."""
        self._running = False

    async def fetch_config(self) -> bool:
        """Fetch remote configuration.

        Returns:
            True if config was fetched successfully
        """
        import httpx

        endpoint = self._config.config_endpoint
        if not endpoint:
            return False

        url = f"{endpoint}/{self._device_id}"

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    url,
                    headers={
                        "Authorization": f"Bearer {self._config.api_key}",
                        "Content-Type": "application/json",
                    },
                )
                response.raise_for_status()

                remote_config = response.json()
                self._config.update_remote_config(remote_config)
                self._last_config = remote_config

                import time

                self._last_fetch_time = time.time()

                logger.info(f"Remote config fetched: {len(remote_config)} keys")
                return True

        except Exception as e:
            logger.warning(f"Failed to fetch remote config: {e}")
            return False

    def should_poll(self) -> bool:
        """Check if it's time to poll for config updates.

        Returns:
            True if config should be polled
        """
        if not self._config.remote_config_enabled:
            return False

        import time

        if self._last_fetch_time is None:
            return True

        elapsed = time.time() - self._last_fetch_time
        return elapsed >= self._config.config_poll_interval


def get_config(config_path: Optional[str] = None) -> Config:
    """Get configuration instance.

    Args:
        config_path: Optional custom config file path

    Returns:
        Config instance
    """
    return Config(config_path)

```


### File: devise-eye\context.md
```md
Devise AI Governance — Complete Architecture Context
You are tasked with building the Devise Desktop Agent, a background Python script that runs on employee machines. To build this correctly, you must understand the entire end-to-end architecture of Devise, an enterprise B2B SaaS platform for AI Governance.

This document explicitly details the React frontend architecture, the complete feature set of the web dashboard, the Firebase serverless backend, and exactly how the Desktop Agent must integrate with them.

1. System Architecture Overview
Devise operates on a fully serverless, real-time architecture:

Frontend Dashboard (React SPA): Hosted on Vercel. Admins log in here to view team AI usage, configure policies, and mitigate data risks.
Backend (Firebase): Cloud Firestore acts as the central state engine. Authentication is handled by Firebase Auth.
Desktop Agent (Python): Runs locally on Windows/macOS. It monitors the OS for AI tool usage, enforces policies, detects sensitive data patterns (e.g., source code in clipboard), and pushes findings directly to Firestore.
Core Philosophy:

The Frontend NEVER talks to a traditional API server (like Node.js or Python FastAPI). It talks directly to Firestore.
The Desktop Agent NEVER talks to a traditional API server. It talks directly to Firestore using firebase-admin and a 
service-account.json
.
The two systems (Frontend & Agent) synchronize entirely by reading and writing to the same Firestore collections, relying on Firestore's real-time listeners (onSnapshot) to update instantly.
2. The Frontend Codebase (React + Vite + TypeScript)
The frontend is a modern React Single Page Application (SPA).

Tech Stack
Framework: React 18 + TypeScript + Vite
Styling: Tailwind CSS + custom glassmorphic CSS (
index.css
)
UI Components: shadcn/ui (Radix UI primitives) and Tabler/Lucide icons.
Data Fetching: @tanstack/react-query and native Firebase JS SDK.
Routing: React Router DOM (/, /login, /dashboard). Vercel is configured with a root 
vercel.json
 SPA rewrite (/(.*) -> /index.html).
Project Structure (src/)
App.tsx
: Main routing engine. Defines the 
Tab
 state for the Dashboard.
components/layout/: Holds the main structural shells: 
DashboardLayout
, 
Sidebar
, 
TopBar
.
components/dashboard/: Holds the individual feature tabs (e.g., 
FirewallTab.tsx
, 
DataRiskTab.tsx
, 
LiveFeedTab.tsx
).
pages/: Full-page routes (e.g., landing/LandingPage.tsx, auth/LoginPage.tsx).
services/api.ts
: The most critical file. Contains all Firestore wrapper functions (e.g., 
fetchBlockEvents()
, 
subscribeToHighRiskEvents()
).
Security & Multi-Tenancy
Every company using Devise is assigned an org_id upon signup. Every single document in Firestore requires an org_id field. The Frontend enforces this via Firestore Security Rules (users can only read docs matching their profile's org_id).

3. End-to-End Feature Map
When building the agent, remember that its data populates these specific frontend tabs:

A. Dashboard Overview (overview)
Shows high-level metrics: Active Agents, Time Saved, Alerts.

Agent Requirement: Writes to the heartbeats collection every 5 mins. The frontend counts unique device_ids in heartbeats to determine "Active Agents" online.
B. Live Feed (live-feed)
A real-time scrolling table of what tools are being opened right now.

Agent Requirement: When an app launches (e.g., cursor.exe, ChatGPT in Chrome), the agent writes a basic document to detection_events with event_type: "detected". The frontend listens via onSnapshot and animates these rows in.
C. AI Firewall (firewall)
Allows admins to block specific AI tools company-wide.

Frontend Logic: Admins toggle tools ALLOWED/BLOCKED. Writes to org_settings/{org_id}/firewall_rules.
Agent Requirement: Periodically fetches firewall_rules. If a user opens a blocked tool, the agent must intercept/kill it.
Agent Requirement: Write to detection_events with event_type: "blocked" and block_reason. This populates the "Block Events" table in the UI.
D. Data Risk (data-risk)
Detects sensitive data leakage (PII, source code, financial docs) into AI tools.

Frontend Logic: A feed of high-risk events, plus an "Employee Risk Leaderboard" showing who violates policies the most. High-risk events trigger real-time toast alerts on the admin's screen.
Agent Requirement: Monitors window titles and clipboard size (NOT content). If it sees an anomaly (e.g., "ChatGPT - Uploading financials.pdf" or pasting > 5000 chars), it writes to detection_events with sensitivity_flag: "FINANCIAL_KEYWORDS" and sensitivity_score: 85.
E. Team & Devices (team, devices)
Lists all employees and their laptops.

Agent Requirement: Uses local OS module (os, getpass) to capture the local Windows/Mac username and device hostname, attaching them as user_id and device_id to every event.
4. Firestore Database Schema
The Desktop Agent must write payloads exactly matching these TypeScript interfaces used by the Frontend.

Collection: heartbeats
Used to track online/offline status of employee laptops.

json
{
  "device_id": "HOSTNAME-MAC_ADDRESS",
  "org_id": "your_org_id_here",
  "user_email": "john.doe@company.com", // Or local Windows username
  "status": "active", // or "idle"
  "last_seen": "<Firestore Server Timestamp>",
  "os_version": "Windows 11",
  "agent_version": "1.0.0"
}
Collection: detection_events
The central nervous system of Devise. Used for Live Feed, Firewall Blocks, and Data Risks.

json
{
  "device_id": "HOSTNAME-MAC_ADDRESS",
  "org_id": "your_org_id_here",
  "user_id": "john.doe@company.com", 
  "tool_name": "ChatGPT",          // e.g., "Claude", "Notion AI", "Cursor"
  "domain": "chat.openai.com",     // Optional URL if intercepted via browser
  "timestamp": "<Firestore Server Timestamp>",
  
  // -- FIREWALL FIELDS --
  "event_type": "detected",        // MUST BE either "detected" or "blocked"
  "block_reason": null,            // Populate if blocked! (e.g., "Admin Policy")
  "policy_matched": "ChatGPT",     // The rule ID that caused the block
  
  // -- DATA RISK FIELDS --
  "sensitivity_flag": null,        // e.g., "SOURCE_CODE", "LARGE_PASTE", "FINANCIAL_KEYWORDS", "CREDENTIALS_PATTERN", "FILE_UPLOAD"
  "sensitivity_score": 0,          // Integer 0 to 100
  "window_title": "ChatGPT - Uploading financial_report.pdf", 
  "paste_size_chars": 5432,        // Approximate length of clipboard paste
  "file_name": "financial_report.pdf",
  "reviewed": false                // Dashboard sets this to true when admin clicks "Mark Reviewed"
}
Subcollection: org_settings/{org_id}/firewall_rules/{tool_name}
The agent READS from here to enforce blocks.

json
{
  "tool_name": "ChatGPT",
  "domain": "chat.openai.com",
  "status": "blocked", // If "blocked", the agent must intercept
  "updated_at": "<Timestamp>"
}
5. Desktop Agent Implementation Guidelines (Python)
To fulfill the requirements of the React frontend, the Python agent must follow these rules:

Libraries: Use firebase-admin (Firestore), psutil (Process enumeration/killing), pygetwindow or win32gui / AppKit (Active window titles), and pyperclip (Clipboard monitoring).
Authentication: Initialize firebase-admin using a downloaded 
service-account.json
. Do NOT hardcode the org_id—load it from a local config file (e.g., config.yaml).
Privacy Guarantee (CRITICAL): Devise is B2B software. You must never read or transmit the actual text of employee conversations or clipboard contents to Firebase. You are only transmitting lengths (len(clipboard)), window titles, and metadata tags (sensitivity_flag).
Graceful Degeneration: If the internet drops, the agent should ideally queue detection_events locally (e.g., SQLite or simple JSON queue) and flush them to Firebase when the connection returns, ensuring the dashboard's Analytics tab remains accurate.
Multi-Threading: You will need a main loop with multiple timed threads:
Thread A: Active Window / DNS monitor (every 1 second)
Thread B: Clipboard size monitor (every 1 second)
Thread C: Pull firewall_rules from Firestore (every 5 minutes)
Thread D: Push heartbeats to Firestore (every 5-10 minutes)

# Devise AI Governance — Complete Architecture Context

You are tasked with building the **Devise Desktop Agent**, a background Python script that runs on employee machines. To build this correctly, you must understand the entire end-to-end architecture of **Devise**, an enterprise B2B SaaS platform for AI Governance.

This document explicitly details the React frontend architecture, the complete feature set of the web dashboard, the Firebase serverless backend, and exactly how the Desktop Agent must integrate with them.

---

## 1. System Architecture Overview

Devise operates on a fully serverless, real-time architecture:
1.  **Frontend Dashboard (React SPA)**: Hosted on Vercel. Admins log in here to view team AI usage, configure policies, and mitigate data risks.
2.  **Backend (Firebase)**: Cloud Firestore acts as the central state engine. Authentication is handled by Firebase Auth.
3.  **Desktop Agent (Python)**: Runs locally on Windows/macOS. It monitors the OS for AI tool usage, enforces policies, detects sensitive data patterns (e.g., source code in clipboard), and pushes findings directly to Firestore.

**Core Philosophy:** 
- The Frontend NEVER talks to a traditional API server (like Node.js or Python FastAPI). It talks directly to Firestore.
- The Desktop Agent NEVER talks to a traditional API server. It talks directly to Firestore using `firebase-admin` and a `service-account.json`.
- The two systems (Frontend & Agent) synchronize entirely by reading and writing to the same Firestore collections, relying on Firestore's real-time listeners (`onSnapshot`) to update instantly.

---

## 2. The Frontend Codebase (React + Vite + TypeScript)

The frontend is a modern React Single Page Application (SPA).

### Tech Stack
-   **Framework**: React 18 + TypeScript + Vite
-   **Styling**: Tailwind CSS + custom glassmorphic CSS ([index.css](cci:7://file:///d:/devise-iris/frontend/src/index.css:0:0-0:0))
-   **UI Components**: shadcn/ui (Radix UI primitives) and Tabler/Lucide icons.
-   **Data Fetching**: `@tanstack/react-query` and native Firebase JS SDK.
-   **Routing**: React Router DOM (`/`, `/login`, `/dashboard`). Vercel is configured with a root [vercel.json](cci:7://file:///d:/devise-iris/vercel.json:0:0-0:0) SPA rewrite (`/(.*) -> /index.html`).

### Project Structure (`src/`)
*   [App.tsx](cci:7://file:///d:/devise-iris/frontend/src/App.tsx:0:0-0:0): Main routing engine. Defines the [Tab](cci:2://file:///d:/devise-iris/frontend/src/components/layout/UserProfileDropdown.tsx:6:0-6:140) state for the Dashboard.
*   `components/layout/`: Holds the main structural shells: [DashboardLayout](cci:1://file:///d:/devise-iris/frontend/src/components/layout/DashboardLayout.tsx:11:0-44:1), [Sidebar](cci:1://file:///d:/devise-iris/frontend/src/components/layout/Sidebar.tsx:37:0-134:1), [TopBar](cci:1://file:///d:/devise-iris/frontend/src/components/layout/TopBar.tsx:116:0-300:1).
*   `components/dashboard/`: Holds the individual feature tabs (e.g., [FirewallTab.tsx](cci:7://file:///d:/devise-iris/frontend/src/components/dashboard/FirewallTab.tsx:0:0-0:0), [DataRiskTab.tsx](cci:7://file:///d:/devise-iris/frontend/src/components/dashboard/DataRiskTab.tsx:0:0-0:0), [LiveFeedTab.tsx](cci:7://file:///d:/devise-iris/frontend/src/components/dashboard/LiveFeedTab.tsx:0:0-0:0)).
*   `pages/`: Full-page routes (e.g., `landing/LandingPage.tsx`, `auth/LoginPage.tsx`).
*   [services/api.ts](cci:7://file:///d:/devise-iris/frontend/src/services/api.ts:0:0-0:0): **The most critical file.** Contains all Firestore wrapper functions (e.g., [fetchBlockEvents()](cci:1://file:///d:/devise-iris/frontend/src/services/api.ts:529:0-540:2), [subscribeToHighRiskEvents()](cci:1://file:///d:/devise-iris/frontend/src/services/api.ts:731:0-749:2)).

### Security & Multi-Tenancy
Every company using Devise is assigned an `org_id` upon signup. **Every single document** in Firestore requires an `org_id` field. The Frontend enforces this via Firestore Security Rules (users can only read docs matching their profile's `org_id`).

---

## 3. End-to-End Feature Map

When building the agent, remember that its data populates these specific frontend tabs:

### A. Dashboard Overview (`overview`)
Shows high-level metrics: Active Agents, Time Saved, Alerts.
*   *Agent Requirement*: Writes to the `heartbeats` collection every 5 mins. The frontend counts unique `device_id`s in `heartbeats` to determine "Active Agents" online.

### B. Live Feed (`live-feed`)
A real-time scrolling table of what tools are being opened right now.
*   *Agent Requirement*: When an app launches (e.g., cursor.exe, ChatGPT in Chrome), the agent writes a basic document to `detection_events` with `event_type: "detected"`. The frontend listens via `onSnapshot` and animates these rows in.

### C. AI Firewall (`firewall`)
Allows admins to block specific AI tools company-wide.
*   *Frontend Logic*: Admins toggle tools ALLOWED/BLOCKED. Writes to `org_settings/{org_id}/firewall_rules`.
*   *Agent Requirement*: Periodically fetches `firewall_rules`. If a user opens a blocked tool, the agent must intercept/kill it.
*   *Agent Requirement*: Write to `detection_events` with `event_type: "blocked"` and `block_reason`. This populates the "Block Events" table in the UI.

### D. Data Risk (`data-risk`)
Detects sensitive data leakage (PII, source code, financial docs) into AI tools.
*   *Frontend Logic*: A feed of high-risk events, plus an "Employee Risk Leaderboard" showing who violates policies the most. High-risk events trigger real-time toast alerts on the admin's screen.
*   *Agent Requirement*: Monitors window titles and clipboard size (NOT content). If it sees an anomaly (e.g., "ChatGPT - Uploading financials.pdf" or pasting > 5000 chars), it writes to `detection_events` with `sensitivity_flag: "FINANCIAL_KEYWORDS"` and `sensitivity_score: 85`.

### E. Team & Devices (`team`, `devices`)
Lists all employees and their laptops.
*   *Agent Requirement*: Uses local OS module (`os`, `getpass`) to capture the local Windows/Mac username and device hostname, attaching them as `user_id` and `device_id` to every event.

---

## 4. Firestore Database Schema

The Desktop Agent must write payloads exactly matching these TypeScript interfaces used by the Frontend.

### Collection: `heartbeats`
Used to track online/offline status of employee laptops.
```json
{
  "device_id": "HOSTNAME-MAC_ADDRESS",
  "org_id": "your_org_id_here",
  "user_email": "john.doe@company.com", // Or local Windows username
  "status": "active", // or "idle"
  "last_seen": "<Firestore Server Timestamp>",
  "os_version": "Windows 11",
  "agent_version": "1.0.0"
}
Collection: detection_events
The central nervous system of Devise. Used for Live Feed, Firewall Blocks, and Data Risks.

json
{
  "device_id": "HOSTNAME-MAC_ADDRESS",
  "org_id": "your_org_id_here",
  "user_id": "john.doe@company.com", 
  "tool_name": "ChatGPT",          // e.g., "Claude", "Notion AI", "Cursor"
  "domain": "chat.openai.com",     // Optional URL if intercepted via browser
  "timestamp": "<Firestore Server Timestamp>",
  
  // -- FIREWALL FIELDS --
  "event_type": "detected",        // MUST BE either "detected" or "blocked"
  "block_reason": null,            // Populate if blocked! (e.g., "Admin Policy")
  "policy_matched": "ChatGPT",     // The rule ID that caused the block
  
  // -- DATA RISK FIELDS --
  "sensitivity_flag": null,        // e.g., "SOURCE_CODE", "LARGE_PASTE", "FINANCIAL_KEYWORDS", "CREDENTIALS_PATTERN", "FILE_UPLOAD"
  "sensitivity_score": 0,          // Integer 0 to 100
  "window_title": "ChatGPT - Uploading financial_report.pdf", 
  "paste_size_chars": 5432,        // Approximate length of clipboard paste
  "file_name": "financial_report.pdf",
  "reviewed": false                // Dashboard sets this to true when admin clicks "Mark Reviewed"
}
Subcollection: org_settings/{org_id}/firewall_rules/{tool_name}
The agent READS from here to enforce blocks.

json
{
  "tool_name": "ChatGPT",
  "domain": "chat.openai.com",
  "status": "blocked", // If "blocked", the agent must intercept
  "updated_at": "<Timestamp>"
}
5. Desktop Agent Implementation Guidelines (Python)
To fulfill the requirements of the React frontend, the Python agent must follow these rules:

Libraries: Use firebase-admin (Firestore), psutil (Process enumeration/killing), pygetwindow or win32gui / AppKit (Active window titles), and pyperclip (Clipboard monitoring).
Authentication: Initialize firebase-admin using a downloaded service-account.json. Do NOT hardcode the org_id—load it from a local config file (e.g., config.yaml).
Privacy Guarantee (CRITICAL): Devise is B2B software. You must never read or transmit the actual text of employee conversations or clipboard contents to Firebase. You are only transmitting lengths (len(clipboard)), window titles, and metadata tags (sensitivity_flag).
Graceful Degeneration: If the internet drops, the agent should ideally queue detection_events locally (e.g., SQLite or simple JSON queue) and flush them to Firebase when the connection returns, ensuring the dashboard's Analytics tab remains accurate.
Multi-Threading: You will need a main loop with multiple timed threads:
Thread A: Active Window / DNS monitor (every 1 second)
Thread B: Clipboard size monitor (every 1 second)
Thread C: Pull firewall_rules from Firestore (every 5 minutes)
Thread D: Push heartbeats to Firestore (every 5-10 minutes)



```


### File: devise-eye\debug_orgs.py
```py
import firebase_admin
from firebase_admin import credentials, firestore
import json

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Listing unique Org IDs from recent events...")
docs = db.collection('detection_events').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(20).get()

orgs = set()
for doc in docs:
    data = doc.to_dict()
    org_id = data.get('org_id')
    orgs.add(org_id)
    print(f"Doc: {doc.id} | Org: {org_id} | Tool: {data.get('tool_name')} | TS: {data.get('timestamp')}")

print("\nSummary of unique Org IDs found:")
for org in orgs:
    print(f"- {org}")

```


### File: devise-eye\deduplicator.py
```py
"""Deduplication module for Devise Desktop Agent."""

import logging
from typing import Dict, Tuple, Optional
from datetime import datetime, timedelta
from collections import OrderedDict
import threading


logger = logging.getLogger(__name__)


class Deduplicator:
    """Session-scoped deduplication for AI events."""

    def __init__(self, window_seconds: int = 300):
        """Initialize deduplicator.

        Args:
            window_seconds: Deduplication window in seconds (default 5 min)
        """
        self._window = timedelta(seconds=window_seconds)
        self._cache: OrderedDict[Tuple[str, str], datetime] = OrderedDict()
        self._lock = threading.Lock()

    def should_report(self, tool_name: str, process_name: str) -> bool:
        """Check if this tool+process combination should be reported.

        Args:
            tool_name: Name of the AI tool
            process_name: Name of the process

        Returns:
            True if should report, False if duplicate
        """
        key = (tool_name.lower(), process_name.lower() if process_name else "unknown")

        with self._lock:
            now = datetime.utcnow()

            # Check if key exists and is within window
            if key in self._cache:
                last_seen = self._cache[key]

                if now - last_seen < self._window:
                    # Within window - duplicate
                    logger.debug(f"Duplicate: {tool_name} from {process_name}")
                    return False
                else:
                    # Outside window - update timestamp and report
                    self._cache[key] = now
                    logger.debug(
                        f"Re-reporting after window: {tool_name} from {process_name}"
                    )
                    return True

            # New entry - report and cache
            self._cache[key] = now
            logger.debug(f"New event: {tool_name} from {process_name}")
            return True

    def should_report_connection(self, hostname: str, pid: Optional[int]) -> bool:
        """Check if connection should be reported based on hostname and PID.

        Args:
            hostname: Remote hostname
            pid: Process ID

        Returns:
            True if should report, False if duplicate
        """
        process_name = str(pid) if pid else "unknown"
        return self.should_report(hostname, process_name)

    def mark_reported(self, tool_name: str, process_name: str) -> None:
        """Manually mark a tool+process as reported.

        Args:
            tool_name: Name of the AI tool
            process_name: Name of the process
        """
        key = (tool_name.lower(), process_name.lower() if process_name else "unknown")

        with self._lock:
            self._cache[key] = datetime.utcnow()

    def clear(self) -> None:
        """Clear all deduplication state."""
        with self._lock:
            self._cache.clear()

    def cleanup_old_entries(self) -> int:
        """Remove entries older than the deduplication window.

        Returns:
            Number of entries removed
        """
        with self._lock:
            now = datetime.utcnow()
            keys_to_remove = []

            for key, timestamp in self._cache.items():
                if now - timestamp >= self._window:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del self._cache[key]

            if keys_to_remove:
                logger.debug(
                    f"Cleaned up {len(keys_to_remove)} old deduplication entries"
                )

            return len(keys_to_remove)

    def get_stats(self) -> Dict[str, int]:
        """Get deduplicator statistics.

        Returns:
            Dict with stats
        """
        with self._lock:
            return {
                "total_entries": len(self._cache),
                "window_seconds": int(self._window.total_seconds()),
            }


def create_deduplicator(window_seconds: int = 300) -> Deduplicator:
    """Create a deduplicator instance.

    Args:
        window_seconds: Deduplication window in seconds

    Returns:
        Deduplicator instance
    """
    return Deduplicator(window_seconds)

```


### File: devise-eye\detector.py
```py
"""Network connection detection module for Devise Desktop Agent."""

import logging
import psutil
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)


class NetworkDetector:
    """Detects network connections to AI tool domains."""

    # Filter to only ESTABLISHED connections (FR-02)
    FILTERED_STATES = {
        "TIME_WAIT",
        "CLOSE_WAIT",
        "LISTEN",
        "SYN_SENT",
        "SYN_RECV",
        "FIN_WAIT1",
        "FIN_WAIT2",
        "CLOSING",
        "LAST_ACK",
        "CLOSED",
    }

    def __init__(self, poll_interval: int = 30, process_resolver=None, dedup_window: int = 300):
        """Initialize network detector.

        Args:
            poll_interval: Polling interval in seconds (default 30)
            process_resolver: Optional ProcessResolver for process info
            dedup_window: Seconds before a seen connection key expires (default 300)
        """
        self._poll_interval = poll_interval
        self._dedup_window = dedup_window
        # Dict[conn_key, first_seen_time] — entries expire after dedup_window seconds
        self._seen_connections: Dict[str, datetime] = {}
        self._process_resolver = process_resolver

    @property
    def poll_interval(self) -> int:
        """Get polling interval."""
        return self._poll_interval

    def set_process_resolver(self, resolver) -> None:
        """Set process resolver for detailed process info.

        Args:
            resolver: ProcessResolver instance
        """
        self._process_resolver = resolver

    def get_established_connections(self) -> List[Dict[str, Any]]:
        """Get all ESTABLISHED network connections.

        Returns:
            List of connection dicts with remote IP, port, status
        """
        connections = []

        try:
            for conn in psutil.net_connections(kind="inet"):
                # Filter by ESTABLISHED state only (FR-02)
                if conn.status not in self.FILTERED_STATES:
                    if conn.raddr:
                        connection_info = {
                            "remote_addr": conn.raddr.ip,
                            "remote_port": conn.raddr.port,
                            "status": conn.status,
                            "pid": conn.pid,
                            "timestamp": datetime.utcnow().isoformat(),
                        }
                        connections.append(connection_info)

        except (psutil.AccessDenied, PermissionError) as e:
            logger.warning(f"Access denied when enumerating connections: {e}")
        except Exception as e:
            logger.error(f"Error enumerating connections: {e}")

        return connections

    def get_unique_remote_ips(self) -> List[str]:
        """Get unique remote IPs from ESTABLISHED connections.

        Returns:
            List of unique remote IP addresses
        """
        connections = self.get_established_connections()
        unique_ips = list(
            set(conn["remote_addr"] for conn in connections if conn["remote_addr"])
        )

        logger.debug(f"Found {len(unique_ips)} unique remote IPs")
        return unique_ips

    def get_connections_by_process(self) -> Dict[int, List[Dict]]:
        """Get connections grouped by process PID.

        Returns:
            Dict mapping PID to list of connections
        """
        connections = self.get_established_connections()
        by_process: Dict[int, List[Dict]] = {}

        for conn in connections:
            pid = conn.get("pid")
            if pid:
                if pid not in by_process:
                    by_process[pid] = []
                by_process[pid].append(conn)

        return by_process

    def get_process_name(self, pid: int) -> Optional[str]:
        """Get process name from PID.

        Args:
            pid: Process ID

        Returns:
            Process name or None if not found
        """
        if self._process_resolver:
            name, _, _ = self._process_resolver.resolve(pid)
            return name

        try:
            process = psutil.Process(pid)
            return process.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None

    def get_process_info(self, pid: int) -> Dict[str, str]:
        """Get full process info from PID.

        Args:
            pid: Process ID

        Returns:
            Dict with process_name and process_path
        """
        if self._process_resolver:
            name, path, _ = self._process_resolver.resolve(pid)
            return {"process_name": name, "process_path": path}

        # Fallback to basic psutil
        try:
            process = psutil.Process(pid)
            name = process.name()
            try:
                path = process.exe() or ""
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                path = ""
            return {"process_name": name, "process_path": path}
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return {"process_name": "unknown", "process_path": ""}

    def run_detection_cycle(self) -> List[Dict[str, Any]]:
        """Run a single detection cycle.

        Returns:
            List of new connections not seen in previous cycle
        """
        current_connections = self.get_established_connections()
        now = datetime.utcnow()

        # Evict expired entries based on deduplication window (Fix 3)
        cutoff = now - timedelta(seconds=self._dedup_window)
        self._seen_connections = {
            k: v for k, v in self._seen_connections.items() if v > cutoff
        }

        # Create unique key for each connection
        new_connections = []
        for conn in current_connections:
            conn_key = f"{conn['remote_addr']}:{conn['remote_port']}:{conn.get('pid', 'unknown')}"

            if conn_key not in self._seen_connections:
                self._seen_connections[conn_key] = now

                # Add process info if resolver available
                if self._process_resolver and conn.get("pid"):
                    process_info = self.get_process_info(conn["pid"])
                    conn["process_name"] = process_info["process_name"]
                    conn["process_path"] = process_info["process_path"]

                new_connections.append(conn)

        return new_connections


def create_detector(
    poll_interval: int = 30,
    process_resolver=None,
    dedup_window: int = 300,
) -> NetworkDetector:
    """Create a network detector instance.

    Args:
        poll_interval: Polling interval in seconds
        process_resolver: Optional ProcessResolver
        dedup_window: TTL for seen connections cache in seconds

    Returns:
        NetworkDetector instance
    """
    return NetworkDetector(poll_interval, process_resolver, dedup_window)

```


### File: devise-eye\diag_event.py
```py
import firebase_admin
from firebase_admin import credentials, firestore
import json
import datetime

cred_path = r'C:\ProgramData\Devise\service_account.json'
config_path = r'C:\ProgramData\Devise\config.json'

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

with open(config_path, 'r') as f:
    config = json.load(f)
org_id = config.get('org_id')

print(f"DEBUG: Org ID from config is '{org_id}'")

# Query without order_by first to see what we have
docs = db.collection('detection_events').where('org_id', '==', org_id).limit(1).get()

if not docs:
    print("No documents found for this org_id.")
else:
    for doc in docs:
        print("DOCUMENT DATA:")
        data = doc.to_dict()
        # Convert datetime to string for printing
        for k, v in data.items():
            if isinstance(v, datetime.datetime):
                data[k] = v.isoformat()
        print(json.dumps(data, indent=2))

```


### File: devise-eye\dns_resolver.py
```py
"""DNS resolution module for Devise Desktop Agent."""

import socket
import logging
from typing import Optional, Dict, Tuple
from datetime import datetime, timedelta
from collections import OrderedDict
import threading


logger = logging.getLogger(__name__)


class DNSResolver:
    """DNS resolver with LRU cache for reverse lookups."""

    def __init__(self, cache_size: int = 1000, timeout: float = 2.0):
        """Initialize DNS resolver.

        Args:
            cache_size: Maximum number of cached resolutions
            timeout: Timeout in seconds for each lookup
        """
        self._cache: OrderedDict[str, Optional[str]] = OrderedDict()
        self._cache_size = cache_size
        self._timeout = timeout
        self._lock = threading.Lock()

    def reverse_lookup(self, ip_address: str) -> Optional[str]:
        """Perform reverse DNS lookup on an IP address.

        Args:
            ip_address: IP address to resolve

        Returns:
            Hostname or None if resolution fails
        """
        # Check cache first
        cached = self._get_from_cache(ip_address)
        if cached is not None or cached == "":
            return cached

        # Perform actual lookup
        try:
            socket.setdefaulttimeout(self._timeout)
            hostname, _, _ = socket.gethostbyaddr(ip_address)

            # Cache successful result
            self._add_to_cache(ip_address, hostname)
            logger.debug(f"Resolved {ip_address} -> {hostname}")
            return hostname

        except socket.herror as e:
            # No reverse DNS record
            logger.debug(f"No reverse DNS for {ip_address}: {e}")
            self._add_to_cache(ip_address, None)
            return None

        except socket.timeout:
            logger.debug(f"DNS lookup timeout for {ip_address}")
            self._add_to_cache(ip_address, None)
            return None

        except Exception as e:
            logger.warning(f"Error resolving {ip_address}: {e}")
            self._add_to_cache(ip_address, None)
            return None

    def _get_from_cache(self, ip: str) -> Optional[str]:
        """Get value from cache.

        Args:
            ip: IP address

        Returns:
            Cached hostname or None
        """
        with self._lock:
            if ip in self._cache:
                # Move to end (most recently used)
                self._cache.move_to_end(ip)
                return self._cache[ip]
        return None

    def _add_to_cache(self, ip: str, hostname: Optional[str]) -> None:
        """Add value to cache.

        Args:
            ip: IP address
            hostname: Resolved hostname or None
        """
        with self._lock:
            # Evict oldest if cache is full
            if len(self._cache) >= self._cache_size and ip not in self._cache:
                self._cache.popitem(last=False)

            self._cache[ip] = hostname

    def resolve_multiple(self, ip_addresses: list) -> Dict[str, Optional[str]]:
        """Resolve multiple IP addresses.

        Args:
            ip_addresses: List of IP addresses

        Returns:
            Dict mapping IP to hostname
        """
        results = {}

        for ip in ip_addresses:
            hostname = self.reverse_lookup(ip)
            results[ip] = hostname

        return results

    def clear_cache(self) -> None:
        """Clear the DNS cache."""
        with self._lock:
            self._cache.clear()

    def get_cache_stats(self) -> Dict[str, int]:
        """Get cache statistics.

        Returns:
            Dict with cache stats
        """
        with self._lock:
            total = len(self._cache)
            resolved = sum(1 for v in self._cache.values() if v is not None)
            unresolved = total - resolved

            return {"total": total, "resolved": resolved, "unresolved": unresolved}


def create_resolver(cache_size: int = 1000, timeout: float = 2.0) -> DNSResolver:
    """Create a DNS resolver instance.

    Args:
        cache_size: Maximum cache size
        timeout: Lookup timeout in seconds

    Returns:
        DNSResolver instance
    """
    return DNSResolver(cache_size, timeout)

```


### File: devise-eye\doh_resolver.py
```py
"""DNS-over-HTTPS (DoH) resolver for Devise Desktop Agent.

Provides privacy-preserving DNS resolution via Cloudflare/Google DoH APIs
with automatic fallback to system DNS.
"""

import logging
from functools import lru_cache
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

# DoH endpoint URLs
CLOUDFLARE_DOH_URL = "https://cloudflare-dns.com/dns-query"
GOOGLE_DOH_URL = "https://dns.google/resolve"

# Timeout for DoH requests (seconds)
DOH_TIMEOUT = 2.0


def _ip_to_ptr(ip: str) -> str:
    """Convert IP address to PTR record format.

    Args:
        ip: IPv4 address (e.g., "1.2.3.4")

    Returns:
        PTR format string (e.g., "4.3.2.1.in-addr.arpa")
    """
    parts = ip.strip().split(".")
    return ".".join(reversed(parts)) + ".in-addr.arpa"


class DoHResolver:
    """DNS-over-HTTPS resolver with Cloudflare/Google fallback and LRU cache.

    Interface matches dns_resolver.DNSResolver for drop-in compatibility.
    Resolution order:
      1. Cloudflare DoH (primary)
      2. Google DoH (fallback on Cloudflare timeout/error)
      3. System DNS via dns_resolver.DNSResolver (final fallback)
    """

    def __init__(self, timeout: float = DOH_TIMEOUT):
        """Initialize DoH resolver.

        Args:
            timeout: HTTP request timeout in seconds
        """
        self._timeout = timeout
        # Use a single shared httpx client for connection reuse
        self._client = httpx.Client(timeout=self._timeout)

    def _query_cloudflare(self, ptr_name: str) -> Optional[str]:
        """Query Cloudflare DoH for PTR record.

        Args:
            ptr_name: PTR record name (e.g., "4.3.2.1.in-addr.arpa")

        Returns:
            Hostname string or None
        """
        try:
            response = self._client.get(
                CLOUDFLARE_DOH_URL,
                params={"name": ptr_name, "type": "PTR"},
                headers={"Accept": "application/dns-json"},
            )
            response.raise_for_status()
            data = response.json()
            answers = data.get("Answer", [])
            for answer in answers:
                if answer.get("type") == 12:  # PTR record type
                    return answer.get("data", "").rstrip(".")
        except httpx.TimeoutException:
            logger.debug(f"Cloudflare DoH timeout for {ptr_name}")
        except Exception as e:
            logger.debug(f"Cloudflare DoH error for {ptr_name}: {e}")
        return None

    def _query_google(self, ptr_name: str) -> Optional[str]:
        """Query Google DoH for PTR record.

        Args:
            ptr_name: PTR record name (e.g., "4.3.2.1.in-addr.arpa")

        Returns:
            Hostname string or None
        """
        try:
            response = self._client.get(
                GOOGLE_DOH_URL,
                params={"name": ptr_name, "type": "PTR"},
                headers={"Accept": "application/dns-json"},
            )
            response.raise_for_status()
            data = response.json()
            answers = data.get("Answer", [])
            for answer in answers:
                if answer.get("type") == 12:  # PTR record type
                    return answer.get("data", "").rstrip(".")
        except httpx.TimeoutException:
            logger.debug(f"Google DoH timeout for {ptr_name}")
        except Exception as e:
            logger.debug(f"Google DoH error for {ptr_name}: {e}")
        return None

    def _query_system_dns(self, ip: str) -> Optional[str]:
        """Fall back to system DNS resolver.

        Args:
            ip: IP address to resolve

        Returns:
            Hostname string or None
        """
        try:
            from dns_resolver import DNSResolver

            fallback = DNSResolver()
            return fallback.reverse_lookup(ip)
        except Exception as e:
            logger.debug(f"System DNS fallback error for {ip}: {e}")
        return None

    @lru_cache(maxsize=1024)
    def reverse_lookup(self, ip: str) -> Optional[str]:
        """Perform reverse DNS lookup via DoH with fallback chain.

        Resolution order: Cloudflare DoH → Google DoH → System DNS

        Args:
            ip: IP address to resolve (e.g., "1.2.3.4")

        Returns:
            Hostname or None if all methods fail
        """
        ptr_name = _ip_to_ptr(ip)
        logger.debug(f"DoH reverse lookup: {ip} → {ptr_name}")

        # Primary: Cloudflare DoH
        hostname = self._query_cloudflare(ptr_name)
        if hostname:
            logger.debug(f"Cloudflare DoH resolved {ip} → {hostname}")
            return hostname

        # Fallback: Google DoH
        hostname = self._query_google(ptr_name)
        if hostname:
            logger.debug(f"Google DoH resolved {ip} → {hostname}")
            return hostname

        # Final fallback: system DNS
        hostname = self._query_system_dns(ip)
        if hostname:
            logger.debug(f"System DNS resolved {ip} → {hostname}")
        else:
            logger.debug(f"All DNS methods failed for {ip}")

        return hostname

    def close(self) -> None:
        """Close the HTTP client."""
        try:
            self._client.close()
        except Exception:
            pass


def create_doh_resolver(timeout: float = DOH_TIMEOUT) -> DoHResolver:
    """Create a DoH resolver instance.

    Args:
        timeout: HTTP timeout in seconds

    Returns:
        DoHResolver instance
    """
    return DoHResolver(timeout)

```


### File: devise-eye\event_builder.py
```py
"""Event builder module for Devise Desktop Agent."""

import uuid
import logging
from datetime import datetime, timezone
from typing import Dict, Optional, Any


logger = logging.getLogger(__name__)


class EventBuilder:
    """Builds event objects matching required schema."""

    REQUIRED_FIELDS = [
        "event_id",
        "org_id",
        "user_id",
        "user_email",
        "department",
        "device_id",
        "tool_name",
        "domain",
        "category",
        "vendor",
        "risk_level",
        "source",
        "process_name",
        "process_path",
        "is_approved",
        "is_blocked",
        "sensitivity_score",
        "timestamp",
    ]

    def __init__(self, identity: Dict[str, str], device_id: str, org_id: str):
        """Initialize event builder.

        Args:
            identity: User identity dict from identity module
            device_id: Device ID from config
            org_id: Organization ID from config
        """
        self._identity = identity
        self._device_id = device_id
        self._org_id = org_id

    def build_event(
        self,
        tool_name: str,
        domain: str,
        category: str,
        vendor: str,
        risk_level: str,
        process_name: str = "unknown",
        process_path: str = "",
        is_approved: bool = False,
        is_blocked: bool = False,
        sensitivity_score: int = 0,
        connection_frequency: Optional[int] = None,
        high_frequency: Optional[bool] = None,
        bytes_read: Optional[int] = None,
        bytes_write: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Build event object with required schema.

        Args:
            tool_name: Name of the AI tool
            domain: Domain of the tool
            category: Tool category
            vendor: Tool vendor
            risk_level: Risk level (low/medium/high)
            process_name: Process name (default: unknown)
            process_path: Full path to executable (default: empty)
            is_approved: Enterprise approval status
            connection_frequency: Number of connections to domain in last 5 minutes
            high_frequency: True if domain exceeds high-frequency threshold
            bytes_read: Disk bytes read by process (proxy for activity)
            bytes_write: Disk bytes written by process (proxy for activity)

        Returns:
            Event dict matching required schema
        """
        event = {
            "event_id": str(uuid.uuid4()),
            "org_id": self._org_id,
            "user_id": self._identity.get("user_id", "unknown"),
            "user_email": self._identity.get("user_email", "unknown"),
            "department": self._identity.get("department", "Unknown"),
            "device_id": self._device_id,
            "tool_name": tool_name,
            "domain": domain,
            "category": category,
            "vendor": vendor,
            "risk_level": risk_level,
            "source": "desktop",
            "process_name": process_name,
            "process_path": process_path,
            "is_approved": is_approved,
            "is_blocked": is_blocked,
            "sensitivity_score": sensitivity_score,
            "timestamp": datetime.now(timezone.utc),
        }

        # Include optional analytics fields only when provided
        if connection_frequency is not None:
            event["connection_frequency"] = connection_frequency
        if high_frequency is not None:
            event["high_frequency"] = high_frequency
        if bytes_read is not None:
            event["bytes_read"] = bytes_read
        if bytes_write is not None:
            event["bytes_write"] = bytes_write

        # Validate required fields
        self._validate_event(event)

        logger.debug(f"Built event for {tool_name} ({domain})")
        return event

    def _validate_event(self, event: Dict[str, Any]) -> None:
        """Validate event has all required fields.

        Args:
            event: Event dict

        Raises:
            ValueError: If required field is missing
        """
        for field in self.REQUIRED_FIELDS:
            if field not in event:
                raise ValueError(f"Missing required field: {field}")

    def is_valid_event(self, event: Dict[str, Any]) -> bool:
        """Check if event has all required fields.

        Args:
            event: Event dict

        Returns:
            True if valid
        """
        for field in self.REQUIRED_FIELDS:
            if field not in event:
                return False
        return True


def create_event_builder(identity: Dict[str, str], device_id: str, org_id: str) -> EventBuilder:
    """Create an event builder instance.

    Args:
        identity: User identity dict
        device_id: Device ID
        org_id: Organization ID

    Returns:
        EventBuilder instance
    """
    return EventBuilder(identity, device_id, org_id)

```


### File: devise-eye\event_queue.py
```py
"""SQLite offline queue module for Devise Desktop Agent.

Provides persistent event buffering when backend is unreachable.
"""

import json
import logging
import os
import platform
import sqlite3
import threading
from datetime import datetime, timezone
from pathlib import Path
import queue as std_queue
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

# Queue capacity
MAX_QUEUE_SIZE = 10000
BATCH_SIZE = 100

# Backoff intervals in seconds
BACKOFF_INTERVALS = [30, 60, 120, 300]
MAX_RETRIES = 4


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime objects."""
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return super().default(obj)



def get_db_path() -> str:
    """Get platform-specific database path.

    Returns:
        Path to SQLite database file
    """
    if platform.system() == "Windows":
        base = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
    elif platform.system() == "Darwin":
        base = str(Path.home() / "Library" / "Application Support")
    else:
        base = os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local" / "share"))

    db_dir = Path(base) / "Devise"
    db_dir.mkdir(parents=True, exist_ok=True)

    return str(db_dir / "event_queue.db")


class EventQueue:
    """SQLite-backed event queue with FIFO overflow."""

    def __init__(self, db_path: Optional[str] = None):
        """Initialize event queue.

        Args:
            db_path: Optional custom database path
        """
        self._db_path = db_path or get_db_path()
        self._lock = threading.Lock()
        self._init_db()

    def _init_db(self) -> None:
        """Initialize database schema."""
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    retry_count INTEGER DEFAULT 0,
                    last_attempt TEXT,
                    status TEXT DEFAULT 'pending'
                )
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_events_status 
                ON events(status, created_at)
            """)

            conn.commit()
            conn.close()

        logger.info(f"Event queue initialized at {self._db_path}")

    def enqueue(self, event: Dict[str, Any]) -> bool:
        """Add event to queue.

        Args:
            event: Event dict to queue

        Returns:
            True if enqueued successfully
        """
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # Check current size
            cursor.execute("SELECT COUNT(*) FROM events WHERE status = 'pending'")
            count = cursor.fetchone()[0]

            # If at capacity, drop oldest
            if count >= MAX_QUEUE_SIZE:
                cursor.execute(
                    """
                    DELETE FROM events 
                    WHERE id IN (
                        SELECT id FROM events 
                        WHERE status = 'pending' 
                        ORDER BY created_at ASC 
                        LIMIT ?
                    )
                """,
                    (count - MAX_QUEUE_SIZE + 1,),
                )
                logger.warning(f"Queue at capacity, dropped oldest events")

            # Insert new event
            event_json = json.dumps(event, cls=DateTimeEncoder)
            created_at = datetime.now(timezone.utc).isoformat()

            cursor.execute(
                """
                INSERT INTO events (event_json, created_at, status)
                VALUES (?, ?, 'pending')
            """,
                (event_json, created_at),
            )

            conn.commit()
            conn.close()

        logger.debug(f"Event enqueued: {event.get('event_id', 'unknown')}")
        return True

    def get_pending(self, limit: int = BATCH_SIZE) -> List[Dict[str, Any]]:
        """Get pending events for sending.

        Args:
            limit: Maximum events to retrieve

        Returns:
            List of event dicts with id
        """
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, event_json, retry_count, created_at
                FROM events
                WHERE status = 'pending'
                AND (last_attempt IS NULL 
                     OR last_attempt < datetime('now', '-' || 
                        CASE retry_count
                            WHEN 0 THEN 30
                            WHEN 1 THEN 60
                            WHEN 2 THEN 120
                            WHEN 3 THEN 300
                            ELSE 300
                        END || ' seconds'))
                ORDER BY created_at ASC
                LIMIT ?
            """,
                (limit,),
            )

            rows = cursor.fetchall()
            conn.close()

            events = []
            for row in rows:
                event = json.loads(row[1])
                event["_queue_id"] = row[0]
                event["_retry_count"] = row[2]
                event["_created_at"] = row[3]
                events.append(event)

            return events

    def mark_success(self, queue_ids: List[int]) -> None:
        """Mark events as successfully sent.

        Args:
            queue_ids: List of queue IDs to mark as success
        """
        if not queue_ids:
            return

        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            placeholders = ",".join("?" * len(queue_ids))
            cursor.execute(
                f"""
                DELETE FROM events 
                WHERE id IN ({placeholders})
            """,
                queue_ids,
            )

            deleted = cursor.rowcount
            conn.commit()
            conn.close()

        logger.debug(f"Marked {deleted} events as successful")

    def mark_failed(self, queue_ids: List[int]) -> None:
        """Mark events as failed (increment retry count).

        Args:
            queue_ids: List of queue IDs to mark as failed
        """
        if not queue_ids:
            return

        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            now = datetime.now(timezone.utc).isoformat()

            for qid in queue_ids:
                cursor.execute(
                    """
                    UPDATE events
                    SET retry_count = retry_count + 1,
                        last_attempt = ?,
                        status = CASE 
                            WHEN retry_count + 1 >= ? THEN 'failed'
                            ELSE 'pending'
                        END
                    WHERE id = ?
                """,
                    (now, MAX_RETRIES, qid),
                )

            conn.commit()
            conn.close()

        logger.debug(f"Marked {len(queue_ids)} events as failed")

    def get_queue_depth(self) -> int:
        """Get current queue depth.

        Returns:
            Number of pending events
        """
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT COUNT(*) FROM events WHERE status = 'pending'
            """)

            count = cursor.fetchone()[0]
            conn.close()

            return count

    def get_failed_count(self) -> int:
        """Get count of events that exceeded max retries.

        Returns:
            Number of failed events
        """
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT COUNT(*) FROM events WHERE status = 'failed'
            """)

            count = cursor.fetchone()[0]
            conn.close()

            return count

    def clear_failed(self) -> int:
        """Clear all failed events.

        Returns:
            Number of events cleared
        """
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM events WHERE status = 'failed'")

            count = cursor.rowcount
            conn.commit()
            conn.close()

        logger.info(f"Cleared {count} failed events")
        return count

    def flush_all(self) -> None:
        """Clear all events (for testing)."""
        with self._lock:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM events")
            conn.commit()
            conn.close()


def create_event_queue(
    db_path: Optional[str] = None,
    encrypted: bool = False,
    api_key: str = "",
    device_id: str = "",
) -> "EventQueue":
    """Create an event queue instance.

    Args:
        db_path: Optional custom database path
        encrypted: Use SQLCipher encryption (requires pysqlcipher3)
        api_key: API key for key derivation (used when encrypted=True)
        device_id: Device ID for key derivation (used when encrypted=True)

    Returns:
        EncryptedEventQueue if encrypted=True and pysqlcipher3 available,
        otherwise EventQueue
    """
    if encrypted:
        return EncryptedEventQueue(
            db_path=db_path, api_key=api_key, device_id=device_id
        )
    return EventQueue(db_path)


class EncryptedEventQueue(EventQueue):
    """SQLCipher-encrypted event queue.

    Uses pysqlcipher3 for AES-256-CBC encrypted SQLite storage.
    Gracefully falls back to plain EventQueue if pysqlcipher3 is unavailable.

    Key derivation: PBKDF2-HMAC-SHA256(api_key, device_id, 100000 iterations, 32 bytes)
    Key storage: OS credential store via keyring, with in-memory fallback.
    """

    def __init__(
        self,
        db_path: Optional[str] = None,
        api_key: str = "",
        device_id: str = "",
    ):
        """Initialize encrypted event queue.

        Args:
            db_path: Optional custom database path
            api_key: API key for key derivation
            device_id: Device ID for key derivation (salt)
        """
        self._api_key = api_key
        self._device_id = device_id
        self._encryption_available = self._check_encryption()
        self._derived_key: Optional[str] = None

        if not self._encryption_available:
            logger.warning(
                "pysqlcipher3 not available — falling back to unencrypted EventQueue"
            )

        super().__init__(db_path)

    def _check_encryption(self) -> bool:
        """Check if pysqlcipher3 is available.

        Returns:
            True if encryption is available
        """
        try:
            from pysqlcipher3 import dbapi2  # noqa: F401

            return True
        except ImportError:
            return False

    def _derive_key(self, api_key: str, device_id: str) -> str:
        """Derive encryption key from api_key and device_id.

        Uses PBKDF2-HMAC-SHA256 for key stretching.

        Args:
            api_key: API key (input key material)
            device_id: Device ID (salt)

        Returns:
            32-byte key as lowercase hex string
        """
        import hashlib

        key_bytes = hashlib.pbkdf2_hmac(
            "sha256",
            api_key.encode("utf-8"),
            device_id.encode("utf-8"),
            100000,
            dklen=32,
        )
        return key_bytes.hex()

    def _get_key(self) -> str:
        """Get or derive the encryption key.

        Attempts to load from keyring first, then derives from credentials.

        Returns:
            Hex-encoded 32-byte encryption key
        """
        # Try keyring first
        try:
            import keyring

            stored = keyring.get_password("devise-agent", "queue-key")
            if stored:
                return stored
        except Exception:
            pass

        # Derive key from credentials
        if self._derived_key is None:
            self._derived_key = self._derive_key(self._api_key, self._device_id)
            # Store in keyring for future use
            try:
                import keyring

                keyring.set_password("devise-agent", "queue-key", self._derived_key)
            except Exception:
                pass

        return self._derived_key

    def _get_connection(self) -> "sqlite3.Connection":
        """Get an encrypted database connection.

        Returns:
            SQLite connection with encryption PRAGMA applied,
            or plain sqlite3 connection if encryption unavailable
        """
        if not self._encryption_available:
            return sqlite3.connect(self._db_path)

        try:
            from pysqlcipher3 import dbapi2 as sqlite3_enc

            conn = sqlite3_enc.connect(self._db_path)
            hex_key = self._get_key()
            conn.execute(f"PRAGMA key = \"x'{hex_key}'\"")
            return conn
        except Exception as e:
            logger.warning(f"Encrypted connection failed, using plain sqlite3: {e}")
            return sqlite3.connect(self._db_path)

    def _init_db(self) -> None:
        """Initialize database schema with encrypted connection."""
        if not self._encryption_available:
            super()._init_db()
            return

        with self._lock:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    retry_count INTEGER DEFAULT 0,
                    last_attempt TEXT,
                    status TEXT DEFAULT 'pending'
                )
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_events_status 
                ON events(status, created_at)
            """)

            conn.commit()
            conn.close()

        logger.info(f"Encrypted event queue initialized at {self._db_path}")

    def enqueue(self, event: Dict[str, Any]) -> bool:
        """Add event to encrypted queue."""
        if not self._encryption_available:
            return super().enqueue(event)

        with self._lock:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM events WHERE status = 'pending'")
            count = cursor.fetchone()[0]

            if count >= MAX_QUEUE_SIZE:
                cursor.execute(
                    """
                    DELETE FROM events 
                    WHERE id IN (
                        SELECT id FROM events 
                        WHERE status = 'pending' 
                        ORDER BY created_at ASC 
                        LIMIT ?
                    )
                """,
                    (count - MAX_QUEUE_SIZE + 1,),
                )
                logger.warning("Encrypted queue at capacity, dropped oldest events")

            event_json = json.dumps(event, cls=DateTimeEncoder)
            created_at = datetime.now(timezone.utc).isoformat()

            cursor.execute(
                """
                INSERT INTO events (event_json, created_at, status)
                VALUES (?, ?, 'pending')
            """,
                (event_json, created_at),
            )

            conn.commit()
            conn.close()

        logger.debug(f"Event enqueued (encrypted): {event.get('event_id', 'unknown')}")
        return True

    def get_pending(self, limit: int = BATCH_SIZE) -> List[Dict[str, Any]]:
        """Get pending events from encrypted queue."""
        if not self._encryption_available:
            return super().get_pending(limit)

        with self._lock:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, event_json, retry_count, created_at
                FROM events
                WHERE status = 'pending'
                AND (last_attempt IS NULL 
                     OR last_attempt < datetime('now', '-' || 
                        CASE retry_count
                            WHEN 0 THEN 30
                            WHEN 1 THEN 60
                            WHEN 2 THEN 120
                            WHEN 3 THEN 300
                            ELSE 300
                        END || ' seconds'))
                ORDER BY created_at ASC
                LIMIT ?
            """,
                (limit,),
            )

            rows = cursor.fetchall()
            conn.close()

            events = []
            for row in rows:
                event = json.loads(row[1])
                event["_queue_id"] = row[0]
                event["_retry_count"] = row[2]
                event["_created_at"] = row[3]
                events.append(event)

            return events

    def mark_success(self, queue_ids: List[int]) -> None:
        """Mark events as success in encrypted queue."""
        if not self._encryption_available:
            return super().mark_success(queue_ids)

        if not queue_ids:
            return

        with self._lock:
            conn = self._get_connection()
            cursor = conn.cursor()

            placeholders = ",".join("?" * len(queue_ids))
            cursor.execute(
                f"DELETE FROM events WHERE id IN ({placeholders})",
                queue_ids,
            )

            conn.commit()
            conn.close()

    def mark_failed(self, queue_ids: List[int]) -> None:
        """Mark events as failed in encrypted queue."""
        if not self._encryption_available:
            return super().mark_failed(queue_ids)

        if not queue_ids:
            return

        with self._lock:
            conn = self._get_connection()
            cursor = conn.cursor()

            now = datetime.now(timezone.utc).isoformat()

            for qid in queue_ids:
                cursor.execute(
                    """
                    UPDATE events
                    SET retry_count = retry_count + 1,
                        last_attempt = ?,
                        status = CASE 
                            WHEN retry_count + 1 >= ? THEN 'failed'
                            ELSE 'pending'
                        END
                    WHERE id = ?
                """,
                    (now, MAX_RETRIES, qid),
                )

            conn.commit()
            conn.close()

```


### File: devise-eye\fetch_latest_data.py
```py
import firebase_admin
from firebase_admin import credentials, firestore

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Fetching latest 5 detection events...")
docs = db.collection('detection_events').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(5).get()

if not docs:
    print("No events found at all.")
else:
    for doc in docs:
        data = doc.to_dict()
        print(f"ID: {doc.id}")
        print(f"  Org ID: {data.get('org_id')}")
        print(f"  Timestamp: {data.get('timestamp')}")
        print(f"  Tool: {data.get('tool_name')}")
        print(f"  Category: {data.get('category')}")
        print(f"  Risk: {data.get('risk_level')}")
        print("-" * 20)

```


### File: devise-eye\firewall_monitor.py
```py
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

```


### File: devise-eye\frequency_tracker.py
```py
"""Connection frequency tracker for Devise Desktop Agent.

Tracks how often each domain is accessed to detect high-frequency
or anomalous connection patterns (FR-10).
"""

import logging
import threading
import time
from dataclasses import dataclass
from typing import Dict, List

logger = logging.getLogger(__name__)

# Frequency window in seconds (5 minutes)
FREQUENCY_WINDOW = 300

# High-frequency threshold: hits per window
HIGH_FREQUENCY_THRESHOLD = 10


@dataclass
class FrequencyResult:
    """Result of recording a domain hit.

    Attributes:
        domain: The domain that was recorded
        count_5min: Number of hits in the last 5 minutes
        high_frequency: True if count_5min >= HIGH_FREQUENCY_THRESHOLD
    """

    domain: str
    count_5min: int
    high_frequency: bool


class FrequencyTracker:
    """Thread-safe connection frequency tracker.

    Maintains a rolling 5-minute window of connection timestamps
    per domain to identify high-frequency access patterns.
    """

    def __init__(
        self,
        window_seconds: int = FREQUENCY_WINDOW,
        threshold: int = HIGH_FREQUENCY_THRESHOLD,
    ):
        """Initialize frequency tracker.

        Args:
            window_seconds: Rolling window size in seconds (default: 300)
            threshold: Hit count threshold for high_frequency flag (default: 10)
        """
        self._window_seconds = window_seconds
        self._threshold = threshold
        self._timestamps: Dict[str, List[float]] = {}
        self._lock = threading.Lock()

    def _prune(self, domain: str, now: float) -> None:
        """Remove timestamps older than the window.

        Must be called with lock held.

        Args:
            domain: Domain to prune
            now: Current Unix timestamp
        """
        cutoff = now - self._window_seconds
        if domain in self._timestamps:
            self._timestamps[domain] = [
                ts for ts in self._timestamps[domain] if ts >= cutoff
            ]

    def record(self, domain: str) -> FrequencyResult:
        """Record a connection to domain and return frequency stats.

        Adds current timestamp, prunes old entries, and returns current
        frequency within the rolling window.

        Args:
            domain: Domain that was accessed

        Returns:
            FrequencyResult with count and high_frequency flag
        """
        now = time.time()

        with self._lock:
            if domain not in self._timestamps:
                self._timestamps[domain] = []

            # Add current timestamp
            self._timestamps[domain].append(now)

            # Prune old entries
            self._prune(domain, now)

            count = len(self._timestamps[domain])

        high_freq = count >= self._threshold

        if high_freq:
            logger.info(
                f"High-frequency domain detected: {domain} ({count} hits in {self._window_seconds}s)"
            )

        return FrequencyResult(
            domain=domain,
            count_5min=count,
            high_frequency=high_freq,
        )

    def get_frequency(self, domain: str) -> int:
        """Get current hit count for domain without recording a new hit.

        Args:
            domain: Domain to query

        Returns:
            Number of recorded hits within the rolling window
        """
        now = time.time()

        with self._lock:
            if domain not in self._timestamps:
                return 0

            # Prune to get accurate current count
            self._prune(domain, now)
            return len(self._timestamps[domain])

    def reset(self, domain: str) -> None:
        """Clear all recorded timestamps for a domain.

        Args:
            domain: Domain to reset
        """
        with self._lock:
            self._timestamps.pop(domain, None)

    def clear_all(self) -> None:
        """Clear all tracked domains (for testing)."""
        with self._lock:
            self._timestamps.clear()

```


### File: devise-eye\generate_traffic.py
```py
import httpx
import time
import socket

domains = ["chatgpt.com", "claude.ai", "openai.com"]
print("Generating traffic to AI domains...")

for i in range(10):
    domain = domains[i % len(domains)]
    print(f"[{i+1}/10] Connecting to {domain}...")
    try:
        # DNS resolution
        socket.gethostbyname(domain)
        # HTTP request
        with httpx.Client(timeout=5.0) as client:
            client.get(f"https://{domain}")
    except Exception as e:
        print(f"Error connecting to {domain}: {e}")
    time.sleep(5)

print("Traffic generation complete.")

```


### File: devise-eye\generate_traffic_fast.py
```py
import httpx
import time
import socket
import threading

domains = ["chatgpt.com", "claude.ai", "openai.com", "gemini.google.com", "huggingface.co"]

def connect(domain):
    try:
        print(f"Connecting to {domain}...")
        socket.gethostbyname(domain)
        with httpx.Client(timeout=10.0) as client:
            client.get(f"https://{domain}")
    except Exception as e:
        pass

print("Starting aggressive traffic generation (30 seconds)...")
start_time = time.time()
while time.time() - start_time < 30:
    for domain in domains:
        t = threading.Thread(target=connect, args=(domain,))
        t.start()
    time.sleep(2)

print("Traffic generation complete.")

```


### File: devise-eye\heartbeat.py
```py
"""Heartbeat module for Devise Desktop Agent.

Sends periodic health signals to the backend.
"""

import logging
import platform
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Heartbeat interval in seconds (5 minutes)
HEARTBEAT_INTERVAL = 300  # 5 minutes


class HeartbeatSender:
    """Sends periodic heartbeat events to backend."""

    def __init__(
        self,
        device_id: str,
        agent_version: str,
        api_key: str,
        event_endpoint: str,
        queue=None,
        timeout: float = 10.0,
    ):
        """Initialize heartbeat sender.

        Args:
            device_id: Device identifier
            agent_version: Agent version string
            api_key: Device API key
            event_endpoint: API endpoint URL
            queue: Optional event queue for queue_depth
            timeout: Request timeout in seconds
        """
        self._device_id = device_id
        self._agent_version = agent_version
        self._api_key = api_key
        self._event_endpoint = event_endpoint
        self._queue = queue
        self._timeout = timeout

        self._last_detection_time: Optional[datetime] = None
        self._restart_detected = False

        # Check for restart
        self._check_for_restart()

    def _check_for_restart(self) -> None:
        """Check for agent restart and flag if detected."""
        import os
        from pathlib import Path

        # Check platform-specific restart marker
        if platform.system() == "Windows":
            base = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
        elif platform.system() == "Darwin":
            base = str(Path.home() / "Library" / "Application Support")
        else:
            base = os.environ.get(
                "XDG_DATA_HOME", str(Path.home() / ".local" / "share")
            )

        marker_path = Path(base) / "Devise" / ".restart_marker"

        if marker_path.exists():
            # Read previous uptime
            try:
                prev_uptime = float(marker_path.read_text().strip())
                # If previous uptime was very short, consider it a crash restart
                if prev_uptime < 60:  # Less than 1 minute = crash
                    self._restart_detected = True
                    logger.info("Agent restart detected (crash recovery)")
            except Exception:
                pass

        # Write current startup time marker
        marker_path.parent.mkdir(parents=True, exist_ok=True)
        marker_path.write_text(str(datetime.now(timezone.utc).timestamp()))

    def update_last_detection(self, timestamp: datetime) -> None:
        """Update last detection time.

        Args:
            timestamp: Detection timestamp
        """
        self._last_detection_time = timestamp

    def get_queue_depth(self) -> int:
        """Get current queue depth.

        Returns:
            Number of pending events in queue, or 0 if no queue
        """
        if self._queue:
            return self._queue.get_queue_depth()
        return 0

    def get_os_version(self) -> str:
        """Get OS version string.

        Returns:
            OS version description
        """
        return f"{platform.system()} {platform.release()}"

    def build_heartbeat_payload(self) -> Dict[str, Any]:
        """Build heartbeat payload.

        Returns:
            Heartbeat event dict
        """
        return {
            "event_type": "heartbeat",
            "device_id": self._device_id,
            "agent_version": self._agent_version,
            "queue_depth": self.get_queue_depth(),
            "last_detection_time": (
                self._last_detection_time.isoformat()
                if self._last_detection_time
                else None
            ),
            "os_version": self.get_os_version(),
            "restart_detected": self._restart_detected,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    async def send_heartbeat(self) -> bool:
        """Send heartbeat to backend.

        Returns:
            True if successful, False otherwise
        """
        import httpx

        payload = self.build_heartbeat_payload()

        try:
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.post(
                    self._event_endpoint,
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self._api_key}",
                        "Content-Type": "application/json",
                    },
                )
                response.raise_for_status()

                logger.info(
                    f"Heartbeat sent: queue_depth={payload['queue_depth']}, "
                    f"restart={payload['restart_detected']}"
                )

                # Reset restart flag after successful send
                self._restart_detected = False
                return True

        except Exception as e:
            logger.warning(f"Failed to send heartbeat: {e}")
            return False


def create_heartbeat_sender(
    device_id: str,
    agent_version: str,
    api_key: str,
    event_endpoint: str,
    queue=None,
) -> HeartbeatSender:
    """Create a heartbeat sender instance.

    Args:
        device_id: Device identifier
        agent_version: Agent version string
        api_key: Device API key
        event_endpoint: API endpoint URL
        queue: Optional event queue

    Returns:
        HeartbeatSender instance
    """
    return HeartbeatSender(
        device_id=device_id,
        agent_version=agent_version,
        api_key=api_key,
        event_endpoint=event_endpoint,
        queue=queue,
    )

```


### File: devise-eye\identity.py
```py
"""User identity resolution for Devise Desktop Agent."""

import os
import getpass
import platform
import subprocess
import uuid
import socket
import time
from typing import Dict, Optional
from config import get_config


# Module-level cache for get_current_user()
_cached_user: Optional[Dict[str, str]] = None
_cache_time: float = 0.0
_USER_CACHE_TTL = 30.0  # seconds


class IdentityResolver:
    """Resolves user identity from config or OS fallback."""

    def __init__(self, config_path: Optional[str] = None):
        """Initialize identity resolver.

        Args:
            config_path: Optional config file path
        """
        self._config = get_config(config_path)
        self._identity = self._resolve_identity()

    def _get_hostname(self) -> str:
        """Get system hostname."""
        return socket.gethostname()

    def _get_device_id(self) -> str:
        """Generate or retrieve device ID."""
        # Try config first
        config_device_id = self._config.device_id
        if config_device_id:
            return config_device_id

        # Generate from hostname + random (stable for this machine)
        hostname = self._get_hostname()
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, hostname))

    def _resolve_identity(self) -> Dict[str, str]:
        """Resolve identity from MDM config or fall back to OS."""
        identity_config = self._config.identity_config

        # Primary: MDM-injected config (FR-23, FR-24)
        user_id = identity_config.get("user_id")
        user_email = identity_config.get("user_email")
        department = identity_config.get("department")

        # Fallback: OS username (FR-22)
        if not user_id:
            username = getpass.getuser()
            user_id = username

        if not user_email:
            # Try to construct from OS
            user_email = f"{getpass.getuser()}@{platform.node()}"

        if not department:
            department = "Unknown"

        device_id = self._get_device_id()

        return {
            "user_id": user_id,
            "user_email": user_email,
            "department": department,
            "device_id": device_id,
            "hostname": self._get_hostname(),
        }

    @property
    def user_id(self) -> str:
        """Get user ID."""
        return self._identity["user_id"]

    @property
    def user_email(self) -> str:
        """Get user email."""
        return self._identity["user_email"]

    @property
    def department(self) -> str:
        """Get department."""
        return self._identity["department"]

    @property
    def device_id(self) -> str:
        """Get device ID."""
        return self._identity["device_id"]

    @property
    def identity(self) -> Dict[str, str]:
        """Get full identity dict."""
        return self._identity.copy()

    def reload(self) -> None:
        """Reload identity from config."""
        self._identity = self._resolve_identity()


def get_identity(config_path: Optional[str] = None) -> IdentityResolver:
    """Get identity resolver instance.

    Args:
        config_path: Optional config file path

    Returns:
        IdentityResolver instance
    """
    return IdentityResolver(config_path)


def get_current_user() -> Dict[str, str]:
    """Get the currently active console user.

    Caches result for 30 seconds to avoid repeated subprocess/syscall overhead.
    Falls back gracefully through multiple resolution methods.

    Returns:
        Dict with keys: "username" (str), "source" (str describing resolution method)
    """
    global _cached_user, _cache_time

    now = time.time()
    if _cached_user is not None and (now - _cache_time) < _USER_CACHE_TTL:
        return _cached_user

    result = _resolve_current_user()

    _cached_user = result
    _cache_time = now
    return result


def _resolve_current_user() -> Dict[str, str]:
    """Resolve current user using platform-specific methods.

    Returns:
        Dict with "username" and "source" keys
    """
    system = platform.system()

    if system == "Windows":
        return _get_windows_user()
    elif system == "Darwin":
        return _get_macos_user()
    else:
        return _get_linux_user()


def _get_windows_user() -> Dict[str, str]:
    """Resolve active console session user on Windows.

    Tries WTS API for service-context compatibility, falls back to os.getlogin().

    Returns:
        Dict with "username" and "source"
    """
    # Try WTS API (works in service context)
    try:
        import ctypes
        import ctypes.wintypes

        wtsapi = ctypes.windll.wtsapi32
        kernel32 = ctypes.windll.kernel32

        WTS_CURRENT_SERVER_HANDLE = None
        WTSUserName = 5  # WTSInfoClass enum value

        # Get active console session ID
        session_id = kernel32.WTSGetActiveConsoleSessionId()

        buf = ctypes.c_wchar_p()
        buf_size = ctypes.c_ulong()

        success = wtsapi.WTSQuerySessionInformationW(
            WTS_CURRENT_SERVER_HANDLE,
            session_id,
            WTSUserName,
            ctypes.byref(buf),
            ctypes.byref(buf_size),
        )

        if success and buf.value:
            username = buf.value
            wtsapi.WTSFreeMemory(buf)
            if username:
                return {"username": username, "source": "wts"}
    except Exception:
        pass

    # Fallback: os.getlogin()
    try:
        username = os.getlogin()
        return {"username": username, "source": "os.getlogin"}
    except OSError:
        pass

    # Final fallback: getpass
    try:
        username = getpass.getuser()
        return {"username": username, "source": "getpass"}
    except Exception:
        pass

    return {"username": "unknown", "source": "fallback"}


def _get_macos_user() -> Dict[str, str]:
    """Resolve active console user on macOS.

    Parses `who` output to find the console session user.

    Returns:
        Dict with "username" and "source"
    """
    try:
        result = subprocess.run(
            ["who"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            # Parse first line: username  console  ...
            first_line = result.stdout.strip().splitlines()[0]
            parts = first_line.split()
            if parts:
                return {"username": parts[0], "source": "who"}
    except Exception:
        pass

    # Fallback
    try:
        username = getpass.getuser()
        return {"username": username, "source": "getpass"}
    except Exception:
        pass

    return {"username": "unknown", "source": "fallback"}


def _get_linux_user() -> Dict[str, str]:
    """Resolve active console user on Linux.

    Parses `who` output looking for local display (:0, tty1) entries.

    Returns:
        Dict with "username" and "source"
    """
    try:
        result = subprocess.run(
            ["who"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().splitlines()
            # Look for local display session first
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    # Check for local display indicators
                    line_str = " ".join(parts)
                    if "(:0)" in line_str or "(tty1)" in line_str or ":0" in line_str:
                        return {"username": parts[0], "source": "who-display"}

            # Fallback: first line of who output
            parts = lines[0].split()
            if parts:
                return {"username": parts[0], "source": "who"}
    except Exception:
        pass

    # Fallback
    try:
        username = getpass.getuser()
        return {"username": username, "source": "getpass"}
    except Exception:
        pass

    return {"username": "unknown", "source": "fallback"}

```


### File: devise-eye\implementation_context.md
```md
# Devise Desktop Agent - Implementation Context

This document outlines the complete current state of the Devise Desktop Agent implementation (`devise-eye`), detailing the modules that have been built, their specific responsibilities, how they integrate with Firebase, and the expected database schema.

## 1. Core Architecture & Main Loop (`main.py`)
The main entry point uses an asynchronous, continuous monitoring loop (`asyncio`).
- **Initialization**: Loads configuration, checks the system environment, and initializes all subsystems (DNS, networking, registry, monitoring).
- **Control Flow**: Enters an infinite loop `_run_detection_cycle()` that orchestrates process monitoring, network detection, evaluation against the AI tool registry, and reporting.
- **Graceful Shutdown**: Intercepts `SIGINT` (Ctrl+C) and `SIGTERM` to flush queues and shut down cleanly.

## 2. Detection & Network Monitoring
- **Connection Detection (`detector.py`)**: Uses `psutil` to list active IPv4/IPv6 network connections. Identifies remote IPs and ports connected by local processes. Maintains a sliding window TTL cache (`_seen_connections`) to avoid processing the same active connection repeatedly within a short timeframe.
- **Process Resolution (`process_resolver.py`)**: Maps connection PIDs to their executable path, process name, and tracks `bytes_read`/`bytes_write` to measure data flow.

## 3. DNS & Domain Resolution
- **Standard DNS (`dns_resolver.py`)**: Uses local system DNS (`socket.getnameinfo`) for reverse lookups to acquire hostnames from IPs.
- **DoH Resolver (`doh_resolver.py`)**: Implements DNS-over-HTTPS (using Cloudflare `1.1.1.1` and Google `8.8.8.8` as fallback) for privacy-preserving, bypass-resistant hostname resolution.
- **Registry & Pre-resolution (`registry.py`)**: Loads a local `.json` or `.csv` catalog of known AI tools (e.g., ChatGPT, Claude) with metadata (category, risk level, vendor). It actively "pre-resolves" known domains to IPs on startup to ensure rapid matching without triggering DNS queries during the detection loop.

## 4. Evaluation & Deduplication
- **Matching Engine (`detector.py` / `registry.py`)**: Matches resolved connection hostnames against the pre-loaded AI tool catalog.
- **Deduplication (`deduplicator.py`)**: Evaluates tool usage and implements a moving window to prevent spamming the backend with duplicate events for continuous/keep-alive connections.

## 5. Metadata, Context & Formatting
- **Identity Resolver (`identity.py`)**: Extracts system context (OS version, hostname) and reads the `config.json` to assign the correct `org_id` and specific active user data to events.
- **Frequency Tracker (`frequency_tracker.py`)**: Monitors how often domains are accessed within a sliding window to tag anomalous high-frequency behaviors.
- **Event Builder (`event_builder.py`)**: Aggregates connection, process, identity, and risk data into the strict JSON schema required by the Firestore `detection_events` collection.

## 6. Firebase Integration & Persistence
- **Service Account Auth (`reporter.py`)**: The agent authenticates directly with GCP/Firebase using a Service Account JSON key (`credentials=service_account.Credentials.from_service_account_file()`). This bypasses the need for interactive user login on the endpoint.
- **Firestore REST API (`reporter.py`)**: Instead of the heavy `firebase-admin` SDK (which causes issues in standalone Windows binaries), the agent uses the lightweight `google-auth` library alongside `httpx` to POST documents directly to the Firestore REST API endpoint (`https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/...`).
- **Offline Queuing (`event_queue.py`)**: Provides robust buffering using SQLite (falling back to unencrypted if `pysqlcipher3` is unavailable). If an event report fails (e.g., no internet), it's stored locally. The `reporter.py` attempts to flush this queue sequentially when connectivity is restored.

## 7. Advanced Monitoring (Phase 2 Modules)
- **Firewall Policy Enforcer (`firewall_monitor.py`)**: Periodically polls the `org_settings/firewall_rules` document via REST. If a monitored process matches a "blocked" policy, it uses `psutil` to aggressively terminate the process.
- **Sensitivity Monitor (`sensitivity_monitor.py`)**: Optionally polls the active foreground window title (via `pywin32`) and clipboard content (via `pyperclip`) at the time of an AI tool detection to assess the risk context of data being shared.
- **Heartbeat Sender (`heartbeat.py`)**: Periodically fires an empty "liveness" ping to update the user's `last_active` timestamp.
- **Liveness Monitor (`liveness_monitor.py`)**: Tracks internal execution loops to detect suspicious gaps (e.g., if the user temporarily suspended the agent process to bypass logging).
- **Tamper Guard (`tamper_guard.py`)**: Checks the executable's hash against expected signatures to detect binary modification.

## 8. Database Schema (Firestore)

The agent interacts primarily with the following Firestore structure configured in project `steadfast-wares-481309-m5`:

### Collection: `detection_events`
The core log of all intercepted AI tool usage.
```json
{
  "event_id": "uuid4_string",
  "org_id": "org_ZNBbHTCO",           // Matches dashboard organization
  "timestamp": "2026-03-17T12:00:00Z",// ISO-8601 UTC
  "tool_name": "ChatGPT",
  "category": "chatbot",
  "vendor": "OpenAI",
  "risk_level": "low|medium|high",
  "process_name": "chrome.exe",
  "process_path": "C:\\Program Files\\...",
  "domain": "chatgpt.com",
  "remote_ip": "104.18.2.161",
  "remote_port": 443,
  "bytes_read": 1048576,
  "bytes_write": 2048,
  "device_id": "Machine-Hostname-UUID",
  "os_version": "Windows 10",
  "user_email": "yashmarlecha13@gmail.com",
  "department": "Engineering",
  "is_approved": true,
  "is_anonymized": false
}
```

### Collection: `org_settings` -> Document: `firewall_rules` (Polled)
Used by the agent's `firewall_monitor.py` to enforce local blocking.
```json
{
  "firewall_rules": {
    "block_chatgpt": {
      "target": "ChatGPT",
      "action": "block"
    }
  }
}
```

### Collection: `organizations` & `profiles` (Context)
While the agent doesn't write directly to these (this is handled by the Dashboard), the agent *must* provide an `org_id` in its events that perfectly matches a document ID in `organizations` to ensure the data is visible to the correct users in the dashboard. The agent pulls this `org_id` from local configuration (`C:\ProgramData\Devise\config.json`).

```


### File: devise-eye\list_all_profiles.py
```py
import firebase_admin
from firebase_admin import credentials, firestore

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Listing all Profiles in Firestore...")
profiles = db.collection('profiles').get()

if not profiles:
    print("No profiles found.")
else:
    for p in profiles:
        data = p.to_dict()
        print(f"UID: {p.id}")
        print(f"  Email: {data.get('email')}")
        print(f"  Org ID: {data.get('org_id')}")
        print("-" * 20)

```


### File: devise-eye\liveness_monitor.py
```py
"""Liveness monitor for kill/suspend detection (FR-29).

Writes periodic heartbeat timestamps to disk. On next startup, detects
suspicious gaps that indicate the agent was killed or suspended.
"""

import json
import logging
import os
import platform
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class GapResult:
    """Result of a liveness gap check.

    Attributes:
        gap_seconds: Seconds elapsed since last liveness write
        last_seen: Datetime of last recorded liveness write
        suspicious: True if gap >> poll_interval (potential kill/suspend)
    """

    gap_seconds: float
    last_seen: datetime
    suspicious: bool


class LivenessMonitor:
    """Monitors agent liveness by writing periodic heartbeat files.

    Detects unexpected gaps between runs (kill signals, suspend, crash)
    by comparing the last recorded timestamp against the expected poll interval.
    """

    LIVENESS_FILE = "liveness.json"

    def __init__(self, poll_interval: int = 30, version: str = "1.0.0"):
        """Initialize liveness monitor.

        Args:
            poll_interval: Expected interval between writes in seconds
            version: Agent version string for liveness record
        """
        self._poll_interval = poll_interval
        self._version = version
        self._liveness_path = self._get_liveness_path()

    def _get_liveness_path(self) -> Path:
        """Get platform-specific liveness file path.

        Returns:
            Path to liveness.json
        """
        system = platform.system()
        if system == "Windows":
            base = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
        elif system == "Darwin":
            base = str(Path.home() / "Library" / "Application Support")
        else:
            base = os.environ.get(
                "XDG_DATA_HOME", str(Path.home() / ".local" / "share")
            )

        d = Path(base) / "Devise"
        d.mkdir(parents=True, exist_ok=True)
        return d / self.LIVENESS_FILE

    def write_liveness(self) -> None:
        """Write current timestamp to liveness file.

        Called each detection cycle to track agent heartbeat.
        Failures are logged but not raised.
        """
        try:
            data = {
                "last_seen": datetime.now(timezone.utc).isoformat(),
                "version": self._version,
                "pid": os.getpid(),
            }
            self._liveness_path.write_text(json.dumps(data))
        except Exception as e:
            logger.warning(f"Failed to write liveness: {e}")

    def check_gap(self) -> Optional[GapResult]:
        """Check for suspicious gap since last liveness write.

        Called on startup to detect if agent was killed or suspended.
        Returns None if no liveness file exists (first run).

        Returns:
            GapResult if gap exceeds 2x poll_interval, None otherwise
        """
        if not self._liveness_path.exists():
            logger.debug("No liveness file found (first run or clean install)")
            return None

        try:
            data = json.loads(self._liveness_path.read_text())
            last_seen_str = data.get("last_seen")
            if not last_seen_str:
                return None

            last_seen = datetime.fromisoformat(last_seen_str)
            now = datetime.now(timezone.utc)
            gap = (now - last_seen).total_seconds()

            # Normal threshold: 2x poll_interval (accounts for shutdown/restart)
            threshold = self._poll_interval * 2

            if gap > threshold:
                # Suspicious if gap is > 10x poll_interval
                suspicious = gap > self._poll_interval * 10
                logger.info(
                    f"Liveness gap detected: {gap:.1f}s "
                    f"(threshold={threshold}s, suspicious={suspicious})"
                )
                return GapResult(
                    gap_seconds=gap,
                    last_seen=last_seen,
                    suspicious=suspicious,
                )

        except Exception as e:
            logger.warning(f"Failed to check liveness gap: {e}")

        return None

```


### File: devise-eye\main.py
```py
"""Devise Desktop Agent - Main Entry Point."""

import asyncio
import signal
import sys
import logging
import os
from pathlib import Path
from typing import Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DeviseAgent:
    """Main Devise Desktop Agent application."""

    def __init__(self, config_path: Optional[str] = None):
        """Initialize the agent.

        Args:
            config_path: Optional config file path
        """
        from config import get_config, ConfigPoller
        from identity import get_identity
        from detector import create_detector
        from process_resolver import create_process_resolver
        from dns_resolver import create_resolver
        from registry import create_registry
        from deduplicator import create_deduplicator
        from event_builder import create_event_builder
        from reporter import create_reporter
        from event_queue import create_event_queue
        from heartbeat import create_heartbeat_sender
        from frequency_tracker import FrequencyTracker
        from liveness_monitor import LivenessMonitor
        from tamper_guard import TamperGuard
        from firewall_monitor import create_firewall_monitor
        from sensitivity_monitor import create_sensitivity_monitor

        # Load configuration
        self._config = get_config(config_path)

        # Initialize components
        self._identity_resolver = get_identity(config_path)

        # Initialize process resolver for FR-06, FR-07, FR-11
        self._process_resolver = create_process_resolver()

        # Initialize queue for FR-18 (offline buffering)
        # Pass api_key + device_id for encrypted queue key derivation
        _api_key = self._config.api_key or "dev-api-key"
        _device_id = self._config.device_id or self._identity_resolver.device_id
        _org_id = self._config.org_id or "local-org"
        self._queue = create_event_queue(
            encrypted=True,
            api_key=_api_key,
            device_id=_device_id,
        )

        # Initialize DNS resolver — DoH if enabled (FR-09), else system DNS
        if self._config.doh_enabled:
            try:
                from doh_resolver import create_doh_resolver

                self._dns_resolver = create_doh_resolver()
                logger.info("DNS-over-HTTPS resolver active (Cloudflare primary)")
            except Exception as e:
                logger.warning(
                    f"DoH resolver init failed, falling back to system DNS: {e}"
                )
                self._dns_resolver = create_resolver()
        else:
            self._dns_resolver = create_resolver()

        # Initialize detector with process resolver
        self._detector = create_detector(
            self._config.poll_interval, process_resolver=self._process_resolver,
            dedup_window=self._config.deduplication_window
        )
        self._registry = create_registry(update_url=self._config.registry_update_url)
        self._registry.preload_dns()
        
        self._deduplicator = create_deduplicator(self._config.deduplication_window)
        self._event_builder = create_event_builder(
            self._identity_resolver.identity,
            _device_id,
            _org_id
        )

        # Initialize reporter with queue for FR-17 (retry logic)
        self._reporter = create_reporter(
            project_id=self._config.firebase_project_id or "dev-project",
            service_account_path=self._config.service_account_path or "service_account.json",
            queue=self._queue,
        )

        # Initialize heartbeat for FR-20
        self._heartbeat = create_heartbeat_sender(
            device_id=self._identity_resolver.device_id,
            agent_version=self._config.agent_version,
            api_key=_api_key,
            event_endpoint=self._config.event_endpoint,
            queue=self._queue,
        )

        # Phase 3: Advanced modules
        self._frequency_tracker = FrequencyTracker()
        self._liveness_monitor = LivenessMonitor(
            poll_interval=self._config.poll_interval,
            version=self._config.agent_version,
        )
        self._tamper_guard = TamperGuard()
        
        # Initialize Phase 2 Advanced Features
        self._firewall_monitor = create_firewall_monitor(
            project_id=self._config.firebase_project_id or "dev-project",
            org_id=_org_id,
            service_account_path=self._config.service_account_path or "service_account.json"
        )
        self._sensitivity_monitor = create_sensitivity_monitor()

        # Initialize config poller for FR-30 (remote config)
        self._config_poller: Optional[ConfigPoller] = None
        if self._config.remote_config_enabled:
            self._config_poller = ConfigPoller(
                self._config,
                self._identity_resolver.device_id,
            )

        self._running = False
        self._shutdown_event = asyncio.Event()

        # Setup signal handlers
        self._setup_signal_handlers()

    def _setup_signal_handlers(self) -> None:
        """Setup graceful shutdown signal handlers."""
        if sys.platform != "win32":
            signal.signal(signal.SIGTERM, self._handle_shutdown)
            signal.signal(signal.SIGINT, self._handle_shutdown)

    def _handle_shutdown(self, signum, frame) -> None:
        """Handle shutdown signals."""
        logger.info(f"Received signal {signum}, initiating graceful shutdown...")
        self._running = False
        self._shutdown_event.set()

    async def _check_registry_updates(self) -> None:
        """Check for registry updates on startup."""
        if self._config.registry_update_url:
            try:
                await self._registry.check_for_updates()
            except Exception as e:
                logger.warning(f"Registry update check failed: {e}")

    async def _check_remote_config(self) -> None:
        """Check for remote config updates."""
        poller = self._config_poller
        if poller and poller.should_poll():
            try:
                await poller.fetch_config()
            except Exception as e:
                logger.warning(f"Remote config poll failed: {e}")

    async def _flush_queue(self) -> None:
        """Flush queued events to backend."""
        if self._queue.get_queue_depth() > 0:
            logger.info(f"Flushing {self._queue.get_queue_depth()} queued events")
            try:
                await self._reporter.flush_queue()
            except Exception as e:
                logger.warning(f"Queue flush failed: {e}")

    async def _send_tamper_alert(self, result) -> None:
        """Send tamper detection alert to backend (fire-and-forget).

        Args:
            result: TamperResult from TamperGuard.check_integrity()
        """
        import httpx

        url = f"{self._config.backend_url}/api/tamper-alert"
        payload = {
            "device_id": self._identity_resolver.device_id,
            "actual_hash": result.actual_hash,
            "expected_hash": result.expected_hash,
            "message": result.message,
            "timestamp": datetime.utcnow().isoformat(),
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    url,
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self._config.api_key or 'dev-api-key'}",
                        "Content-Type": "application/json",
                    },
                )
                logger.warning(f"Tamper alert sent (status={response.status_code})")
        except Exception as e:
            logger.error(f"Failed to send tamper alert: {e}")

    async def _send_gap_event(self, gap) -> None:
        """Send agent gap event to backend.

        Args:
            gap: GapResult from LivenessMonitor.check_gap()
        """
        import httpx

        url = f"{self._config.backend_url}/api/event"
        payload = {
            "type": "agent_gap",
            "device_id": self._identity_resolver.device_id,
            "gap_seconds": gap.gap_seconds,
            "last_seen": gap.last_seen.isoformat(),
            "suspicious": gap.suspicious,
            "timestamp": datetime.utcnow().isoformat(),
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    url,
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self._config.api_key or 'dev-api-key'}",
                        "Content-Type": "application/json",
                    },
                )
                logger.info(
                    f"Agent gap event sent: {gap.gap_seconds:.1f}s gap "
                    f"(suspicious={gap.suspicious}, status={response.status_code})"
                )
        except Exception as e:
            logger.warning(f"Failed to send gap event: {e}")

    async def _process_connection(self, connection: dict) -> None:
        """Process a single connection.

        Args:
            connection: Connection dict from detector
        """
        remote_ip = connection.get("remote_addr")
        pid = connection.get("pid")

        if not remote_ip:
            return

        # Phase 1 Match: Try direct IP match FIRST for CDN tools like ChatGPT
        entry = self._registry.find_match_by_ip(remote_ip)
        
        # Phase 2 Match: Fall back to reverse DNS + hostname match
        if not entry:
            hostname = self._dns_resolver.reverse_lookup(remote_ip)
            if hostname:
                entry = self._registry.find_match(hostname)

        if not entry:
            logger.debug(f"No registry match for IP {remote_ip}")
            return

        # Check deduplication
        if not self._deduplicator.should_report(entry.tool_name, str(pid)):
            return

        # Get process name and path (FR-06, FR-07)
        process_name = connection.get("process_name", "unknown")
        process_path = connection.get("process_path", "")

        if not process_name or process_name == "unknown":
            if pid:
                process_info = self._detector.get_process_info(pid)
                process_name = process_info.get("process_name", "unknown")
                process_path = process_info.get("process_path", "")

        # Get I/O counters (FR-11)
        bytes_read = None
        bytes_write = None
        if pid:
            try:
                proc_info = self._process_resolver.resolve_with_io(pid)
                bytes_read = proc_info.bytes_read
                bytes_write = proc_info.bytes_write
            except Exception:
                pass

        # Check local firewall policy
        is_blocked = self._firewall_monitor.is_blocked(entry.domain)
        
        # Get context sensitivity score
        sensitivity_score = self._sensitivity_monitor.get_current_score()

        # Track connection frequency (FR-10)
        freq_result = self._frequency_tracker.record(entry.domain)

        # Build event with process path (FR-07) + analytics fields (FR-10, FR-11)
        event = self._event_builder.build_event(
            tool_name=entry.tool_name,
            domain=entry.domain,
            category=entry.category,
            vendor=entry.vendor,
            risk_level=entry.risk_level,
            process_name=process_name or "unknown",
            process_path=process_path or "",
            is_approved=entry.enterprise_flag,
            is_blocked=is_blocked,
            sensitivity_score=sensitivity_score,
            connection_frequency=freq_result.count_5min,
            high_frequency=freq_result.high_frequency,
            bytes_read=bytes_read,
            bytes_write=bytes_write,
        )

        # Update heartbeat with last detection time (FR-20)
        self._heartbeat.update_last_detection(datetime.utcnow())

        # Report event (with retry logic - FR-17)
        success = await self._reporter.report_event(event)

        if success:
            logger.info(f"Reported: {entry.tool_name} from {process_name}")
        else:
            logger.warning(f"Failed to report: {entry.tool_name}, queued for retry")

    async def _detection_loop(self) -> None:
        """Main detection loop - runs every poll_interval seconds."""
        heartbeat_counter = 0
        config_check_counter = 0

        logger.info(
            f"Starting detection loop (interval: {self._config.poll_interval}s)"
        )

        while self._running:
            try:
                # Check remote config periodically (every ~5 minutes)
                config_check_counter += 1
                if config_check_counter >= 10:  # Every ~5 minutes
                    await self._check_remote_config()
                    config_check_counter = 0

                # Send heartbeat periodically (every ~5 minutes)
                heartbeat_counter += 1
                if heartbeat_counter >= 10:  # Every ~5 minutes (10 * 30s)
                    try:
                        await self._heartbeat.send_heartbeat()
                    except Exception as e:
                        logger.warning(f"Heartbeat failed: {e}")
                    heartbeat_counter = 0

                    # Also try to flush queue on heartbeat
                    await self._flush_queue()

                # Get new connections
                connections = self._detector.run_detection_cycle()

                logger.debug(f"Found {len(connections)} new connections")

                # Process each connection
                for connection in connections:
                    await self._process_connection(connection)

                # Cleanup old deduplication entries
                self._deduplicator.cleanup_old_entries()

                # Write liveness heartbeat (FR-29)
                self._liveness_monitor.write_liveness()

            except Exception as e:
                logger.error(f"Error in detection loop: {e}")

            # Wait for next cycle or shutdown
            try:
                await asyncio.wait_for(
                    self._shutdown_event.wait(), timeout=self._config.poll_interval
                )
                # Shutdown was requested
                break
            except asyncio.TimeoutError:
                # Normal timeout - continue loop
                continue

    async def run(self) -> None:
        """Run the agent."""
        logger.info("Devise Desktop Agent starting...")

        # Start config poller
        poller = self._config_poller
        if poller:
            await poller.start()
            
        # Start Phase 2 background monitors
        self._firewall_monitor.start()
        self._sensitivity_monitor.start()

        # Phase 3: Check for liveness gap (FR-29) — detect unexpected kill/suspend
        gap = self._liveness_monitor.check_gap()
        if gap:
            logger.warning(
                f"Liveness gap detected: {gap.gap_seconds:.1f}s "
                f"(suspicious={gap.suspicious})"
            )
            # Fire-and-forget gap event (don't block startup)
            asyncio.ensure_future(self._send_gap_event(gap))

        # Phase 3: Check binary integrity (FR-28)
        tamper_result = self._tamper_guard.check_integrity()
        if not tamper_result.ok:
            logger.error(f"Tamper check failed: {tamper_result.message}")
            # Fire-and-forget tamper alert (don't block startup)
            asyncio.ensure_future(self._send_tamper_alert(tamper_result))

        # Check for registry updates
        await self._check_registry_updates()

        logger.info(f"Registry loaded with {self._registry.entry_count} entries")
        logger.info(f"Identity: {self._identity_resolver.user_email}")
        logger.info(f"Device: {self._identity_resolver.device_id}")
        logger.info(f"Queue depth: {self._queue.get_queue_depth()}")
        logger.info(f"DoH enabled: {self._config.doh_enabled}")

        # Send initial heartbeat
        try:
            await self._heartbeat.send_heartbeat()
        except Exception as e:
            logger.warning(f"Initial heartbeat failed: {e}")

        self._running = True

        try:
            await self._detection_loop()
        finally:
            # Final flush on shutdown
            await self._flush_queue()
            await self._reporter.close()

            # Stop config poller
            poller = self._config_poller
            if poller:
                await poller.stop()
                
            # Stop Phase 2 background monitors
            self._firewall_monitor.stop()
            self._sensitivity_monitor.stop()

            logger.info("Devise Desktop Agent stopped")

    def start(self) -> None:
        """Start the agent (sync wrapper)."""
        try:
            asyncio.run(self.run())
        except KeyboardInterrupt:
            logger.info("Agent interrupted by user")
        except Exception as e:
            logger.error(f"Agent error: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    # Determine config path
    config_path = os.environ.get("DEVISE_CONFIG_PATH") or None

    agent = DeviseAgent(config_path)
    agent.start()


if __name__ == "__main__":
    main()

```


### File: devise-eye\process_resolver.py
```py
"""Process resolution module for Devise Desktop Agent.

Provides detailed process attribution including executable path and
I/O counter estimation (FR-11). Note: io_counters() returns disk I/O bytes,
not network bytes — used as a proxy for process activity.
"""

import logging
import psutil
from dataclasses import dataclass, field
from typing import Tuple, Optional, Dict

logger = logging.getLogger(__name__)


@dataclass
class ProcessInfo:
    """Resolved process information.

    Attributes:
        name: Process name (e.g., "chrome.exe")
        path: Full executable path or empty string if unavailable
        pid: Process ID
        bytes_read: Disk bytes read by process (proxy for activity; None if unavailable)
        bytes_write: Disk bytes written by process (proxy for activity; None if unavailable)
    """

    name: str
    path: str
    pid: int
    bytes_read: Optional[int] = None
    bytes_write: Optional[int] = None


# Mapping of process names to human-readable labels
PROCESS_NAME_MAPPING: Dict[str, str] = {
    "python.exe": "Python",
    "python3.exe": "Python",
    "python": "Python",
    "python3": "Python",
    "node.exe": "Node.js",
    "node": "Node.js",
    "chrome.exe": "Google Chrome",
    "msedge.exe": "Microsoft Edge",
    "firefox.exe": "Mozilla Firefox",
    "safari": "Safari",
    "code.exe": "Visual Studio Code",
    "cursor.exe": "Cursor IDE",
    "slack.exe": "Slack",
    "teams.exe": "Microsoft Teams",
    "zoom.exe": "Zoom",
    "discord.exe": "Discord",
    "postman.exe": "Postman",
    "curl.exe": "cURL",
    "wget.exe": "Wget",
    "git.exe": "Git",
    "powershell.exe": "PowerShell",
    "cmd.exe": "Command Prompt",
    "explorer.exe": "Windows Explorer",
    "brave.exe": "Brave Browser",
    "opera.exe": "Opera",
    "vivaldi.exe": "Vivaldi",
    "spotify.exe": "Spotify",
    "slack": "Slack",
    "teams": "Microsoft Teams",
    "zoom": "Zoom",
    "code": "Visual Studio Code",
    "cursor": "Cursor IDE",
    "chrome": "Google Chrome",
    "firefox": "Mozilla Firefox",
    "msedge": "Microsoft Edge",
    "Safari": "Safari",
    "postman": "Postman",
    "git": "Git",
    "docker.exe": "Docker Desktop",
    "docker": "Docker Desktop",
    "idea.exe": "IntelliJ IDEA",
    "idea64.exe": "IntelliJ IDEA",
    "pycharm64.exe": "PyCharm",
    "pycharm": "PyCharm",
    "webstorm64.exe": "WebStorm",
    "rider64.exe": "Rider",
    "goland64.exe": "GoLand",
    "datagrip64.exe": "DataGrip",
}


def get_human_readable_name(process_name: str) -> str:
    """Get human-readable name for a process.

    Args:
        process_name: Short process name (e.g., "python.exe")

    Returns:
        Human-readable name or original if not found in mapping
    """
    return PROCESS_NAME_MAPPING.get(process_name, process_name)


class ProcessResolver:
    """Resolves process information from PID."""

    def __init__(self):
        """Initialize process resolver."""
        self._cache: Dict[int, Tuple[str, str]] = {}
        self._cache_max_size = 1000

    def resolve(self, pid: int) -> Tuple[str, str, int]:
        """Resolve process name and executable path from PID.

        Args:
            pid: Process ID

        Returns:
            Tuple of (process_name, process_path, pid)
            process_path is empty string if unavailable
        """
        # Check cache first
        if pid in self._cache:
            name, path = self._cache[pid]
            return name, path, pid

        process_name = "unknown"
        process_path = None

        try:
            process = psutil.Process(pid)
            process_name = process.name()
            try:
                process_path = process.exe()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                # Can't get exe path - common for some system processes
                process_path = ""
            except Exception as e:
                logger.debug(f"Error getting exe for PID {pid}: {e}")
                process_path = ""

        except psutil.NoSuchProcess:
            logger.debug(f"Process {pid} not found (terminated)")
            process_name = "unknown"
            process_path = ""

        except psutil.AccessDenied:
            logger.debug(f"Access denied for process {pid}")
            process_name = "unknown"
            process_path = ""

        except Exception as e:
            logger.warning(f"Error resolving process {pid}: {e}")
            process_name = "unknown"
            process_path = ""

        # Cache the result (store as string, use empty string for None)
        if len(self._cache) < self._cache_max_size:
            self._cache[pid] = (process_name, process_path)

        return process_name, process_path, pid

    def resolve_with_io(self, pid: int) -> ProcessInfo:
        """Resolve process info including I/O counters.

        I/O counters represent disk bytes (not network) — used as a proxy
        for process activity level. Returns None for bytes fields if the OS
        denies access or the process no longer exists.

        Args:
            pid: Process ID

        Returns:
            ProcessInfo dataclass with name, path, pid, and optional I/O bytes
        """
        process_name, process_path, pid = self.resolve(pid)
        bytes_read: Optional[int] = None
        bytes_write: Optional[int] = None

        try:
            proc = psutil.Process(pid)
            io = proc.io_counters()
            bytes_read = io.read_bytes
            bytes_write = io.write_bytes
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
        except AttributeError:
            # io_counters() not available on all platforms
            pass
        except Exception as e:
            logger.debug(f"IO counter error for PID {pid}: {e}")

        return ProcessInfo(
            name=process_name,
            path=process_path,
            pid=pid,
            bytes_read=bytes_read,
            bytes_write=bytes_write,
        )

    def resolve_name_only(self, pid: int) -> str:
        """Resolve just the process name.

        Args:
            pid: Process ID

        Returns:
            Process name or "unknown"
        """
        name, _, _ = self.resolve(pid)
        return name

    def resolve_path_only(self, pid: int) -> Optional[str]:
        """Resolve just the process executable path.

        Args:
            pid: Process ID

        Returns:
            Process path or None
        """
        _, path, _ = self.resolve(pid)
        return path

    def clear_cache(self) -> None:
        """Clear the process resolution cache."""
        self._cache.clear()


def create_process_resolver() -> ProcessResolver:
    """Create a process resolver instance.

    Returns:
        ProcessResolver instance
    """
    return ProcessResolver()

```


### File: devise-eye\registry.py
```py
"""AI Tools Registry module for Devise Desktop Agent."""

import json
import logging
import os
import socket
from typing import List, Dict, Optional, Any
from pathlib import Path
import httpx


logger = logging.getLogger(__name__)


class RegistryEntry:
    """Represents a single AI tool in the registry."""

    def __init__(self, data: Dict[str, Any]):
        """Initialize registry entry.

        Args:
            data: Entry data from registry
        """
        self.domain = data.get("domain", "")
        self.tool_name = data.get("tool_name", "")
        self.category = data.get("category", "unknown")
        self.vendor = data.get("vendor", "unknown")
        self.risk_level = data.get("risk_level", "medium")
        self.enterprise_flag = data.get("enterprise_flag", False)
        self.api_domain_flag = data.get("api_domain_flag", False)

    def matches(self, hostname: str) -> bool:
        """Check if hostname matches this entry.

        Args:
            hostname: Hostname to check

        Returns:
            True if hostname matches
        """
        if not hostname or not self.domain:
            return False

        hostname_lower = hostname.lower()
        domain_lower = self.domain.lower()

        # Exact match
        if hostname_lower == domain_lower:
            return True

        # Wildcard match (subdomain)
        if hostname_lower.endswith("." + domain_lower):
            return True

        return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dict representation
        """
        return {
            "domain": self.domain,
            "tool_name": self.tool_name,
            "category": self.category,
            "vendor": self.vendor,
            "risk_level": self.risk_level,
            "enterprise_flag": self.enterprise_flag,
            "api_domain_flag": self.api_domain_flag,
        }


class Registry:
    """AI Tools Registry with matching and update support."""

    def __init__(
        self, registry_path: Optional[str] = None, update_url: Optional[str] = None
    ):
        """Initialize registry.

        Args:
            registry_path: Path to bundled registry JSON
            update_url: URL to check for registry updates
        """
        self._entries: List[RegistryEntry] = []
        self._update_url = update_url
        self._ip_to_entry: Dict[str, RegistryEntry] = {}  # ip -> entry
        self._load_registry(registry_path)

    def preload_dns(self) -> None:
        """Resolve all registry domains to IPs at startup."""
        for entry in self._entries:
            try:
                results = socket.getaddrinfo(entry.domain, None)
                for r in results:
                    ip = r[4][0]
                    self._ip_to_entry[ip] = entry
            except Exception:
                pass
        logger.info(f"Pre-resolved {len(self._ip_to_entry)} IPs from registry")

    def find_match_by_ip(self, ip: str) -> Optional[RegistryEntry]:
        """Direct IP lookup — works for CDN-hosted tools."""
        return self._ip_to_entry.get(ip)

    def _load_registry(self, registry_path: Optional[str]) -> None:
        """Load registry from bundled file.

        Args:
            registry_path: Path to registry file
        """
        if registry_path is None:
            # Default to bundled registry
            registry_path = self._get_default_registry_path()

        if os.path.exists(registry_path):
            try:
                with open(registry_path, "r") as f:
                    data = json.load(f)

                tools = data.get("tools", [])
                self._entries = [RegistryEntry(t) for t in tools]
                logger.info(f"Loaded {len(self._entries)} entries from registry")

            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"Failed to load registry: {e}")
                self._entries = []
        else:
            logger.warning(f"Registry file not found: {registry_path}")
            self._entries = []

    def _get_default_registry_path(self) -> str:
        """Get default bundled registry path."""
        # Relative to this module
        module_dir = Path(__file__).parent
        return str(module_dir / "data" / "ai_tools_registry.json")

    async def check_for_updates(self) -> bool:
        """Check for registry updates from backend.

        Returns:
            True if updates were applied
        """
        if not self._update_url:
            return False

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(self._update_url)
                response.raise_for_status()

                data = response.json()
                new_entries = [RegistryEntry(t) for t in data.get("tools", [])]

                if new_entries:
                    self._entries = new_entries
                    logger.info(f"Updated registry with {len(new_entries)} entries")
                    return True

        except Exception as e:
            logger.warning(f"Failed to check for registry updates: {e}")

        return False

    def find_match(self, hostname: str) -> Optional[RegistryEntry]:
        """Find registry entry matching hostname.

        Args:
            hostname: Hostname to match

        Returns:
            Matching RegistryEntry or None
        """
        for entry in self._entries:
            if entry.matches(hostname):
                return entry
        return None

    def find_all_matches(self, hostname: str) -> List[RegistryEntry]:
        """Find all registry entries matching hostname.

        Args:
            hostname: Hostname to match

        Returns:
            List of matching entries
        """
        matches = []
        for entry in self._entries:
            if entry.matches(hostname):
                matches.append(entry)
        return matches

    @property
    def entries(self) -> List[RegistryEntry]:
        """Get all registry entries."""
        return self._entries

    @property
    def entry_count(self) -> int:
        """Get number of entries."""
        return len(self._entries)

    def get_tools_by_category(self, category: str) -> List[RegistryEntry]:
        """Get entries by category.

        Args:
            category: Category to filter by

        Returns:
            List of entries in category
        """
        return [e for e in self._entries if e.category == category]

    def get_tools_by_vendor(self, vendor: str) -> List[RegistryEntry]:
        """Get entries by vendor.

        Args:
            vendor: Vendor to filter by

        Returns:
            List of entries from vendor
        """
        return [e for e in self._entries if e.vendor == vendor]


def create_registry(
    registry_path: Optional[str] = None, update_url: Optional[str] = None
) -> Registry:
    """Create a registry instance.

    Args:
        registry_path: Path to bundled registry
        update_url: URL for registry updates

    Returns:
        Registry instance
    """
    return Registry(registry_path, update_url)

```


### File: devise-eye\reporter.py
```py
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
    """Convert a Python dict to Firestore REST typed fields format.

    Args:
        d: Plain Python dictionary

    Returns:
        Firestore fields dict with typed values
    """
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
        elif hasattr(value, 'strftime') and hasattr(value, 'isoformat'):
            # Convert to RFC 3339 format for Firestore REST API
            ts_str = value.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (value.microsecond // 1000) + "Z"
            fields[key] = {"timestampValue": ts_str}
        elif key == "timestamp" and isinstance(value, str):
            # If it's already a string (e.g. from JSON queue), ensure it's in RFC 3339 format
            # Firestore expects 'Z' suffix and no offset for UTC
            ts_str = value
            if "+" in ts_str:
                ts_str = ts_str.split("+")[0]
            if not ts_str.endswith("Z"):
                ts_str += "Z"
            fields[key] = {"timestampValue": ts_str}
        else:
            # Fallback: convert to string
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
        """Initialize Firestore reporter.

        Args:
            project_id: Firebase/GCP project ID
            service_account_path: Path to service account JSON file
            timeout: Request timeout in seconds
            queue: Optional EventQueue for offline buffering
        """
        self._project_id = project_id
        self._service_account_path = service_account_path
        self._timeout = timeout
        self._queue = queue
        self._client: Optional[httpx.AsyncClient] = None
        self._credentials = None
        self._access_token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None

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
            raise RuntimeError(
                "google-auth not installed. Run: pip install google-auth"
            )
        except FileNotFoundError:
            raise RuntimeError(
                f"Service account file not found: {self._service_account_path}"
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load service account: {e}")

    def _get_access_token(self) -> str:
        """Get a valid OAuth2 access token, refreshing if expired.

        Returns:
            Valid access token string
        """
        self._load_credentials()

        # Check if token is still valid (with 60s buffer)
        now = datetime.utcnow().replace(tzinfo=None)
        if (
            self._credentials.token is not None
            and self._credentials.expiry is not None
            and self._credentials.expiry.replace(tzinfo=None) > now
        ):
            return self._credentials.token

        # Refresh the token
        import google.auth.transport.requests
        import requests as google_requests

        request = google.auth.transport.requests.Request(
            session=google_requests.Session()
        )
        self._credentials.refresh(request)
        logger.debug("OAuth2 access token refreshed")
        return self._credentials.token

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create async HTTP client with current auth token."""
        token = self._get_access_token()

        # Create a fresh client if we don't have one, or refresh headers
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
        """Build Firestore REST URL for a collection."""
        return (
            f"{self.FIRESTORE_BASE}/projects/{self._project_id}"
            f"/databases/(default)/documents/{collection}"
        )

    async def _write_to_firestore(
        self, event: Dict[str, Any], collection: str = "detection_events"
    ) -> bool:
        """Write a single event document to Firestore.

        Args:
            event: Event dict to write
            collection: Firestore collection name

        Returns:
            True if successful
        """
        url = self._build_collection_url(collection)
        body = {"fields": dict_to_firestore_fields(event)}

        for attempt in range(MAX_RETRIES + 1):
            try:
                client = await self._get_client()
                response = await client.post(url, json=body)

                if response.status_code == 401:
                    # Token expired mid-request, force refresh on next attempt
                    logger.warning("Firestore auth 401, refreshing token...")
                    self._credentials.token = None
                    if attempt < MAX_RETRIES:
                        continue

                response.raise_for_status()
                logger.debug(f"Firestore write OK: {response.status_code}")
                return True

            except httpx.HTTPStatusError as e:
                if 400 <= e.response.status_code < 500 and e.response.status_code != 401:
                    logger.warning(
                        f"Firestore client error {e.response.status_code}: {e.response.text[:200]}"
                    )
                    return False
                logger.warning(
                    f"Firestore server error (attempt {attempt + 1}): {e.response.status_code}"
                )
            except httpx.RequestError as e:
                logger.warning(f"Network error (attempt {attempt + 1}): {e}")
            except Exception as e:
                logger.warning(f"Unexpected error (attempt {attempt + 1}): {e}")

            if attempt < MAX_RETRIES:
                backoff = BACKOFF_INTERVALS[attempt]
                logger.info(f"Retrying Firestore write in {backoff}s...")
                await asyncio.sleep(backoff)

        return False

    def set_queue(self, queue) -> None:
        """Set the event queue for offline buffering."""
        self._queue = queue

    async def report_event(
        self, event: Dict[str, Any], collection: str = "detection_events"
    ) -> bool:
        """Report event to Firestore with retry/queue fallback.

        Args:
            event: Event dict to send
            collection: Firestore collection (default: detection_events)

        Returns:
            True if written to Firestore, False if queued or failed
        """
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
        """Report multiple events.

        Args:
            events: List of event dicts

        Returns:
            Dict with success/failure counts
        """
        results = {"success": 0, "failure": 0, "queued": 0}

        for event in events:
            if await self.report_event(event):
                results["success"] += 1
            else:
                results["failure"] += 1

        return results

    async def flush_queue(self) -> Dict[str, int]:
        """Flush queued events to Firestore.

        Returns:
            Dict with success/failure counts
        """
        if not self._queue:
            return {"success": 0, "failure": 0, "skipped": 0}

        results = {"success": 0, "failure": 0, "skipped": 0}
        pending = self._queue.get_pending(limit=BATCH_SIZE)

        if not pending:
            logger.debug("No pending events in queue")
            return results

        logger.info(f"Flushing {len(pending)} queued events to Firestore")

        success_ids = []
        failed_ids = []

        for event in pending:
            queue_id = event.get("_queue_id")
            if await self.report_event(event):
                if queue_id:
                    success_ids.append(queue_id)
                results["success"] += 1
            else:
                if queue_id:
                    failed_ids.append(queue_id)
                results["failure"] += 1

        if success_ids:
            self._queue.mark_success(success_ids)
        if failed_ids:
            self._queue.mark_failed(failed_ids)

        logger.info(
            f"Queue flush done: {results['success']} sent, {results['failure']} failed"
        )
        return results

    async def close(self) -> None:
        """Close HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "FirestoreReporter":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()


# Keep legacy class name as alias for backward compatibility
Reporter = FirestoreReporter


def create_reporter(
    api_key: str = "",
    endpoint: str = "",
    timeout: float = 10.0,
    queue=None,
    project_id: str = "",
    service_account_path: str = "",
) -> FirestoreReporter:
    """Create a Firestore reporter instance.

    Accepts legacy args (api_key, endpoint) for backward compatibility,
    but the Firestore reporter uses project_id and service_account_path.

    Args:
        api_key: (legacy) unused
        endpoint: (legacy) unused
        timeout: Request timeout
        queue: Optional EventQueue
        project_id: Firebase project ID
        service_account_path: Path to service account JSON

    Returns:
        FirestoreReporter instance
    """
    return FirestoreReporter(
        project_id=project_id,
        service_account_path=service_account_path,
        timeout=timeout,
        queue=queue,
    )

```


### File: devise-eye\requirements.txt
```txt
psutil>=5.9.0
dnspython>=2.4.0
APScheduler>=3.10.0
httpx>=0.25.0
python-dotenv>=1.0.0
PyInstaller>=6.0.0
keyring>=24.0.0
google-auth>=2.23.0
pywin32>=306
pyperclip>=1.8.2

```


### File: devise-eye\sensitivity_monitor.py
```py
"""Sensitivity monitor for Devise Desktop Agent.

Monitors clipboard content and active window titles to calculate local
risk scores and determine the sensitivity of data being sent to AI tools.
"""

import logging
import threading
import time
from typing import Dict, Any, Optional

try:
    import pyperclip
    _HAS_PYPERCLIP = True
except ImportError:
    _HAS_PYPERCLIP = False

try:
    import win32gui
    import win32process
    _HAS_WIN32 = True
except ImportError:
    _HAS_WIN32 = False

logger = logging.getLogger(__name__)


class SensitivityMonitor:
    """Monitors clipboard and active windows for sensitive data indicators."""

    # Keywords that suggest sensitive data might be in context
    SENSITIVE_KEYWORDS = [
        "confidential", "internal use only", "secret",
        "ssn", "social security", "password", "credential",
        "salary", "payroll", "financial", "patient data",
        "phi", "pii", "api key", "auth_token"
    ]

    def __init__(self, poll_interval: int = 1):
        """Initialize SensitivityMonitor.

        Args:
            poll_interval: How often to check clipboard/windows (seconds)
        """
        self._poll_interval = poll_interval
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

        self._last_clipboard_content = ""
        self._current_sensitivity_score = 0
        self._last_active_window_title = ""

    def _get_active_window_title(self) -> str:
        """Get the title of the currently focused window on Windows."""
        if not _HAS_WIN32:
            return ""
        try:
            window = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(window)
            return title.lower()
        except Exception as e:
            logger.debug(f"Failed to get active window title: {e}")
            return ""

    def _get_clipboard_content(self) -> str:
        """Get current text from the clipboard."""
        if not _HAS_PYPERCLIP:
            return ""
        try:
            content = pyperclip.paste()
            return content.lower() if content else ""
        except Exception as e:
            logger.debug(f"Failed to read clipboard: {e}")
            return ""

    def _calculate_sensitivity(self, text: str) -> int:
        """Calculate a basic sensitivity score based on keyword matching.
        
        Args:
            text: The text to analyze
            
        Returns:
            Score from 0 to 100 based on hits.
        """
        score = 0
        if not text:
            return score

        for keyword in self.SENSITIVE_KEYWORDS:
            if keyword in text:
                score += 20  # +20 risk per keyword hit

        return min(score, 100)  # Cap at 100

    def _monitor_loop(self):
        """Main loop for polling sensors."""
        logger.info("Sensitivity monitor started.")
        while not self._stop_event.is_set():
            clipboard_text = self._get_clipboard_content()
            window_title = self._get_active_window_title()

            # Optional: only recalculate if changed
            if clipboard_text != self._last_clipboard_content or window_title != self._last_active_window_title:
                clip_score = self._calculate_sensitivity(clipboard_text)
                title_score = self._calculate_sensitivity(window_title)

                # Use the highest risk observed in the current context
                self._current_sensitivity_score = max(clip_score, title_score)

                self._last_clipboard_content = clipboard_text
                self._last_active_window_title = window_title

            self._stop_event.wait(self._poll_interval)
            
        logger.info("Sensitivity monitor stopped.")

    def start(self):
        """Start the monitor thread."""
        if not _HAS_PYPERCLIP and not _HAS_WIN32:
            logger.warning("pyperclip and pywin32 not installed. Sensitivity monitor disabled.")
            return

        if self._thread and self._thread.is_alive():
            return
            
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the monitor thread."""
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=2.0)

    def get_current_score(self) -> int:
        """Retrieve the latest sensitivity risk score.
        
        Returns:
            Int between 0 and 100
        """
        return self._current_sensitivity_score

    def get_context_summary(self) -> Dict[str, Any]:
        """Return a summary of the current sensitive context."""
        return {
            "score": self._current_sensitivity_score,
            "window_title": self._last_active_window_title,
            # We purposely do NOT send raw clipboard data to the backend,
            # only the boolean indicator if it contained sensitive keywords.
            "clipboard_has_sensitive_data": self._calculate_sensitivity(self._last_clipboard_content) > 0
        }


def create_sensitivity_monitor(poll_interval: int = 1) -> SensitivityMonitor:
    """Create a sensitivity monitor instance."""
    return SensitivityMonitor(poll_interval)

```


### File: devise-eye\tamper_guard.py
```py
"""Tamper detection for Devise Desktop Agent binary integrity (FR-28)."""

import hashlib
import sys
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class TamperResult:
    """Result of a tamper integrity check.

    Attributes:
        ok: True if binary matches trusted hash (or first run)
        actual_hash: SHA-256 hash of current binary
        expected_hash: Trusted hash from storage (None if unavailable)
        message: Human-readable status message
    """

    ok: bool
    actual_hash: str
    expected_hash: Optional[str]
    message: str


class TamperGuard:
    """Detects tampering by comparing running binary SHA-256 hash.

    On first run (no trusted hash stored), stores current hash as trusted.
    Subsequent runs compare against stored trusted hash and alert on mismatch.
    """

    HASH_FILE = "binary_hash.txt"  # relative to package data dir

    def compute_hash(self, path: str) -> str:
        """Compute SHA-256 hash of a file.

        Args:
            path: File path to hash

        Returns:
            Hex string SHA-256 digest
        """
        sha256 = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def get_trusted_hash(self) -> Optional[str]:
        """Read trusted hash from keyring, with fallback to hash file.

        Returns:
            Trusted hash hex string or None if not stored
        """
        # Try keyring first
        try:
            import keyring

            val = keyring.get_password("devise-agent", "binary-hash")
            if val:
                return val
        except Exception:
            pass

        # Fallback to file
        hash_path = Path(__file__).parent / "data" / self.HASH_FILE
        if hash_path.exists():
            content = hash_path.read_text().strip()
            # Ignore placeholder text (empty or non-hex content)
            if (
                content
                and len(content) == 64
                and all(c in "0123456789abcdef" for c in content)
            ):
                return content

        return None

    def store_trusted_hash(self, hash_val: str) -> None:
        """Store trusted hash in keyring and hash file.

        Args:
            hash_val: SHA-256 hex string to store as trusted
        """
        # Store in keyring
        try:
            import keyring

            keyring.set_password("devise-agent", "binary-hash", hash_val)
        except Exception as e:
            logger.debug(f"Keyring store failed (non-fatal): {e}")

        # Store in file as fallback
        hash_path = Path(__file__).parent / "data" / self.HASH_FILE
        hash_path.parent.mkdir(parents=True, exist_ok=True)
        hash_path.write_text(hash_val)

    def check_integrity(self) -> TamperResult:
        """Check if running binary matches trusted hash.

        On first run (no trusted hash), stores current hash as trusted.

        Returns:
            TamperResult with ok=True if binary is trusted, ok=False if tampered
        """
        try:
            actual = self.compute_hash(sys.executable)
        except Exception as e:
            logger.warning(f"Failed to hash binary: {e}")
            return TamperResult(
                ok=True,
                actual_hash="",
                expected_hash=None,
                message=f"Hash computation failed (skipping check): {e}",
            )

        expected = self.get_trusted_hash()

        if expected is None:
            # First run — store hash as trusted
            self.store_trusted_hash(actual)
            logger.info("TamperGuard: First run — hash stored as trusted")
            return TamperResult(
                ok=True,
                actual_hash=actual,
                expected_hash=actual,
                message="First run: hash stored as trusted",
            )

        if actual == expected:
            return TamperResult(
                ok=True,
                actual_hash=actual,
                expected_hash=expected,
                message="Binary integrity verified",
            )

        logger.error(
            f"TAMPER DETECTED: binary hash mismatch! "
            f"expected={expected[:16]}... actual={actual[:16]}..."
        )
        return TamperResult(
            ok=False,
            actual_hash=actual,
            expected_hash=expected,
            message=f"TAMPER DETECTED: hash mismatch",
        )

```


### File: devise-eye\__init__.py
```py
# Devise Desktop Agent

```


### File: devise-eye\data\ai_tools_registry.json
```json
{
  "version": "1.0.0",
  "last_updated": "2026-03-17T00:00:00Z",
  "tools": [
    {
      "domain": "chatgpt.com",
      "tool_name": "ChatGPT",
      "category": "Generative AI",
      "vendor": "OpenAI",
      "risk_level": "medium",
      "enterprise_flag": false,
      "api_domain_flag": false
    },
    {
      "domain": "openai.com",
      "tool_name": "OpenAI API / Platform",
      "category": "api",
      "vendor": "OpenAI",
      "risk_level": "high",
      "enterprise_flag": true,
      "api_domain_flag": true
    },
    {
      "domain": "claude.ai",
      "tool_name": "Claude",
      "category": "Generative AI",
      "vendor": "Anthropic",
      "risk_level": "medium",
      "enterprise_flag": false,
      "api_domain_flag": false
    },
    {
      "domain": "anthropic.com",
      "tool_name": "Anthropic Console",
      "category": "api",
      "vendor": "Anthropic",
      "risk_level": "high",
      "enterprise_flag": false,
      "api_domain_flag": true
    },
    {
      "domain": "github.com",
      "tool_name": "GitHub Copilot",
      "category": "Development",
      "vendor": "Microsoft",
      "risk_level": "low",
      "enterprise_flag": true,
      "api_domain_flag": false
    },
    {
      "domain": "gemini.google.com",
      "tool_name": "Google Gemini",
      "category": "Generative AI",
      "vendor": "Google",
      "risk_level": "medium",
      "enterprise_flag": false,
      "api_domain_flag": false
    },
    {
      "domain": "vertexai.googleapis.com",
      "tool_name": "Google Vertex AI",
      "category": "api",
      "vendor": "Google",
      "risk_level": "high",
      "enterprise_flag": true,
      "api_domain_flag": true
    },
    {
      "domain": "midjourney.com",
      "tool_name": "Midjourney",
      "category": "Design/Media",
      "vendor": "Midjourney",
      "risk_level": "medium",
      "enterprise_flag": false,
      "api_domain_flag": false
    },
    {
      "domain": "huggingface.co",
      "tool_name": "Hugging Face",
      "category": "Development",
      "vendor": "Hugging Face",
      "risk_level": "medium",
      "enterprise_flag": false,
      "api_domain_flag": false
    }
  ]
}
```


### File: devise-eye\data\binary_hash.txt
```txt
a2a4eff8d0b0c845284c607d50a3b5b966ac5a3121736a2e38e165bd6644d9fe
```


### File: devise-eye\data\cdn_ip_ranges.json
```json
{
  "version": "1.0.0",
  "updated_at": "2026-03-07",
  "description": "CIDR ranges for AI API CDN providers",
  "ranges": [
    {
      "cdn": "Cloudflare",
      "tool": "OpenAI",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Anthropic",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Google AI",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Cohere",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "AWS CloudFront",
      "tool": "OpenAI",
      "ranges": [
        "18.164.0.0/15",
        "18.208.0.0/12",
        "52.94.76.0/10",
        "54.182.0.0/16",
        "54.192.0.0/16"
      ]
    },
    {
      "cdn": "AWS CloudFront",
      "tool": "Anthropic",
      "ranges": [
        "18.164.0.0/15",
        "18.208.0.0/12",
        "52.94.76.0/10",
        "54.182.0.0/16",
        "54.192.0.0/16"
      ]
    },
    {
      "cdn": "AWS CloudFront",
      "tool": "Hugging Face",
      "ranges": [
        "18.164.0.0/15",
        "18.208.0.0/12",
        "52.94.76.0/10"
      ]
    },
    {
      "cdn": "AWS CloudFront",
      "tool": "Replicate",
      "ranges": [
        "18.164.0.0/15",
        "18.208.0.0/12"
      ]
    },
    {
      "cdn": "Azure CDN",
      "tool": "Microsoft AI",
      "ranges": [
        "13.64.0.0/11",
        "13.96.0.0/13",
        "13.104.0.0/12",
        "20.0.0.0/10",
        "40.64.0.0/10",
        "52.0.0.0/8"
      ]
    },
    {
      "cdn": "Azure CDN",
      "tool": "OpenAI",
      "ranges": [
        "13.64.0.0/11",
        "13.96.0.0/13",
        "13.104.0.0/12",
        "20.0.0.0/10",
        "40.64.0.0/10"
      ]
    },
    {
      "cdn": "Azure CDN",
      "tool": "Mistral AI",
      "ranges": [
        "13.64.0.0/11",
        "20.0.0.0/10",
        "40.64.0.0/10"
      ]
    },
    {
      "cdn": "Azure CDN",
      "tool": "AI21 Labs",
      "ranges": [
        "13.64.0.0/11",
        "20.0.0.0/10"
      ]
    },
    {
      "cdn": "Fastly",
      "tool": "OpenAI",
      "ranges": [
        "23.32.0.0/11",
        "23.32.0.0/12",
        "199.232.0.0/16"
      ]
    },
    {
      "cdn": "Fastly",
      "tool": "Cohere",
      "ranges": [
        "23.32.0.0/11",
        "199.232.0.0/16"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Perplexity",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Together AI",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Meta AI",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    },
    {
      "cdn": "Cloudflare",
      "tool": "Mistral AI",
      "ranges": [
        "13.0.0.0/8",
        "104.16.0.0/12"
      ]
    }
  ],
  "notes": "These ranges are used to attribute CDN IPs back to their origin AI tool. When a connection is detected to a CDN IP, the agent checks if the IP falls within any of these ranges and attributes the traffic to the corresponding tool based on reverse DNS or other signals."
}

```


### File: devise-eye\installers\linux\devise-agent.service
```service
[Unit]
Description=Devise Desktop Agent
Documentation=https://devise.ai
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/opt/devise-agent/devise-agent
Restart=always
RestartSec=10
User=root
Environment=DEVISE_CONFIG_PATH=/etc/devise/config.json
StandardOutput=journal
StandardError=journal
SyslogIdentifier=devise-agent

[Install]
WantedBy=multi-user.target

```


### File: devise-eye\installers\linux\install.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

BINARY_NAME="devise-agent"
INSTALL_DIR="/opt/devise-agent"
CONFIG_DIR="/etc/devise"
SERVICE_FILE="devise-agent.service"

echo "Installing Devise Desktop Agent..."

# Check root
if [[ $EUID -ne 0 ]]; then
    echo "Error: must run as root" >&2
    exit 1
fi

# Install binary
mkdir -p "$INSTALL_DIR"
cp "$BINARY_NAME" "$INSTALL_DIR/$BINARY_NAME"
chmod 755 "$INSTALL_DIR/$BINARY_NAME"

# Create config dir
mkdir -p "$CONFIG_DIR"
if [[ ! -f "$CONFIG_DIR/config.json" ]]; then
    echo '{"api_key": "", "backend_url": "https://api.devise.ai"}' > "$CONFIG_DIR/config.json"
    chmod 600 "$CONFIG_DIR/config.json"
fi

# Install systemd service
cp "$SERVICE_FILE" "/etc/systemd/system/$SERVICE_FILE"
chmod 644 "/etc/systemd/system/$SERVICE_FILE"

# Enable and start
systemctl daemon-reload
systemctl enable "$SERVICE_FILE"
systemctl start "$SERVICE_FILE"

if systemctl is-active --quiet "$SERVICE_FILE"; then
    echo "Devise Desktop Agent installed and running."
else
    echo "Warning: service installed but not running. Check: journalctl -u devise-agent" >&2
fi

```


### File: devise-eye\installers\macos\com.devise.agent.plist
```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.devise.agent</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/devise-agent.app/Contents/MacOS/devise-agent</string>
        <string>--config</string>
        <string>/Library/Application Support/Devise/config.json</string>
    </array>
    
    <key>RunAtLoad</key>
    <true/>
    
    <key>KeepAlive</key>
    <true/>
    
    <key>StandardOutPath</key>
    <string>/var/log/devise-agent.log</string>
    
    <key>StandardErrorPath</key>
    <string>/var/log/devise-agent-error.log</string>
    
    <key>ProcessType</key>
    <string>Background</string>
    
    <key>ThrottleInterval</key>
    <integer>10</integer>
    
    <key>ExitTimeOut</key>
    <integer>60</integer>
    
    <key>HangTimeout</key>
    <integer>120</integer>
</dict>
</plist>

```


### File: devise-eye\installers\windows\install-service.ps1
```ps1
# Devise Desktop Agent - Windows Service Setup
# Run as Administrator

# Configuration
$ServiceName = "DeviseAgent"
$DisplayName = "Devise Desktop Agent"
$Description = "Enterprise AI Governance - Desktop Detection Agent"
$ExePath = "$PSScriptRoot\devise-agent.exe"
$ConfigPath = "C:\ProgramData\Devise\config.json"

# Create config directory if not exists
if (!(Test-Path "C:\ProgramData\Devise")) {
    New-Item -ItemType Directory -Path "C:\ProgramData\Devise" -Force
}

# Create default config if not exists
if (!(Test-Path $ConfigPath)) {
    @{
        api_key = "YOUR-API-KEY-HERE"
        backend_url = "https://api.devise.example.com"
        device_id = ""
        identity = @{
            user_id = ""
            user_email = ""
            department = ""
        }
        poll_interval = 30
        deduplication_window = 300
    } | ConvertTo-Json | Set-Content $ConfigPath
}

# Check if service exists
$service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

if ($service) {
    # Stop and remove existing service
    Stop-Service -Name $ServiceName -Force -ErrorAction SilentlyContinue
    sc.exe delete $ServiceName
    Start-Sleep -Seconds 2
}

# Create new service using NSSM (if available) or sc.exe
# Using sc.exe for built-in service creation
$binPath = "`"$ExePath`" --config `"$ConfigPath`""

# Create service with sc.exe
New-Service -Name $ServiceName `
    -BinaryPathName $binPath `
    -DisplayName $DisplayName `
    -Description $Description `
    -StartupType Automatic `
    -ErrorAction Stop

# Set service to restart on failure
sc.exe failure $ServiceName reset= 86400 actions= restart/60000/restart/60000/restart/60000

# Start the service
Start-Service -Name $ServiceName

Write-Host "Devise Agent service installed and started successfully"
Get-Service -Name $ServiceName | Select-Object Status, StartType, DisplayName

```


### File: devise-eye\installers\windows\uninstall-service.ps1
```ps1
# Devise Desktop Agent - Windows Service Uninstall
# Run as Administrator

$ServiceName = "DeviseAgent"

# Check if service exists
$service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

if ($service) {
    # Stop the service
    Stop-Service -Name $ServiceName -Force -ErrorAction SilentlyContinue
    Write-Host "Service stopped"
    
    # Delete the service
    sc.exe delete $ServiceName
    Write-Host "Service deleted"
    
    Write-Host "Devise Agent service uninstalled successfully"
} else {
    Write-Host "Service '$ServiceName' not found"
}

# Optional: Remove config directory
# Remove-Item -Path "C:\ProgramData\Devise" -Recurse -Force -ErrorAction SilentlyContinue

```


### File: devise-eye\scripts\create_config.py
```py
"""
One-time setup script for Devise Desktop Agent.
Run this script to generate the default configuration file before starting the agent.
"""

import json
import os
import sys
from pathlib import Path


def main():
    # Only for Windows currently as per requirements
    if sys.platform != "win32":
        print("This script is currently designed for Windows.")
        print("For other platforms, please refer to the documentation.")
        return

    config_dir = r"C:\ProgramData\Devise"
    config_path = os.path.join(config_dir, "config.json")

    template = {
        "firebase_project_id": "your-project-id",
        "firebase_api_key": "your-web-api-key",
        "service_account_path": r"C:\ProgramData\Devise\service_account.json",
        "org_id": "your-org-id",
        "device_id": "",
        "poll_interval": 30,
        "heartbeat_interval": 300,
        "deduplication_window": 300,
        "debug": False
    }

    print("Devise Desktop Agent - Configuration Setup")
    print("-" * 45)

    try:
        # Create directory if it doesn't exist
        os.makedirs(config_dir, exist_ok=True)
        print(f"[*] Ensuring config directory exists: {config_dir}")

        # Check if config already exists
        if os.path.exists(config_path):
            print(f"[!] Configuration file already exists at: {config_path}")
            choice = input("Do you want to overwrite it? (y/n): ")
            if choice.lower() != 'y':
                print("Aborting setup.")
                return

        # Write the config file
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(template, f, indent=2)
            
        print(f"[*] Successfully created configuration template at: {config_path}")
        print("\n" + "=" * 60)
        print("                             ACTION REQUIRED")
        print("=" * 60)
        print("1. Open the file:")
        print(f"   {config_path}")
        print("2. Fill in the following required values:")
        print("   - firebase_project_id")
        print("   - firebase_api_key")
        print("   - org_id")
        print(f"3. Place your Firebase service account JSON key file at:")
        print(f"   C:\\ProgramData\\Devise\\service_account.json")
        print("=" * 60 + "\n")

    except PermissionError:
        print("\n[!] ERROR: Permission denied.")
        print(f"Cannot create or write to {config_dir}.")
        print("Please run this script as an Administrator.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

```


## 3. Environment Variables Used (Keys Only)


## 4. Architecture & Communication Flow
- **Frontend (devise-iris)**: React/Vite/TypeScript Single Page Application.
- **Backend/DB**: Google Firebase (Firestore for logs, Authentication for users).
- **Desktop Agent (devise-eye)**: Python asynchronous daemon running on Windows.
- **Communication Flow**: 
  1. Agent detects tools locally, adds machine context, and securely POSTs JSON payloads to the Firestore REST API using a Google Service Account (`reporter.py`).
  2. Frontend dashboard retrieves these events directly from Firestore using Firebase Web SDK (`api.ts` -> `useEvents`).
  3. The link between events and dashboard visibility is the `org_id`. The agent hardcodes this in `C:\ProgramData\Devise\config.json`, and the frontend resolves the active user's `org_id` from their `profiles` document.

## 5. API Endpoints & Firebase Functions
- **Backend API**: Currently severely lightweight; primary ingress is direct Firestore REST API for desktop agents.
- **Agent Reporter Endpoint (REST)**: `https://firestore.googleapis.com/v1/projects/{projectId}/databases/(default)/documents/detection_events`

## 6. Shared Data Models
The primary shared model is the **Detection Event**:
```json
{
  "event_id": "string",
  "org_id": "string",
  "timestamp": "ISO-8601 string",
  "tool_name": "string",
  "category": "string",
  "vendor": "string",
  "risk_level": "string",
  "process_name": "string",
  "domain": "string",
  "remote_ip": "string",
  "device_id": "string",
  "user_email": "string",
  "department": "string",
  "is_approved": boolean
}
```
