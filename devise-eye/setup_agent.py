"""
Devise Agent Setup Utility
--------------------------
Run this script ONCE to configure the agent.
It creates a local config.json in the current directory.

Usage:
  python setup_agent.py
"""

import json
import os
import shutil
from pathlib import Path

CONFIG_FILENAME = "config.json"
DEFAULT_SA_SRC  = str(Path(__file__).parent.parent / "steadfast-wares-481309-m5-firebase-adminsdk-fbsvc-3cd157ae5c.json")
SA_DEST         = str(Path(__file__).parent / "service_account.json")

def main():
    print("=== Devise Agent Setup ===\n")

    # 1. Locate service account file
    sa_path = DEFAULT_SA_SRC
    if not os.path.exists(sa_path):
        sa_path = input("Enter the full path to your Firebase service account JSON file:\n> ").strip().strip('"')
        if not os.path.exists(sa_path):
            print(f"[ERROR] File not found: {sa_path}")
            return

    # Copy service account next to the agent for easy access
    if sa_path != SA_DEST:
        shutil.copy2(sa_path, SA_DEST)
        print(f"[OK] Service account copied to: {SA_DEST}")
    else:
        print(f"[OK] Service account already at: {SA_DEST}")

    # 2. Get org_id from user
    print("\nOpen the Dashboard at http://localhost:8081")
    print("Go to Settings -> General, then copy the Organization ID.")
    org_id = input("\nPaste your Organization ID here:\n> ").strip()

    if not org_id:
        print("[WARNING] No org_id entered. You must configure this before the agent will report data.")

    # 3. Get firebase project ID from the service account
    try:
        with open(SA_DEST, "r") as f:
            sa_data = json.load(f)
        project_id = sa_data.get("project_id", "steadfast-wares-481309-m5")
    except Exception:
        project_id = "steadfast-wares-481309-m5"

    # 4. Write config.json
    config = {
        "firebase_project_id":  project_id,
        "service_account_path": SA_DEST,
        "org_id":               org_id,
        "poll_interval":        30,
        "heartbeat_interval":   60,
        "debug":                True
    }

    config_path = Path(__file__).parent / CONFIG_FILENAME
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\n[OK] Config written to: {config_path}")
    print("\n=== Setup complete! ===")
    print("Now restart the agent:")
    print("  python main.py")

if __name__ == "__main__":
    main()
