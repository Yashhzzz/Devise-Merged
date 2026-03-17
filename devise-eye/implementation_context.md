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
