import os
import json

app_dir = r"d:\devise-iris"
agent_dir = r"d:\Oximy\devise-agent"
output_file = r"d:\devise-iris\CURSOR_CONTEXT.md"

ignore_dirs = {'.git', 'node_modules', 'dist', 'build', '__pycache__', 'venv', '.venv', '.temp', 'temp-landingpage'}
ignore_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip', '.tar', '.gz', '.mp4', '.mp3', '.wav', '.exe', '.pyc'}

def is_binary(file_path):
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read(1024)
            return False
    except UnicodeDecodeError:
        return True

def get_tree(root_dir):
    tree_str = f"{os.path.basename(root_dir)}/\n"
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        if root != root_dir:
            tree_str += f"{indent}{os.path.basename(root)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.endswith(tuple(ignore_exts)):
                tree_str += f"{subindent}{f}\n"
    return tree_str

def dump_files(root_dir, outfile):
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ignore_exts:
                continue
            
            file_path = os.path.join(root, file)
            if file == 'generate_cursor_context.py' or file == 'CURSOR_CONTEXT.md':
                continue
            if file == 'package-lock.json':
                continue
            
            if is_binary(file_path):
                continue
            
            if os.path.getsize(file_path) > 100000: # skip files > 100KB to save space
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                rel_path = os.path.relpath(file_path, root_dir)
                outfile.write(f"### {os.path.basename(root_dir)}/{rel_path}\n\n")
                outfile.write(f"```{ext.replace('.', '')}\n")
                outfile.write(content)
                if not content.endswith('\n'):
                    outfile.write('\n')
                outfile.write("```\n\n")
            except Exception as e:
                pass

with open(output_file, 'w', encoding='utf-8') as out:
    out.write("# Comprehensive Codebase Context: Devise Iris & Desktop Agent\n\n")
    
    out.write("## 1. Overall System Architecture & Communication\n")
    out.write("- **Frontend:** React 18 SPA built with Vite. Communicates directly with Firebase services (Auth, Firestore) via the Firebase Web SDK (`api.ts`).\n")
    out.write("- **Desktop Agent:** Python application running on client machines (`d:\\Oximy\\devise-agent`). It monitors active window titles, executing processes, and network connections (`detector.py`).\n")
    out.write("- **Firebase Backend:** Acts as the central data store and pub/sub system. The desktop agent authenticates using custom tokens or service accounts and writes detection events directly to Firestore (`detection_events` collection). The Frontend listens to these collections in real-time.\n\n")

    out.write("## 2. API Endpoints & Shared Models\n")
    out.write("- **Endpoints:** We use Firebase Firestore directly instead of traditional REST endpoints. The primary operations are CRUD on `detection_events`, `profiles`, `organizations`, `org_settings`, and `heartbeats`.\n")
    out.write("- **Shared Types:** Look in `frontend/src/services/api.ts` for interfaces like `DetectionEvent`, `UserProfile`, `OrgSettings`, and `AlertItem`. The Python agent payload matches `DetectionEvent`.\n\n")

    out.write("## 3. Folder Purposes\n")
    out.write("- `devise-iris/frontend/`: React SPA source code.\n")
    out.write("- `devise-iris/frontend/src/components/`: Reusable UI components (tables, layout, cards).\n")
    out.write("- `devise-iris/frontend/src/services/`: Firebase interaction layer (`api.ts`).\n")
    out.write("- `devise-iris/frontend/src/hooks/`: React Query custom hooks for data fetching.\n")
    out.write("- `devise-iris/api/`: Python Vercel serverless functions (if used, mostly legacy or helper endpoints).\n")
    out.write("- `Oximy/devise-agent/`: Python desktop agent source code tracking processes and network calls.\n\n")

    out.write("## 4. Environment Variables\n")
    out.write("```bash\n")
    out.write("# Frontend (.env)\n")
    out.write("VITE_FIREBASE_API_KEY\n")
    out.write("VITE_FIREBASE_AUTH_DOMAIN\n")
    out.write("VITE_FIREBASE_PROJECT_ID\n")
    out.write("VITE_FIREBASE_STORAGE_BUCKET\n")
    out.write("VITE_FIREBASE_MESSAGING_SENDER_ID\n")
    out.write("VITE_FIREBASE_APP_ID\n")
    out.write("\n")
    out.write("# Agent (.env)\n")
    out.write("FIREBASE_CREDENTIALS_PATH\n")
    out.write("AGENT_POLL_INTERVAL\n")
    out.write("```\n\n")

    out.write("## 5. Folder / File Tree Structure\n")
    out.write("```text\n")
    out.write(get_tree(app_dir))
    out.write(get_tree(agent_dir))
    out.write("```\n\n")
    
    out.write("## 6. Complete File Contents\n\n")
    dump_files(app_dir, out)
    dump_files(agent_dir, out)

print("Context generated!")
