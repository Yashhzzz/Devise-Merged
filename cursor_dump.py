import os
import json

ROOT_DIRS = [
    r"d:\Devise eye\devise-eye",
    r"d:\Devise eye\devise-iris"
]
OUTPUT_FILE = r"d:\Devise eye\cursor_codebase_dump.txt"

IGNORE_DIRS = {
    ".git", "__pycache__", "node_modules", "dist", "build", ".next", 
    "venv", ".venv", "env", ".env", "out", ".vercel", ".turbo"
}
IGNORE_EXTS = {
    ".pyc", ".pyo", ".pyd", ".so", ".dll", ".exe", ".bin", ".zip", 
    ".tar", ".gz", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico", 
    ".pdf", ".sqlite3", ".db", ".log", ".lock" # keep lock files out for brevity
}

def is_ignored(path):
    name = os.path.basename(path)
    if name in IGNORE_DIRS: return True
    if any(path.endswith(ext) for ext in IGNORE_EXTS): return True
    return False

def generate_tree(dir_path, prefix=""):
    tree_str = ""
    try:
        entries = sorted(os.listdir(dir_path))
    except Exception:
        return ""
        
    entries = [e for e in entries if not is_ignored(os.path.join(dir_path, e))]
    
    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        tree_str += f"{prefix}{connector}{entry}\n"
        
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix + extension)
            
    return tree_str

def extract_env_vars(content):
    import re
    vars_found = set()
    # matches VAR_NAME=...
    env_matches = re.finditer(r'^([A-Z0-9_]+)=', content, re.MULTILINE)
    for m in env_matches:
        vars_found.add(m.group(1))
    return vars_found

def run():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write("# COMPREHENSIVE CODEBASE DUMP FOR CURSOR\n\n")
        
        # 1. Structure
        out.write("## 1. Directory Structure\n")
        for root in ROOT_DIRS:
            out.write(f"\n### {os.path.basename(root)}/\n")
            out.write(generate_tree(root))
            
        # 2. Files
        all_env_vars = set()
        configs = {}
        deps = {}
        
        out.write("\n\n## 2. File Contents\n")
        
        for root_dir in ROOT_DIRS:
            for root, dirs, files in os.walk(root_dir):
                # Filter dirs in-place
                dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d))]
                
                for file in files:
                    file_path = os.path.join(root, file)
                    if is_ignored(file_path): continue
                    
                    rel_path = os.path.relpath(file_path, os.path.dirname(root_dir))
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except UnicodeDecodeError:
                        continue # Skip binary/garbled files
                        
                    # Extract specifics
                    if file in ['.env', '.env.local', '.env.example']:
                        all_env_vars.update(extract_env_vars(content))
                    
                    if file in ['package.json', 'requirements.txt', 'firebase.json', '.firebaserc', 'vite.config.ts', 'tailwind.config.js']:
                        configs[rel_path] = content
                        
                    out.write(f"\n\n### File: {rel_path}\n")
                    out.write("```" + (file.split('.')[-1] if '.' in file else "text") + "\n")
                    out.write(content)
                    out.write("\n```\n")

        # 3. Environment Variables
        out.write("\n\n## 3. Environment Variables Used (Keys Only)\n")
        for var in sorted(list(all_env_vars)):
            out.write(f"- {var}\n")

        # 4. Architecture Notes
        out.write("""

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
""")

    print(f"Dump complete: {OUTPUT_FILE}")

if __name__ == "__main__":
    run()
