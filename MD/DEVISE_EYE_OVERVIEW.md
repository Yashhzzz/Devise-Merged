# Devise Eye — Desktop Agent Overview

**Devise Eye** is a lightweight Python-based monitoring agent designed to run silently in the background of macOS, Windows, or Linux machines. Its primary mission is to detect outbound connections to AI platforms and report them to the Devise Iris dashboard.

---

## 🏗️ 1. Core Architecture

The agent is built using an asynchronous architecture (`asyncio`) to ensure it monitors network traffic without impacting the user's system performance.

| Module | Responsibility |
|---|---|
| **`main.py`** | The entry point. Initializes all components and runs the main loop. |
| **`detector.py`** | Monitors active network connections using `psutil` and looks for AI domains. |
| **`reporter.py`** | Handles the heavy lifting of authenticated communication with the Firestore REST API. |
| **`identity.py`** | Uniquely identifies the machine using hardware fingerprints (MAC addresses, OS info). |
| **`registry.py`** | A curated library of known AI domains (ChatGPT, Claude, deepseek, etc.). |
| **`setup_agent.py`** | A CLI tool to help users configure their Organization ID and Service Account. |

---

## 🔍 2. How Detection Works

Detection is **non-intrusive**. We do not inspect the *content* of packets (SSL/TLS decryption is not required). Instead, we monitor **Connection Metadata**.

1.  **Polling Loop**: Every 30 seconds (configurable), the `NetworkDetector` scans the system's `ESTABLISHED` network sockets.
2.  **Domain Matching**: It extracts the remote IP addresses of these connections.
3.  **Process Resolution**: Using `psutil`, the agent identifies **which process** owns the connection (e.g., `chrome.exe`, `slack.app`, `vscode.exe`).
4.  **Registry Lookup**: It checks if the destination domain or IP matches the known list of AI platforms in our registry.
5.  **Deduplication**: To avoid spamming the dashboard, the agent only reports a "New Event" when a connection is first established or if the process name changes.

---

## 📡 3. Communication & Security

### **Heartbeats vs. Events**
- **Heartbeat**: Every 60 seconds, the agent sends a tiny ping to Firestore. This lets the dashboard know the device is "Online."
- **Events**: Sent immediately upon detection of an AI connection.

### **Authentication**
The agent uses a **Google Service Account JSON** file to authenticate. 
- It exchanges the private key for a short-lived **OAuth2 Access Token**.
- It communicates directly with the **Firestore REST API** over HTTPS (Port 443).
- **Security Note:** The agent logic is designed to be "Write-Only" — it can report its own events but cannot read data from other devices.

---

## ⚙️ 4. Setup and Installation

The agent is designed to be portable and easy to deploy across an organization.

### **Step 1: Environment**
The agent requires **Python 3.8+** and a few specific libraries:
- `psutil`: For network and process enumeration.
- `httpx`: For asynchronous API calls.
- `google-auth`: For Service Account integration.

### **Step 2: Configuration**
Users run `python setup_agent.py`. This utility:
1.  Copies the company’s `service_account.json` to the agent directory.
2.  Asks for the **Organization ID** (found in the dashboard settings).
3.  Generates a local `config.json` that the agent reads on startup.

---

## 🛠️ 5. Key Logic Features

- **DNS Persistence**: The agent caches resolved DNS names to speed up matching during high-traffic periods.
- **Error Resilience**: If the internet drops, the agent queues detected events in memory and "burps" them to the server once the connection is restored.
- **Low Footprint**: Typically consumes < 20MB of RAM and < 1% CPU.

---

## 🧪 6. Testing the Agent
To verify the agent is working correctly:
1.  Run `python main.py`.
2.  Open a browser and visit `chat.openai.com`.
3.  The agent console will log: `[INFO] Detected AI connection from chrome.exe to openai.com`.
4.  Check the **Live Feed** in the Devise Dashboard to see the event appear.
