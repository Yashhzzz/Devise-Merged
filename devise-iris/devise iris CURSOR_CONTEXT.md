# Comprehensive Codebase Context: Devise Iris & Desktop Agent

## 1. Overall System Architecture & Communication
- **Frontend:** React 18 SPA built with Vite. Communicates directly with Firebase services (Auth, Firestore) via the Firebase Web SDK (`api.ts`).
- **Desktop Agent:** Python application running on client machines (`d:\Oximy\devise-agent`). It monitors active window titles, executing processes, and network connections (`detector.py`).
- **Firebase Backend:** Acts as the central data store and pub/sub system. The desktop agent authenticates using custom tokens or service accounts and writes detection events directly to Firestore (`detection_events` collection). The Frontend listens to these collections in real-time.

## 2. API Endpoints & Shared Models
- **Endpoints:** We use Firebase Firestore directly instead of traditional REST endpoints. The primary operations are CRUD on `detection_events`, `profiles`, `organizations`, `org_settings`, and `heartbeats`.
- **Shared Types:** Look in `frontend/src/services/api.ts` for interfaces like `DetectionEvent`, `UserProfile`, `OrgSettings`, and `AlertItem`. The Python agent payload matches `DetectionEvent`.

## 3. Folder Purposes
- `devise-iris/frontend/`: React SPA source code.
- `devise-iris/frontend/src/components/`: Reusable UI components (tables, layout, cards).
- `devise-iris/frontend/src/services/`: Firebase interaction layer (`api.ts`).
- `devise-iris/frontend/src/hooks/`: React Query custom hooks for data fetching.
- `devise-iris/api/`: Python Vercel serverless functions (if used, mostly legacy or helper endpoints).
- `Oximy/devise-agent/`: Python desktop agent source code tracking processes and network calls.

## 4. Environment Variables
```bash
# Frontend (.env)
VITE_FIREBASE_API_KEY
VITE_FIREBASE_AUTH_DOMAIN
VITE_FIREBASE_PROJECT_ID
VITE_FIREBASE_STORAGE_BUCKET
VITE_FIREBASE_MESSAGING_SENDER_ID
VITE_FIREBASE_APP_ID

# Agent (.env)
FIREBASE_CREDENTIALS_PATH
AGENT_POLL_INTERVAL
```

## 5. Folder / File Tree Structure
```text
devise-iris/
    .gitignore
    .python-version
    CURSOR_CONTEXT.md
    dump_code.py
    generate_cursor_context.py
    package-lock.json
    PROJECT_DETAILS.md
    requirements.txt
    vercel.json
    .ruff_cache/
        .gitignore
        CACHEDIR.TAG
        0.15.5/
            11183078880789648790
            232439852216815567
    api/
        index.py
    frontend/
        .gitignore
        build_log.txt
        build_log_utf8.txt
        components.json
        eslint.config.js
        index.html
        package-lock.json
        package.json
        postcss.config.js
        README.md
        tailwind.config.ts
        tsconfig.app.json
        tsconfig.json
        tsconfig.node.json
        vercel.json
        vite.config.ts
        vitest.config.ts
        public/
            placeholder.svg
            robots.txt
        src/
            App.css
            App.tsx
            index.css
            main.tsx
            vite-env.d.ts
            assets/
            components/
                NavLink.tsx
                ThemeToggle.tsx
                dashboard/
                    AlertsList.tsx
                    AlertsTab.tsx
                    AnalyticsCharts.tsx
                    AnalyticsTab.tsx
                    BentoRow.tsx
                    BudgetProgress.tsx
                    CategoryBadge.tsx
                    DataRiskTab.tsx
                    DevicesTab.tsx
                    DevicesTable.tsx
                    FirewallTab.tsx
                    KpiCards.tsx
                    LiveFeedTab.tsx
                    LiveFeedTable.tsx
                    RecentDetectionsTable.tsx
                    RiskBadge.tsx
                    SettingsTab.tsx
                    StatsCard.tsx
                    SubscriptionList.tsx
                    SubscriptionsTab.tsx
                    TeamTab.tsx
                    UsageTrendChart.tsx
                landing/
                    DashboardMockups.tsx
                    Footer.tsx
                    Layout.tsx
                    Navbar.tsx
                    OrangeWaveBackground.tsx
                layout/
                    AccountSettingsPanel.tsx
                    DashboardLayout.tsx
                    HelpModal.tsx
                    MyProfilePanel.tsx
                    NotificationDropdown.tsx
                    SearchModal.tsx
                    Sidebar.tsx
                    SignOutModal.tsx
                    TopBar.tsx
                    UserProfileDropdown.tsx
                ui/
                    accordion.tsx
                    alert-dialog.tsx
                    alert.tsx
                    aspect-ratio.tsx
                    avatar.tsx
                    badge.tsx
                    breadcrumb.tsx
                    button.tsx
                    calendar.tsx
                    card.tsx
                    carousel.tsx
                    chart.tsx
                    checkbox.tsx
                    collapsible.tsx
                    command.tsx
                    context-menu.tsx
                    dialog.tsx
                    drawer.tsx
                    dropdown-menu.tsx
                    form.tsx
                    hover-card.tsx
                    input-otp.tsx
                    input.tsx
                    label.tsx
                    menubar.tsx
                    navigation-menu.tsx
                    pagination.tsx
                    popover.tsx
                    progress.tsx
                    radio-group.tsx
                    resizable.tsx
                    scroll-area.tsx
                    select.tsx
                    separator.tsx
                    sheet.tsx
                    sidebar.tsx
                    skeleton.tsx
                    slider.tsx
                    sonner.tsx
                    switch.tsx
                    table.tsx
                    tabs.tsx
                    textarea.tsx
                    toast.tsx
                    toaster.tsx
                    toggle-group.tsx
                    toggle.tsx
                    tooltip.tsx
                    use-toast.ts
            data/
                mockData.backup.ts
                mockData.ts
            hooks/
                use-mobile.tsx
                use-toast.ts
                useDashboard.ts
            lib/
                aiToolsRegistry.ts
                AuthContext.tsx
                firebase.ts
                utils.ts
            pages/
                Alerts.tsx
                Analytics.tsx
                Devices.tsx
                Index.tsx
                LiveFeed.tsx
                LoginPage.tsx
                NotFound.tsx
                SignupPage.tsx
                landing/
                    AboutPage.tsx
                    DemoPage.tsx
                    Index.tsx
                    LandingPage.tsx
                    NotFound.tsx
                    OversightPage.tsx
                    PulsePage.tsx
                    SpendPage.tsx
                    UseCasesPage.tsx
            services/
                api.ts
            test/
                example.test.ts
                setup.ts
devise-agent/
    build-arm64.spec
    build-x86_64.spec
    build.spec
    config.py
    deduplicator.py
    detector.py
    dns_resolver.py
    doh_resolver.py
    event_builder.py
    frequency_tracker.py
    heartbeat.py
    identity.py
    liveness_monitor.py
    main.py
    process_resolver.py
    queue.py
    registry.py
    reporter.py
    requirements.txt
    tamper_guard.py
    __init__.py
    data/
        ai_tools_registry.json
        binary_hash.txt
        cdn_ip_ranges.json
    installers/
        linux/
            devise-agent.service
            install.sh
        macos/
            com.devise.agent.plist
        windows/
            install-service.ps1
            uninstall-service.ps1
```

## 6. Complete File Contents

### devise-iris/.gitignore

```
node_modules/
__pycache__/
*.pyc
.env
.venv
venv/
env/
dist/
build/
.DS_Store
```

### devise-iris/.python-version

```
3.12
```

### devise-iris/dump_code.py

```py
import os

def is_binary(file_path):
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read(1024)
            return False
    except UnicodeDecodeError:
        return True

def dump_codebase(root_dir, output_file):
    ignore_dirs = {'.git', 'node_modules', '.next', 'dist', 'build', '__pycache__', '.venv', 'venv', '.ruff_cache', 'temp-landingpage'}
    ignore_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip', '.tar', '.gz', '.mp4', '.mp3', '.wav'}
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# Codebase Context\n\n")
        
        for root, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to avoid walking ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in ignore_exts:
                    continue
                
                file_path = os.path.join(root, file)
                
                # Skip the output file itself and the script
                if file_path == os.path.abspath(output_file) or file == 'dump_code.py':
                    continue
                
                if is_binary(file_path):
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                    
                    rel_path = os.path.relpath(file_path, root_dir)
                    outfile.write(f"## File: {rel_path}\n\n")
                    outfile.write(f"```{ext.replace('.', '')}\n")
                    # Using a placeholder if content is extremely large, but for a codebase context, usually we dump the whole thing.
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
                    outfile.write("```\n\n")
                    print(f"Added {rel_path}")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

if __name__ == '__main__':
    root_directory = r'd:\devise-iris'
    output_filename = r'd:\devise-iris\codebase_context.md'
    dump_codebase(root_directory, output_filename)
    print(f"Dump complete at {output_filename}")
```

### devise-iris/PROJECT_DETAILS.md

```md
# Devise Iris: Technical Implementation Details

This document outlines the architecture, data flow, and frontend implementation of the Devise Iris web dashboard. Devise Iris is an AI governance and shadow IT detection platform.

## 1. System Architecture Overview

The system consists of two primary components:
1. **Devise Desktop Agent (Python):** Runs on endpoints, monitors process execution, captures active window titles/URLs, detects AI tool usage, and sends events to the backend.
2. **Devise Iris Web Dashboard (React + Vite):** A serverless SPA hosted on Vercel. It provides a real-time, interactive UI for IT admins to monitor AI usage, set policies, manage budgets, and review alerts.
3. **Backend Service (Firebase):** Handles authentication, real-time database (Firestore), and serverless functions (if needed).

The dashboard connects directly to Firebase using the official Firebase Web SDK, eliminating the need for a custom intermediate API layer (Node.js/Python server) for core CRUD operations.

---

## 2. Frontend Technology Stack

*   **Framework:** React 18
*   **Build Tool:** Vite
*   **Routing:** React Router DOM (v6)
*   **Styling:** Tailwind CSS + standard CSS modules (for complex animations)
*   **UI Components:** Radix UI primitives, custom generic components (buttons, inputs, modals), Lucide React (icons)
*   **Data Fetching & State:** React Query (`@tanstack/react-query`) for caching, pagination, and real-time synchronisation.
*   **Authentication:** Firebase Auth
*   **Database:** Firebase Firestore
*   **Deployment:** Vercel

---

## 3. Firebase Integration & API Layer

The application interacts with Firebase primarily through the `src/services/api.ts` file. This acts as our data access layer, abstracting raw Firestore queries away from the UI components.

### 3.1 Authentication Flow
*   **Login/Signup:** Handled via Firebase Auth (`createUserWithEmailAndPassword`, `signInWithEmailAndPassword`) in `AuthContext.tsx`.
*   **Session Management:** The `AuthProvider` component wraps the app, listening to `onAuthStateChanged`. It provides the `user` object and `loading` state to all children via Context.
*   **Profile Sync:** On login, we fetch or lazily-create a user document in the `profiles` Firestore collection and link it to an `organizations` document via an `org_id`.

### 3.2 Service Layer (`api.ts`)
We use a centralized API service rather than querying Firestore directly inside components. 

**Key Design Patterns in `api.ts`:**
1.  **Context Aware:** Every request automatically fetches the user's `org_id` (via `getOrgId()`) and scopes the Firestore query to that specific workspace. Multi-tenancy is baked in at the query level.
2.  **Date Normalization:** Firestore returns dates as custom `Timestamp` objects. These cause "Invalid Date" errors in React if passed directly to `new Date()`. The `api.ts` layer uses a `normalizeDate` helper to convert all incoming timestamps, strings, or numbers into standard ISO strings before returning data to the UI.
3.  **Index-Safe Queries:** Complex queries (multiple `where` and `orderBy` clauses) require composite indexes in Firestore. For non-critical stats (like `tamper_alerts`), we wrap the queries in `try/catch` blocks so that a missing index doesn't crash the entire dashboard view.
4.  **Fallback Data:** If fields like `department` are missing from a detection event, `api.ts` or the UI components apply a "General" fallback.

**Core API Functions:**
*   `fetchEvents(category, riskLevel)`: Retrieves paginated/filtered AI detection events.
*   `fetchStats()`: Aggregates daily detections, high-risk counts, and online device metrics for the KPIs.
*   `fetchAnalytics()`: Groups events by hour, tool, and category for the Recharts graphs.
*   `fetchMe()`, `updateMe()`: Manages the currently logged-in admin's profile.

---

## 4. Custom React Hooks (`useDashboard.ts`)

UI components consume data via custom hooks built on top of React Query. This provides automatic caching, background refetching, and clean loading/error states.

*   `useEvents()`: Fetches the live feed. Refetches every 10 seconds to keep the dashboard real-time.
*   `useStats()` / `useAnalytics()`: Fetches KPI and chart data. Refetches every 30-60 seconds to reduce Firestore read costs while remaining fresh.
*   `useProfile()`: Fetches the admin's profile, including their role and workspace info.
*   `useSpendOverview()`: Aggregates subscription costs from the `subscriptions` collection.

---

## 5. UI Architecture & Dashboard Layout

The dashboard uses a layout-wrapper pattern (`DashboardLayout.tsx`) that persists the sidebar and top navigation while swapping out the main content area based on the selected tab (or route).

### 5.1 Main Content Areas
The dashboard is split into logical tabs (controlled via state or React Router, depending on implementation detail):

1.  **Overview (`OverviewTab.tsx` / `App.tsx` router):**
    *   **KPI Cards (`KpiCards.tsx`):** Displays top-level metrics (Total Detections, High Risk, etc.).
    *   **Bento Row (`BentoRow.tsx`):** Displays spend metrics, active agent counts, and zombie license alerts.
    *   **Recent Detections (`RecentDetectionsTable.tsx`):** A simplified view of the latest events.
    *   **Usage Trend Chart (`UsageTrendChart.tsx`):** Uses Recharts to plot `detections` vs `violations` over time.
2.  **Live Feed (`LiveFeedTab.tsx`):**
    *   A detailed, paginated table (`LiveFeedTable.tsx`) showing raw detection events.
    *   Supports filtering by risk level, category, and searching by tool/process name.
3.  **Analytics (`AnalyticsTab.tsx`):**
    *   Deeper dive charts (pie charts, bar charts) breaking down usage by department, tool, and category.
4.  **Settings & Profile:**
    *   Slide-over panels (`MyProfilePanel.tsx`, `SettingsSlideover.tsx`) for managing account details, dark mode, and notification preferences.

### 5.2 Styling Approach
We employ a hybrid styling approach:
*   **Tailwind CSS:** Used for layout grids, flexbox alignment, spacing (margins/padding), and typography classes (`text-sm`, `font-bold`).
*   **Inline Styles / CSS-in-JS Concepts:** Used extensively for exact color matches (e.g., `#FF5C1A` for the brand orange), precise border radii (`borderRadius: 16`), and specific hover transformations (`transform: translateY(-2px)`). This allows for pixel-perfect implementation of the premium Figma designs.
*   **Animations:** The dashboard relies on subtle CSS transitions (fades, slides, shadows) to feel responsive and high-end.

---

## 6. Firestore Database Schema

The Firebase Firestore database is organized into the following collections. Every document is scoped to an organism/workspace using the `org_id` field.

### Profiles (`profiles/{uid}`)
Stores user-specific settings.
*   `id` (string): Firebase Auth UID.
*   `org_id` (string): Reference to the workspace.
*   `full_name`, `email`, `role`, `department` (strings)
*   `last_active` (Timestamp): Updated automatically on auth session start.
*   `dark_mode` (boolean)

### Organizations (`organizations/{org_id}`)
Stores workspace-level data.
*   `id`, `name`, `slug` (strings)
*   `created_at` (ISO string)

### Detection Events (`detection_events/{event_id}`)
The core log of intercepted AI usage.
*   `org_id` (string)
*   `user_id` / `user_email` (string): The employee who triggered the event.
*   `device_id` (string): Machine identifier.
*   `tool_name` (string): E.g., "ChatGPT", "GitHub Copilot".
*   `category` (string): E.g., "chatbot", "code-assistant".
*   `risk_level` (string): "low", "medium", "high".
*   `process_name`, `domain` (strings)
*   `is_approved` (boolean): Whether the tool is sanctioned.
*   `timestamp` (Timestamp or ISO string)

### Heartbeats (`heartbeats/{doc_id}`)
Tracks agent uptime and versioning.
*   `org_id`, `device_id` (strings)
*   `timestamp` (Timestamp)
*   `agent_version`, `os_version` (strings)

### Subscriptions (`subscriptions/{doc_id}`)
Tracks approved tools and software spend.
*   `org_id` (string)
*   `tool_name`, `vendor` (strings)
*   `seats`, `seats_used` (numbers)
*   `cost_monthly` (number)
*   `status` (string): "active", "zombie" (unused licenses).

### Organization Settings (`org_settings/{org_id}`)
Global policies for the workspace.
*   `monthly_budget`, `alert_threshold` (numbers)
*   `auto_block` (boolean)
*   `allowed_categories`, `blocked_domains` (arrays)

*(Subcollection)* `firewall_rules/{rule_id}`
*   `tool_name`, `domain` (strings)
*   `status` (string): "allowed", "blocked"
*   `updated_by` (string)
```

### devise-iris/requirements.txt

```txt
fastapi
uvicorn[standard]
firebase-admin
python-jose[cryptography]
python-dotenv
pydantic
httpx>=0.25.0
```

### devise-iris/vercel.json

```json
{
  "cleanUrls": true,
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/frontend/dist/index.html"
    }
  ]
}
```

### devise-iris/.ruff_cache\.gitignore

```
# Automatically created by ruff.
*
```

### devise-iris/.ruff_cache\CACHEDIR.TAG

```tag
Signature: 8a477f597d28d172789f06886806bc55
```

### devise-iris/api\index.py

```py
"""
Vercel ASGI entrypoint for Devise Dashboard backend.
"""

import sys
import os

# Make the backend package importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.server import app  # noqa: F401
```

### devise-iris/frontend\.gitignore

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

### devise-iris/frontend\build_log_utf8.txt

```txt
﻿
> devise-dashboard@0.0.0 build
> vite build

[36mvite v5.4.19 [32mbuilding for production...[36m[39m
transforming...
[32mΓ£ô[39m 96 modules transformed.
```

### devise-iris/frontend\components.json

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/index.css",
    "baseColor": "slate",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

### devise-iris/frontend\eslint.config.js

```js
import js from "@eslint/js";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["dist"] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ["**/*.{ts,tsx}"],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      "react-refresh/only-export-components": ["warn", { allowConstantExport: true }],
      "@typescript-eslint/no-unused-vars": "off",
    },
  },
);
```

### devise-iris/frontend\index.html

```html
<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Devise Dashboard — AI Tool Monitoring</title>
    <meta name="description" content="Monitor and manage AI tool usage across your organization with Devise Dashboard." />
    <meta name="author" content="Devise" />
    <meta property="og:title" content="Devise Dashboard" />
    <meta property="og:description" content="Real-time AI tool monitoring and analytics" />
    <meta property="og:type" content="website" />
    <meta name="twitter:card" content="summary_large_image" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

### devise-iris/frontend\package.json

```json
{
  "name": "devise-dashboard",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "build:dev": "vite build --mode development",
    "lint": "eslint .",
    "preview": "vite preview",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@radix-ui/react-accordion": "^1.2.11",
    "@radix-ui/react-alert-dialog": "^1.1.14",
    "@radix-ui/react-aspect-ratio": "^1.1.7",
    "@radix-ui/react-avatar": "^1.1.10",
    "@radix-ui/react-checkbox": "^1.3.2",
    "@radix-ui/react-collapsible": "^1.1.11",
    "@radix-ui/react-context-menu": "^2.2.15",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-dropdown-menu": "^2.1.15",
    "@radix-ui/react-hover-card": "^1.1.14",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-menubar": "^1.1.15",
    "@radix-ui/react-navigation-menu": "^1.2.13",
    "@radix-ui/react-popover": "^1.1.14",
    "@radix-ui/react-progress": "^1.1.7",
    "@radix-ui/react-radio-group": "^1.3.7",
    "@radix-ui/react-scroll-area": "^1.2.9",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-separator": "^1.1.7",
    "@radix-ui/react-slider": "^1.3.5",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-switch": "^1.2.5",
    "@radix-ui/react-tabs": "^1.1.12",
    "@radix-ui/react-toast": "^1.2.14",
    "@radix-ui/react-toggle": "^1.1.9",
    "@radix-ui/react-toggle-group": "^1.1.10",
    "@radix-ui/react-tooltip": "^1.2.7",
    "firebase": "^10.8.0",
    "@tanstack/react-query": "^5.83.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.6.0",
    "input-otp": "^1.4.2",
    "lucide-react": "^0.462.0",
    "next-themes": "^0.3.0",
    "react": "^18.3.1",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.61.1",
    "react-resizable-panels": "^2.1.9",
    "react-router-dom": "^6.30.1",
    "recharts": "^2.15.4",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.0",
    "tailwindcss-animate": "^1.0.7",
    "vaul": "^0.9.9",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@eslint/js": "^9.32.0",
    "@tailwindcss/typography": "^0.5.16",
    "@testing-library/jest-dom": "^6.6.0",
    "@testing-library/react": "^16.0.0",
    "@types/node": "^22.19.15",
    "@types/react": "^18.3.23",
    "@types/react-dom": "^18.3.7",
    "@vitejs/plugin-react-swc": "^3.11.0",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.32.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^15.15.0",
    "jsdom": "^20.0.3",
    "lovable-tagger": "^1.1.13",
    "postcss": "^8.5.6",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.8.3",
    "typescript-eslint": "^8.38.0",
    "vite": "^5.4.19",
    "vitest": "^3.2.4"
  }
}
```

### devise-iris/frontend\postcss.config.js

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### devise-iris/frontend\README.md

```md
# Devise Dashboard

AI Tool Monitoring & Detection Platform

## Overview

Devise is an AI tool monitoring platform that helps organizations track, control, and secure AI tool usage across their workforce. It detects when employees use AI tools (ChatGPT, Claude, Copilot, etc.), categorizes them by risk level, and provides real-time visibility into AI adoption.

## Features

- **Real-time Detection** — Monitor AI tool usage as it happens
- **Risk Assessment** — Automatically categorize tools by risk level (low/medium/high)
- **Approval Workflow** — Track which tools are approved vs unapproved
- **Device Monitoring** — See which machines are running the agent
- **Alerting** — Get notified of security concerns (tampering, gaps, high-risk usage)
- **Analytics** — Visualize AI adoption trends across your organization

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React + TypeScript + Vite |
| UI | shadcn-ui + Tailwind CSS |
| Charts | Recharts |
| Data Fetching | TanStack React Query |
| Backend | FastAPI (Python) |
| Database | SQLite (demo) / PostgreSQL (production) |

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.10+
- npm or yarn

### Installation

```bash
# Install frontend dependencies
cd devise-dashboard
npm install

# Start frontend dev server
npm run dev
```

### Running the Backend

```bash
# Navigate to backend
cd ../backend

# Install Python dependencies
pip install fastapi uvicorn

# Start backend server
python -c "import uvicorn; uvicorn.run('server:app', host='0.0.0.0', port=8080, reload=True)"
```

### Access

- Frontend: http://localhost:8081
- Backend API: http://localhost:8080
- API Docs: http://localhost:8080/docs

## Project Structure

```
devise-dashboard/
├── src/
│   ├── components/      # React components
│   ├── pages/           # Page components
│   ├── hooks/           # Custom React hooks
│   ├── services/        # API service layer
│   ├── data/            # Type definitions
│   └── lib/             # Utilities and registry
├── public/              # Static assets
└── package.json

backend/
├── server.py            # FastAPI application
└── devise_dashboard.db  # SQLite database
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/event` | POST | Ingest detection events |
| `/api/events` | GET | Query detection events |
| `/api/heartbeats` | GET | Get device heartbeats |
| `/api/stats` | GET | Get aggregated stats |
| `/api/alerts` | GET | Get all alerts |
| `/api/analytics` | GET | Get analytics data |

## License

MIT
```

### devise-iris/frontend\tailwind.config.ts

```ts
import type { Config } from "tailwindcss";

export default {
  darkMode: ["class"],
  content: ["./pages/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./app/**/*.{ts,tsx}", "./src/**/*.{ts,tsx}"],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
      colors: {
        "brand-cream": "#F5EDE0",
        "brand-orange": "#F04E23",
        "brand-navy": "#1A1A2E",
        "brand-blue": "#1A56FF",
        "brand-purple": "#7B2FFF",
        "brand-green": "#16A34A",
        "brand-dark": "#1A1A1A",
        "brand-gray": "#6B7280",
        "brand-white": "#FFFFFF",
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        sidebar: {
          DEFAULT: "hsl(var(--sidebar-background))",
          foreground: "hsl(var(--sidebar-foreground))",
          primary: "hsl(var(--sidebar-primary))",
          "primary-foreground": "hsl(var(--sidebar-primary-foreground))",
          accent: "hsl(var(--sidebar-accent))",
          "accent-foreground": "hsl(var(--sidebar-accent-foreground))",
          border: "hsl(var(--sidebar-border))",
          ring: "hsl(var(--sidebar-ring))",
        },
        success: {
          DEFAULT: "hsl(var(--success))",
          foreground: "hsl(var(--success-foreground))",
        },
        warning: {
          DEFAULT: "hsl(var(--warning))",
          foreground: "hsl(var(--warning-foreground))",
        },
        chart: {
          "1": "hsl(var(--chart-1))",
          "2": "hsl(var(--chart-2))",
          "3": "hsl(var(--chart-3))",
          "4": "hsl(var(--chart-4))",
          "5": "hsl(var(--chart-5))",
        },
      },
      boxShadow: {
        soft: "0 0 0 1px rgba(0,0,0,.06), 0 1px 2px -1px rgba(0,0,0,.06), 0 2px 4px rgba(0,0,0,.04)",
        heavy: "0 0 0 1px rgba(0,0,0,.04), 0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -2px rgba(0,0,0,.05)",
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config;

```

### devise-iris/frontend\tsconfig.app.json

```json
{
  "compilerOptions": {
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "lib": [
      "ES2020",
      "DOM",
      "DOM.Iterable"
    ],
    "module": "ESNext",
    "moduleDetection": "force",
    "moduleResolution": "bundler",
    "noEmit": true,
    "noFallthroughCasesInSwitch": false,
    "noImplicitAny": false,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "paths": {
      "@/*": [
        "./src/*"
      ]
    },
    "skipLibCheck": true,
    "strict": false,
    "target": "ES2020",
    "types": [
      "vitest/globals"
    ],
    "useDefineForClassFields": true
  },
  "include": [
    "src"
  ]
}
```

### devise-iris/frontend\tsconfig.json

```json
{
  "compilerOptions": {
    "allowJs": true,
    "noImplicitAny": false,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "paths": {
      "@/*": [
        "./src/*"
      ]
    },
    "skipLibCheck": true,
    "strictNullChecks": false
  },
  "files": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.node.json"
    }
  ]
}
```

### devise-iris/frontend\tsconfig.node.json

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["vite.config.ts"]
}
```

### devise-iris/frontend\vercel.json

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

### devise-iris/frontend\vite.config.ts

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
    hmr: {
      overlay: false,
    },
  },
  plugins: [react(), mode === "development" && componentTagger()].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
}));
```

### devise-iris/frontend\vitest.config.ts

```ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react-swc";
import path from "path";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/test/setup.ts"],
    include: ["src/**/*.{test,spec}.{ts,tsx}"],
  },
  resolve: {
    alias: { "@": path.resolve(__dirname, "./src") },
  },
});
```

### devise-iris/frontend\public\placeholder.svg

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" fill="none"><rect width="1200" height="1200" fill="#EAEAEA" rx="3"/><g opacity=".5"><g opacity=".5"><path fill="#FAFAFA" d="M600.709 736.5c-75.454 0-136.621-61.167-136.621-136.62 0-75.454 61.167-136.621 136.621-136.621 75.453 0 136.62 61.167 136.62 136.621 0 75.453-61.167 136.62-136.62 136.62Z"/><path stroke="#C9C9C9" stroke-width="2.418" d="M600.709 736.5c-75.454 0-136.621-61.167-136.621-136.62 0-75.454 61.167-136.621 136.621-136.621 75.453 0 136.62 61.167 136.62 136.621 0 75.453-61.167 136.62-136.62 136.62Z"/></g><path stroke="url(#a)" stroke-width="2.418" d="M0-1.209h553.581" transform="scale(1 -1) rotate(45 1163.11 91.165)"/><path stroke="url(#b)" stroke-width="2.418" d="M404.846 598.671h391.726"/><path stroke="url(#c)" stroke-width="2.418" d="M599.5 795.742V404.017"/><path stroke="url(#d)" stroke-width="2.418" d="m795.717 796.597-391.441-391.44"/><path fill="#fff" d="M600.709 656.704c-31.384 0-56.825-25.441-56.825-56.824 0-31.384 25.441-56.825 56.825-56.825 31.383 0 56.824 25.441 56.824 56.825 0 31.383-25.441 56.824-56.824 56.824Z"/><g clip-path="url(#e)"><path fill="#666" fill-rule="evenodd" d="M616.426 586.58h-31.434v16.176l3.553-3.554.531-.531h9.068l.074-.074 8.463-8.463h2.565l7.18 7.181V586.58Zm-15.715 14.654 3.698 3.699 1.283 1.282-2.565 2.565-1.282-1.283-5.2-5.199h-6.066l-5.514 5.514-.073.073v2.876a2.418 2.418 0 0 0 2.418 2.418h26.598a2.418 2.418 0 0 0 2.418-2.418v-8.317l-8.463-8.463-7.181 7.181-.071.072Zm-19.347 5.442v4.085a6.045 6.045 0 0 0 6.046 6.045h26.598a6.044 6.044 0 0 0 6.045-6.045v-7.108l1.356-1.355-1.282-1.283-.074-.073v-17.989h-38.689v23.43l-.146.146.146.147Z" clip-rule="evenodd"/></g><path stroke="#C9C9C9" stroke-width="2.418" d="M600.709 656.704c-31.384 0-56.825-25.441-56.825-56.824 0-31.384 25.441-56.825 56.825-56.825 31.383 0 56.824 25.441 56.824 56.825 0 31.383-25.441 56.824-56.824 56.824Z"/></g><defs><linearGradient id="a" x1="554.061" x2="-.48" y1=".083" y2=".087" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="b" x1="796.912" x2="404.507" y1="599.963" y2="599.965" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="c" x1="600.792" x2="600.794" y1="403.677" y2="796.082" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="d" x1="404.85" x2="796.972" y1="403.903" y2="796.02" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><clipPath id="e"><path fill="#fff" d="M581.364 580.535h38.689v38.689h-38.689z"/></clipPath></defs></svg>
```

### devise-iris/frontend\public\robots.txt

```txt
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Twitterbot
Allow: /

User-agent: facebookexternalhit
Allow: /

User-agent: *
Allow: /
```

### devise-iris/frontend\src\App.css

```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}
```

### devise-iris/frontend\src\App.tsx

```tsx
import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthProvider, useAuth } from "@/lib/AuthContext";
import { auth } from "@/lib/firebase";

// Dashboard Imports
import { LoginPage } from "@/pages/LoginPage";
import { SignupPage } from "@/pages/SignupPage";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { KpiCards } from "@/components/dashboard/KpiCards";
import { BentoRow } from "@/components/dashboard/BentoRow";
import { UsageTrendChart } from "@/components/dashboard/UsageTrendChart";
import { BudgetProgress } from "@/components/dashboard/BudgetProgress";
import { SubscriptionList } from "@/components/dashboard/SubscriptionList";
import { RecentDetectionsTable } from "@/components/dashboard/RecentDetectionsTable";
import { LiveFeedTab } from "@/components/dashboard/LiveFeedTab";
import { AnalyticsTab } from "@/components/dashboard/AnalyticsTab";
import { DevicesTab } from "@/components/dashboard/DevicesTab";
import { AlertsTab } from "@/components/dashboard/AlertsTab";
import { SubscriptionsTab } from "@/components/dashboard/SubscriptionsTab";
import { SettingsTab } from "@/components/dashboard/SettingsTab";
import { TeamTab } from "@/components/dashboard/TeamTab";
import { FirewallTab } from "@/components/dashboard/FirewallTab";
import { DataRiskTab } from "@/components/dashboard/DataRiskTab";

// Landing Page Imports
import { LandingPage } from "./pages/landing/LandingPage";
import { OversightPage } from "./pages/landing/OversightPage";
import { PulsePage } from "./pages/landing/PulsePage";
import { SpendPage } from "./pages/landing/SpendPage";
import { AboutPage } from "./pages/landing/AboutPage";
import { UseCasesPage } from "./pages/landing/UseCasesPage";
import { DemoPage } from "./pages/landing/DemoPage";
import NotFound from "./pages/landing/NotFound";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";

const queryClient = new QueryClient();

function Dashboard() {
  const [activeTab, setActiveTab] = useState<Tab>("overview");

  return (
    <DashboardLayout activeTab={activeTab} onTabChange={setActiveTab}>
      <div
        key={activeTab}
        className="animate-in fade-in duration-300 fill-mode-both"
      >
        {activeTab === "overview" && (
          <div className="flex flex-col gap-4">
            <KpiCards onNavigate={setActiveTab as (tab: string) => void} />
            <div className="flex gap-4">
              <BentoRow onNavigate={setActiveTab as (tab: string) => void} />
              <UsageTrendChart />
            </div>
            <div className="flex gap-4" style={{ alignItems: "stretch" }}>
              <div className="flex flex-col gap-4" style={{ flex: "0 0 auto", width: 424 }}>
                <BudgetProgress />
                <SubscriptionList onNavigate={setActiveTab as (tab: string) => void} />
              </div>
              <RecentDetectionsTable />
            </div>
          </div>
        )}
        {activeTab === "live-feed"  && <LiveFeedTab />}
        {activeTab === "analytics"  && <AnalyticsTab />}
        {activeTab === "devices"    && <DevicesTab />}
        {activeTab === "team"       && <TeamTab />}
        {activeTab === "alerts"     && <AlertsTab />}
        {activeTab === "subscriptions" && <SubscriptionsTab />}
        {activeTab === "settings"   && <SettingsTab />}
        {activeTab === "firewall"   && <FirewallTab />}
        {activeTab === "data-risk"  && <DataRiskTab />}
      </div>
    </DashboardLayout>
  );
}

const AppContent = () => {
  const { user, loading } = useAuth();

  if (loading) return null;

  return (
    <Routes>
      {/* Landing Page Routes */}
      <Route path="/" element={<LandingPage />} />
      <Route path="/product/oversight" element={<OversightPage />} />
      <Route path="/product/pulse" element={<PulsePage />} />
      <Route path="/product/spend" element={<SpendPage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/use-cases" element={<UseCasesPage />} />
      <Route path="/demo" element={<DemoPage />} />
      
      {/* Auth Routes */}
      <Route 
        path="/login" 
        element={user ? <Navigate to="/dashboard" replace /> : <LoginPage />} 
      />
      <Route 
        path="/signup" 
        element={user ? <Navigate to="/dashboard" replace /> : <SignupPage />} 
      />
      
      {/* Dashboard Routes (Protected) */}
      <Route 
        path="/dashboard/*" 
        element={user ? <Dashboard /> : <Navigate to="/login" replace />} 
      />
      
      {/* Fallback */}
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

const App = () => {
  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <TooltipProvider>
          <Toaster />
          <Sonner />
          <AuthProvider>
            <AppContent />
          </AuthProvider>
        </TooltipProvider>
      </QueryClientProvider>
    </BrowserRouter>
  );
};

export default App;
```

### devise-iris/frontend\src\index.css

```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap");

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 220 14% 95%;
    --foreground: 240 10% 10%;

    --card: 0 0% 100%;
    --card-foreground: 240 10% 10%;

    --popover: 0 0% 100%;
    --popover-foreground: 240 10% 10%;

    --primary: 16 100% 54%;
    --primary-foreground: 0 0% 100%;

    --secondary: 220 14% 96%;
    --secondary-foreground: 240 6% 20%;

    --muted: 220 14% 96%;
    --muted-foreground: 215 16% 65%;

    --accent: 220 14% 96%;
    --accent-foreground: 240 6% 20%;

    --destructive: 0 84% 60%;
    --destructive-foreground: 0 0% 100%;

    --border: 220 13% 91%;
    --input: 220 13% 91%;
    --ring: 16 100% 54%;

    --radius: 0.75rem;

    --success: 142 71% 45%;
    --success-foreground: 0 0% 100%;
    --warning: 38 92% 50%;
    --warning-foreground: 0 0% 100%;

    --chart-1: 16 100% 54%;
    --chart-2: 200 70% 50%;
    --chart-3: 142 71% 45%;
    --chart-4: 280 65% 60%;
    --chart-5: 38 92% 50%;
  }
}

@layer base {
  * {
    @apply border-border;
    box-sizing: border-box;
  }

  html,
  body,
  #root {
    height: 100%;
    font-family:
      "Inter",
      -apple-system,
      BlinkMacSystemFont,
      sans-serif;
  }

  body {
    background-color: #f0f2f5;
    color: #1a1a2e;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
}
```

### devise-iris/frontend\src\main.tsx

```tsx
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";

createRoot(document.getElementById("root")!).render(<App />);
```

### devise-iris/frontend\src\vite-env.d.ts

```ts
/// <reference types="vite/client" />
```

### devise-iris/frontend\src\components\NavLink.tsx

```tsx
import { NavLink as RouterNavLink, NavLinkProps } from "react-router-dom";
import { forwardRef } from "react";
import { cn } from "@/lib/utils";

interface NavLinkCompatProps extends Omit<NavLinkProps, "className"> {
  className?: string;
  activeClassName?: string;
  pendingClassName?: string;
}

const NavLink = forwardRef<HTMLAnchorElement, NavLinkCompatProps>(
  ({ className, activeClassName, pendingClassName, to, ...props }, ref) => {
    return (
      <RouterNavLink
        ref={ref}
        to={to}
        className={({ isActive, isPending }) =>
          cn(className, isActive && activeClassName, isPending && pendingClassName)
        }
        {...props}
      />
    );
  },
);

NavLink.displayName = "NavLink";

export { NavLink };
```

### devise-iris/frontend\src\components\ThemeToggle.tsx

```tsx
import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";
import { Button } from "@/components/ui/button";

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
      className="h-9 w-9 rounded-lg"
    >
      <Sun className="h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  );
}
```

### devise-iris/frontend\src\components\dashboard\AlertsList.tsx

```tsx
import { formatDistanceToNow } from "date-fns";
import { AlertTriangle, Shield, Clock, Zap, CheckCircle2, X } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { RiskBadge } from "./RiskBadge";
import { useAlerts } from "@/hooks/useDashboard";
import { dismissAlert, resolveAlert } from "@/services/api";
import type { AlertItem } from "@/services/api";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useToast } from "@/hooks/use-toast";

const ICON_MAP: Record<string, typeof AlertTriangle> = {
  high_risk:      AlertTriangle,
  unapproved:     Shield,
  tamper:         Shield,
  agent_gap:      Clock,
  high_frequency: Zap,
};

export function AlertsList() {
  const { data: alerts = [], isLoading } = useAlerts();
  const queryClient = useQueryClient();
  const { toast } = useToast();

  const dismissMutation = useMutation({
    mutationFn: dismissAlert,
    onMutate: async (alertId) => {
      // Optimistic update: remove from cache immediately
      await queryClient.cancelQueries({ queryKey: ["alerts"] });
      const previous = queryClient.getQueryData<AlertItem[]>(["alerts"]);
      queryClient.setQueryData<AlertItem[]>(["alerts"], (old) =>
        old ? old.filter((a) => a.id !== alertId) : []
      );
      return { previous };
    },
    onError: (_err, _id, context) => {
      queryClient.setQueryData(["alerts"], context?.previous);
      toast({ title: "Failed to dismiss alert", variant: "destructive" });
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["alerts"] });
      queryClient.invalidateQueries({ queryKey: ["stats"] });
    },
    onSuccess: () => {
      toast({ title: "Alert dismissed" });
    },
  });

  const resolveMutation = useMutation({
    mutationFn: resolveAlert,
    onMutate: async (alertId) => {
      await queryClient.cancelQueries({ queryKey: ["alerts"] });
      const previous = queryClient.getQueryData<AlertItem[]>(["alerts"]);
      queryClient.setQueryData<AlertItem[]>(["alerts"], (old) =>
        old ? old.filter((a) => a.id !== alertId) : []
      );
      return { previous };
    },
    onError: (_err, _id, context) => {
      queryClient.setQueryData(["alerts"], context?.previous);
      toast({ title: "Failed to resolve alert", variant: "destructive" });
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["alerts"] });
      queryClient.invalidateQueries({ queryKey: ["stats"] });
    },
    onSuccess: () => {
      toast({ title: "Alert resolved" });
    },
  });

  if (isLoading && alerts.length === 0) {
    return (
      <p className="text-center text-xs text-muted-foreground py-8">Loading alerts…</p>
    );
  }

  if (alerts.length === 0) {
    return (
      <p className="text-center text-xs text-muted-foreground py-8">
        No alerts. Start the agent to begin receiving data.
      </p>
    );
  }

  return (
    <div className="space-y-3">
      {alerts.map((alert: AlertItem) => {
        const Icon = ICON_MAP[alert.type] ?? AlertTriangle;
        return (
          <Card key={alert.id} className={`border-l-4 ${
            alert.severity === "high" ? "border-l-red-500" : alert.severity === "medium" ? "border-l-amber-500" : "border-l-emerald-500"
          }`}>
            <CardContent className="flex items-start justify-between gap-4 p-4">
              <div className="flex items-start gap-3">
                <div className={`mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg ${
                  alert.severity === "high" ? "bg-red-500/15" : "bg-amber-500/15"
                }`}>
                  <Icon className={`h-4 w-4 ${
                    alert.severity === "high" ? "text-red-500" : "text-amber-500"
                  }`} />
                </div>
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className="text-sm font-medium">{alert.title}</span>
                    <RiskBadge level={alert.severity} />
                  </div>
                  <p className="text-xs text-muted-foreground">{alert.description}</p>
                  <p className="text-xs text-muted-foreground">
                    {formatDistanceToNow(new Date(alert.timestamp), { addSuffix: true })}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-1.5 shrink-0">
                {alert.severity === "high" && (
                  <Button
                    variant="ghost"
                    size="sm"
                    className="text-xs text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
                    onClick={() => resolveMutation.mutate(alert.id)}
                    disabled={resolveMutation.isPending}
                  >
                    <CheckCircle2 className="h-3.5 w-3.5 mr-1" />
                    Resolve
                  </Button>
                )}
                <Button
                  variant="ghost"
                  size="sm"
                  className="text-xs"
                  onClick={() => dismissMutation.mutate(alert.id)}
                  disabled={dismissMutation.isPending}
                >
                  <X className="h-3.5 w-3.5 mr-1" />
                  Dismiss
                </Button>
              </div>
            </CardContent>
          </Card>
        );
      })}
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\AlertsTab.tsx

```tsx
import { useState, useMemo } from "react";
import {
  AlertTriangle, Info, CheckCircle2,
  ChevronDown, Bell, ShieldAlert, Pencil, Plus,
} from "lucide-react";
import { useToast } from "@/components/ui/use-toast";
import { useAlerts } from "@/hooks/useDashboard";
import { resolveAlert, dismissAlert, type AlertItem } from "@/services/api";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Types ─────────────────────────────────────────────────────────────────

type Severity = "critical" | "high" | "medium" | "resolved";

interface Alert {
  id: string;
  severity: Severity;
  unread: boolean;
  title: string;
  desc: string;
  user: string;
  tool: string;
  dept: string;
  time: string;
  resolvedBy?: string;
}

// ─── Helpers ───────────────────────────────────────────────────────────────

function formatRelativeTime(timestamp: string): string {
  const now = Date.now();
  const then = new Date(timestamp).getTime();
  const diffMs = now - then;
  if (diffMs < 0) return "Just now";
  const mins = Math.floor(diffMs / 60_000);
  if (mins < 1) return "Just now";
  if (mins < 60) return `${mins} min ago`;
  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return `${hrs} hr ago`;
  const days = Math.floor(hrs / 24);
  if (days === 1) return "Yesterday";
  return `${days} days ago`;
}

function mapAlertSeverity(item: AlertItem): Severity {
  if (item.type === "high_risk" || item.type === "tamper") return "critical";
  if (item.type === "unapproved" || item.type === "high_frequency") return "high";
  return "medium";
}

function extractToolFromAlert(item: AlertItem): string {
  // Try to extract a tool name from title or description
  const toolPatterns = /\b(ChatGPT|OpenAI|Midjourney|Claude|Perplexity|Copilot|Replicate|Runway|Cursor|Gemini|Character\.ai|Grammarly|Notion|Jasper)\b/i;
  const titleMatch = item.title.match(toolPatterns);
  if (titleMatch) return titleMatch[1];
  const descMatch = item.description.match(toolPatterns);
  if (descMatch) return descMatch[1];
  return "\u2014";
}

function mapAlertItemToAlert(item: AlertItem): Alert {
  return {
    id: item.id,
    severity: mapAlertSeverity(item),
    unread: true,
    title: item.title,
    desc: item.description,
    user: "\u2014",
    tool: extractToolFromAlert(item),
    dept: "\u2014",
    time: formatRelativeTime(item.timestamp),
  };
}

// ─── Severity config ───────────────────────────────────────────────────────

const sevConf: Record<Severity, { border: string; badge: string; badgeText: string; badgeBorder: string; iconBg: string; iconColor: string; label: string }> = {
  critical: { border:"#DC2626", badge:"rgba(220,38,38,0.08)", badgeText:"#DC2626", badgeBorder:"rgba(220,38,38,0.2)", iconBg:"rgba(220,38,38,0.08)", iconColor:"#DC2626", label:"Critical" },
  high:     { border:"#FF5C1A", badge:"rgba(255,92,26,0.08)",  badgeText:"#FF5C1A", badgeBorder:"rgba(255,92,26,0.2)",  iconBg:"rgba(255,92,26,0.08)",  iconColor:"#FF5C1A", label:"High"     },
  medium:   { border:"#D97706", badge:"rgba(217,119,6,0.08)",  badgeText:"#D97706", badgeBorder:"rgba(217,119,6,0.2)",  iconBg:"rgba(217,119,6,0.08)",  iconColor:"#D97706", label:"Medium"   },
  resolved: { border:"#16A34A", badge:"rgba(22,163,74,0.08)",  badgeText:"#16A34A", badgeBorder:"rgba(22,163,74,0.2)",  iconBg:"rgba(22,163,74,0.08)",  iconColor:"#16A34A", label:"Resolved" },
};

function alertIcon(s: Severity) {
  if (s === "critical" || s === "high") return AlertTriangle;
  if (s === "resolved") return CheckCircle2;
  return Info;
}

// ─── Pill Toggle ───────────────────────────────────────────────────────────

function PillToggle({ on, onToggle }: { on: boolean; onToggle: () => void }) {
  return (
    <button
      onClick={onToggle}
      aria-pressed={on}
      style={{
        width: 44, height: 24, borderRadius: 9999,
        backgroundColor: on ? "#FF5C1A" : "#F0F2F5",
        border: "none", cursor: "pointer", position: "relative",
        flexShrink: 0, transition: "background-color 200ms ease",
      }}
    >
      <span style={{
        position: "absolute", top: 3, left: on ? 23 : 3,
        width: 18, height: 18, borderRadius: 9999,
        backgroundColor: "#ffffff",
        transition: "left 200ms ease",
        boxShadow: "0 1px 3px rgba(0,0,0,0.20)",
        display: "block",
      }} />
    </button>
  );
}

// ─── Select Dropdown ───────────────────────────────────────────────────────

function FilterSelect({ label }: { label: string }) {
  return (
    <div className="relative flex items-center">
      <select className="appearance-none outline-none cursor-pointer pr-8 font-medium"
        style={{ backgroundColor:"#F8FAFC", border:"1px solid #E2E8F0", borderRadius:12, padding:"7px 14px", fontSize:13, color:"#1A1A2E", fontFamily:"Inter, sans-serif" }}>
        <option>{label}</option>
      </select>
      <ChevronDown size={13} color="#94A3B8" className="absolute right-3 pointer-events-none" />
    </div>
  );
}

// ─── Single Alert Row ──────────────────────────────────────────────────────

function AlertRow({ alert, onResolve, isResolving }: { alert: Alert; onResolve: (id: string) => void; isResolving?: boolean }) {
  const cf = sevConf[alert.severity];
  const Icon = alertIcon(alert.severity);
  const isResolved = alert.severity === "resolved";

  return (
    <div
      style={{
        display: "flex", alignItems: "flex-start", gap: 16,
        padding: "18px 20px",
        borderLeft: `3px solid ${cf.border}`,
        borderBottom: "1px solid #F8FAFC",
        position: "relative",
        opacity: isResolved ? 0.75 : 1,
        transition: "background-color 150ms",
        backgroundColor: "transparent",
      }}
      onMouseEnter={e => { (e.currentTarget as HTMLDivElement).style.backgroundColor = "#FAFAFA"; }}
      onMouseLeave={e => { (e.currentTarget as HTMLDivElement).style.backgroundColor = "transparent"; }}
    >
      {/* Icon */}
      <div className="flex items-center justify-center rounded-xl flex-shrink-0"
        style={{ width: 38, height: 38, backgroundColor: cf.iconBg, marginTop: 2 }}>
        <Icon size={17} strokeWidth={2} color={cf.iconColor} />
      </div>

      {/* Content */}
      <div className="flex-1 min-w-0">
        {/* Title row */}
        <div className="flex items-center gap-2 flex-wrap">
          {/* Severity badge */}
          <span className="font-semibold" style={{ fontSize: 11, backgroundColor: cf.badge, color: cf.badgeText, border: `1px solid ${cf.badgeBorder}`, borderRadius: 9999, padding: "2px 8px", letterSpacing: "0.04em", textTransform: "uppercase" }}>
            {cf.label}
          </span>
          <span className="font-semibold" style={{ fontSize: 14, color: "#1A1A2E" }}>{alert.title}</span>
        </div>

        {/* Description */}
        <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 4, lineHeight: 1.4 }}>{alert.desc}</p>

        {/* Meta row */}
        <div className="flex items-center flex-wrap gap-1 mt-2" style={{ fontSize: 12, color: "#94A3B8" }}>
          <span>User: <span style={{ color: "#64748B" }}>{alert.user}</span></span>
          <span style={{ color: "#CBD5E1" }}>•</span>
          <span>Tool: <span style={{ color: "#64748B" }}>{alert.tool}</span></span>
          <span style={{ color: "#CBD5E1" }}>•</span>
          <span>Dept: <span style={{ color: "#64748B" }}>{alert.dept}</span></span>
          <span style={{ color: "#CBD5E1" }}>•</span>
          <span>{alert.time}</span>
          {alert.resolvedBy && (
            <>
              <span style={{ color: "#CBD5E1" }}>•</span>
              <span>Resolved by <span style={{ color: "#16A34A" }}>{alert.resolvedBy}</span></span>
            </>
          )}
        </div>
      </div>

      {/* Right: unread dot + actions */}
      <div className="flex flex-col items-end gap-2 flex-shrink-0">
        {/* Unread dot */}
        {alert.unread && (
          <span className="rounded-full" style={{ width: 8, height: 8, backgroundColor: "#FF5C1A", display: "block", marginBottom: 4 }} />
        )}

        {isResolved ? (
          <span className="font-semibold" style={{ fontSize: 12, backgroundColor: "rgba(22,163,74,0.08)", color: "#16A34A", border: "1px solid rgba(22,163,74,0.2)", borderRadius: 9999, padding: "3px 10px" }}>
            Resolved ✓
          </span>
        ) : (
          <div className="flex items-center gap-3">
            <button className="font-semibold" style={{ background: "none", border: "none", cursor: "pointer", fontSize: 13, color: "#FF5C1A", fontFamily: "Inter, sans-serif", padding: 0 }}>
              View Details
            </button>
            <button className="font-medium" style={{ background: "none", border: "none", cursor: isResolving ? "wait" : "pointer", fontSize: 13, color: "#94A3B8", fontFamily: "Inter, sans-serif", padding: 0, opacity: isResolving ? 0.5 : 1 }}
              onClick={() => onResolve(alert.id)}
              disabled={isResolving}>
              {isResolving ? "Resolving..." : "Resolve"}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

// ─── MAIN COMPONENT ─────────────────────────────────────────────────────────

export function AlertsTab() {
  const [unreadOnly, setUnreadOnly] = useState(false);
  const [localResolved, setLocalResolved] = useState<Map<string, string>>(new Map());
  const [rules, setRules] = useState([true, true, false]);
  const [hoverRule, setHoverRule] = useState<number | null>(null);
  const { toast } = useToast();
  const queryClient = useQueryClient();

  const { data: alertItems, isLoading, error } = useAlerts();

  const resolveMutation = useMutation({
    mutationFn: resolveAlert,
    onSuccess: (_data, alertId) => {
      setLocalResolved(prev => new Map(prev).set(alertId, "Admin"));
      queryClient.invalidateQueries({ queryKey: ["alerts"] });
      toast({
        title: "Alert Resolved",
        description: "Policy violation marked as cleared successfully.",
        duration: 3000,
      });
    },
    onError: (err: Error) => {
      toast({
        title: "Failed to resolve alert",
        description: err.message,
        duration: 4000,
      });
    },
  });

  const alerts: Alert[] = useMemo(() => {
    if (!alertItems) return [];
    return alertItems.map(item => {
      const alert = mapAlertItemToAlert(item);
      if (localResolved.has(item.id)) {
        return { ...alert, severity: "resolved" as Severity, unread: false, resolvedBy: localResolved.get(item.id) };
      }
      return alert;
    });
  }, [alertItems, localResolved]);

  const displayed = unreadOnly ? alerts.filter(a => a.unread) : alerts;

  const handleResolve = (id: string) => {
    resolveMutation.mutate(id);
  };

  // Computed stats
  const criticalCount = alerts.filter(a => a.severity === "critical").length;
  const highCount = alerts.filter(a => a.severity === "high").length;
  const mediumCount = alerts.filter(a => a.severity === "medium").length;
  const resolvedCount = alerts.filter(a => a.severity === "resolved").length;

  const ruleConf = [
    { Icon: ShieldAlert, color: "#FF5C1A", label: "Finance dept uses unapproved tool", action: "Block + Alert", actionColor: "#DC2626", actionBg: "rgba(220,38,38,0.08)", actionBorder: "rgba(220,38,38,0.2)" },
    { Icon: AlertTriangle, color: "#DC2626", label: "HIGH risk tool detected",          action: "Alert only",   actionColor: "#D97706", actionBg: "rgba(217,119,6,0.08)",  actionBorder: "rgba(217,119,6,0.2)"  },
    { Icon: Bell,          color: "#D97706", label: "After-hours usage",                action: "Log only",     actionColor: "#64748B", actionBg: "#F8FAFC",               actionBorder: "#E2E8F0"              },
  ];

  // ─── Loading skeleton ──────────────────────────────────────────────────
  if (isLoading) {
    return (
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Alerts</h1>
            <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Policy violations and high-risk activity notifications</p>
          </div>
        </div>
        <div className="flex gap-4">
          {[1, 2, 3, 4].map(i => (
            <div key={i} className="flex-1" style={{ borderRadius: 16, padding: 20, border: "1px solid #F0F2F5" }}>
              <Skeleton className="h-3 w-20 mb-3" />
              <Skeleton className="h-9 w-12 mb-2" />
              <Skeleton className="h-3 w-28" />
            </div>
          ))}
        </div>
        <div style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 16, overflow: "hidden" }}>
          <div className="px-5 py-4" style={{ borderBottom: "1px solid #F8FAFC" }}>
            <Skeleton className="h-5 w-32" />
          </div>
          {Array.from({ length: 5 }).map((_, i) => (
            <div key={i} className="flex items-start gap-4 px-5 py-4" style={{ borderBottom: "1px solid #F8FAFC" }}>
              <Skeleton className="h-9 w-9 rounded-xl flex-shrink-0" />
              <div className="flex-1">
                <Skeleton className="h-4 w-48 mb-2" />
                <Skeleton className="h-3 w-64 mb-2" />
                <Skeleton className="h-3 w-40" />
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // ─── Error state ───────────────────────────────────────────────────────
  if (error) {
    return (
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Alerts</h1>
            <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Policy violations and high-risk activity notifications</p>
          </div>
        </div>
        <div style={{ backgroundColor: "#FEF2F2", border: "1px solid #FECACA", borderRadius: 16, padding: "16px 20px" }}>
          <p style={{ fontSize: 14, color: "#DC2626", fontWeight: 500 }}>
            Failed to load alerts: {error.message}
          </p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 4 }}>
            Data will retry automatically. Check your connection if this persists.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4">

      {/* ── Header ─────────────────────────────────────────────── */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Alerts</h1>
          <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Policy violations and high-risk activity notifications</p>
        </div>
        <div className="flex items-center gap-3">
          <button className="font-semibold" style={{ background: "none", border: "none", cursor: "pointer", fontSize: 13, color: "#FF5C1A", fontFamily: "Inter, sans-serif" }}>
            Mark all read
          </button>
          <button className="flex items-center gap-2 font-medium"
            style={{ backgroundColor: "#ffffff", border: "1px solid #E2E8F0", borderRadius: 12, padding: "8px 14px", fontSize: 13, color: "#1A1A2E", cursor: "pointer", fontFamily: "Inter, sans-serif" }}
            onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#ffffff"; }}>
            Configure Alerts
          </button>
        </div>
      </div>

      {/* ── Stats Row ───────────────────────────────────────────── */}
      <div className="flex gap-4">
        {[
          { label: "Critical",       value: String(criticalCount),  sub: "Immediate action",       orange: true,  dotColor: "", subColor: "rgba(255,255,255,0.80)" },
          { label: "High",           value: String(highCount),      sub: "Needs review",           orange: false, dotColor: "#DC2626", subColor: "#DC2626" },
          { label: "Medium",         value: String(mediumCount),    sub: "Monitor closely",        orange: false, dotColor: "#D97706", subColor: "#D97706" },
          { label: "Resolved",       value: String(resolvedCount),  sub: "Closed successfully",    orange: false, dotColor: "#16A34A", subColor: "#16A34A" },
        ].map(card => (
          <div key={card.label} className="flex-1"
            style={{ backgroundColor: card.orange ? "#FF5C1A" : "#ffffff", border: `1px solid ${card.orange ? "#FDDCC8" : "#F0F2F5"}`, borderRadius: 16, padding: 20, boxShadow: "0 1px 3px rgba(0,0,0,0.06)", transition: "transform 200ms, box-shadow 200ms", cursor: "default" }}
            onMouseEnter={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(-1px)"; el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)"; }}
            onMouseLeave={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(0)"; el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)"; }}
          >
            <p className="font-semibold tracking-widest uppercase" style={{ fontSize: 10, color: card.orange ? "rgba(255,255,255,0.75)" : "#94A3B8", letterSpacing: "0.08em" }}>{card.label}</p>
            <p className="font-bold mt-2" style={{ fontSize: 36, color: card.orange ? "#ffffff" : "#1A1A2E", lineHeight: 1 }}>{card.value}</p>
            <div className="flex items-center gap-1.5 mt-2">
              {card.dotColor && <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: card.dotColor, display: "inline-block", flexShrink: 0 }} />}
              <span style={{ fontSize: 12, color: card.subColor }}>{card.sub}</span>
            </div>
          </div>
        ))}
      </div>

      {/* ── Filter Row ──────────────────────────────────────────── */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <FilterSelect label="All Severity" />
          <FilterSelect label="All Types"    />
        </div>
        <div className="flex items-center gap-2.5">
          <span style={{ fontSize: 13, color: "#64748B", fontWeight: 500 }}>Unread only</span>
          <PillToggle on={unreadOnly} onToggle={() => setUnreadOnly(v => !v)} />
        </div>
      </div>

      {/* ── Alerts List ─────────────────────────────────────────── */}
      <div style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 16, boxShadow: "0 1px 3px rgba(0,0,0,0.06)", overflow: "hidden" }}>
        {/* List header */}
        <div className="flex items-center justify-between px-5 py-4" style={{ borderBottom: "1px solid #F8FAFC" }}>
          <p className="font-semibold" style={{ fontSize: 15, color: "#1A1A2E" }}>
            All Alerts
            <span className="font-normal ml-2" style={{ fontSize: 13, color: "#94A3B8" }}>
              ({displayed.length} showing)
            </span>
          </p>
          <span style={{ fontSize: 12, color: "#94A3B8" }}>
            {alerts.filter(a => a.unread).length} unread
          </span>
        </div>

        {/* Alert rows */}
        {displayed.length > 0 ? (
          displayed.map((alert) => (
            <AlertRow
              key={alert.id}
              alert={alert}
              onResolve={handleResolve}
              isResolving={resolveMutation.isPending && resolveMutation.variables === alert.id}
            />
          ))
        ) : (
          <div className="flex flex-col items-center justify-center py-12">
            <CheckCircle2 size={32} strokeWidth={1.5} color="#CBD5E1" />
            <p className="mt-3 font-medium" style={{ fontSize: 14, color: "#94A3B8" }}>
              {unreadOnly ? "No unread alerts" : "No active alerts"}
            </p>
          </div>
        )}
      </div>

      {/* ── Alert Rules ─────────────────────────────────────────── */}
      <div style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 16, padding: 24, boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}>
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div>
            <p className="font-semibold" style={{ fontSize: 15, color: "#1A1A2E" }}>Active Alert Rules</p>
            <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>Automation policies governing alert behavior</p>
          </div>
          <button className="flex items-center gap-1.5 font-semibold"
            style={{ backgroundColor: "#FF5C1A", color: "#ffffff", border: "none", borderRadius: 10, padding: "7px 14px", fontSize: 13, cursor: "pointer", fontFamily: "Inter, sans-serif", transition: "background-color 200ms" }}
            onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#E5521A"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#FF5C1A"; }}>
            <Plus size={13} strokeWidth={2.5} /> Add Rule
          </button>
        </div>

        {/* Rules */}
        <div className="flex flex-col gap-3">
          {ruleConf.map((rule, i) => (
            <div key={i}
              className="flex items-center gap-4 rounded-xl px-4 py-3 transition-colors"
              style={{ border: "1px solid #F0F2F5", cursor: "default", position: "relative" }}
              onMouseEnter={() => setHoverRule(i)}
              onMouseLeave={() => setHoverRule(null)}
            >
              {/* Icon */}
              <div className="flex items-center justify-center rounded-xl flex-shrink-0"
                style={{ width: 36, height: 36, backgroundColor: `${rule.color}14` }}>
                <rule.Icon size={16} strokeWidth={2} color={rule.color} />
              </div>

              {/* Label */}
              <span className="font-medium flex-1" style={{ fontSize: 14, color: "#1A1A2E" }}>{rule.label}</span>

              {/* Action badge */}
              <span className="font-semibold flex-shrink-0" style={{ fontSize: 12, backgroundColor: rule.actionBg, color: rule.actionColor, border: `1px solid ${rule.actionBorder}`, borderRadius: 9999, padding: "3px 10px" }}>
                {rule.action}
              </span>

              {/* Edit icon (hover) */}
              {hoverRule === i && (
                <button style={{ background: "none", border: "none", cursor: "pointer", padding: 4, flexShrink: 0 }}>
                  <Pencil size={14} strokeWidth={2} color="#94A3B8" />
                </button>
              )}

              {/* Toggle */}
              <PillToggle on={rules[i]} onToggle={() => setRules(prev => prev.map((v, j) => j === i ? !v : v))} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\AnalyticsCharts.tsx

```tsx
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell, LineChart, Line,
} from "recharts";
import { useAnalytics } from "@/hooks/useDashboard";

const COLORS = [
  "hsl(16, 90%, 55%)",
  "hsl(200, 70%, 50%)",
  "hsl(142, 71%, 45%)",
  "hsl(280, 65%, 60%)",
  "hsl(38, 92%, 50%)",
  "hsl(340, 75%, 55%)",
  "hsl(180, 60%, 45%)",
  "hsl(60, 80%, 45%)",
];

export function AnalyticsCharts() {
  const { data } = useAnalytics();

  const byTool      = data?.byTool      ?? [];
  const byCategory  = data?.byCategory  ?? [];
  const overTime    = data?.overTime    ?? [];
  const topProcesses = data?.topProcesses ?? [];

  return (
    <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm font-medium text-muted-foreground">Detections by Tool</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[260px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={byTool} layout="vertical" margin={{ left: 0, right: 16 }}>
                <CartesianGrid strokeDasharray="3 3" className="stroke-border" horizontal={false} />
                <XAxis type="number" className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <YAxis type="category" dataKey="name" width={110} className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <Tooltip contentStyle={{ background: "hsl(var(--card))", border: "1px solid hsl(var(--border))", borderRadius: 8, fontSize: 12 }} />
                <Bar dataKey="count" fill="hsl(var(--primary))" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm font-medium text-muted-foreground">By Category</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[260px]">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={byCategory} cx="50%" cy="50%" innerRadius={55} outerRadius={90} dataKey="value" nameKey="name" label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`} labelLine={false} className="text-xs">
                  {byCategory.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip contentStyle={{ background: "hsl(var(--card))", border: "1px solid hsl(var(--border))", borderRadius: 8, fontSize: 12 }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm font-medium text-muted-foreground">Detections Over Time</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[260px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={overTime} margin={{ left: 0, right: 16 }}>
                <CartesianGrid strokeDasharray="3 3" className="stroke-border" />
                <XAxis dataKey="time" className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <YAxis className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <Tooltip contentStyle={{ background: "hsl(var(--card))", border: "1px solid hsl(var(--border))", borderRadius: 8, fontSize: 12 }} />
                <Line type="monotone" dataKey="count" stroke="hsl(var(--primary))" strokeWidth={2} dot={{ fill: "hsl(var(--primary))", r: 4 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm font-medium text-muted-foreground">Top Processes</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[260px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={topProcesses} margin={{ left: 0, right: 16 }}>
                <CartesianGrid strokeDasharray="3 3" className="stroke-border" />
                <XAxis dataKey="name" className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <YAxis className="text-xs" tick={{ fill: "hsl(var(--muted-foreground))" }} />
                <Tooltip contentStyle={{ background: "hsl(var(--card))", border: "1px solid hsl(var(--border))", borderRadius: 8, fontSize: 12 }} />
                <Bar dataKey="count" fill="hsl(200, 70%, 50%)" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\AnalyticsTab.tsx

```tsx
import { useState, useEffect, useRef } from "react";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip as RTooltip,
  ResponsiveContainer, PieChart, Pie, Cell,
} from "recharts";
import { ChevronDown, Check } from "lucide-react";
import { useAnalytics } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Shared card shell ─────────────────────────────────────────────────────
function Card({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <div
      className={`flex flex-col ${className}`}
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        padding: 24,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      }}
    >
      {children}
    </div>
  );
}

function CardHeader({ title, sub }: { title: string; sub: string }) {
  return (
    <div className="mb-5">
      <p className="font-semibold" style={{ fontSize: 16, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>{title}</p>
      <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>{sub}</p>
    </div>
  );
}

// ─── Pie chart colors ──────────────────────────────────────────────────────
const PIE_COLORS = ["#DC2626", "#D97706", "#16A34A", "#3B82F6", "#7C3AED", "#0891B2", "#DB2777", "#64748B"];

// ─── Horizontal bar custom tooltip ────────────────────────────────────────
function BarTip({ active, payload, label }: any) {
  if (!active || !payload?.length) return null;
  return (
    <div style={{ background:"#1A1A2E", color:"#fff", padding:"6px 12px", borderRadius:8, fontSize:12 }}>
      <b>{label}</b>: {payload[0].value}
    </div>
  );
}

// ─── Skeleton placeholders ─────────────────────────────────────────────────
function ChartSkeleton({ height = 200 }: { height?: number }) {
  return (
    <div className="flex flex-col gap-3" style={{ height }}>
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i} className="flex items-center gap-3">
          <Skeleton className="h-4 w-20" />
          <Skeleton className="h-4 flex-1" />
        </div>
      ))}
    </div>
  );
}

function ListSkeleton({ rows = 5 }: { rows?: number }) {
  return (
    <div className="flex flex-col gap-3">
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="flex items-center gap-3">
          <Skeleton className="h-7 w-7 rounded-full" />
          <div className="flex-1">
            <Skeleton className="h-4 w-24 mb-1" />
            <Skeleton className="h-3 w-full" />
          </div>
          <Skeleton className="h-5 w-10 rounded-full" />
        </div>
      ))}
    </div>
  );
}

// ─── MAIN COMPONENT ────────────────────────────────────────────────────────
export function AnalyticsTab() {
  const [dateFilter, setDateFilter] = useState("Last 30 days");
  const [isDateOpen, setIsDateOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const { data: analytics, isLoading, error } = useAnalytics();

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setIsDateOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const handleDateChange = (range: string) => {
    setDateFilter(range);
    setIsDateOpen(false);
    // Phase 2: re-fetch analytics with date range param
  };

  // Derived data from API
  const byCategory = analytics?.byCategory ?? [];
  const byTool = analytics?.byTool ?? [];
  const overTime = analytics?.overTime ?? [];
  const topProcesses = analytics?.topProcesses ?? [];

  // Prepare bar chart data (byCategory → horizontal bars)
  const barData = byCategory.map(c => ({ dept: c.name, count: c.value }));

  // Prepare pie chart data (byCategory as donut)
  const pieTotal = byCategory.reduce((sum, c) => sum + c.value, 0);
  const pieData = byCategory.map((c, i) => ({
    name: c.name,
    value: c.value,
    color: PIE_COLORS[i % PIE_COLORS.length],
  }));

  // Prepare top tools with rank and percent bar
  const maxToolCount = byTool.length > 0 ? Math.max(...byTool.map(t => t.count)) : 1;
  const toolsDisplay = byTool.slice(0, 5).map((t, i) => ({
    rank: i + 1,
    name: t.name,
    uses: t.count,
    pct: Math.round((t.count / maxToolCount) * 100),
  }));

  // Prepare overTime for vertical bar chart
  const overTimeData = overTime.map(d => ({ time: d.time, count: d.count }));

  // Top processes
  const maxProcCount = topProcesses.length > 0 ? Math.max(...topProcesses.map(p => p.count)) : 1;
  const processesDisplay = topProcesses.slice(0, 5).map((p, i) => ({
    rank: i + 1,
    name: p.name,
    uses: p.count,
    pct: Math.round((p.count / maxProcCount) * 100),
  }));

  return (
    <div className="flex flex-col gap-4">

      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-bold" style={{ fontSize:22, color:"#1A1A2E", fontFamily:"Inter, sans-serif" }}>Analytics</h1>
          <p style={{ fontSize:14, color:"#94A3B8", marginTop:3 }}>AI adoption and usage insights across your organization</p>
        </div>
        <div className="relative" ref={dropdownRef}>
          <button
            onClick={() => setIsDateOpen(!isDateOpen)}
            className="flex items-center gap-2 font-medium"
            style={{ backgroundColor:"#F8FAFC", border:"1px solid #E2E8F0", borderRadius:12, padding:"8px 14px", fontSize:14, color:"#1A1A2E", cursor:"pointer", fontFamily:"Inter, sans-serif" }}
          >
            {dateFilter} <ChevronDown size={14} color="#94A3B8" strokeWidth={2} />
          </button>
          {isDateOpen && (
            <div 
              className="absolute top-full right-0 mt-2 bg-white flex flex-col z-10"
              style={{ width: 160, border: "1px solid #F0F2F5", borderRadius: 12, boxShadow: "0 10px 24px rgba(0,0,0,0.08)", padding: 6 }}
            >
              {["Last 7 days", "Last 30 days", "Last 3 months", "Last 12 months"].map(opt => (
                <button
                  key={opt}
                  onClick={() => handleDateChange(opt)}
                  className="flex items-center justify-between w-full text-left transition-colors"
                  style={{ padding: "8px 12px", borderRadius: 8, fontSize: 13, color: dateFilter === opt ? "#FF5C1A" : "#1A1A2E", fontFamily: "Inter, sans-serif", backgroundColor: dateFilter === opt ? "#FFF3EE" : "transparent" }}
                  onMouseEnter={e => { if (dateFilter !== opt) e.currentTarget.style.backgroundColor = "#F8FAFC"; }}
                  onMouseLeave={e => { if (dateFilter !== opt) e.currentTarget.style.backgroundColor = "transparent"; }}
                >
                  {opt}
                  {dateFilter === opt && <Check size={14} color="#FF5C1A" strokeWidth={2.5} />}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Error message */}
      {error && (
        <p style={{ fontSize: 13, color: "#DC2626", padding: "4px 0" }}>
          Failed to load analytics data. Retrying…
        </p>
      )}

      {/* Row 1 — Charts */}
      <div className="flex gap-4">

        {/* Left: Horizontal bar chart — Usage by Category */}
        <Card className="flex-1">
          <CardHeader title="Usage by Category" sub={`Total detections per category (${dateFilter.toLowerCase()})`} />
          {isLoading ? (
            <ChartSkeleton height={200} />
          ) : barData.length === 0 ? (
            <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center", padding: "40px 0" }}>No analytics data yet</p>
          ) : (
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={barData} layout="vertical" margin={{ top:0, right:16, left:0, bottom:0 }} barCategoryGap="28%">
                <XAxis type="number" axisLine={false} tickLine={false}
                  tick={{ fontSize:11, fill:"#CBD5E1" }} />
                <YAxis type="category" dataKey="dept" axisLine={false} tickLine={false}
                  tick={{ fontSize:13, fill:"#94A3B8", fontFamily:"Inter, sans-serif" }} width={90} />
                <RTooltip content={<BarTip />} cursor={{ fill:"rgba(0,0,0,0.03)" }} />
                <Bar dataKey="count" fill="#FF5C1A" radius={[0, 6, 6, 0]} maxBarSize={28} />
              </BarChart>
            </ResponsiveContainer>
          )}
        </Card>

        {/* Right: Donut chart — Category Distribution */}
        <div style={{ flex:"0 0 320px" }}>
          <Card>
          <CardHeader title="Category Distribution" sub={`Detections by category (${dateFilter.toLowerCase()})`} />
          {isLoading ? (
            <div className="flex flex-col items-center gap-4">
              <Skeleton className="rounded-full" style={{ width: 200, height: 200 }} />
              <div className="flex gap-4">
                <Skeleton className="h-4 w-16" />
                <Skeleton className="h-4 w-16" />
                <Skeleton className="h-4 w-16" />
              </div>
            </div>
          ) : pieData.length === 0 ? (
            <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center", padding: "40px 0" }}>No analytics data yet</p>
          ) : (
            <div className="flex flex-col items-center">
              {/* Donut chart with center overlay */}
              <div className="relative inline-block">
                <ResponsiveContainer width={200} height={200}>
                  <PieChart>
                    <Pie
                      data={pieData}
                      cx="50%"
                      cy="50%"
                      innerRadius={60}
                      outerRadius={90}
                      paddingAngle={3}
                      dataKey="value"
                      labelLine={false}
                      strokeWidth={0}
                    >
                      {pieData.map((d, i) => <Cell key={i} fill={d.color} />)}
                    </Pie>
                  </PieChart>
                </ResponsiveContainer>
                {/* Center label as absolute overlay */}
                <div
                  className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none"
                >
                  <span className="font-bold" style={{ fontSize: 24, color: "#1A1A2E", lineHeight: 1.1 }}>{pieTotal}</span>
                  <span style={{ fontSize: 12, color: "#94A3B8" }}>Total</span>
                </div>
              </div>

              {/* Legend */}
              <div className="flex items-center gap-5 mt-1 flex-wrap justify-center">
                {pieData.map((d) => (
                  <div key={d.name} className="flex items-center gap-1.5">
                    <span className="rounded-full" style={{ width:9, height:9, backgroundColor:d.color, display:"inline-block" }} />
                    <span style={{ fontSize:13, color:"#64748B" }}>{d.name}</span>
                    <span className="font-semibold" style={{ fontSize:13, color:"#1A1A2E" }}>
                      {pieTotal > 0 ? Math.round((d.value / pieTotal) * 100) : 0}%
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </Card>
        </div>{/* end 320px wrapper */}
      </div>{/* end Row 1 flex */}

      {/* Row 2 — Detections Over Time (replaces heatmap) */}
      <Card>
        <CardHeader title="Detections Over Time" sub={`Detection volume trend (${dateFilter.toLowerCase()})`} />
        {isLoading ? (
          <ChartSkeleton height={200} />
        ) : overTimeData.length === 0 ? (
          <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center", padding: "40px 0" }}>No time-series data yet</p>
        ) : (
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={overTimeData} margin={{ top:0, right:16, left:0, bottom:0 }} barCategoryGap="20%">
              <XAxis dataKey="time" axisLine={false} tickLine={false}
                tick={{ fontSize:11, fill:"#CBD5E1" }} />
              <YAxis axisLine={false} tickLine={false}
                tick={{ fontSize:11, fill:"#CBD5E1" }} />
              <RTooltip content={<BarTip />} cursor={{ fill:"rgba(0,0,0,0.03)" }} />
              <Bar dataKey="count" fill="#FF5C1A" radius={[4, 4, 0, 0]} maxBarSize={32} />
            </BarChart>
          </ResponsiveContainer>
        )}
      </Card>

      {/* Row 3 — Three cards */}
      <div className="flex gap-4">

        {/* Top Tools */}
        <Card className="flex-1">
          <CardHeader title={`Top Tools (${dateFilter})`} sub="By detection volume" />
          {isLoading ? (
            <ListSkeleton rows={5} />
          ) : toolsDisplay.length === 0 ? (
            <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center", padding: "40px 0" }}>No tool data yet</p>
          ) : (
            <div className="flex flex-col gap-3">
              {toolsDisplay.map(t => (
                <div key={t.rank} className="flex items-center gap-3">
                  {/* Rank circle */}
                  <div
                    className="flex items-center justify-center rounded-full flex-shrink-0 font-bold"
                    style={{ width:26, height:26, backgroundColor: t.rank === 1 ? "#FFF3EE" : "#F8FAFC", fontSize:12, color: t.rank === 1 ? "#FF5C1A" : "#94A3B8" }}
                  >
                    {t.rank}
                  </div>

                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-semibold truncate" style={{ fontSize:13, color:"#1A1A2E" }}>{t.name}</span>
                      <span style={{ fontSize:12, color:"#94A3B8", flexShrink:0, marginLeft:8 }}>{t.uses} uses</span>
                    </div>
                    <div className="w-full rounded-full" style={{ height:6, backgroundColor:"#FFF3EE" }}>
                      <div className="rounded-full" style={{ height:6, width:`${t.pct}%`, backgroundColor:"#FF5C1A", transition:"width 600ms ease" }} />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Card>

        {/* Top Processes */}
        <Card className="flex-1">
          <CardHeader title="Top Processes" sub={`By detection count (${dateFilter.toLowerCase()})`} />
          {isLoading ? (
            <ListSkeleton rows={5} />
          ) : processesDisplay.length === 0 ? (
            <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center", padding: "40px 0" }}>No process data yet</p>
          ) : (
            <div className="flex flex-col gap-3">
              {processesDisplay.map(p => (
                <div key={p.rank} className="flex items-center gap-3">
                  {/* Rank circle */}
                  <div
                    className="flex items-center justify-center rounded-full flex-shrink-0 font-bold"
                    style={{ width:26, height:26, backgroundColor: p.rank === 1 ? "#FFF3EE" : "#F8FAFC", fontSize:12, color: p.rank === 1 ? "#FF5C1A" : "#94A3B8" }}
                  >
                    {p.rank}
                  </div>

                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-semibold truncate" style={{ fontFamily: "'JetBrains Mono', 'Fira Code', monospace", fontSize:13, color:"#1A1A2E" }}>{p.name}</span>
                      <span style={{ fontSize:12, color:"#94A3B8", flexShrink:0, marginLeft:8 }}>{p.uses} detections</span>
                    </div>
                    <div className="w-full rounded-full" style={{ height:6, backgroundColor:"#FFF3EE" }}>
                      <div className="rounded-full" style={{ height:6, width:`${p.pct}%`, backgroundColor:"#FF5C1A", transition:"width 600ms ease" }} />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Card>

        {/* Data Not Available — placeholder for Shadow AI / Most Active Users */}
        <Card className="flex-1">
          <div className="mb-4">
            <p className="font-semibold" style={{ fontSize:16, color:"#1A1A2E" }}>Most Active Users</p>
            <p style={{ fontSize:13, color:"#94A3B8", marginTop:2 }}>Top users by event count</p>
          </div>
          <div className="flex-1 flex items-center justify-center" style={{ minHeight: 180 }}>
            <p style={{ fontSize: 14, color: "#94A3B8", textAlign: "center" }}>
              Data not available — coming in a future update
            </p>
          </div>
        </Card>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\BentoRow.tsx

```tsx
import {
  Briefcase,
  Wallet,
  Monitor,
  Trash2,
  ArrowUpRight,
  ArrowDownRight,
} from "lucide-react";
import { useSpendOverview, useStats } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Error badge ───────────────────────────────────────────────────────────

function ErrorBadge() {
  return (
    <span
      className="absolute top-2 left-2 flex items-center justify-center rounded-full font-bold"
      style={{
        width: 18,
        height: 18,
        backgroundColor: "#DC2626",
        color: "#ffffff",
        fontSize: 11,
        lineHeight: 1,
        zIndex: 2,
      }}
      title="Failed to load data"
    >
      !
    </span>
  );
}

// ─── Pulse placeholder ────────────────────────────────────────────────────

function ValueSkeleton() {
  return (
    <Skeleton
      style={{ width: 96, height: 28, borderRadius: 6, marginTop: 8 }}
    />
  );
}

// ─── Currency formatter (Indian Rupee) ─────────────────────────────────────

function formatINR(n: number): string {
  return "₹" + n.toLocaleString("en-IN");
}

// ─── Shared metric card shell ──────────────────────────────────────────────

interface MetricCardProps {
  label: string;
  value: React.ReactNode;
  sub: React.ReactNode;
  iconBg: string;
  icon: React.ElementType;
  iconColor: string;
  onClick?: () => void;
  isDanger?: boolean;
  isLoading?: boolean;
  error?: boolean;
}

function MetricCard({
  label,
  value,
  sub,
  iconBg,
  icon: Icon,
  iconColor,
  onClick,
  isDanger,
  isLoading,
  error,
}: MetricCardProps) {
  return (
    <div
      onClick={onClick}
      className="relative cursor-pointer transition-all duration-200 flex flex-col justify-between"
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        padding: "20px 20px",
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        height: "100%"
      }}
      onMouseEnter={(e) => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(-2px)";
        el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)";
      }}
      onMouseLeave={(e) => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(0)";
        el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)";
      }}
    >
      {error && <ErrorBadge />}

      {/* Top-right icon */}
      <div
        className="absolute top-4 right-4 flex items-center justify-center rounded-full flex-shrink-0"
        style={{ width: 32, height: 32, backgroundColor: iconBg }}
      >
        <Icon size={16} strokeWidth={1.5} color={iconColor} />
      </div>

      {/* Content wrapper to match exact spacing */}
      <div>
        {/* Label */}
        <p
          className="font-medium tracking-widest uppercase"
          style={{ fontSize: 11, color: "#94A3B8", letterSpacing: "0.08em", fontFamily: "Inter, sans-serif" }}
        >
          {label}
        </p>

        {/* Value */}
        {isLoading ? (
          <ValueSkeleton />
        ) : (
          <p
            className="font-bold"
            style={{
              fontSize: 32,
              color: isDanger ? "#DC2626" : "#1A1A2E",
              fontFamily: "Inter, sans-serif",
              lineHeight: 1.1,
              marginTop: 8
            }}
          >
            {value}
          </p>
        )}

        {/* Sub-line */}
        <div style={{ marginTop: 6 }} className="flex items-center gap-1.5">{sub}</div>
      </div>
    </div>
  );
}

// ─── Sub-line helpers ──────────────────────────────────────────────────────

function GreenUp({ text }: { text: string }) {
  return (
    <>
      <ArrowUpRight size={14} color="#16A34A" strokeWidth={2} />
      <span style={{ fontSize: 13, color: "#16A34A", fontFamily: "Inter, sans-serif", fontWeight: 400 }}>{text}</span>
    </>
  );
}

function RedDown({ text }: { text: string }) {
  return (
    <>
      <ArrowDownRight size={14} color="#DC2626" strokeWidth={2} />
      <span style={{ fontSize: 13, color: "#DC2626", fontFamily: "Inter, sans-serif", fontWeight: 400 }}>{text}</span>
    </>
  );
}

function GreenDot({ text }: { text: string }) {
  return (
    <>
      <span
        className="rounded-full flex-shrink-0"
        style={{ width: 8, height: 8, backgroundColor: "#16A34A" }}
      />
      <span style={{ fontSize: 13, color: "#16A34A", fontFamily: "Inter, sans-serif", fontWeight: 400 }}>{text}</span>
    </>
  );
}

function RedText({ text }: { text: string }) {
  return <span style={{ fontSize: 13, color: "#DC2626", fontFamily: "Inter, sans-serif", fontWeight: 400 }}>{text}</span>;
}

// ─── Exported component ────────────────────────────────────────────────────

export function BentoRow({ onNavigate }: { onNavigate: (tab: string) => void }) {
  const { data: spend, isLoading: spendLoading, error: spendError } = useSpendOverview();
  const { data: stats, isLoading: statsLoading, error: statsError } = useStats();

  const hasSpendError = !!spendError;
  const hasStatsError = !!statsError;

  return (
    <div
      style={{
        flex: "0 0 auto",
        width: 424,
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gridTemplateRows: "1fr 1fr",
        gap: 16,
        alignItems: "stretch"
      }}
    >
      {/* Card A — Total AI Spend */}
      <MetricCard
        label="TOTAL AI SPEND"
        value={spend ? formatINR(spend.totalMonthlySpend) : "—"}
        sub={<GreenUp text="8% this month" />}
        iconBg="#F0FDF4"
        icon={Briefcase}
        iconColor="#16A34A"
        onClick={() => onNavigate("subscriptions")}
        isLoading={spendLoading}
        error={hasSpendError}
      />

      {/* Card B — Budget Remaining */}
      <MetricCard
        label="BUDGET REMAINING"
        value={spend ? formatINR(spend.budgetRemaining) : "—"}
        sub={<RedDown text="5% this month" />}
        iconBg="#FFF7ED"
        icon={Wallet}
        iconColor="#D97706"
        onClick={() => onNavigate("subscriptions")}
        isLoading={spendLoading}
        error={hasSpendError}
      />

      {/* Card C — Active Agents */}
      <MetricCard
        label="ACTIVE AGENTS"
        value={stats ? `${stats.onlineDevices}/${stats.totalDevices}` : "—"}
        sub={<GreenDot text="Browser + Desktop" />}
        iconBg="#EFF6FF"
        icon={Monitor}
        iconColor="#3B82F6"
        onClick={() => onNavigate("devices")}
        isLoading={statsLoading}
        error={hasStatsError}
      />

      {/* Card D — Zombie Licenses */}
      <MetricCard
        label="ZOMBIE LICENSES"
        value={spend?.zombieLicenses ?? 0}
        sub={<RedText text={spend ? `${formatINR(spend.zombieCost)} wasted` : "—"} />}
        iconBg="#FEF2F2"
        icon={Trash2}
        iconColor="#DC2626"
        isDanger={true}
        onClick={() => {
          onNavigate("subscriptions");
          // Dispatch a custom event to tell the Subscriptions page to filter by Zombie
          setTimeout(() => {
            window.dispatchEvent(new CustomEvent('filter-zombie-licenses'));
          }, 50);
        }}
        isLoading={spendLoading}
        error={hasSpendError}
      />
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\BudgetProgress.tsx

```tsx
import { useSpendOverview } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";

export function BudgetProgress() {
  const { data: spend, isLoading, error } = useSpendOverview();

  const spent = spend?.totalMonthlySpend ?? 0;
  const total = spend?.monthlyBudget ?? 0;
  const pct = total > 0 ? Math.round((spent / total) * 100) : 0;

  const fmt = (n: number) =>
    "₹" + n.toLocaleString("en-IN");

  return (
    <div
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        padding: 24,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        transition: "box-shadow 200ms ease",
      }}
      onMouseEnter={(e) => { (e.currentTarget as HTMLDivElement).style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)"; }}
      onMouseLeave={(e) => { (e.currentTarget as HTMLDivElement).style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)"; }}
    >
      {/* Title */}
      <p
        className="font-semibold"
        style={{ fontSize: 15, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
      >
        Monthly Budget Usage
      </p>

      {error && (
        <p style={{ fontSize: 12, color: "#DC2626", marginTop: 6 }}>
          Unable to load budget data
        </p>
      )}

      {/* Progress bar */}
      {isLoading ? (
        <Skeleton className="w-full mt-4" style={{ height: 10, borderRadius: 9999 }} />
      ) : (
        <div
          className="w-full rounded-full overflow-hidden mt-4"
          style={{ height: 10, backgroundColor: "#F0F2F5" }}
        >
          <div
            className="h-full rounded-full"
            style={{
              width: `${pct}%`,
              background: "linear-gradient(to right, #FF5C1A, #FF8C42)",
              transition: "width 600ms ease",
            }}
          />
        </div>
      )}

      {/* Labels */}
      {isLoading ? (
        <div className="flex items-center justify-between mt-2.5">
          <Skeleton style={{ width: 100, height: 14, borderRadius: 4 }} />
          <Skeleton style={{ width: 72, height: 14, borderRadius: 4 }} />
        </div>
      ) : (
        <div className="flex items-center justify-between mt-2.5">
          <span style={{ fontSize: 13, color: "#1A1A2E", fontWeight: 500 }}>
            {fmt(spent)} spent
          </span>
          <span style={{ fontSize: 13, color: "#94A3B8" }}>
            {fmt(total)}
          </span>
        </div>
      )}
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\CategoryBadge.tsx

```tsx
import { Badge } from "@/components/ui/badge";

interface CategoryBadgeProps {
  category: string;
}

const categoryColors: Record<string, string> = {
  chat: "bg-blue-500/15 text-blue-600 dark:text-blue-400 border-blue-500/20",
  coding: "bg-violet-500/15 text-violet-600 dark:text-violet-400 border-violet-500/20",
  api: "bg-red-500/15 text-red-600 dark:text-red-400 border-red-500/20",
  image: "bg-pink-500/15 text-pink-600 dark:text-pink-400 border-pink-500/20",
  audio: "bg-cyan-500/15 text-cyan-600 dark:text-cyan-400 border-cyan-500/20",
  video: "bg-orange-500/15 text-orange-600 dark:text-orange-400 border-orange-500/20",
  search: "bg-teal-500/15 text-teal-600 dark:text-teal-400 border-teal-500/20",
  productivity: "bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/20",
};

export function CategoryBadge({ category }: CategoryBadgeProps) {
  return (
    <Badge
      variant="outline"
      className={`text-[11px] font-medium capitalize ${categoryColors[category] || "bg-secondary text-secondary-foreground"} hover:bg-opacity-100`}
    >
      {category}
    </Badge>
  );
}
```

### devise-iris/frontend\src\components\dashboard\DataRiskTab.tsx

```tsx
import { useState, useEffect, useRef, useCallback } from "react";
import { AlertTriangle, RefreshCw, Eye, CheckCheck, User, FileCode, Upload, Clipboard, DollarSign, Key, TrendingUp, Clock, Laptop, ShieldAlert, Activity } from "lucide-react";
import { toast } from "sonner";
import {
  fetchSensitivityEvents,
  fetchEmployeeRiskScores,
  fetchDataRiskStats,
  markSensitivityEventReviewed,
  subscribeToHighRiskEvents,
  rebuildEmployeeRiskScores,
  type SensitivityEvent,
  type EmployeeRiskScore,
  type DataRiskStats,
  type SensitivityFlag,
} from "@/services/api";
import { auth } from "@/lib/firebase";

// ─── Helpers ────────────────────────────────────────────────────────────────
function fmtTs(ts: string | undefined) {
  if (!ts) return "—";
  const d = new Date(ts);
  return isNaN(d.getTime()) ? ts : d.toLocaleString("en-IN", { dateStyle: "short", timeStyle: "short" });
}

const FLAG_META: Record<SensitivityFlag, { label: string; color: string; bg: string; icon: React.ElementType; emoji: string }> = {
  SOURCE_CODE:          { label: "Source Code",         color: "#991B1B", bg: "#FEE2E2",  icon: FileCode,   emoji: "🔴" },
  FILE_UPLOAD:          { label: "File Upload",          color: "#991B1B", bg: "#FEE2E2",  icon: Upload,     emoji: "🔴" },
  LARGE_PASTE:          { label: "Large Paste",          color: "#92400E", bg: "#FEF3C7",  icon: Clipboard,  emoji: "🟡" },
  FINANCIAL_KEYWORDS:   { label: "Financial Keywords",   color: "#92400E", bg: "#FEF3C7",  icon: DollarSign, emoji: "🟡" },
  CREDENTIALS_PATTERN:  { label: "Credentials Pattern",  color: "#7C2D12", bg: "#FFEDD5",  icon: Key,        emoji: "🟠" },
};

function SensitivityBadge({ flag }: { flag: SensitivityFlag }) {
  const m = FLAG_META[flag] ?? { label: flag, color: "#6B7280", bg: "#F3F4F6", icon: AlertTriangle, emoji: "⚪" };
  const Icon = m.icon;
  return (
    <span style={{ background: m.bg, color: m.color, border: `1px solid ${m.color}40`, fontWeight: 600, fontSize: 11, borderRadius: 8, padding: "3px 8px" }}
      className="inline-flex items-center gap-1">
      <Icon size={11} strokeWidth={2} /> {m.emoji} {m.label}
    </span>
  );
}

function RiskScorePill({ score }: { score: number }) {
  const color = score >= 80 ? "#EF4444" : score >= 50 ? "#F59E0B" : "#10B981";
  const bg = score >= 80 ? "#FEE2E2" : score >= 50 ? "#FEF3C7" : "#D1FAE5";
  const label = score >= 80 ? "Critical" : score >= 50 ? "Medium" : "Low";
  return (
    <span style={{ background: bg, color, fontWeight: 700, fontSize: 12, borderRadius: 20, padding: "2px 10px", minWidth: 70, display: "inline-block", textAlign: "center" }}>
      {score} · {label}
    </span>
  );
}

function StatCard({ label, value, icon: Icon, color }: { label: string; value: string | number; icon: React.ElementType; color: string }) {
  return (
    <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16 }} className="flex flex-col gap-2 p-4 flex-1 min-w-0">
      <div className="flex items-center gap-2">
        <div style={{ background: `${color}18`, borderRadius: 8, padding: 6 }}>
          <Icon size={16} strokeWidth={1.5} style={{ color }} />
        </div>
        <span style={{ color: "#8A94A6", fontSize: 12, fontWeight: 500 }}>{label}</span>
      </div>
      <span style={{ color: "#1A1D23", fontSize: 26, fontWeight: 700, lineHeight: 1 }}>{value}</span>
    </div>
  );
}

// ─── Employee Slide-over ─────────────────────────────────────────────────────
function EmployeeDrawer({ employee, events, onClose }: { employee: EmployeeRiskScore; events: SensitivityEvent[]; onClose: () => void }) {
  const empEvents = events.filter(e => e.user_id === employee.user_email);
  return (
    <div className="fixed inset-0 z-50 flex" style={{ background: "rgba(0,0,0,0.35)" }} onClick={onClose}>
      <div className="ml-auto h-full flex flex-col"
        style={{ width: 440, background: "#fff", boxShadow: "-8px 0 32px rgba(0,0,0,0.12)" }}
        onClick={e => e.stopPropagation()}>
        <div className="px-6 py-5" style={{ borderBottom: "1px solid #F0F2F5" }}>
          <div className="flex items-center justify-between mb-1">
            <div className="flex items-center gap-3">
              <div style={{ width: 38, height: 38, borderRadius: "50%", background: "#FF5C1A22", display: "flex", alignItems: "center", justifyContent: "center" }}>
                <User size={18} strokeWidth={1.5} style={{ color: "#FF5C1A" }} />
              </div>
              <div>
                <div style={{ fontWeight: 700, fontSize: 15, color: "#1A1D23" }}>{employee.user_email}</div>
                <RiskScorePill score={employee.risk_score} />
              </div>
            </div>
            <button onClick={onClose} style={{ border: "none", background: "transparent", cursor: "pointer", color: "#9CA3AF", fontSize: 20, lineHeight: 1 }}>×</button>
          </div>
          <div className="flex gap-4 mt-4">
            <div className="text-center"><div style={{ fontSize: 20, fontWeight: 700, color: "#EF4444" }}>{employee.high_risk_events}</div><div style={{ fontSize: 11, color: "#8A94A6" }}>High Risk</div></div>
            <div className="text-center"><div style={{ fontSize: 20, fontWeight: 700, color: "#F59E0B" }}>{employee.medium_risk_events}</div><div style={{ fontSize: 11, color: "#8A94A6" }}>Medium Risk</div></div>
            <div className="text-center"><div style={{ fontSize: 20, fontWeight: 700, color: "#8B5CF6" }}>{employee.top_sensitivity_type || "—"}</div><div style={{ fontSize: 11, color: "#8A94A6" }}>Top Flag</div></div>
          </div>
        </div>
        <div className="flex-1 overflow-y-auto px-6 py-4">
          <div style={{ fontWeight: 600, fontSize: 14, color: "#1A1D23", marginBottom: 12 }}>Event History</div>
          {empEvents.length === 0 ? (
            <p style={{ color: "#9CA3AF", fontSize: 13 }}>No events found for this employee in this view window.</p>
          ) : (
            <div className="flex flex-col gap-3">
              {empEvents.map(ev => (
                <div key={ev.id} style={{ border: "1px solid #F0F2F5", borderRadius: 12, padding: "12px 14px" }}>
                  <div className="flex items-center justify-between mb-2">
                    <SensitivityBadge flag={ev.sensitivity_flag} />
                    <span style={{ fontSize: 11, color: "#9CA3AF" }}>{fmtTs(ev.timestamp)}</span>
                  </div>
                  <div style={{ fontSize: 13, color: "#374151", fontWeight: 600 }}>{ev.tool_name}</div>
                  {ev.window_title && <div style={{ fontSize: 12, color: "#8A94A6", marginTop: 2 }}>🪟 {ev.window_title}</div>}
                  {ev.paste_size_chars && <div style={{ fontSize: 12, color: "#8A94A6" }}>📋 {ev.paste_size_chars.toLocaleString()} chars</div>}
                  {ev.file_name && <div style={{ fontSize: 12, color: "#8A94A6" }}>📄 {ev.file_name}</div>}
                  <div style={{ fontSize: 12, color: "#8A94A6", marginTop: 4 }}>Risk Score: <strong style={{ color: ev.sensitivity_score >= 70 ? "#EF4444" : "#F59E0B" }}>{ev.sensitivity_score}</strong></div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// ─── Main Tab ────────────────────────────────────────────────────────────────
export function DataRiskTab() {
  const [events, setEvents] = useState<SensitivityEvent[]>([]);
  const [riskScores, setRiskScores] = useState<EmployeeRiskScore[]>([]);
  const [stats, setStats] = useState<DataRiskStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [rebuilding, setRebuilding] = useState(false);
  const [selectedFlag, setSelectedFlag] = useState<SensitivityFlag | "all">("all");
  const [selectedEmployee, setSelectedEmployee] = useState<EmployeeRiskScore | null>(null);
  const unsubRef = useRef<(() => void) | null>(null);

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const [ev, rs, st] = await Promise.all([
        fetchSensitivityEvents(),
        fetchEmployeeRiskScores(),
        fetchDataRiskStats(),
      ]);
      setEvents(ev);
      setRiskScores(rs);
      setStats(st);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    load();
    // Real-time listener for high-risk events
    const user = auth.currentUser;
    if (user) {
      // Get orgId from profile first, then subscribe
      import("@/services/api").then(({ fetchMe }) => {
        fetchMe().then(profile => {
          unsubRef.current = subscribeToHighRiskEvents(profile.org_id, (newEvents) => {
            if (newEvents.length > 0) {
              const latest = newEvents[0];
              toast.warning(`🔴 High-risk event detected: ${latest.tool_name} — ${FLAG_META[latest.sensitivity_flag]?.label ?? latest.sensitivity_flag}`, {
                duration: 6000,
              });
            }
          });
        }).catch(() => {});
      });
    }
    return () => { unsubRef.current?.(); };
  }, [load]);

  const handleRebuild = async () => {
    setRebuilding(true);
    try {
      await rebuildEmployeeRiskScores();
      const rs = await fetchEmployeeRiskScores();
      setRiskScores(rs);
      toast.success("Employee risk scores rebuilt!");
    } catch (e: any) {
      toast.error("Rebuild failed: " + e.message);
    } finally {
      setRebuilding(false);
    }
  };

  const handleMarkReviewed = async (ev: SensitivityEvent) => {
    try {
      await markSensitivityEventReviewed(ev.id);
      setEvents(prev => prev.map(e => e.id === ev.id ? { ...e, reviewed: true } : e));
      toast.success("Event marked as reviewed");
    } catch (e: any) {
      toast.error("Failed: " + e.message);
    }
  };

  const filteredEvents = selectedFlag === "all"
    ? events
    : events.filter(e => e.sensitivity_flag === selectedFlag);

  const flags: (SensitivityFlag | "all")[] = ["all", "SOURCE_CODE", "FILE_UPLOAD", "LARGE_PASTE", "FINANCIAL_KEYWORDS", "CREDENTIALS_PATTERN"];

  return (
    <div className="flex flex-col gap-5">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 style={{ fontWeight: 700, fontSize: 22, color: "#1A1D23", marginBottom: 2 }}>Data Risk</h2>
          <p style={{ color: "#8A94A6", fontSize: 13 }}>Detect potential sensitive data exposure across all AI tools. Real-time signal monitoring.</p>
        </div>
        <button onClick={handleRebuild} disabled={rebuilding}
          style={{ display: "flex", alignItems: "center", gap: 6, padding: "9px 16px", borderRadius: 12, border: "1px solid #E5E7EB", background: "#fff", color: "#6B7280", fontWeight: 600, fontSize: 13, cursor: rebuilding ? "not-allowed" : "pointer" }}>
          <RefreshCw size={14} strokeWidth={1.5} className={rebuilding ? "animate-spin" : ""} />
          {rebuilding ? "Rebuilding…" : "Rebuild Risk Scores"}
        </button>
      </div>

      {/* Stats */}
      <div className="flex gap-4">
        <StatCard label="High Risk Events Today" value={stats?.highRiskToday ?? "—"} icon={ShieldAlert} color="#EF4444" />
        <StatCard label="Employees at Risk" value={stats?.employeesWithRisk ?? "—"} icon={User} color="#8B5CF6" />
        <StatCard label="Most Common Flag" value={stats?.mostCommonType || "—"} icon={AlertTriangle} color="#F59E0B" />
        <StatCard label="Org Risk Score" value={stats ? `${stats.orgRiskScore}%` : "—"} icon={Activity} color="#FF5C1A" />
      </div>

      {/* Events Feed */}
      <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16, overflow: "hidden" }}>
        <div className="px-5 py-4" style={{ borderBottom: "1px solid #F0F2F5" }}>
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <AlertTriangle size={16} strokeWidth={1.5} style={{ color: "#EF4444" }} />
              <span style={{ fontWeight: 700, fontSize: 15, color: "#1A1D23" }}>Risk Events Feed</span>
              {events.length > 0 && (
                <span style={{ background: "#FEE2E2", color: "#991B1B", fontWeight: 700, fontSize: 11, borderRadius: 20, padding: "2px 8px" }}>
                  {events.filter(e => !e.reviewed).length} unreviewed
                </span>
              )}
            </div>
          </div>
          {/* Flag Filter */}
          <div className="flex gap-2 flex-wrap">
            {flags.map(f => {
              const isActive = selectedFlag === f;
              return (
                <button key={f} onClick={() => setSelectedFlag(f)}
                  style={{
                    padding: "4px 12px", borderRadius: 20, border: "1px solid #E5E7EB", fontSize: 12, fontWeight: 600, cursor: "pointer",
                    background: isActive ? "#FF5C1A" : "#fff", color: isActive ? "#fff" : "#6B7280",
                    borderColor: isActive ? "#FF5C1A" : "#E5E7EB"
                  }}>
                  {f === "all" ? "All" : (FLAG_META[f as SensitivityFlag]?.emoji + " " + FLAG_META[f as SensitivityFlag]?.label)}
                </button>
              );
            })}
          </div>
        </div>

        {loading ? (
          <div className="flex items-center justify-center py-16" style={{ color: "#8A94A6" }}>
            <RefreshCw size={20} strokeWidth={1.5} className="animate-spin mr-2" /> Loading risk events…
          </div>
        ) : filteredEvents.length === 0 ? (
          <div className="flex flex-col items-center py-16 gap-3">
            <ShieldAlert size={40} strokeWidth={1} style={{ color: "#D1D5DB" }} />
            <p style={{ color: "#9CA3AF", fontSize: 14 }}>No sensitivity events found.</p>
            <p style={{ color: "#C0C8D4", fontSize: 12 }}>Events appear here when the Desktop Agent detects data sensitivity signals.</p>
          </div>
        ) : (
          <div className="flex flex-col">
            {filteredEvents.map((ev, i) => (
              <div key={ev.id}
                style={{
                  padding: "14px 20px", borderBottom: i < filteredEvents.length - 1 ? "1px solid #F9FAFB" : "none",
                  opacity: ev.reviewed ? 0.5 : 1, transition: "opacity 200ms"
                }}
                className="flex items-start justify-between gap-4">
                <div className="flex items-start gap-3 min-w-0">
                  <div style={{ width: 36, height: 36, borderRadius: "50%", background: "#F0F2F5", display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
                    <User size={16} strokeWidth={1.5} style={{ color: "#8A94A6" }} />
                  </div>
                  <div className="min-w-0">
                    <div className="flex items-center gap-2 mb-1 flex-wrap">
                      <span style={{ fontWeight: 700, fontSize: 14, color: "#1A1D23" }}>{ev.user_id || "Unknown"}</span>
                      <SensitivityBadge flag={ev.sensitivity_flag} />
                      {ev.reviewed && <span style={{ background: "#D1FAE5", color: "#065F46", fontSize: 11, fontWeight: 600, borderRadius: 20, padding: "1px 8px" }}>✓ Reviewed</span>}
                    </div>
                    <div style={{ fontSize: 13, color: "#374151", marginBottom: 4 }}>
                      Used <strong>{ev.tool_name}</strong>
                      {ev.domain && <span style={{ color: "#9CA3AF" }}> ({ev.domain})</span>}
                    </div>
                    {ev.window_title && (
                      <div style={{ fontSize: 12, color: "#6B7280", marginBottom: 2 }}>🪟 <em>{ev.window_title}</em></div>
                    )}
                    {ev.paste_size_chars && (
                      <div style={{ fontSize: 12, color: "#6B7280", marginBottom: 2 }}>📋 {ev.paste_size_chars.toLocaleString()} chars pasted</div>
                    )}
                    {ev.file_name && (
                      <div style={{ fontSize: 12, color: "#6B7280", marginBottom: 2 }}>📄 {ev.file_name}</div>
                    )}
                    <div className="flex items-center gap-3 mt-2">
                      <div className="flex items-center gap-1" style={{ color: "#9CA3AF", fontSize: 11 }}>
                        <Clock size={11} strokeWidth={1.5} /> {fmtTs(ev.timestamp)}
                      </div>
                      {ev.device_id && (
                        <div className="flex items-center gap-1" style={{ color: "#9CA3AF", fontSize: 11 }}>
                          <Laptop size={11} strokeWidth={1.5} /> {ev.device_id.slice(0, 10)}…
                        </div>
                      )}
                    </div>
                  </div>
                </div>
                <div className="flex items-center gap-3 flex-shrink-0">
                  <div style={{ textAlign: "right" }}>
                    <div style={{ fontSize: 11, color: "#9CA3AF", marginBottom: 4 }}>Risk Score</div>
                    <span style={{
                      fontWeight: 800, fontSize: 18,
                      color: ev.sensitivity_score >= 70 ? "#EF4444" : ev.sensitivity_score >= 40 ? "#F59E0B" : "#10B981"
                    }}>{ev.sensitivity_score}</span>
                  </div>
                  {!ev.reviewed && (
                    <button onClick={() => handleMarkReviewed(ev)}
                      style={{ display: "flex", alignItems: "center", gap: 4, padding: "6px 12px", borderRadius: 10, border: "1px solid #E5E7EB", background: "#fff", color: "#6B7280", fontWeight: 600, fontSize: 12, cursor: "pointer" }}
                      onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.borderColor = "#10B981"; (e.currentTarget as HTMLButtonElement).style.color = "#065F46"; }}
                      onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.borderColor = "#E5E7EB"; (e.currentTarget as HTMLButtonElement).style.color = "#6B7280"; }}>
                      <CheckCheck size={12} strokeWidth={2} /> Mark Reviewed
                    </button>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Employee Risk Leaderboard */}
      <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16, overflow: "hidden" }}>
        <div className="flex items-center justify-between px-5 py-4" style={{ borderBottom: "1px solid #F0F2F5" }}>
          <div className="flex items-center gap-2">
            <TrendingUp size={16} strokeWidth={1.5} style={{ color: "#8B5CF6" }} />
            <span style={{ fontWeight: 700, fontSize: 15, color: "#1A1D23" }}>Employee Risk Leaderboard</span>
          </div>
          <span style={{ fontSize: 12, color: "#8A94A6" }}>Click a row to see full history</span>
        </div>

        {riskScores.length === 0 ? (
          <div className="flex flex-col items-center py-12 gap-3">
            <User size={36} strokeWidth={1} style={{ color: "#D1D5DB" }} />
            <p style={{ color: "#9CA3AF", fontSize: 14 }}>No risk scores yet. Click <strong>Rebuild Risk Scores</strong> after events are collected.</p>
          </div>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#FAFAFA", borderBottom: "1px solid #F0F2F5" }}>
                {["Employee", "Risk Score", "High Risk Events", "Last Incident", "Top Flag"].map(h => (
                  <th key={h} style={{ padding: "10px 16px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#8A94A6", letterSpacing: "0.05em", textTransform: "uppercase" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {riskScores.map((emp, i) => (
                <tr key={emp.id}
                  onClick={() => setSelectedEmployee(emp)}
                  style={{ borderBottom: i < riskScores.length - 1 ? "1px solid #F0F2F5" : "none", cursor: "pointer", transition: "background 150ms" }}
                  onMouseEnter={e => (e.currentTarget.style.background = "#FAFAFA")}
                  onMouseLeave={e => (e.currentTarget.style.background = "transparent")}>
                  <td style={{ padding: "12px 16px" }}>
                    <div className="flex items-center gap-2">
                      <div style={{ width: 30, height: 30, borderRadius: "50%", background: "#FF5C1A22", display: "flex", alignItems: "center", justifyContent: "center" }}>
                        <User size={14} strokeWidth={1.5} style={{ color: "#FF5C1A" }} />
                      </div>
                      <span style={{ fontWeight: 600, fontSize: 13, color: "#1A1D23" }}>{emp.user_email}</span>
                    </div>
                  </td>
                  <td style={{ padding: "12px 16px" }}><RiskScorePill score={emp.risk_score} /></td>
                  <td style={{ padding: "12px 16px" }}>
                    <span style={{ fontWeight: 700, fontSize: 14, color: emp.high_risk_events > 0 ? "#EF4444" : "#9CA3AF" }}>
                      {emp.high_risk_events}
                    </span>
                  </td>
                  <td style={{ padding: "12px 16px", color: "#6B7280", fontSize: 12 }}>{fmtTs(emp.last_incident)}</td>
                  <td style={{ padding: "12px 16px" }}>
                    {emp.top_sensitivity_type ? (
                      <SensitivityBadge flag={emp.top_sensitivity_type as SensitivityFlag} />
                    ) : <span style={{ color: "#9CA3AF", fontSize: 12 }}>—</span>}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* Slide-over */}
      {selectedEmployee && (
        <EmployeeDrawer
          employee={selectedEmployee}
          events={events}
          onClose={() => setSelectedEmployee(null)}
        />
      )}
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\DevicesTab.tsx

```tsx
import { useState, useMemo } from "react";
import {
  Plus, Search, ChevronDown, Monitor,
  CheckCircle2, XCircle, MoreHorizontal,
  RefreshCw, Trash2, Eye, ChevronLeft, ChevronRight,
} from "lucide-react";
import {
  ResponsiveContainer, PieChart, Pie, Cell,
} from "recharts";
import { useToast } from "@/components/ui/use-toast";
import { useHeartbeats } from "@/hooks/useDashboard";
import type { HeartbeatEvent } from "@/data/mockData";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Types ─────────────────────────────────────────────────────────────────

type DeviceStatus = "healthy" | "outdated" | "offline";
type OS = "macos" | "windows";
type LastSeenStatus = "online" | "recent" | "offline";

interface Device {
  id: string;
  name: string;
  hostname: string;
  userInitials: string;
  userName: string;
  userDept: string;
  os: OS;
  osVersion: string;
  browserAgent: boolean;
  desktopAgent: boolean;
  lastSeen: string;
  lastSeenStatus: LastSeenStatus;
  version: string;
  status: DeviceStatus;
}

// ─── Helpers ────────────────────────────────────────────────────────────────

function formatRelativeTime(timestamp: string): string {
  const now = Date.now();
  const then = new Date(timestamp).getTime();
  const diffMs = now - then;
  if (diffMs < 0) return "Just now";
  const mins = Math.floor(diffMs / 60_000);
  if (mins < 1) return "Just now";
  if (mins < 60) return `${mins} min ago`;
  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return `${hrs} hr ago`;
  const days = Math.floor(hrs / 24);
  return `${days} day${days > 1 ? "s" : ""} ago`;
}

function computeLastSeenStatus(timestamp: string): LastSeenStatus {
  const diffMs = Date.now() - new Date(timestamp).getTime();
  if (diffMs < 10 * 60_000) return "online";
  if (diffMs < 60 * 60_000) return "recent";
  return "offline";
}

function deriveOS(osVersion: string): OS {
  if (osVersion.toLowerCase().includes("mac")) return "macos";
  return "windows";
}

function deriveDeviceName(osVersion: string, deviceId: string): string {
  const os = osVersion.toLowerCase();
  if (os.includes("macos") || os.includes("mac os")) return "macOS Device";
  if (os.includes("windows")) return "Windows Device";
  return deviceId.substring(0, 12);
}

function mapHeartbeatToDevice(hb: HeartbeatEvent, latestVersion: string): Device {
  const lastSeenStatus = computeLastSeenStatus(hb.timestamp);
  const os = deriveOS(hb.os_version);
  let status: DeviceStatus = "healthy";
  if (lastSeenStatus === "offline") status = "offline";
  else if (hb.agent_version !== latestVersion) status = "outdated";

  return {
    id: hb.device_id,
    name: deriveDeviceName(hb.os_version, hb.device_id),
    hostname: hb.device_id.length > 20 ? hb.device_id.substring(0, 20) + "…" : hb.device_id,
    userInitials: hb.device_id.substring(0, 2).toUpperCase(),
    userName: "Device " + hb.device_id.substring(0, 4),
    userDept: "Unknown",
    os,
    osVersion: hb.os_version,
    browserAgent: true,
    desktopAgent: true,
    lastSeen: formatRelativeTime(hb.timestamp),
    lastSeenStatus,
    version: hb.agent_version,
    status,
  };
}

function findLatestVersion(heartbeats: HeartbeatEvent[]): string {
  if (heartbeats.length === 0) return "";
  const versions = heartbeats.map(h => h.agent_version);
  // Sort versions semantically, pick the highest
  const sorted = [...new Set(versions)].sort((a, b) => {
    const pa = a.replace(/^v/, "").split(".").map(Number);
    const pb = b.replace(/^v/, "").split(".").map(Number);
    for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
      const diff = (pb[i] || 0) - (pa[i] || 0);
      if (diff !== 0) return diff;
    }
    return 0;
  });
  return sorted[0] || "";
}

function rowShadow(s: DeviceStatus): string {
  if (s === "offline")  return "inset 3px 0 0 #DC2626";
  if (s === "outdated") return "inset 3px 0 0 #D97706";
  return "none";
}

const dotColor: Record<LastSeenStatus, string> = {
  online:  "#16A34A",
  recent:  "#D97706",
  offline: "#DC2626",
};

// ─── OS icon SVGs ───────────────────────────────────────────────────────────

function AppleIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor">
      <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/>
    </svg>
  );
}

function WindowsIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor">
      <path d="M3 12V6.75l6-1.32v6.57H3zm17 0V3.43l-9 1.98V12h9zm-17 1h6v6.57l-6-1.32V13zm17 0h-9v6.58l9 1.99V13z"/>
    </svg>
  );
}

// ─── Shared card ────────────────────────────────────────────────────────────

function Card({ children, style }: { children: React.ReactNode; style?: React.CSSProperties }) {
  return (
    <div style={{
      backgroundColor: "#ffffff",
      border: "1px solid #F0F2F5",
      borderRadius: 16,
      padding: 24,
      boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      ...style,
    }}>
      {children}
    </div>
  );
}

// ─── MAIN COMPONENT ─────────────────────────────────────────────────────────

export function DevicesTab() {
  const [openMenu, setOpenMenu] = useState<string | null>(null);
  const [page, setPage] = useState(1);
  const [isFading, setIsFading] = useState(false);
  const [removedIds, setRemovedIds] = useState<Set<string>>(new Set());
  const [syncedIds, setSyncedIds] = useState<Set<string>>(new Set());
  const { toast } = useToast();

  const { data: heartbeats, isLoading, error } = useHeartbeats();

  const latestVersion = useMemo(
    () => findLatestVersion(heartbeats ?? []),
    [heartbeats]
  );

  const allDevices: Device[] = useMemo(() => {
    if (!heartbeats) return [];
    return heartbeats
      .filter(hb => !removedIds.has(hb.device_id))
      .map(hb => {
        const device = mapHeartbeatToDevice(hb, latestVersion);
        if (syncedIds.has(hb.device_id)) {
          return { ...device, lastSeen: "Just now", lastSeenStatus: "online" as LastSeenStatus, status: "healthy" as DeviceStatus };
        }
        return device;
      });
  }, [heartbeats, latestVersion, removedIds, syncedIds]);

  const ITEMS_PER_PAGE = 10;
  const totalItems = allDevices.length;
  const totalPages = Math.max(1, Math.ceil(totalItems / ITEMS_PER_PAGE));

  const handlePageChange = (p: number) => {
    if (p === page || p < 1 || p > totalPages) return;
    setIsFading(true);
    setTimeout(() => {
      setPage(p);
      setIsFading(false);
    }, 200);
  };

  const handleForceSync = (id: string, name: string) => {
    setSyncedIds(prev => new Set(prev).add(id));
    toast({
      title: "Sync Command Sent",
      description: `Requested state refresh from ${name}.`,
      duration: 3000,
    });
  };

  const handleRemoveAgent = (id: string, name: string) => {
    setRemovedIds(prev => new Set(prev).add(id));
    toast({
      title: "Agent Removed",
      description: `Successfully unlinked ${name} from governance.`,
      duration: 3000,
    });
  };

  const paginatedDevices = allDevices.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE);

  const getPages = () => {
    if (totalPages <= 5) return Array.from({ length: totalPages }, (_, i) => i + 1);
    if (page <= 3) return [1, 2, 3, 4, "...", totalPages];
    if (page >= totalPages - 2) return [1, "...", totalPages - 3, totalPages - 2, totalPages - 1, totalPages];
    return [1, "...", page - 1, page, page + 1, "...", totalPages];
  };

  // Computed stats
  const agentsActive = allDevices.filter(d => d.lastSeenStatus === "online" || d.lastSeenStatus === "recent").length;
  const needsAttention = allDevices.filter(d => d.status === "offline" || d.status === "outdated").length;

  // Coverage donut
  const activeCount = allDevices.filter(d => d.lastSeenStatus !== "offline").length;
  const inactiveCount = allDevices.length - activeCount;
  const coverageData = [
    { name: "Active",   value: activeCount || 0,   color: "#FF5C1A" },
    { name: "Inactive", value: inactiveCount || 0,  color: "#E2E8F0" },
  ];
  const coveragePct = totalItems > 0 ? ((activeCount / totalItems) * 100).toFixed(1) : "0";

  // OS breakdown
  const macCount = allDevices.filter(d => d.os === "macos").length;
  const winCount = allDevices.filter(d => d.os === "windows").length;

  // Version distribution
  const versionMap = useMemo(() => {
    const map = new Map<string, number>();
    allDevices.forEach(d => {
      map.set(d.version, (map.get(d.version) || 0) + 1);
    });
    // Sort: latest first, then by count descending
    const entries = [...map.entries()].sort((a, b) => {
      if (a[0] === latestVersion) return -1;
      if (b[0] === latestVersion) return 1;
      return b[1] - a[1];
    });
    return entries.map(([version, count]) => {
      const pct = totalItems > 0 ? Math.round((count / totalItems) * 100) : 0;
      let color = "#D97706"; // default non-latest
      if (version === latestVersion) color = "#16A34A";
      else {
        // older versions get red if very old
        const vParts = version.replace(/^v/, "").split(".").map(Number);
        const lParts = latestVersion.replace(/^v/, "").split(".").map(Number);
        const majorDiff = (lParts[0] || 0) - (vParts[0] || 0);
        const minorDiff = (lParts[1] || 0) - (vParts[1] || 0);
        if (majorDiff > 0 || minorDiff > 1) color = "#DC2626";
      }
      return {
        version: version === latestVersion ? `${version} (latest)` : version,
        count,
        pct,
        color,
      };
    });
  }, [allDevices, latestVersion, totalItems]);

  const cols = ["DEVICE", "USER", "OS", "AGENT STATUS", "LAST SEEN", "VERSION", "ACTIONS"];

  // ─── Loading skeleton ──────────────────────────────────────────────────
  if (isLoading) {
    return (
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Devices</h1>
            <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Monitor agent status across all managed devices</p>
          </div>
          <Skeleton className="h-9 w-32 rounded-xl" />
        </div>
        <div className="flex gap-4">
          {[1, 2, 3].map(i => (
            <div key={i} className="flex-1" style={{ borderRadius: 16, padding: 20, border: "1px solid #F0F2F5" }}>
              <Skeleton className="h-3 w-24 mb-3" />
              <Skeleton className="h-9 w-16 mb-2" />
              <Skeleton className="h-3 w-32" />
            </div>
          ))}
        </div>
        <Card style={{ padding: 0, overflow: "hidden" }}>
          <div className="px-6 py-4" style={{ borderBottom: "1px solid #F8FAFC" }}>
            <Skeleton className="h-5 w-28" />
          </div>
          <div className="px-6 py-3">
            {Array.from({ length: 8 }).map((_, i) => (
              <div key={i} className="flex items-center gap-4 py-3">
                <Skeleton className="h-8 w-8 rounded-xl" />
                <Skeleton className="h-4 w-32" />
                <Skeleton className="h-4 w-20" />
                <Skeleton className="h-4 w-24" />
                <Skeleton className="h-4 w-16" />
                <Skeleton className="h-4 w-16" />
                <Skeleton className="h-4 w-8" />
              </div>
            ))}
          </div>
        </Card>
      </div>
    );
  }

  // ─── Error state ───────────────────────────────────────────────────────
  if (error) {
    return (
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Devices</h1>
            <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Monitor agent status across all managed devices</p>
          </div>
        </div>
        <div style={{ backgroundColor: "#FEF2F2", border: "1px solid #FECACA", borderRadius: 16, padding: "16px 20px" }}>
          <p style={{ fontSize: 14, color: "#DC2626", fontWeight: 500 }}>
            Failed to load devices: {error.message}
          </p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 4 }}>
            Data will retry automatically. Check your connection if this persists.
          </p>
        </div>
      </div>
    );
  }

  // ─── Empty state ───────────────────────────────────────────────────────
  if (allDevices.length === 0) {
    return (
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Devices</h1>
            <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Monitor agent status across all managed devices</p>
          </div>
          <button
            className="flex items-center gap-2 font-semibold"
            style={{ backgroundColor: "#FF5C1A", color: "#ffffff", border: "none", borderRadius: 12, padding: "9px 18px", fontSize: 14, cursor: "pointer", fontFamily: "Inter, sans-serif", transition: "background-color 200ms ease" }}
            onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#E5521A"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#FF5C1A"; }}
          >
            <Plus size={15} strokeWidth={2.5} /> Deploy Agent
          </button>
        </div>
        <Card>
          <div className="flex flex-col items-center justify-center py-16">
            <Monitor size={40} strokeWidth={1.5} color="#CBD5E1" />
            <p className="mt-4 font-medium" style={{ fontSize: 16, color: "#94A3B8" }}>No devices registered yet</p>
            <p style={{ fontSize: 13, color: "#CBD5E1", marginTop: 4 }}>Deploy the agent to start monitoring devices</p>
          </div>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4">

      {/* ── Header ─────────────────────────────────────────────────── */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Devices</h1>
          <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>Monitor agent status across all managed devices</p>
        </div>
        <button
          className="flex items-center gap-2 font-semibold"
          style={{ backgroundColor: "#FF5C1A", color: "#ffffff", border: "none", borderRadius: 12, padding: "9px 18px", fontSize: 14, cursor: "pointer", fontFamily: "Inter, sans-serif", transition: "background-color 200ms ease" }}
          onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#E5521A"; }}
          onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#FF5C1A"; }}
        >
          <Plus size={15} strokeWidth={2.5} /> Deploy Agent
        </button>
      </div>

      {/* ── Stats Row ───────────────────────────────────────────────── */}
      <div className="flex gap-4">
        {/* Card 1 orange */}
        <div className="flex-1" style={{ backgroundColor: "#FF5C1A", border: "1px solid #FDDCC8", borderRadius: 16, padding: 20, boxShadow: "0 1px 3px rgba(0,0,0,0.06)", transition: "transform 200ms, box-shadow 200ms" }}
          onMouseEnter={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(-1px)"; el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)"; }}
          onMouseLeave={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(0)"; el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)"; }}
        >
          <p className="font-semibold tracking-widest uppercase" style={{ fontSize: 10, color: "rgba(255,255,255,0.75)", letterSpacing: "0.08em" }}>Total Devices</p>
          <p className="font-bold mt-2" style={{ fontSize: 36, color: "#ffffff", lineHeight: 1 }}>{totalItems}</p>
          <p style={{ fontSize: 12, color: "rgba(255,255,255,0.80)", marginTop: 6 }}>Managed endpoints</p>
        </div>

        {/* Card 2 white */}
        <div className="flex-1" style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 16, padding: 20, boxShadow: "0 1px 3px rgba(0,0,0,0.06)", transition: "transform 200ms, box-shadow 200ms" }}
          onMouseEnter={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(-1px)"; el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)"; }}
          onMouseLeave={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(0)"; el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)"; }}
        >
          <p className="font-semibold tracking-widest uppercase" style={{ fontSize: 10, color: "#94A3B8", letterSpacing: "0.08em" }}>Agents Active</p>
          <p className="font-bold mt-2" style={{ fontSize: 36, color: "#1A1A2E", lineHeight: 1 }}>{agentsActive}</p>
          <div className="flex items-center gap-1.5 mt-2">
            <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: "#16A34A", display: "inline-block", flexShrink: 0 }} />
            <span style={{ fontSize: 12, color: "#64748B" }}>Browser + Desktop running</span>
          </div>
        </div>

        {/* Card 3 white */}
        <div className="flex-1" style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 16, padding: 20, boxShadow: "0 1px 3px rgba(0,0,0,0.06)", transition: "transform 200ms, box-shadow 200ms" }}
          onMouseEnter={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(-1px)"; el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)"; }}
          onMouseLeave={e => { const el = e.currentTarget as HTMLDivElement; el.style.transform = "translateY(0)"; el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)"; }}
        >
          <p className="font-semibold tracking-widest uppercase" style={{ fontSize: 10, color: "#94A3B8", letterSpacing: "0.08em" }}>Needs Attention</p>
          <p className="font-bold mt-2" style={{ fontSize: 36, color: "#1A1A2E", lineHeight: 1 }}>{needsAttention}</p>
          <div className="flex items-center gap-1.5 mt-2">
            <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: "#DC2626", display: "inline-block", flexShrink: 0 }} />
            <span style={{ fontSize: 12, color: "#DC2626" }}>Offline or outdated</span>
          </div>
        </div>
      </div>

      {/* ── Device Table ────────────────────────────────────────────── */}
      <Card style={{ padding: 0, overflow: "hidden" }}>
        {/* Table header controls */}
        <div className="flex items-center justify-between px-6 py-4" style={{ borderBottom: "1px solid #F8FAFC" }}>
          <p className="font-semibold" style={{ fontSize: 16, color: "#1A1A2E" }}>All Devices</p>
          <div className="flex items-center gap-3">
            {/* Search */}
            <div className="relative flex items-center">
              <Search size={13} color="#94A3B8" className="absolute left-3 pointer-events-none" />
              <input
                type="text"
                placeholder="Search devices..."
                className="outline-none"
                style={{ paddingLeft: 30, paddingRight: 12, paddingTop: 7, paddingBottom: 7, backgroundColor: "#F8FAFC", border: "1px solid #E2E8F0", borderRadius: 12, fontSize: 13, color: "#1A1A2E", width: 180, fontFamily: "Inter, sans-serif" }}
              />
            </div>
            {/* Status filter */}
            <div className="relative flex items-center">
              <select className="appearance-none outline-none cursor-pointer pr-8 font-medium"
                style={{ backgroundColor: "#F8FAFC", border: "1px solid #E2E8F0", borderRadius: 12, padding: "7px 14px", fontSize: 13, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                <option>All Status</option>
                <option>Healthy</option>
                <option>Outdated</option>
                <option>Offline</option>
              </select>
              <ChevronDown size={13} color="#94A3B8" className="absolute right-3 pointer-events-none" />
            </div>
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full" style={{ borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ backgroundColor: "#F8FAFC" }}>
                {cols.map((col, i) => (
                  <th key={i} className="text-left font-semibold"
                    style={{ padding: i === 0 ? "10px 12px 10px 24px" : i === cols.length - 1 ? "10px 24px 10px 12px" : "10px 12px", fontSize: 11, color: "#94A3B8", letterSpacing: "0.07em", textTransform: "uppercase", whiteSpace: "nowrap" }}>
                    {col}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody style={{ opacity: isFading ? 0 : 1, transition: "opacity 200ms ease" }}>
              {paginatedDevices.map((d, idx) => {
                const isLast = idx === paginatedDevices.length - 1;
                return (
                  <tr key={d.id}
                    style={{ boxShadow: rowShadow(d.status), borderBottom: isLast ? "none" : "1px solid #F8FAFC", transition: "background-color 150ms" }}
                    onMouseEnter={e => { (e.currentTarget as HTMLElement).style.backgroundColor = "#FAFAFA"; }}
                    onMouseLeave={e => { (e.currentTarget as HTMLElement).style.backgroundColor = "transparent"; }}
                  >
                    {/* DEVICE */}
                    <td style={{ padding: "14px 12px 14px 24px", minWidth: 180 }}>
                      <div className="flex items-center gap-2.5">
                        <div className="flex items-center justify-center rounded-xl flex-shrink-0"
                          style={{ width: 34, height: 34, backgroundColor: "#F8FAFC", border: "1px solid #E2E8F0" }}>
                          <Monitor size={16} strokeWidth={1.8} color="#64748B" />
                        </div>
                        <div>
                          <p className="font-semibold" style={{ fontSize: 13, color: "#1A1A2E", lineHeight: 1.3 }}>{d.name}</p>
                          <p style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, color: "#94A3B8", lineHeight: 1.3 }}>{d.hostname}</p>
                        </div>
                      </div>
                    </td>

                    {/* USER */}
                    <td style={{ padding: "14px 12px", minWidth: 150 }}>
                      <div className="flex items-center gap-2">
                        <div className="flex items-center justify-center rounded-full font-bold flex-shrink-0"
                          style={{ width: 28, height: 28, backgroundColor: "#FF5C1A", color: "#ffffff", fontSize: 10 }}>
                          {d.userInitials}
                        </div>
                        <div>
                          <p className="font-medium" style={{ fontSize: 13, color: "#1A1A2E", lineHeight: 1.3 }}>{d.userName}</p>
                          <p style={{ fontSize: 11, color: "#94A3B8", lineHeight: 1.3 }}>{d.userDept}</p>
                        </div>
                      </div>
                    </td>

                    {/* OS */}
                    <td style={{ padding: "14px 12px", minWidth: 140 }}>
                      <div className="flex items-center gap-1.5">
                        <span style={{ color: d.os === "macos" ? "#1A1A2E" : "#0078D4", flexShrink: 0 }}>
                          {d.os === "macos" ? <AppleIcon size={14} /> : <WindowsIcon size={14} />}
                        </span>
                        <span style={{ fontSize: 13, color: "#1A1A2E" }}>{d.osVersion}</span>
                      </div>
                    </td>

                    {/* AGENT STATUS */}
                    <td style={{ padding: "14px 12px", minWidth: 155 }}>
                      <div className="flex flex-col gap-1.5">
                        <div className="flex items-center gap-1">
                          {d.browserAgent
                            ? <CheckCircle2 size={13} strokeWidth={2} color="#16A34A" />
                            : <XCircle      size={13} strokeWidth={2} color="#DC2626" />}
                          <span style={{ fontSize: 12, color: d.browserAgent ? "#16A34A" : "#DC2626" }}>
                            Browser {d.browserAgent ? "Active" : "Not installed"}
                          </span>
                        </div>
                        <div className="flex items-center gap-1">
                          {d.desktopAgent
                            ? <CheckCircle2 size={13} strokeWidth={2} color="#16A34A" />
                            : <XCircle      size={13} strokeWidth={2} color="#DC2626" />}
                          <span style={{ fontSize: 12, color: d.desktopAgent ? "#16A34A" : "#DC2626" }}>
                            Desktop {d.desktopAgent ? "Active" : "Not installed"}
                          </span>
                        </div>
                      </div>
                    </td>

                    {/* LAST SEEN */}
                    <td style={{ padding: "14px 12px", whiteSpace: "nowrap" }}>
                      <div className="flex items-center gap-1.5">
                        <span className="rounded-full flex-shrink-0" style={{ width: 7, height: 7, backgroundColor: dotColor[d.lastSeenStatus], display: "inline-block" }} />
                        <span style={{ fontSize: 13, color: "#64748B" }}>{d.lastSeen}</span>
                      </div>
                    </td>

                    {/* VERSION */}
                    <td style={{ padding: "14px 12px" }}>
                      <p style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: "#94A3B8" }}>{d.version}</p>
                      {d.status === "outdated" && (
                        <span style={{ fontSize: 11, backgroundColor: "rgba(217,119,6,0.08)", border: "1px solid rgba(217,119,6,0.2)", color: "#D97706", borderRadius: 9999, padding: "1px 7px", marginTop: 3, display: "inline-block" }}>
                          Update available
                        </span>
                      )}
                    </td>

                    {/* ACTIONS */}
                    <td style={{ padding: "14px 24px 14px 12px" }}>
                      <div className="relative">
                        <button
                          className="flex items-center justify-center rounded-lg transition-colors"
                          style={{ width: 30, height: 30, border: "1px solid #E2E8F0", backgroundColor: openMenu === d.id ? "#F8FAFC" : "transparent", cursor: "pointer" }}
                          onClick={() => setOpenMenu(openMenu === d.id ? null : d.id)}
                          onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                          onMouseLeave={e => { if (openMenu !== d.id) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                        >
                          <MoreHorizontal size={15} color="#64748B" />
                        </button>
                        {openMenu === d.id && (
                          <div className="absolute right-0 z-50"
                            style={{ top: 34, backgroundColor: "#ffffff", border: "1px solid #E2E8F0", borderRadius: 12, boxShadow: "0 8px 24px rgba(0,0,0,0.10)", minWidth: 155, overflow: "hidden" }}>
                            <button className="flex items-center gap-2.5 w-full font-medium"
                              style={{ padding: "9px 14px", fontSize: 13, color: "#1A1A2E", backgroundColor: "transparent", border: "none", cursor: "pointer", fontFamily: "Inter, sans-serif", textAlign: "left" }}
                              onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                              onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                              onClick={() => { setOpenMenu(null); toast({ title: "View Details", description: "Opening device profile..." }); }}
                            >
                              <Eye size={13} strokeWidth={2} /> View Details
                            </button>

                            <button className="flex items-center gap-2.5 w-full font-medium"
                              style={{ padding: "9px 14px", fontSize: 13, color: "#1A1A2E", backgroundColor: "transparent", border: "none", cursor: "pointer", fontFamily: "Inter, sans-serif", textAlign: "left" }}
                              onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                              onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                              onClick={() => { setOpenMenu(null); handleForceSync(d.id, d.name); }}
                            >
                              <RefreshCw size={13} strokeWidth={2} /> Force Sync
                            </button>

                            <button className="flex items-center gap-2.5 w-full font-medium"
                              style={{ padding: "9px 14px", fontSize: 13, color: "#DC2626", backgroundColor: "transparent", border: "none", cursor: "pointer", fontFamily: "Inter, sans-serif", textAlign: "left" }}
                              onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#FEF2F2"; }}
                              onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                              onClick={() => { setOpenMenu(null); handleRemoveAgent(d.id, d.name); }}
                            >
                              <Trash2 size={13} strokeWidth={2} /> Remove Agent
                            </button>
                          </div>
                        )}
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        
        {/* Table footer / pagination */}
        <div
          className="flex items-center justify-between px-5 py-3"
          style={{ borderTop: "1px solid #F8FAFC" }}
        >
          <span style={{ fontSize: 13, color: "#94A3B8" }}>
            Showing {totalItems > 0 ? (page - 1) * ITEMS_PER_PAGE + 1 : 0}-{Math.min(page * ITEMS_PER_PAGE, totalItems)} of {totalItems} devices
          </span>

          <div className="flex items-center gap-1">
            <button
              disabled={page === 1}
              className="flex items-center gap-1 font-medium transition-colors"
              style={{ fontSize: 13, color: page === 1 ? "#CBD5E1" : "#64748B", padding: "5px 10px", borderRadius: 8, border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: page === 1 ? "not-allowed" : "pointer" }}
              onMouseEnter={e => { if (page !== 1) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
              onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
              onClick={() => handlePageChange(page - 1)}
            >
              <ChevronLeft size={13} strokeWidth={2} /> Prev
            </button>

            {getPages().map((p, idx) => (
              p === "..." ? (
                <span key={`dots-${idx}`} style={{ fontSize: 13, color: "#CBD5E1", padding: "0 4px" }}>…</span>
              ) : (
                <button
                  key={p}
                  onClick={() => handlePageChange(p as number)}
                  style={{
                    width: 30, height: 30, borderRadius: 8, fontSize: 13, cursor: "pointer",
                    border: p === page ? "1px solid #1A1A2E" : "1px solid #E2E8F0",
                    backgroundColor: p === page ? "#1A1A2E" : "transparent",
                    color: p === page ? "#ffffff" : "#64748B",
                    fontWeight: p === page ? 600 : 400,
                    transition: "all 150ms ease",
                  }}
                  onMouseEnter={e => { if (p !== page) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                  onMouseLeave={e => { if (p !== page) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                >
                  {p}
                </button>
              )
            ))}

            <button
              disabled={page === totalPages}
              className="flex items-center gap-1 font-medium transition-colors"
              style={{ fontSize: 13, color: page === totalPages ? "#CBD5E1" : "#64748B", padding: "5px 10px", borderRadius: 8, border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: page === totalPages ? "not-allowed" : "pointer" }}
              onMouseEnter={e => { if (page !== totalPages) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
              onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
              onClick={() => handlePageChange(page + 1)}
            >
              Next <ChevronRight size={13} strokeWidth={2} />
            </button>
          </div>
        </div>
      </Card>

      {/* ── Bottom section ──────────────────────────────────────────── */}
      <div className="flex gap-4">

        {/* Left — Deployment Coverage donut */}
        <Card style={{ flex: "0 0 320px" }}>
          <p className="font-semibold mb-1" style={{ fontSize: 15, color: "#1A1A2E" }}>Deployment Coverage</p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginBottom: 16 }}>Active agents across all devices</p>
          <div className="flex flex-col items-center">
            <div className="relative inline-block">
              <ResponsiveContainer width={180} height={180}>
                <PieChart>
                  <Pie data={coverageData} cx="50%" cy="50%" innerRadius={55} outerRadius={80}
                    paddingAngle={3} dataKey="value" labelLine={false} strokeWidth={0}>
                    {coverageData.map((d, i) => <Cell key={i} fill={d.color} />)}
                  </Pie>
                </PieChart>
              </ResponsiveContainer>
              <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
                <span className="font-bold" style={{ fontSize: 22, color: "#1A1A2E", lineHeight: 1.1 }}>{coveragePct}%</span>
                <span style={{ fontSize: 11, color: "#94A3B8" }}>coverage</span>
              </div>
            </div>
            <div className="flex items-center gap-4 mt-2">
              <div className="flex items-center gap-1.5">
                <span className="rounded-full" style={{ width: 8, height: 8, backgroundColor: "#FF5C1A", display: "inline-block" }} />
                <span style={{ fontSize: 12, color: "#64748B" }}>macOS: {macCount}</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="rounded-full" style={{ width: 8, height: 8, backgroundColor: "#E2E8F0", display: "inline-block", border: "1px solid #CBD5E1" }} />
                <span style={{ fontSize: 12, color: "#64748B" }}>Windows: {winCount}</span>
              </div>
            </div>
          </div>
        </Card>

        {/* Right — Agent Version Distribution */}
        <Card style={{ flex: 1 }}>
          <div className="flex items-center justify-between mb-4">
            <div>
              <p className="font-semibold" style={{ fontSize: 15, color: "#1A1A2E" }}>Agent Version Distribution</p>
              <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>Across all {totalItems} managed devices</p>
            </div>
            <button style={{ background: "none", border: "none", cursor: "pointer", fontSize: 13, color: "#FF5C1A", fontWeight: 600, fontFamily: "Inter, sans-serif" }}>
              Update all outdated →
            </button>
          </div>
          <div className="flex flex-col gap-4">
            {versionMap.length > 0 ? versionMap.map(v => (
              <div key={v.version}>
                <div className="flex items-center justify-between mb-1.5">
                  <span style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 13, color: "#1A1A2E" }}>{v.version}</span>
                  <span style={{ fontSize: 13, color: "#94A3B8" }}>{v.count} devices</span>
                </div>
                <div className="w-full rounded-full" style={{ height: 8, backgroundColor: "#F8FAFC" }}>
                  <div className="rounded-full" style={{ height: 8, width: `${v.pct}%`, backgroundColor: v.color, transition: "width 600ms ease" }} />
                </div>
              </div>
            )) : (
              <p style={{ fontSize: 13, color: "#94A3B8" }}>No version data available</p>
            )}
          </div>
        </Card>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\DevicesTable.tsx

```tsx
import { formatDistanceToNow } from "date-fns";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { useHeartbeats, useAlerts } from "@/hooks/useDashboard";

export function DevicesTable() {
  const { data: heartbeats = [] } = useHeartbeats();
  const { data: alerts = [] } = useAlerts();

  const tamperDevices = new Set(
    alerts.filter(a => a.type === "tamper").map(a => {
      const parts = a.id.split("-");
      return parts.slice(1, -1).join("-");
    })
  );

  return (
    <div className="rounded-lg border border-border bg-card">
      <Table>
        <TableHeader>
          <TableRow className="hover:bg-transparent">
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Device ID</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">OS</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Agent</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Last Heartbeat</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Status</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Queue</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Tamper</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {heartbeats.map((hb) => {
            const minutesAgo = (Date.now() - new Date(hb.timestamp).getTime()) / 60000;
            const isOnline = minutesAgo < 6;
            const hasTamper = tamperDevices.has(hb.device_id);

            return (
              <TableRow key={hb.device_id}>
                <TableCell className="font-mono text-xs">{hb.device_id.slice(0, 8)}…</TableCell>
                <TableCell className="text-sm">{hb.os_version}</TableCell>
                <TableCell className="text-sm font-mono">v{hb.agent_version}</TableCell>
                <TableCell className="text-xs text-muted-foreground">
                  {formatDistanceToNow(new Date(hb.timestamp), { addSuffix: true })}
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-2">
                    <div className={`h-2 w-2 rounded-full ${isOnline ? "bg-emerald-500" : "bg-muted-foreground"}`} />
                    <span className="text-sm">{isOnline ? "Online" : "Offline"}</span>
                  </div>
                </TableCell>
                <TableCell>
                  <span className={`text-sm font-mono ${hb.queue_depth > 0 ? "text-warning" : "text-muted-foreground"}`}>
                    {hb.queue_depth}
                  </span>
                </TableCell>
                <TableCell>
                  {hasTamper ? (
                    <Badge variant="destructive" className="text-[11px]">Alert</Badge>
                  ) : (
                    <span className="text-xs text-muted-foreground">—</span>
                  )}
                </TableCell>
              </TableRow>
            );
          })}
          {heartbeats.length === 0 && (
            <TableRow>
              <TableCell colSpan={7} className="text-center text-xs text-muted-foreground py-8">
                No devices reporting yet. Start the agent to see data here.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\FirewallTab.tsx

```tsx
import { useState, useEffect, useCallback } from "react";
import { Shield, ShieldOff, Plus, RefreshCw, CheckCircle, XCircle, Trash2, Clock, Laptop, AlertTriangle, Lock } from "lucide-react";
import { toast } from "sonner";
import {
  fetchFirewallRules,
  updateFirewallRule,
  deleteFirewallRule,
  fetchBlockEvents,
  fetchFirewallStats,
  syncFirewallRulesFromEvents,
  type FirewallRule,
  type BlockEvent,
  type FirewallStats,
} from "@/services/api";

// ─── Helpers ───────────────────────────────────────────────────────────────
function fmtTs(ts: string | undefined) {
  if (!ts) return "—";
  const d = new Date(ts);
  return isNaN(d.getTime())
    ? ts
    : d.toLocaleString("en-IN", { dateStyle: "short", timeStyle: "short" });
}

function RiskBadge({ status }: { status: "allowed" | "blocked" }) {
  return status === "allowed" ? (
    <span style={{ background: "#D1FAE5", color: "#065F46", border: "1px solid #6EE7B7" }}
      className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold">
      <CheckCircle size={11} strokeWidth={2} /> ALLOWED
    </span>
  ) : (
    <span style={{ background: "#FEE2E2", color: "#991B1B", border: "1px solid #FCA5A5" }}
      className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold">
      <XCircle size={11} strokeWidth={2} /> BLOCKED
    </span>
  );
}

function StatCard({ label, value, icon: Icon, color }: { label: string; value: string | number; icon: React.ElementType; color: string }) {
  return (
    <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16 }} className="flex flex-col gap-2 p-4 flex-1 min-w-0">
      <div className="flex items-center gap-2">
        <div style={{ background: `${color}18`, borderRadius: 8, padding: 6 }}>
          <Icon size={16} strokeWidth={1.5} style={{ color }} />
        </div>
        <span style={{ color: "#8A94A6", fontSize: 12, fontWeight: 500 }}>{label}</span>
      </div>
      <span style={{ color: "#1A1D23", fontSize: 26, fontWeight: 700, lineHeight: 1 }}>{value}</span>
    </div>
  );
}

// ─── Add Tool Modal ─────────────────────────────────────────────────────────
function AddToolModal({ onClose, onSave }: { onClose: () => void; onSave: (rule: { tool_name: string; domain: string; status: "allowed" | "blocked" }) => void }) {
  const [toolName, setToolName] = useState("");
  const [domain, setDomain] = useState("");
  const [status, setStatus] = useState<"allowed" | "blocked">("blocked");

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ background: "rgba(0,0,0,0.35)" }}>
      <div style={{ background: "#fff", borderRadius: 20, border: "1px solid #F0F2F5", width: 420, padding: 28 }}>
        <h3 style={{ fontWeight: 700, fontSize: 18, color: "#1A1D23", marginBottom: 20 }}>Add Custom Domain Rule</h3>
        <div className="flex flex-col gap-3">
          <div className="flex flex-col gap-1">
            <label style={{ fontSize: 12, color: "#8A94A6", fontWeight: 500 }}>Tool Name</label>
            <input value={toolName} onChange={e => setToolName(e.target.value)} placeholder="e.g. ChatGPT"
              style={{ border: "1px solid #E5E7EB", borderRadius: 10, padding: "8px 12px", fontSize: 14, outline: "none" }} />
          </div>
          <div className="flex flex-col gap-1">
            <label style={{ fontSize: 12, color: "#8A94A6", fontWeight: 500 }}>Domain</label>
            <input value={domain} onChange={e => setDomain(e.target.value)} placeholder="e.g. chat.openai.com"
              style={{ border: "1px solid #E5E7EB", borderRadius: 10, padding: "8px 12px", fontSize: 14, outline: "none" }} />
          </div>
          <div className="flex flex-col gap-1">
            <label style={{ fontSize: 12, color: "#8A94A6", fontWeight: 500 }}>Policy</label>
            <div className="flex gap-2">
              <button onClick={() => setStatus("allowed")}
                style={{ flex: 1, padding: "8px 0", borderRadius: 10, border: `1px solid ${status === "allowed" ? "#10B981" : "#E5E7EB"}`,
                  background: status === "allowed" ? "#D1FAE5" : "#fff", color: status === "allowed" ? "#065F46" : "#6B7280", fontWeight: 600, fontSize: 14 }}>
                ✅ Allow
              </button>
              <button onClick={() => setStatus("blocked")}
                style={{ flex: 1, padding: "8px 0", borderRadius: 10, border: `1px solid ${status === "blocked" ? "#EF4444" : "#E5E7EB"}`,
                  background: status === "blocked" ? "#FEE2E2" : "#fff", color: status === "blocked" ? "#991B1B" : "#6B7280", fontWeight: 600, fontSize: 14 }}>
                🚫 Block
              </button>
            </div>
          </div>
        </div>
        <div className="flex gap-2 mt-6">
          <button onClick={onClose} style={{ flex: 1, padding: "10px 0", borderRadius: 12, border: "1px solid #E5E7EB", background: "#fff", color: "#6B7280", fontWeight: 600, fontSize: 14 }}>Cancel</button>
          <button onClick={() => { if (toolName && domain) { onSave({ tool_name: toolName, domain, status }); onClose(); } }}
            style={{ flex: 1, padding: "10px 0", borderRadius: 12, border: "none", background: "#FF5C1A", color: "#fff", fontWeight: 600, fontSize: 14, cursor: "pointer" }}>
            Save Rule
          </button>
        </div>
      </div>
    </div>
  );
}

// ─── Main Tab ───────────────────────────────────────────────────────────────
export function FirewallTab() {
  const [rules, setRules] = useState<FirewallRule[]>([]);
  const [blockEvents, setBlockEvents] = useState<BlockEvent[]>([]);
  const [stats, setStats] = useState<FirewallStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);
  const [saving, setSaving] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const [r, b, s] = await Promise.all([
        fetchFirewallRules(),
        fetchBlockEvents(),
        fetchFirewallStats(),
      ]);
      setRules(r);
      setBlockEvents(b);
      setStats(s);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { load(); }, [load]);

  const handleSync = async () => {
    setSyncing(true);
    try {
      await syncFirewallRulesFromEvents();
      await load();
      toast.success("Synced AI tools from detection events!");
    } catch (e: any) {
      toast.error("Sync failed: " + e.message);
    } finally {
      setSyncing(false);
    }
  };

  const handleToggle = async (rule: FirewallRule) => {
    const newStatus = rule.status === "allowed" ? "blocked" : "allowed";
    // Optimistic update
    setRules(prev => prev.map(r => r.id === rule.id ? { ...r, status: newStatus } : r));
    try {
      await updateFirewallRule({ tool_name: rule.tool_name, domain: rule.domain, status: newStatus });
      toast.success(`${rule.tool_name} set to ${newStatus.toUpperCase()}`);
    } catch (e: any) {
      // Revert on failure
      setRules(prev => prev.map(r => r.id === rule.id ? { ...r, status: rule.status } : r));
      toast.error("Failed to update rule: " + e.message);
    }
  };

  const handleDelete = async (rule: FirewallRule) => {
    setRules(prev => prev.filter(r => r.id !== rule.id));
    try {
      await deleteFirewallRule(rule.tool_name);
      toast.success(`Removed rule for ${rule.tool_name}`);
    } catch (e: any) {
      toast.error("Failed to delete: " + e.message);
      load();
    }
  };

  const handleAddRule = async (rule: { tool_name: string; domain: string; status: "allowed" | "blocked" }) => {
    setSaving(true);
    try {
      await updateFirewallRule(rule);
      await load();
      toast.success(`Rule added for ${rule.tool_name}`);
    } catch (e: any) {
      toast.error("Failed to save: " + e.message);
    } finally {
      setSaving(false);
    }
  };

  const blockedCount = rules.filter(r => r.status === "blocked").length;

  return (
    <div className="flex flex-col gap-5">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 style={{ fontWeight: 700, fontSize: 22, color: "#1A1D23", marginBottom: 2 }}>AI Firewall</h2>
          <p style={{ color: "#8A94A6", fontSize: 13 }}>Control which AI tools employees can access. Changes sync to all active agents.</p>
        </div>
        <div className="flex gap-2">
          <button onClick={handleSync} disabled={syncing}
            style={{ display: "flex", alignItems: "center", gap: 6, padding: "9px 16px", borderRadius: 12, border: "1px solid #E5E7EB", background: "#fff", color: "#6B7280", fontWeight: 600, fontSize: 13, cursor: syncing ? "not-allowed" : "pointer" }}>
            <RefreshCw size={14} strokeWidth={1.5} className={syncing ? "animate-spin" : ""} />
            {syncing ? "Syncing…" : "Sync from Events"}
          </button>
          <button onClick={() => setShowAddModal(true)}
            style={{ display: "flex", alignItems: "center", gap: 6, padding: "9px 16px", borderRadius: 12, border: "none", background: "#FF5C1A", color: "#fff", fontWeight: 600, fontSize: 13, cursor: "pointer" }}>
            <Plus size={14} strokeWidth={2} /> Add Rule
          </button>
        </div>
      </div>

      {/* Stats */}
      <div className="flex gap-4">
        <StatCard label="Tools Blocked Today" value={stats?.blockedToday ?? "—"} icon={ShieldOff} color="#EF4444" />
        <StatCard label="Block Events This Week" value={stats?.blockEventsThisWeek ?? "—"} icon={AlertTriangle} color="#F59E0B" />
        <StatCard label="Total Violations" value={stats?.policyViolations ?? "—"} icon={Lock} color="#8B5CF6" />
        <StatCard label="Compliance Score" value={stats ? `${stats.complianceScore}%` : "—"} icon={Shield} color="#10B981" />
      </div>

      {/* Policy Rules Table */}
      <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16, overflow: "hidden" }}>
        <div className="flex items-center justify-between px-5 py-4" style={{ borderBottom: "1px solid #F0F2F5" }}>
          <div className="flex items-center gap-2">
            <Shield size={16} strokeWidth={1.5} style={{ color: "#FF5C1A" }} />
            <span style={{ fontWeight: 700, fontSize: 15, color: "#1A1D23" }}>Policy Rules</span>
            {blockedCount > 0 && (
              <span style={{ background: "#FEE2E2", color: "#991B1B", fontWeight: 700, fontSize: 11, borderRadius: 20, padding: "2px 8px" }}>
                {blockedCount} BLOCKED
              </span>
            )}
          </div>
          <span style={{ fontSize: 12, color: "#8A94A6" }}>{rules.length} rules configured</span>
        </div>

        {loading ? (
          <div className="flex items-center justify-center py-16" style={{ color: "#8A94A6" }}>
            <RefreshCw size={20} strokeWidth={1.5} className="animate-spin mr-2" /> Loading firewall rules…
          </div>
        ) : rules.length === 0 ? (
          <div className="flex flex-col items-center py-16 gap-3">
            <Shield size={40} strokeWidth={1} style={{ color: "#D1D5DB" }} />
            <p style={{ color: "#9CA3AF", fontSize: 14 }}>No rules yet. Click <strong>Sync from Events</strong> to auto-populate from your detected tools.</p>
          </div>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#FAFAFA", borderBottom: "1px solid #F0F2F5" }}>
                {["Tool", "Domain", "Status", "Last Updated By", "Block Count", ""].map(h => (
                  <th key={h} style={{ padding: "10px 16px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#8A94A6", letterSpacing: "0.05em", textTransform: "uppercase" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rules.map((rule, i) => (
                <tr key={rule.id} style={{ borderBottom: i < rules.length - 1 ? "1px solid #F0F2F5" : "none" }}>
                  <td style={{ padding: "12px 16px", fontWeight: 600, color: "#1A1D23", fontSize: 14 }}>{rule.tool_name}</td>
                  <td style={{ padding: "12px 16px", color: "#6B7280", fontSize: 13, fontFamily: "monospace" }}>{rule.domain || "—"}</td>
                  <td style={{ padding: "12px 16px" }}><RiskBadge status={rule.status} /></td>
                  <td style={{ padding: "12px 16px", color: "#8A94A6", fontSize: 12 }}>{rule.updated_by || "—"}</td>
                  <td style={{ padding: "12px 16px" }}>
                    {rule.block_count > 0 ? (
                      <span style={{ background: "#FEE2E2", color: "#991B1B", fontWeight: 700, fontSize: 12, borderRadius: 20, padding: "2px 8px" }}>
                        {rule.block_count}
                      </span>
                    ) : <span style={{ color: "#9CA3AF", fontSize: 12 }}>0</span>}
                  </td>
                  <td style={{ padding: "12px 16px" }}>
                    <div className="flex items-center gap-2">
                      {/* Toggle */}
                      <button onClick={() => handleToggle(rule)}
                        style={{
                          width: 42, height: 22, borderRadius: 11, border: "none", cursor: "pointer",
                          background: rule.status === "allowed" ? "#10B981" : "#EF4444",
                          position: "relative", transition: "background 200ms"
                        }}>
                        <span style={{
                          position: "absolute", top: 3, left: rule.status === "allowed" ? 22 : 3,
                          width: 16, height: 16, background: "#fff", borderRadius: "50%", transition: "left 200ms"
                        }} />
                      </button>
                      <button onClick={() => handleDelete(rule)}
                        style={{ padding: "4px", borderRadius: 8, border: "none", background: "transparent", cursor: "pointer", color: "#9CA3AF" }}
                        onMouseEnter={e => (e.currentTarget.style.color = "#EF4444")}
                        onMouseLeave={e => (e.currentTarget.style.color = "#9CA3AF")}>
                        <Trash2 size={14} strokeWidth={1.5} />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* Block Events Table */}
      <div style={{ background: "#fff", border: "1px solid #F0F2F5", borderRadius: 16, overflow: "hidden" }}>
        <div className="flex items-center gap-2 px-5 py-4" style={{ borderBottom: "1px solid #F0F2F5" }}>
          <ShieldOff size={16} strokeWidth={1.5} style={{ color: "#EF4444" }} />
          <span style={{ fontWeight: 700, fontSize: 15, color: "#1A1D23" }}>Block Events</span>
          {blockEvents.length > 0 && (
            <span style={{ background: "#FEE2E2", color: "#991B1B", fontWeight: 700, fontSize: 11, borderRadius: 20, padding: "2px 8px" }}>
              {blockEvents.length}
            </span>
          )}
        </div>

        {blockEvents.length === 0 ? (
          <div className="flex flex-col items-center py-12 gap-3">
            <CheckCircle size={36} strokeWidth={1} style={{ color: "#D1FAE5" }} />
            <p style={{ color: "#9CA3AF", fontSize: 14 }}>No block events recorded yet.</p>
            <p style={{ color: "#C0C8D4", fontSize: 12 }}>Block events appear here when the Desktop Agent intercepts a connection.</p>
          </div>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#FAFAFA", borderBottom: "1px solid #F0F2F5" }}>
                {["Time", "Employee", "Tool", "Reason", "Device"].map(h => (
                  <th key={h} style={{ padding: "10px 16px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#8A94A6", letterSpacing: "0.05em", textTransform: "uppercase" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {blockEvents.map((ev, i) => (
                <tr key={ev.id} style={{ borderBottom: i < blockEvents.length - 1 ? "1px solid #F0F2F5" : "none" }}>
                  <td style={{ padding: "11px 16px", color: "#6B7280", fontSize: 12, whiteSpace: "nowrap" }}>
                    <div className="flex items-center gap-1"><Clock size={12} strokeWidth={1.5} /> {fmtTs(ev.timestamp)}</div>
                  </td>
                  <td style={{ padding: "11px 16px", fontWeight: 600, color: "#1A1D23", fontSize: 13 }}>{ev.user_id || "—"}</td>
                  <td style={{ padding: "11px 16px" }}>
                    <span style={{ background: "#FEE2E2", color: "#991B1B", fontWeight: 600, fontSize: 12, borderRadius: 8, padding: "3px 8px" }}>
                      🚫 {ev.tool_name}
                    </span>
                  </td>
                  <td style={{ padding: "11px 16px", color: "#8A94A6", fontSize: 12 }}>{ev.block_reason || ev.policy_matched || "Policy violation"}</td>
                  <td style={{ padding: "11px 16px" }}>
                    <div className="flex items-center gap-1" style={{ color: "#8A94A6", fontSize: 12 }}>
                      <Laptop size={12} strokeWidth={1.5} /> {ev.device_id ? ev.device_id.slice(0, 12) + "…" : "—"}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {showAddModal && (
        <AddToolModal onClose={() => setShowAddModal(false)} onSave={handleAddRule} />
      )}
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\KpiCards.tsx

```tsx
import { Activity, Layers, AlertTriangle, ShieldOff, ArrowUpRight } from "lucide-react";
import { useStats } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Error badge ──────────────────────────────────────────────────────────────

function ErrorBadge() {
  return (
    <span
      className="absolute top-2 left-2 flex items-center justify-center rounded-full font-bold"
      style={{
        width: 18,
        height: 18,
        backgroundColor: "#DC2626",
        color: "#ffffff",
        fontSize: 11,
        lineHeight: 1,
        zIndex: 2,
      }}
      title="Failed to load data"
    >
      !
    </span>
  );
}

// ─── Pulse placeholder for loading numbers ────────────────────────────────────

function NumberSkeleton({ white = false }: { white?: boolean }) {
  return (
    <Skeleton
      className="mt-2"
      style={{
        width: 72,
        height: 36,
        borderRadius: 8,
        backgroundColor: white ? "rgba(255,255,255,0.30)" : undefined,
      }}
    />
  );
}

// ─── Shared card shell ────────────────────────────────────────────────────────

interface CardShellProps {
  children: React.ReactNode;
  orange?: boolean;
  onClick?: () => void;
}

function CardShell({ children, orange = false, onClick }: CardShellProps) {
  return (
    <div
      onClick={onClick}
      className="flex-1 min-w-0 relative cursor-pointer select-none"
      style={{
        backgroundColor: orange ? "#FF5C1A" : "#ffffff",
        border: `1px solid ${orange ? "#FDDCC8" : "#F0F2F5"}`,
        borderRadius: 16,
        padding: 24,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        transition: "transform 200ms ease, box-shadow 200ms ease",
      }}
      onMouseEnter={(e) => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(-1px)";
        el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)";
      }}
      onMouseLeave={(e) => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(0)";
        el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)";
      }}
    >
      {children}
    </div>
  );
}

// ─── Card 1 — Total Detections (orange hero) ─────────────────────────────────

function TotalDetectionsCard({
  value,
  isLoading,
  error,
  onClick,
}: {
  value: number;
  isLoading: boolean;
  error: boolean;
  onClick?: () => void;
}) {
  return (
    <CardShell orange onClick={onClick}>
      {error && <ErrorBadge />}

      {/* Top-right icon */}
      <div
        className="absolute top-5 right-5 flex items-center justify-center rounded-full"
        style={{ width: 36, height: 36, backgroundColor: "rgba(255,255,255,0.25)" }}
      >
        <Activity size={16} strokeWidth={2} color="#ffffff" />
      </div>

      <p
        className="font-semibold tracking-widest uppercase"
        style={{ fontSize: 11, color: "rgba(255,255,255,0.80)", letterSpacing: "0.08em" }}
      >
        Total Detections
      </p>

      {isLoading ? (
        <NumberSkeleton white />
      ) : (
        <p
          className="font-bold mt-2 leading-none"
          style={{ fontSize: 40, color: "#ffffff", fontFamily: "Inter, sans-serif" }}
        >
          {value}
        </p>
      )}

      <div className="flex items-center gap-1 mt-3">
        <ArrowUpRight size={14} color="rgba(255,255,255,0.80)" strokeWidth={2.5} />
        <span style={{ fontSize: 13, color: "rgba(255,255,255,0.80)" }}>
          12% vs yesterday
        </span>
      </div>
    </CardShell>
  );
}

// ─── Card 2 — Unique Tools ────────────────────────────────────────────────────

function UniqueToolsCard({
  value,
  isLoading,
  error,
  onClick,
}: {
  value: number;
  isLoading: boolean;
  error: boolean;
  onClick?: () => void;
}) {
  return (
    <CardShell onClick={onClick}>
      {error && <ErrorBadge />}

      {/* Top-right icon */}
      <div
        className="absolute top-5 right-5 flex items-center justify-center rounded-full"
        style={{ width: 36, height: 36, backgroundColor: "#EFF6FF" }}
      >
        <Layers size={16} strokeWidth={2} color="#3B82F6" />
      </div>

      <p
        className="font-semibold tracking-widest uppercase"
        style={{ fontSize: 11, color: "#94A3B8", letterSpacing: "0.08em" }}
      >
        Unique Tools
      </p>

      {isLoading ? (
        <NumberSkeleton />
      ) : (
        <p
          className="font-bold mt-2 leading-none"
          style={{ fontSize: 36, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          {value}
        </p>
      )}

      <div className="flex items-center gap-1 mt-3">
        <ArrowUpRight size={14} color="#16A34A" strokeWidth={2.5} />
        <span style={{ fontSize: 13, color: "#16A34A" }}>
          3 new this week
        </span>
      </div>
    </CardShell>
  );
}

// ─── Card 3 — High Risk Events ────────────────────────────────────────────────

function HighRiskCard({
  value,
  isLoading,
  error,
  onClick,
}: {
  value: number;
  isLoading: boolean;
  error: boolean;
  onClick?: () => void;
}) {
  return (
    <CardShell onClick={onClick}>
      {error && <ErrorBadge />}

      {/* Top-right icon */}
      <div
        className="absolute top-5 right-5 flex items-center justify-center rounded-full"
        style={{ width: 36, height: 36, backgroundColor: "#FEF2F2" }}
      >
        <AlertTriangle size={16} strokeWidth={2} color="#DC2626" />
      </div>

      <p
        className="font-semibold tracking-widest uppercase"
        style={{ fontSize: 11, color: "#94A3B8", letterSpacing: "0.08em" }}
      >
        High Risk
      </p>

      {isLoading ? (
        <NumberSkeleton />
      ) : (
        <p
          className="font-bold mt-2 leading-none"
          style={{ fontSize: 36, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          {value}
        </p>
      )}

      <div className="flex items-center gap-1 mt-3">
        <ArrowUpRight size={14} color="#DC2626" strokeWidth={2.5} />
        <span style={{ fontSize: 13, color: "#DC2626" }}>
          Needs review
        </span>
      </div>
    </CardShell>
  );
}

// ─── Card 4 — Unapproved Tools ────────────────────────────────────────────────

function UnapprovedCard({
  value,
  isLoading,
  error,
  onClick,
}: {
  value: number;
  isLoading: boolean;
  error: boolean;
  onClick?: () => void;
}) {
  return (
    <CardShell onClick={onClick}>
      {error && <ErrorBadge />}

      {/* Top-right icon */}
      <div
        className="absolute top-5 right-5 flex items-center justify-center rounded-full"
        style={{ width: 36, height: 36, backgroundColor: "#FFFBEB" }}
      >
        <ShieldOff size={16} strokeWidth={2} color="#D97706" />
      </div>

      <p
        className="font-semibold tracking-widest uppercase"
        style={{ fontSize: 11, color: "#94A3B8", letterSpacing: "0.08em" }}
      >
        Unapproved
      </p>

      {isLoading ? (
        <NumberSkeleton />
      ) : (
        <p
          className="font-bold mt-2 leading-none"
          style={{ fontSize: 36, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          {value}
        </p>
      )}

      <div className="flex items-center gap-1 mt-3">
        {/* Amber dot instead of arrow */}
        <span
          className="rounded-full flex-shrink-0"
          style={{ width: 7, height: 7, backgroundColor: "#D97706" }}
        />
        <span style={{ fontSize: 13, color: "#D97706" }}>
          Not sanctioned
        </span>
      </div>
    </CardShell>
  );
}

// ─── Exported row ─────────────────────────────────────────────────────────────

interface KpiCardsProps {
  onNavigate?: (tab: string) => void;
}

export function KpiCards({ onNavigate }: KpiCardsProps) {
  const { data: stats, isLoading, error } = useStats();
  const hasError = !!error;

  return (
    <div className="flex gap-4 w-full">
      <TotalDetectionsCard
        value={stats?.totalDetections ?? 0}
        isLoading={isLoading}
        error={hasError}
        onClick={() => onNavigate?.("live-feed")}
      />
      <UniqueToolsCard
        value={stats?.uniqueTools ?? 0}
        isLoading={isLoading}
        error={hasError}
        onClick={() => onNavigate?.("subscriptions")}
      />
      <HighRiskCard
        value={stats?.highRiskCount ?? 0}
        isLoading={isLoading}
        error={hasError}
        onClick={() => onNavigate?.("alerts")}
      />
      <UnapprovedCard
        value={stats?.unapprovedCount ?? 0}
        isLoading={isLoading}
        error={hasError}
        onClick={() => onNavigate?.("alerts")}
      />
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\LiveFeedTab.tsx

```tsx
import { useState } from "react";
import { useToast } from "@/components/ui/use-toast";
import {
  ChevronDown,
  Download,
  CheckCircle2,
  XCircle,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { useEvents, useStats } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";
import type { DetectionEvent } from "@/data/mockData";

// ─── Types ─────────────────────────────────────────────────────────────────

type CategoryKey = "api" | "coding" | "video" | "search" | "image" | "productivity";
type RiskKey = "high" | "medium" | "low";

// ─── Helpers ───────────────────────────────────────────────────────────────

function formatRelativeTime(timestamp: string): string {
  const now = Date.now();
  const then = new Date(timestamp).getTime();
  const diffMs = now - then;
  if (diffMs < 0) return "just now";
  const diffMin = Math.floor(diffMs / 60_000);
  if (diffMin < 1) return "just now";
  if (diffMin < 60) return `${diffMin}min ago`;
  const diffHr = Math.floor(diffMin / 60);
  if (diffHr < 24) return `${diffHr}hr ago`;
  const d = new Date(timestamp);
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

// ─── Badge configs ──────────────────────────────────────────────────────────

const categoryConf: Record<CategoryKey, { label: string; bg: string; text: string; border: string }> = {
  api:          { label:"Api",          bg:"rgba(59,130,246,0.08)",  text:"#3B82F6", border:"rgba(59,130,246,0.2)"  },
  coding:       { label:"Coding",       bg:"rgba(6,182,212,0.08)",   text:"#0891B2", border:"rgba(6,182,212,0.2)"   },
  video:        { label:"Video",        bg:"rgba(139,92,246,0.08)",  text:"#7C3AED", border:"rgba(139,92,246,0.2)"  },
  search:       { label:"Search",       bg:"rgba(20,184,166,0.08)",  text:"#0D9488", border:"rgba(20,184,166,0.2)"  },
  image:        { label:"Image",        bg:"rgba(236,72,153,0.08)",  text:"#DB2777", border:"rgba(236,72,153,0.2)"  },
  productivity: { label:"Productivity", bg:"rgba(34,197,94,0.08)",   text:"#16A34A", border:"rgba(34,197,94,0.2)"   },
};

const defaultCategoryConf = { label: "Other", bg: "rgba(100,116,139,0.08)", text: "#64748B", border: "rgba(100,116,139,0.2)" };

const riskConf: Record<RiskKey, { label: string; bg: string; text: string; border: string }> = {
  high:   { label:"High",   bg:"rgba(220,38,38,0.08)",   text:"#DC2626", border:"rgba(220,38,38,0.2)"   },
  medium: { label:"Medium", bg:"rgba(217,119,6,0.08)",   text:"#D97706", border:"rgba(217,119,6,0.2)"   },
  low:    { label:"Low",    bg:"rgba(22,163,74,0.08)",   text:"#16A34A", border:"rgba(22,163,74,0.2)"   },
};

// ─── Mini components ────────────────────────────────────────────────────────

function Pill({ bg, text, border, label }: { bg: string; text: string; border: string; label: string }) {
  return (
    <span
      className="inline-flex items-center font-medium"
      style={{
        backgroundColor: bg,
        color: text,
        border: `1px solid ${border}`,
        borderRadius: 9999,
        padding: "3px 10px",
        fontSize: 12,
        fontFamily: "Inter, sans-serif",
        whiteSpace: "nowrap",
      }}
    >
      {label}
    </span>
  );
}

function KpiCard({
  label, value, sub,
  orange = false,
  isLoading = false,
}: {
  label: string;
  value: string;
  sub: React.ReactNode;
  orange?: boolean;
  isLoading?: boolean;
}) {
  return (
    <div
      className="flex-1 min-w-0 cursor-pointer"
      style={{
        backgroundColor: orange ? "#FF5C1A" : "#ffffff",
        border: `1px solid ${orange ? "#FDDCC8" : "#F0F2F5"}`,
        borderRadius: 16,
        padding: 20,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        transition: "transform 200ms ease, box-shadow 200ms ease",
      }}
      onMouseEnter={e => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(-1px)";
        el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)";
      }}
      onMouseLeave={e => {
        const el = e.currentTarget as HTMLDivElement;
        el.style.transform = "translateY(0)";
        el.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)";
      }}
    >
      <p
        className="font-semibold tracking-widest uppercase"
        style={{ fontSize: 10, color: orange ? "rgba(255,255,255,0.75)" : "#94A3B8", letterSpacing: "0.08em" }}
      >
        {label}
      </p>
      {isLoading ? (
        <Skeleton className="h-8 w-16 mt-2" style={{ backgroundColor: orange ? "rgba(255,255,255,0.2)" : undefined }} />
      ) : (
        <p
          className="font-bold mt-2 leading-none"
          style={{ fontSize: 32, color: orange ? "#ffffff" : "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          {value}
        </p>
      )}
      <div className="flex items-center gap-1.5 mt-2">{sub}</div>
    </div>
  );
}

function SelectDropdown({ 
  label, 
  value, 
  onChange, 
  options 
}: { 
  label: string; 
  value: string; 
  onChange: (v: string) => void; 
  options: { label: string; value: string }[] 
}) {
  return (
    <div className="relative flex items-center">
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="appearance-none outline-none cursor-pointer pr-8 font-medium"
        style={{
          backgroundColor: value ? "#FFF3EE" : "#F8FAFC",
          border: value ? "1px solid #FDDCC8" : "1px solid #E2E8F0",
          borderRadius: 12,
          padding: "8px 14px",
          fontSize: 14,
          color: value ? "#FF5C1A" : "#1A1A2E",
          fontFamily: "Inter, sans-serif",
          transition: "all 150ms ease"
        }}
      >
        <option value="">{label}</option>
        {options.map(opt => (
          <option key={opt.value} value={opt.value}>{opt.label}</option>
        ))}
      </select>
      <ChevronDown
        size={14}
        color={value ? "#FF5C1A" : "#94A3B8"}
        className="absolute right-3 pointer-events-none transition-colors"
      />
    </div>
  );
}

// ─── Skeleton rows for loading state ────────────────────────────────────────

function TableRowSkeleton() {
  return (
    <tr style={{ borderBottom: "1px solid #F8FAFC" }}>
      <td style={{ padding: "0 0 0 20px", width: 36 }}>
        <Skeleton className="h-4 w-4 rounded" />
      </td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-4 w-16" /></td>
      <td style={{ padding: "18px 12px" }}>
        <Skeleton className="h-4 w-24 mb-1" />
        <Skeleton className="h-3 w-16" />
      </td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-5 w-16 rounded-full" /></td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-5 w-14 rounded-full" /></td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-4 w-20" /></td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-4 w-28" /></td>
      <td style={{ padding: "18px 12px" }}><Skeleton className="h-4 w-20" /></td>
      <td style={{ padding: "18px 20px 18px 12px" }}><Skeleton className="h-4 w-4 rounded-full" /></td>
    </tr>
  );
}

// ─── Main exported component ────────────────────────────────────────────────

export function LiveFeedTab() {
  const { toast } = useToast();
  const [page, setPage] = useState(1);
  const [isFading, setIsFading] = useState(false);
  const [checked, setChecked] = useState<Set<string>>(new Set());

  // Filters State
  const [categoryFilter, setCategoryFilter] = useState("");
  const [riskFilter, setRiskFilter] = useState("");
  const [sourceFilter, setSourceFilter] = useState("");

  // API hooks — pass category and risk filters to the API
  const {
    data: eventsData,
    isLoading: eventsLoading,
    error: eventsError,
  } = useEvents(
    categoryFilter || undefined,
    riskFilter || undefined,
  );

  const {
    data: statsData,
    isLoading: statsLoading,
    error: statsError,
  } = useStats();

  // Map API events to display rows
  const apiEvents: DetectionEvent[] = eventsData?.events ?? [];

  // Client-side filter for vendor (sourceFilter)
  const filteredEvents = apiEvents.filter(ev => {
    if (sourceFilter && ev.vendor !== sourceFilter) return false;
    return true;
  });

  const ITEMS_PER_PAGE = 10;
  const totalItems = filteredEvents.length;
  const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE) || 1;

  const handlePageChange = (p: number) => {
    if (p === page || p < 1 || p > totalPages) return;
    setIsFading(true);
    setTimeout(() => {
      setPage(p);
      setIsFading(false);
    }, 200);
  };

  // Reset page when filters change
  const handleFilterChange = (setter: React.Dispatch<React.SetStateAction<string>>) => (val: string) => {
    setter(val);
    setPage(1);
    setChecked(new Set());
  };

  const paginatedEvents = filteredEvents.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE);

  const getPages = () => {
    if (totalPages <= 5) return Array.from({ length: totalPages }, (_, i) => i + 1);
    if (page <= 3) return [1, 2, 3, 4, "...", totalPages];
    if (page >= totalPages - 2) return [1, "...", totalPages - 3, totalPages - 2, totalPages - 1, totalPages];
    return [1, "...", page - 1, page, page + 1, "...", totalPages];
  };

  const toggle = (id: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();
    setChecked(prev => {
      const n = new Set(prev);
      n.has(id) ? n.delete(id) : n.add(id);
      return n;
    });
  };

  const isAllChecked = paginatedEvents.length > 0 && paginatedEvents.every(ev => checked.has(ev.event_id));
  const toggleAll = () => {
    if (isAllChecked) {
      setChecked(new Set());
    } else {
      const newChecked = new Set(checked);
      paginatedEvents.forEach(ev => newChecked.add(ev.event_id));
      setChecked(newChecked);
    }
  };

  const handleExport = () => {
    toast({
      title: "Export Started",
      description: `Downloading ${totalItems} event records as CSV.`,
      duration: 3000,
    });
  };

  const handleBulkAction = (action: string) => {
    toast({
      title: "Bulk Action Applied",
      description: `Successfully applied '${action}' to ${checked.size} events.`,
      duration: 3000,
    });
    setChecked(new Set());
  };

  const cols = ["", "TIME", "TOOL", "CATEGORY", "RISK", "PROCESS", "DOMAIN", "DEPARTMENT", "APPROVED"];

  // KPI values from stats API
  const kpiEventsToday = statsData?.totalDetections ?? 0;
  const kpiUniqueTools = statsData?.uniqueTools ?? 0;
  const kpiHighRisk = statsData?.highRiskCount ?? 0;
  const kpiUnapproved = statsData?.unapprovedCount ?? 0;

  return (
    <div className="flex flex-col gap-4">

      {/* ── Section 1: Header ────────────────────────────────────────── */}
      <div className="flex items-center justify-between">
        <div>
          <h1
            className="font-bold leading-tight"
            style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
          >
            Live Feed
          </h1>
          <p style={{ fontSize: 14, color: "#94A3B8", marginTop: 3 }}>
            Real-time AI tool detections across all devices
          </p>
        </div>

        <div className="flex items-center gap-2.5">
          <span
            className="relative flex h-2.5 w-2.5"
            aria-hidden
          >
            <span
              className="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
              style={{ backgroundColor: "#16A34A" }}
            />
            <span
              className="relative inline-flex rounded-full h-2.5 w-2.5"
              style={{ backgroundColor: "#16A34A" }}
            />
          </span>
          <span
            className="font-semibold"
            style={{ fontSize: 13, color: "#16A34A" }}
          >
            Live
          </span>
          <span style={{ fontSize: 12, color: "#94A3B8" }}>
            · Auto-refreshing every 10s
          </span>
        </div>
      </div>

      {/* ── Section 2: KPI strip ─────────────────────────────────────── */}
      {statsError && (
        <p style={{ fontSize: 13, color: "#DC2626", padding: "4px 0" }}>
          Failed to load stats. Retrying…
        </p>
      )}
      <div className="flex gap-4">
        <KpiCard
          label="Events Today"
          value={String(kpiEventsToday)}
          orange
          isLoading={statsLoading}
          sub={
            <span style={{ fontSize: 12, color: "rgba(255,255,255,0.80)" }}>
              Detected today
            </span>
          }
        />
        <KpiCard
          label="Unique Tools"
          value={String(kpiUniqueTools)}
          isLoading={statsLoading}
          sub={
            <>
              <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: "#3B82F6", display: "inline-block" }} />
              <span style={{ fontSize: 12, color: "#64748B" }}>Active right now</span>
            </>
          }
        />
        <KpiCard
          label="High Risk"
          value={String(kpiHighRisk)}
          isLoading={statsLoading}
          sub={
            <>
              <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: "#DC2626", display: "inline-block" }} />
              <span style={{ fontSize: 12, color: "#DC2626" }}>Needs review</span>
            </>
          }
        />
        <KpiCard
          label="Unapproved"
          value={String(kpiUnapproved)}
          isLoading={statsLoading}
          sub={
            <>
              <span className="rounded-full" style={{ width: 7, height: 7, backgroundColor: "#D97706", display: "inline-block" }} />
              <span style={{ fontSize: 12, color: "#D97706" }}>Not sanctioned</span>
            </>
          }
        />
      </div>

      {/* ── Section 3: Filter row & Bulk Actions ────────────────────────── */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <SelectDropdown 
            label="All Categories" 
            value={categoryFilter} 
            onChange={handleFilterChange(setCategoryFilter)}
            options={[
              { label: "API", value: "api" },
              { label: "Coding", value: "coding" },
              { label: "Video", value: "video" },
              { label: "Search", value: "search" },
              { label: "Image", value: "image" },
              { label: "Productivity", value: "productivity" },
            ]}
          />
          <SelectDropdown 
            label="All Risk Levels" 
            value={riskFilter}
            onChange={handleFilterChange(setRiskFilter)}
            options={[
              { label: "High Risk", value: "high" },
              { label: "Medium Risk", value: "medium" },
              { label: "Low Risk", value: "low" },
            ]}
          />
          <SelectDropdown 
            label="All Sources" 
            value={sourceFilter}
            onChange={handleFilterChange(setSourceFilter)}
            options={[
              { label: "OpenAI", value: "OpenAI" },
              { label: "Anthropic", value: "Anthropic" },
              { label: "Microsoft", value: "Microsoft" },
              { label: "Google", value: "Google" },
              { label: "Runway", value: "Runway" },
            ]}
          />
          {checked.size > 0 && (
            <div className="flex items-center gap-2 ml-4 animate-in fade-in slide-in-from-left-2 text-sm font-medium text-[#FF5C1A] bg-[#FFF3EE] px-3 py-1.5 rounded-xl border border-[#FDDCC8]">
              <span>{checked.size} selected</span>
              <div className="w-px h-4 bg-[#FFD1B8] mx-1" />
              <button 
                onClick={() => handleBulkAction("Mark Approved")}
                className="hover:underline transition-all"
              >
                Approve
              </button>
              <button 
                onClick={() => handleBulkAction("Escalate Risk")}
                className="hover:underline transition-all ml-1"
              >
                Escalate
              </button>
            </div>
          )}
        </div>

        <button
          onClick={handleExport}
          className="flex items-center gap-2 font-medium transition-colors"
          style={{
            padding: "8px 16px",
            backgroundColor: "#ffffff",
            border: "1px solid #E2E8F0",
            borderRadius: 12,
            fontSize: 14,
            color: "#1A1A2E",
            cursor: "pointer",
            fontFamily: "Inter, sans-serif",
          }}
          onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
          onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#ffffff"; }}
        >
          <Download size={15} strokeWidth={2} />
          Export CSV
        </button>
      </div>

      {/* ── Section 4: Main event table ───────────────────────────────── */}
      {eventsError && (
        <p style={{ fontSize: 13, color: "#DC2626", padding: "4px 0" }}>
          Failed to load events. Retrying…
        </p>
      )}
      <div
        style={{
          backgroundColor: "#ffffff",
          border: "1px solid #F0F2F5",
          borderRadius: 16,
          boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
          overflow: "hidden",
        }}
      >
        <div className="overflow-x-auto">
          <table className="w-full" style={{ borderCollapse: "collapse" }}>
            {/* Header */}
            <thead>
              <tr style={{ backgroundColor: "#F8FAFC" }}>
                {cols.map((col, i) => (
                  <th
                    key={i}
                    className="text-left font-semibold tracking-widest"
                    style={{
                      padding: i === 0 ? "12px 0 12px 20px" : i === cols.length - 1 ? "12px 20px 12px 12px" : "12px 12px",
                      fontSize: 11,
                      color: "#94A3B8",
                      letterSpacing: "0.07em",
                      whiteSpace: "nowrap",
                      textTransform: "uppercase",
                    }}
                  >
                    {i === 0 ? (
                      <div
                        onClick={toggleAll}
                        className="flex items-center justify-center rounded cursor-pointer"
                        style={{
                          width: 16, height: 16,
                          border: isAllChecked ? "none" : "1.5px solid #D1D5DB",
                          backgroundColor: isAllChecked ? "#FF5C1A" : "transparent",
                          borderRadius: 4,
                          flexShrink: 0,
                          transition: "all 150ms ease"
                        }}
                      >
                        {isAllChecked && (
                          <svg width="10" height="8" viewBox="0 0 10 8" fill="none">
                            <path d="M1 4L3.5 6.5L9 1" stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
                          </svg>
                        )}
                      </div>
                    ) : (
                      col
                    )}
                  </th>
                ))}
              </tr>
            </thead>

            {/* Rows */}
            <tbody style={{ opacity: isFading ? 0 : 1, transition: "opacity 200ms ease" }}>
              {eventsLoading ? (
                // Skeleton loading rows
                Array.from({ length: ITEMS_PER_PAGE }).map((_, i) => (
                  <TableRowSkeleton key={`skel-${i}`} />
                ))
              ) : paginatedEvents.length === 0 ? (
                // Empty state
                <tr>
                  <td colSpan={cols.length} style={{ padding: "48px 0", textAlign: "center" }}>
                    <p style={{ fontSize: 15, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>
                      No events detected yet
                    </p>
                  </td>
                </tr>
              ) : (
                paginatedEvents.map((ev, idx) => {
                  const isChecked = checked.has(ev.event_id);
                  const isLast = idx === paginatedEvents.length - 1;
                  const catKey = ev.category as CategoryKey;
                  const cat = categoryConf[catKey] ?? defaultCategoryConf;
                  const riskKey = ev.risk_level as RiskKey;
                  const risk = riskConf[riskKey] ?? riskConf.low;
                  return (
                    <tr
                      key={ev.event_id}
                      className="cursor-pointer transition-colors"
                      style={{
                        backgroundColor: isChecked ? "#FFF8F5" : "transparent",
                        borderBottom: isLast ? "none" : "1px solid #F8FAFC",
                        minHeight: 60,
                        transition: "background-color 150ms ease",
                      }}
                      onMouseEnter={e => { if (!isChecked) (e.currentTarget as HTMLElement).style.backgroundColor = "#FAFAFA"; }}
                      onMouseLeave={e => { (e.currentTarget as HTMLElement).style.backgroundColor = isChecked ? "#FFF8F5" : "transparent"; }}
                    >
                      {/* Checkbox */}
                      <td style={{ padding: "0 0 0 20px", width: 36 }}>
                        <div
                          onClick={() => toggle(ev.event_id)}
                          className="flex items-center justify-center rounded cursor-pointer"
                          style={{
                            width: 16, height: 16,
                            border: isChecked ? "none" : "1.5px solid #D1D5DB",
                            backgroundColor: isChecked ? "#FF5C1A" : "transparent",
                            borderRadius: 4,
                            flexShrink: 0,
                          }}
                        >
                          {isChecked && (
                            <svg width="10" height="8" viewBox="0 0 10 8" fill="none">
                              <path d="M1 4L3.5 6.5L9 1" stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
                            </svg>
                          )}
                        </div>
                      </td>

                      {/* Time */}
                      <td style={{ padding: "18px 12px", whiteSpace: "nowrap" }}>
                        <span style={{ fontSize: 13, color: "#94A3B8" }}>{formatRelativeTime(ev.timestamp)}</span>
                      </td>

                      {/* Tool + vendor */}
                      <td style={{ padding: "18px 12px" }}>
                        <p className="font-semibold" style={{ fontSize: 14, color: "#1A1A2E", lineHeight: 1.3 }}>{ev.tool_name}</p>
                        <p style={{ fontSize: 12, color: "#94A3B8", lineHeight: 1.3 }}>{ev.vendor}</p>
                      </td>

                      {/* Category badge */}
                      <td style={{ padding: "18px 12px" }}>
                        <Pill bg={cat.bg} text={cat.text} border={cat.border} label={cat.label} />
                      </td>

                      {/* Risk badge */}
                      <td style={{ padding: "18px 12px" }}>
                        <Pill bg={risk.bg} text={risk.text} border={risk.border} label={risk.label} />
                      </td>

                      {/* Process — monospace orange */}
                      <td style={{ padding: "18px 12px", whiteSpace: "nowrap" }}>
                        <span style={{ fontFamily: "'JetBrains Mono', 'Fira Code', monospace", fontSize: 13, color: "#FF5C1A" }}>
                          {ev.process_name}
                        </span>
                      </td>

                      {/* Domain */}
                      <td style={{ padding: "18px 12px", whiteSpace: "nowrap" }}>
                        <span style={{ fontSize: 13, color: "#64748B" }}>{ev.domain}</span>
                      </td>

                      {/* Department */}
                      <td style={{ padding: "18px 12px" }}>
                        <span style={{ fontSize: 14, color: "#1A1A2E" }}>{ev.department || "General"}</span>
                      </td>

                      {/* Approved */}
                      <td style={{ padding: "18px 20px 18px 12px" }}>
                        {ev.is_approved
                          ? <CheckCircle2 size={18} strokeWidth={2} color="#16A34A" />
                          : <XCircle     size={18} strokeWidth={2} color="#DC2626" />
                        }
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* Table footer / pagination */}
        {!eventsLoading && totalItems > 0 && (
          <div
            className="flex items-center justify-between px-5 py-3"
            style={{ borderTop: "1px solid #F8FAFC" }}
          >
            <span style={{ fontSize: 13, color: "#94A3B8" }}>
              Showing {(page - 1) * ITEMS_PER_PAGE + 1}-{Math.min(page * ITEMS_PER_PAGE, totalItems)} of {totalItems} events
            </span>

            <div className="flex items-center gap-1">
              <button
                disabled={page === 1}
                className="flex items-center gap-1 font-medium transition-colors"
                style={{ fontSize: 13, color: page === 1 ? "#CBD5E1" : "#64748B", padding: "5px 10px", borderRadius: 8, border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: page === 1 ? "not-allowed" : "pointer" }}
                onMouseEnter={e => { if (page !== 1) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                onClick={() => handlePageChange(page - 1)}
              >
                <ChevronLeft size={13} strokeWidth={2} /> Prev
              </button>

              {getPages().map((p, idx) => (
                p === "..." ? (
                  <span key={`dots-${idx}`} style={{ fontSize: 13, color: "#CBD5E1", padding: "0 4px" }}>…</span>
                ) : (
                  <button
                    key={p}
                    onClick={() => handlePageChange(p as number)}
                    style={{
                      width: 30, height: 30, borderRadius: 8, fontSize: 13, cursor: "pointer",
                      border: p === page ? "1px solid #1A1A2E" : "1px solid #E2E8F0",
                      backgroundColor: p === page ? "#1A1A2E" : "transparent",
                      color: p === page ? "#ffffff" : "#64748B",
                      fontWeight: p === page ? 600 : 400,
                      transition: "all 150ms ease",
                    }}
                    onMouseEnter={e => { if (p !== page) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                    onMouseLeave={e => { if (p !== page) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                  >
                    {p}
                  </button>
                )
              ))}

              <button
                disabled={page === totalPages}
                className="flex items-center gap-1 font-medium transition-colors"
                style={{ fontSize: 13, color: page === totalPages ? "#CBD5E1" : "#64748B", padding: "5px 10px", borderRadius: 8, border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: page === totalPages ? "not-allowed" : "pointer" }}
                onMouseEnter={e => { if (page !== totalPages) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                onClick={() => handlePageChange(page + 1)}
              >
                Next <ChevronRight size={13} strokeWidth={2} />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\LiveFeedTable.tsx

```tsx
import { formatDistanceToNow } from "date-fns";
import { Check, X } from "lucide-react";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { RiskBadge } from "./RiskBadge";
import { CategoryBadge } from "./CategoryBadge";
import type { DetectionEvent } from "@/data/mockData";

interface LiveFeedTableProps {
  events: DetectionEvent[];
}

export function LiveFeedTable({ events }: LiveFeedTableProps) {
  return (
    <div className="rounded-lg border border-border bg-card">
      <Table>
        <TableHeader>
          <TableRow className="hover:bg-transparent">
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Time</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Tool</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Category</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Risk</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Process</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Domain</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">User</TableHead>
            <TableHead className="text-xs font-medium uppercase text-muted-foreground">Approved</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {events.map((event) => (
            <TableRow key={event.event_id} className="group">
              <TableCell className="text-xs text-muted-foreground whitespace-nowrap">
                {formatDistanceToNow(new Date(event.timestamp), { addSuffix: true })}
              </TableCell>
              <TableCell>
                <div className="flex flex-col">
                  <span className="text-sm font-medium">{event.tool_name}</span>
                  <span className="text-xs text-muted-foreground">{event.vendor}</span>
                </div>
              </TableCell>
              <TableCell><CategoryBadge category={event.category} /></TableCell>
              <TableCell><RiskBadge level={event.risk_level} /></TableCell>
              <TableCell className="text-sm font-mono text-muted-foreground">{event.process_name}</TableCell>
              <TableCell className="text-xs text-muted-foreground max-w-[140px] truncate">{event.domain}</TableCell>
              <TableCell className="text-sm">{event.department || "General"}</TableCell>
              <TableCell>
                {event.is_approved ? (
                  <div className="flex h-5 w-5 items-center justify-center rounded-full bg-emerald-500/15">
                    <Check className="h-3 w-3 text-emerald-500" />
                  </div>
                ) : (
                  <div className="flex h-5 w-5 items-center justify-center rounded-full bg-red-500/15">
                    <X className="h-3 w-3 text-red-500" />
                  </div>
                )}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\RecentDetectionsTable.tsx

```tsx
import { useState, useMemo } from "react";
import { Search, SlidersHorizontal, MoreHorizontal, ChevronLeft, ChevronRight, X, Activity, AlertTriangle, ExternalLink } from "lucide-react";
import { useEvents } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";
import type { DetectionEvent } from "@/data/mockData";

// ─── Internal row type ─────────────────────────────────────────────────────

type Status = "approved" | "high-risk" | "pending";

interface Detection {
  id: string;
  orderId: string;
  activityColor: string;
  activityLabel: string;
  process: string;
  department: string;
  status: Status;
  date: string;
  checked?: boolean;
}

// ─── Color mapping ─────────────────────────────────────────────────────────

const categoryColorMap: Record<string, string> = {
  "code-assistant": "#3B82F6",
  "llm-api": "#8B5CF6",
  "chatbot": "#FF5C1A",
  "image-gen": "#DC2626",
  "search": "#16A34A",
  "writing": "#D97706",
  "video": "#EC4899",
};

const riskColorMap: Record<string, string> = {
  high: "#DC2626",
  medium: "#D97706",
  low: "#16A34A",
};

function getActivityColor(event: DetectionEvent): string {
  return categoryColorMap[event.category] ?? riskColorMap[event.risk_level] ?? "#3B82F6";
}

function mapStatus(event: DetectionEvent): Status {
  if (event.risk_level === "high") return "high-risk";
  if (event.is_approved) return "approved";
  return "pending";
}

function mapDetection(event: DetectionEvent, index: number): Detection {
  return {
    id: event.event_id,
    orderId: `DEV-${event.event_id.slice(0, 8).toUpperCase()}`,
    activityColor: getActivityColor(event),
    activityLabel: event.tool_name,
    process: event.process_name,
    department: event.department || "General",
    status: mapStatus(event),
    date: new Date(event.timestamp as any).toLocaleString(),
  };
}

// ─── Status badge ──────────────────────────────────────────────────────────

const statusConfig: Record<Status, { dot: string; label: string; text: string }> = {
  "approved":  { dot: "#16A34A", label: "Approved",  text: "#16A34A" },
  "high-risk": { dot: "#DC2626", label: "High Risk", text: "#DC2626" },
  "pending":   { dot: "#D97706", label: "Pending",   text: "#D97706" },
};

function StatusBadge({ status }: { status: Status }) {
  const { dot, label, text } = statusConfig[status];
  return (
    <div className="flex items-center gap-1.5">
      <span className="rounded-full flex-shrink-0" style={{ width: 7, height: 7, backgroundColor: dot }} />
      <span style={{ fontSize: 13, color: text, fontFamily: "Inter, sans-serif" }}>{label}</span>
    </div>
  );
}

// ─── Checkbox ─────────────────────────────────────────────────────────────

function Checkbox({ checked, onChange }: { checked: boolean; onChange: (e: React.MouseEvent) => void }) {
  return (
    <div
      onClick={onChange}
      className="flex items-center justify-center rounded flex-shrink-0 cursor-pointer transition-colors"
      style={{
        width: 16,
        height: 16,
        border: checked ? "none" : "1.5px solid #D1D5DB",
        backgroundColor: checked ? "#FF5C1A" : "transparent",
        borderRadius: 4,
      }}
    >
      {checked && (
        <svg width="10" height="8" viewBox="0 0 10 8" fill="none">
          <path d="M1 4L3.5 6.5L9 1" stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      )}
    </div>
  );
}

// ─── Main component ────────────────────────────────────────────────────────

export function RecentDetectionsTable() {
  const { data: eventsData, isLoading, error } = useEvents();

  const allRows = useMemo(() => {
    if (!eventsData?.events?.length) return [];
    return eventsData.events.map((e, i) => mapDetection(e, i));
  }, [eventsData]);

  const [checkedIds, setCheckedIds] = useState<Set<string>>(new Set());
  const [currentPage, setCurrentPage] = useState(1);
  const [searchQuery, setSearchQuery] = useState("");
  const [isFilterOpen, setIsFilterOpen] = useState(false);
  const [selectedEvent, setSelectedEvent] = useState<Detection | null>(null);

  const toggle = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setCheckedIds(prev => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  };

  // Filter & Search Logic
  const filteredRows = useMemo(() => {
    if (!searchQuery) return allRows;
    const q = searchQuery.toLowerCase();
    return allRows.filter(r =>
      r.activityLabel.toLowerCase().includes(q) ||
      r.department.toLowerCase().includes(q) ||
      r.process.toLowerCase().includes(q)
    );
  }, [allRows, searchQuery]);

  const totalPages = Math.ceil(filteredRows.length / 5) || 1;
  const currentRows = filteredRows.slice((currentPage - 1) * 5, currentPage * 5);

  // Generate page buttons — show up to 3 pages around current
  const pageButtons = useMemo(() => {
    const pages: number[] = [];
    const maxButtons = 3;
    let start = Math.max(1, currentPage - 1);
    let end = Math.min(totalPages, start + maxButtons - 1);
    if (end - start < maxButtons - 1) start = Math.max(1, end - maxButtons + 1);
    for (let i = start; i <= end; i++) pages.push(i);
    return pages;
  }, [currentPage, totalPages]);

  const cols = ["", "ORDER ID", "ACTIVITY", "DEPARTMENT", "STATUS", "DATE", ""];

  return (
    <div
      className="flex-1 min-w-0 flex flex-col"
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        overflow: "hidden",
      }}
    >
      {/* ── Card header ─────────────────────────────────────────────── */}
      <div className="flex items-center justify-between px-5 pt-5 pb-4"
           style={{ borderBottom: "1px solid #F8FAFC" }}>
        <div>
          <p className="font-semibold" style={{ fontSize: 16, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
            Recent Detections
          </p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>
            Live AI tool usage across all devices
          </p>
        </div>

        <div className="flex items-center gap-2">
          {/* Search */}
          <div className="relative flex items-center">
            <Search size={14} strokeWidth={2} color="#94A3B8"
              style={{ position: "absolute", left: 10, pointerEvents: "none" }} />
              <input
              placeholder="Search events..."
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                setCurrentPage(1);
              }}
              className="outline-none text-sm transition-colors"
              style={{
                paddingLeft: 32,
                paddingRight: 12,
                paddingTop: 7,
                paddingBottom: 7,
                backgroundColor: "#F8FAFC",
                border: "1px solid #E2E8F0",
                borderRadius: 12,
                fontSize: 13,
                color: "#1A1A2E",
                width: 190,
                fontFamily: "Inter, sans-serif",
              }}
              onFocus={(e) => e.target.style.backgroundColor = "#FFFFFF"}
              onBlur={(e) => {
                if(!searchQuery) e.target.style.backgroundColor = "#F8FAFC";
              }}
            />
          </div>

          {/* Filter button */}
          <div className="relative">
            <button
              onClick={() => setIsFilterOpen(!isFilterOpen)}
              className="flex items-center gap-1.5 transition-colors relative"
              style={{
                padding: "7px 14px",
                backgroundColor: isFilterOpen ? "#F0F2F5" : "#F8FAFC",
                border: isFilterOpen ? "1px solid #CBD5E1" : "1px solid #E2E8F0",
                borderRadius: 10,
                fontSize: 13,
                color: isFilterOpen ? "#1A1A2E" : "#64748B",
                cursor: "pointer",
                fontFamily: "Inter, sans-serif",
                fontWeight: 500,
              }}
              onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F0F2F5"; }}
              onMouseLeave={e => { 
                if(!isFilterOpen) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; 
              }}
            >
              <SlidersHorizontal size={13} strokeWidth={2} />
              Filter
            </button>
            {isFilterOpen && (
              <>
                <div className="fixed inset-0 z-10" onClick={() => setIsFilterOpen(false)} />
                <div className="absolute top-10 right-0 w-48 bg-white border border-[#E2E8F0] shadow-lg rounded-xl flex flex-col p-2 z-20 animate-in fade-in slide-in-from-top-2">
                  <span className="text-xs font-semibold text-[#94A3B8] uppercase px-3 py-1 mb-1">Status</span>
                  <label className="flex items-center gap-2 px-3 py-1.5 hover:bg-[#F8FAFC] rounded-lg cursor-pointer text-sm">
                    <input type="checkbox" className="accent-[#FF5C1A]" /> High Risk
                  </label>
                  <label className="flex items-center gap-2 px-3 py-1.5 hover:bg-[#F8FAFC] rounded-lg cursor-pointer text-sm">
                    <input type="checkbox" className="accent-[#FF5C1A]" /> Approved
                  </label>
                  <label className="flex items-center gap-2 px-3 py-1.5 hover:bg-[#F8FAFC] rounded-lg cursor-pointer text-sm mb-1 border-b border-[#F0F2F5] pb-2">
                    <input type="checkbox" className="accent-[#FF5C1A]" /> Pending
                  </label>
                  <button className="text-[13px] text-[#FF5C1A] text-left px-3 py-1.5 hover:bg-[#FFF3EE] rounded-lg mt-1 font-medium transition-colors">
                    Clear filters
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      {/* ── Table ───────────────────────────────────────────────────── */}
      <div className="overflow-x-auto flex-1">
        <table className="w-full" style={{ borderCollapse: "collapse" }}>
          {/* Header */}
          <thead>
            <tr style={{ backgroundColor: "#F8FAFC" }}>
              {cols.map((col, i) => (
                <th
                  key={i}
                  className="text-left font-semibold tracking-widest"
                  style={{
                    padding: i === 0 ? "10px 0 10px 20px" : i === cols.length - 1 ? "10px 20px 10px 12px" : "10px 12px",
                    fontSize: 11,
                    color: "#94A3B8",
                    letterSpacing: "0.07em",
                    whiteSpace: "nowrap",
                    textTransform: "uppercase",
                  }}
                >
                  {col}
                </th>
              ))}
            </tr>
          </thead>

          {/* Rows */}
          <tbody className="animate-in fade-in duration-300" key={isLoading ? "loading" : currentPage}>
            {isLoading ? (
              // Skeleton loading rows
              Array.from({ length: 5 }).map((_, idx) => (
                <tr key={`skel-${idx}`} style={{ borderBottom: idx === 4 ? "none" : "1px solid #F8FAFC" }}>
                  <td style={{ padding: "14px 0 14px 20px", width: 36 }}>
                    <Skeleton className="w-4 h-4 rounded" />
                  </td>
                  <td style={{ padding: "14px 12px" }}>
                    <Skeleton className="w-20 h-4 rounded" />
                  </td>
                  <td style={{ padding: "14px 12px" }}>
                    <div className="flex items-center gap-2.5">
                      <Skeleton className="w-[30px] h-[30px] rounded-lg" />
                      <div className="flex flex-col gap-1">
                        <Skeleton className="w-24 h-4 rounded" />
                        <Skeleton className="w-16 h-3 rounded" />
                      </div>
                    </div>
                  </td>
                  <td style={{ padding: "14px 12px" }}>
                    <Skeleton className="w-20 h-4 rounded" />
                  </td>
                  <td style={{ padding: "14px 12px" }}>
                    <Skeleton className="w-16 h-4 rounded" />
                  </td>
                  <td style={{ padding: "14px 12px" }}>
                    <Skeleton className="w-32 h-4 rounded" />
                  </td>
                  <td style={{ padding: "14px 20px 14px 12px" }}>
                    <Skeleton className="w-7 h-7 rounded-lg" />
                  </td>
                </tr>
              ))
            ) : error ? (
              <tr>
                <td colSpan={cols.length} style={{ padding: "40px 20px", textAlign: "center" }}>
                  <p style={{ fontSize: 13, color: "#DC2626" }}>
                    Failed to load detection events
                  </p>
                </td>
              </tr>
            ) : currentRows.length === 0 ? (
              <tr>
                <td colSpan={cols.length} style={{ padding: "40px 20px", textAlign: "center" }}>
                  <p style={{ fontSize: 13, color: "#94A3B8" }}>
                    No detections found
                  </p>
                </td>
              </tr>
            ) : (
              currentRows.map((row, idx) => {
                const isChecked = checkedIds.has(row.id);
                const isLast = idx === currentRows.length - 1;
                return (
                  <tr
                    key={row.id}
                    onClick={() => setSelectedEvent(row)}
                    className="cursor-pointer transition-colors"
                    style={{
                      backgroundColor: isChecked ? "#FFF8F5" : "transparent",
                      borderBottom: isLast ? "none" : "1px solid #F8FAFC",
                      minHeight: 56,
                      transition: "background-color 150ms ease",
                    }}
                    onMouseEnter={e => {
                      if (!isChecked)
                        (e.currentTarget as HTMLTableRowElement).style.backgroundColor = "#FAFAFA";
                    }}
                    onMouseLeave={e => {
                      (e.currentTarget as HTMLTableRowElement).style.backgroundColor =
                        isChecked ? "#FFF8F5" : "transparent";
                    }}
                  >
                    {/* Checkbox */}
                    <td style={{ padding: "14px 0 14px 20px", width: 36 }}>
                      <Checkbox checked={isChecked} onChange={(e) => toggle(row.id, e as any)} />
                    </td>

                    {/* Order ID */}
                    <td style={{ padding: "14px 12px" }}>
                      <span style={{ fontSize: 13, color: "#94A3B8", fontFamily: "monospace" }}>
                        {row.orderId}
                      </span>
                    </td>

                    {/* Activity */}
                    <td style={{ padding: "14px 12px" }}>
                      <div className="flex items-center gap-2.5">
                        <div
                          className="rounded-lg flex-shrink-0"
                          style={{ width: 30, height: 30, backgroundColor: row.activityColor + "18" }}
                        >
                          <svg width="30" height="30" viewBox="0 0 30 30">
                            <circle cx="15" cy="15" r="5" fill={row.activityColor} />
                          </svg>
                        </div>
                        <div>
                          <p className="font-semibold" style={{ fontSize: 14, color: "#1A1A2E", lineHeight: 1.3 }}>
                            {row.activityLabel}
                          </p>
                          <p style={{ fontSize: 12, color: "#94A3B8", lineHeight: 1.3 }}>
                            {row.process}
                          </p>
                        </div>
                      </div>
                    </td>

                    {/* Department */}
                    <td style={{ padding: "14px 12px" }}>
                      <span style={{ fontSize: 14, color: "#1A1A2E" }}>{row.department}</span>
                    </td>

                    {/* Status */}
                    <td style={{ padding: "14px 12px" }}>
                      <StatusBadge status={row.status} />
                    </td>

                    {/* Date */}
                    <td style={{ padding: "14px 12px", whiteSpace: "nowrap" }}>
                      <span style={{ fontSize: 13, color: "#94A3B8" }}>{row.date}</span>
                    </td>

                    {/* Menu */}
                    <td style={{ padding: "14px 20px 14px 12px" }}>
                      <button
                        onClick={(e) => { e.stopPropagation(); /* Open Action Menu Context */ }}
                        className="flex items-center justify-center rounded-lg transition-colors"
                        style={{ color: "#C0C8D4", backgroundColor: "transparent", width: 28, height: 28 }}
                        onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.color = "#1A1A2E"; (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
                        onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.color = "#C0C8D4"; (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
                      >
                        <MoreHorizontal size={15} strokeWidth={2} />
                      </button>
                    </td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>

      {/* ── Footer ──────────────────────────────────────────────────── */}
      <div
        className="flex items-center justify-between px-5 py-3"
        style={{ borderTop: "1px solid #F8FAFC" }}
      >
        <span style={{ fontSize: 13, color: "#94A3B8" }}>
          Showing {currentRows.length > 0 ? (currentPage - 1) * 5 + 1 : 0} of {filteredRows.length} events
        </span>

        <div className="flex items-center gap-1">
          {/* Prev */}
          <button
            className="flex items-center gap-1 font-medium transition-colors"
            style={{ fontSize: 13, color: "#64748B", padding: "5px 10px", borderRadius: 8,
              border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: "pointer" }}
            onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
            onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
          >
            <ChevronLeft size={13} strokeWidth={2} /> Prev
          </button>

          {/* Pages */}
          {pageButtons.map(p => (
            <button
              key={p}
              onClick={() => setCurrentPage(p)}
              className="font-medium transition-colors"
              style={{
                width: 30, height: 30,
                borderRadius: 8,
                fontSize: 13,
                border: p === currentPage ? "1px solid #FF5C1A" : "1px solid #E2E8F0",
                backgroundColor: p === currentPage ? "#FFF3EE" : "transparent",
                color: p === currentPage ? "#FF5C1A" : "#64748B",
                cursor: "pointer",
              }}
            >
              {p}
            </button>
          ))}

          {/* Next */}
          <button
            className="flex items-center gap-1 font-medium transition-colors"
            style={{ fontSize: 13, color: currentPage >= totalPages ? "#CBD5E1" : "#64748B", padding: "5px 10px", borderRadius: 8,
              border: "1px solid #E2E8F0", backgroundColor: "transparent", cursor: currentPage >= totalPages ? "not-allowed" : "pointer" }}
            onMouseEnter={e => { if(currentPage < totalPages) (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#F8FAFC"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent"; }}
            onClick={() => setCurrentPage(Math.min(totalPages, currentPage + 1))}
            disabled={currentPage >= totalPages}
          >
            Next <ChevronRight size={13} strokeWidth={2} />
          </button>
        </div>
      </div>
      
      <EventDetailPanel event={selectedEvent} onClose={() => setSelectedEvent(null)} />
    </div>
  );
}

// ─── EVENT DETAIL PANEL ───────────────────────────────────────────────────

function EventDetailPanel({ event, onClose }: { event: Detection | null; onClose: () => void }) {
  if (!event) return null;

  return (
    <div className="fixed inset-0 z-50">
      <div 
        className="absolute inset-0 bg-black/20 backdrop-blur-sm animate-in fade-in duration-200" 
        onClick={onClose} 
      />
      <div 
        className="absolute right-0 top-0 bottom-0 w-[440px] bg-white border-l border-[#F0F2F5] shadow-[0_0_64px_rgba(0,0,0,0.1)] animate-in slide-in-from-right duration-300 flex flex-col"
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-[#F0F2F5]">
          <h2 className="text-lg font-bold text-[#1A1A2E] flex items-center gap-2">
            Event Context
            <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-[#F0F2F5] text-[#64748B]">
              {event.orderId}
            </span>
          </h2>
          <button onClick={onClose} className="p-2 text-[#94A3B8] hover:bg-[#F0F2F5] hover:text-[#1A1A2E] rounded-lg transition-colors">
            <X size={18} />
          </button>
        </div>

        {/* Banner */}
        <div className="p-6 bg-[#FAFAFA] border-b border-[#F0F2F5] flex flex-col items-center gap-4 text-center">
          <div 
            className="w-16 h-16 flex items-center justify-center rounded-2xl shadow-sm"
            style={{ backgroundColor: event.activityColor + "15" }}
          >
            <Activity size={32} color={event.activityColor} />
          </div>
          <div>
            <h3 className="text-xl font-bold text-[#1A1A2E] leading-tight mb-1">{event.activityLabel}</h3>
            <p className="text-[13px] text-[#64748B] flex justify-center items-center gap-2">
              <span className="font-mono bg-[#F0F2F5] px-1.5 py-0.5 rounded">{event.process}</span>
            </p>
          </div>
          <div className="mt-2 text-sm justify-center flex items-center">
             <StatusBadge status={event.status} />
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
          <section>
            <h4 className="text-[12px] font-bold text-[#94A3B8] tracking-widest uppercase mb-3">Event Details</h4>
            <div className="flex flex-col gap-0 border border-[#F0F2F5] rounded-xl overflow-hidden bg-white">
              <div className="flex justify-between items-center p-3 border-b border-[#F0F2F5]">
                <span className="text-[#64748B] text-[13px]">Time Detected</span>
                <span className="text-[#1A1A2E] text-[13px] font-medium">{event.date}</span>
              </div>
              <div className="flex justify-between items-center p-3 border-b border-[#F0F2F5]">
                <span className="text-[#64748B] text-[13px]">Duration</span>
                <span className="text-[#1A1A2E] text-[13px] font-medium">4m 12s active window</span>
              </div>
              <div className="flex justify-between items-center p-3">
                <span className="text-[#64748B] text-[13px]">Data Volume</span>
                <span className="text-[#1A1A2E] text-[13px] font-medium">1.4 MB Sent / 800 KB Received</span>
              </div>
            </div>
          </section>

          <section>
            <h4 className="text-[12px] font-bold text-[#94A3B8] tracking-widest uppercase mb-3">User Context</h4>
            <div className="flex items-center gap-3 p-4 bg-white border border-[#F0F2F5] rounded-xl cursor-pointer hover:border-[#CBD5E1] transition-colors">
              <div className="w-10 h-10 rounded-full bg-[#FF5C1A] flex items-center justify-center text-white font-bold text-sm">
                {event.id.slice(0, 2).toUpperCase()}
              </div>
              <div className="flex-1">
                <p className="font-bold text-[#1A1A2E] text-sm">Target User</p>
                <p className="text-[#64748B] text-xs">{event.id.slice(0, 12)}...</p>
              </div>
              <div className="text-right">
                <span className="text-[#1A1A2E] text-sm font-semibold">{event.department}</span>
                <ExternalLink size={14} className="text-[#94A3B8] inline ml-2 mb-0.5" />
              </div>
            </div>
          </section>

          {event.status === "high-risk" && (
            <div className="bg-[#FEF2F2] border border-[#FECACA] rounded-xl p-4 flex gap-3 text-left">
              <AlertTriangle size={18} className="text-[#DC2626] mt-0.5 flex-shrink-0" />
              <div>
                <p className="font-bold text-[#DC2626] text-[14px] mb-1">Policy Violation Detected</p>
                <p className="text-[13px] text-[#DC2626] opacity-90 leading-relaxed">
                  Usage of {event.activityLabel} is explicitly restricted for the {event.department} department. This incident has been escalated.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Footer actions */}
        <div className="p-6 border-t border-[#F0F2F5] flex gap-3 bg-white">
          <button className="flex-1 px-4 py-2.5 bg-white border border-[#E2E8F0] shadow-sm text-[13px] font-semibold text-[#1A1A2E] rounded-xl hover:bg-[#F8FAFC] transition-colors">
            Force Kill App
          </button>
          <button className="flex-1 px-4 py-2.5 bg-[#FF5C1A] text-white text-[13px] font-semibold rounded-xl hover:bg-[#E65318] active:scale-[0.98] transition-all shadow-sm">
            Resolve Incident
          </button>
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\RiskBadge.tsx

```tsx
import { Badge } from "@/components/ui/badge";

interface RiskBadgeProps {
  level: "low" | "medium" | "high";
}

export function RiskBadge({ level }: RiskBadgeProps) {
  const styles = {
    low: "bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/20 hover:bg-emerald-500/15",
    medium: "bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/20 hover:bg-amber-500/15",
    high: "bg-red-500/15 text-red-600 dark:text-red-400 border-red-500/20 hover:bg-red-500/15",
  };

  return (
    <Badge variant="outline" className={`text-[11px] font-medium capitalize ${styles[level]}`}>
      {level}
    </Badge>
  );
}
```

### devise-iris/frontend\src\components\dashboard\SettingsTab.tsx

```tsx
import { useState, useEffect } from "react";
import { 
  Shield, 
  Users, 
  Bell, 
  Layers, 
  Lock, 
  CreditCard,
  X,
  AlertTriangle
} from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { useSettings, useMe } from "@/hooks/useDashboard";
import { updateSettings } from "@/services/api";
import { useToast } from "@/components/ui/use-toast";

export function SettingsTab() {
  const [activeSection, setActiveSection] = useState("General");
  const [pollingHover, setPollingHover] = useState(false);

  const { data: settings, isLoading: settingsLoading, error: settingsError } = useSettings();
  const { data: me, isLoading: meLoading } = useMe();
  const { toast } = useToast();

  // ── Local state for editable fields ──
  const [orgName, setOrgName] = useState("");
  const [allowedCategories, setAllowedCategories] = useState<string[]>([]);
  const [newCategory, setNewCategory] = useState("");
  const [autoBlock, setAutoBlock] = useState(false);
  const [notificationSlack, setNotificationSlack] = useState(false);
  const [notificationEmail, setNotificationEmail] = useState(false);
  const [slackWebhookUrl, setSlackWebhookUrl] = useState("");
  const [isSaving, setIsSaving] = useState(false);

  // Sync local state when data loads
  useEffect(() => {
    if (me) {
      setOrgName(me.org_name || me.org_id || "");
    }
  }, [me]);

  useEffect(() => {
    if (settings) {
      setAllowedCategories(settings.allowed_categories || []);
      setAutoBlock(settings.auto_block);
      setNotificationSlack(settings.notification_slack);
      setNotificationEmail(settings.notification_email);
      setSlackWebhookUrl(settings.slack_webhook_url || "");
    }
  }, [settings]);

  const navItems = [
    { id: "General", icon: Shield },
    { id: "Team", icon: Users },
    { id: "Notifications", icon: Bell },
    { id: "Integrations", icon: Layers },
    { id: "Security & Privacy", icon: Lock },
    { id: "Billing", icon: CreditCard },
  ];

  const CustomToggle = ({ isOn, onToggle }: { isOn: boolean; onToggle?: () => void }) => (
    <div 
      onClick={onToggle}
      className="relative flex items-center transition-colors duration-200 cursor-pointer"
      style={{
        width: 36, height: 20, borderRadius: 999,
        backgroundColor: isOn ? "#FF5C1A" : "#E2E8F0"
      }}
    >
      <div 
        className="absolute bg-white rounded-full transition-all duration-200 shadow-sm"
        style={{
          width: 16, height: 16, top: 2,
          left: isOn ? 18 : 2
        }}
      />
    </div>
  );

  const handleRemoveCategory = (cat: string) => {
    setAllowedCategories(prev => prev.filter(c => c !== cat));
  };

  const handleAddCategory = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && newCategory.trim()) {
      e.preventDefault();
      if (!allowedCategories.includes(newCategory.trim())) {
        setAllowedCategories(prev => [...prev, newCategory.trim()]);
      }
      setNewCategory("");
    }
  };

  const handleSave = async () => {
    setIsSaving(true);
    try {
      await updateSettings({
        allowed_categories: allowedCategories,
        auto_block: autoBlock,
        notification_slack: notificationSlack,
        notification_email: notificationEmail,
        slack_webhook_url: slackWebhookUrl || null,
      });
      toast({
        title: "Settings saved",
        description: "Your changes have been applied.",
        duration: 3000,
      });
    } catch (err: any) {
      toast({
        title: "Failed to save settings",
        description: err?.message || "Something went wrong. Please try again.",
        duration: 4000,
      });
    } finally {
      setIsSaving(false);
    }
  };

  const isLoading = settingsLoading || meLoading;

  // ── Loading State ──
  if (isLoading) {
    return (
      <div className="flex flex-col gap-8 w-full max-w-[1400px] mx-auto pb-10">
        <div>
          <Skeleton className="h-7 w-32 mb-2" />
          <Skeleton className="h-4 w-64" />
        </div>
        <div className="flex flex-col md:flex-row items-start gap-8 w-full">
          <nav className="flex flex-col gap-1 flex-shrink-0" style={{ width: 200 }}>
            {[0, 1, 2, 3, 4, 5].map(i => (
              <Skeleton key={i} className="h-10 w-full rounded-xl" />
            ))}
          </nav>
          <div className="flex-1 flex flex-col gap-6 w-full max-w-[800px]">
            <div className="flex flex-col gap-5 bg-white" style={{ borderRadius: 16, padding: 24, border: "1px solid #F0F2F5" }}>
              <Skeleton className="h-5 w-32 mb-2" />
              <div className="grid grid-cols-2 gap-5">
                {[0, 1, 2, 3].map(i => (
                  <div key={i} className="flex flex-col gap-1.5">
                    <Skeleton className="h-3 w-20" />
                    <Skeleton className="h-9 w-full rounded-lg" />
                  </div>
                ))}
              </div>
            </div>
            <div className="flex flex-col gap-5 bg-white" style={{ borderRadius: 16, padding: 24, border: "1px solid #F0F2F5" }}>
              <Skeleton className="h-5 w-40 mb-2" />
              <Skeleton className="h-4 w-64 mb-3" />
              <Skeleton className="h-10 w-full rounded-lg" />
              <Skeleton className="h-10 w-full rounded-lg" />
              <Skeleton className="h-10 w-full rounded-lg" />
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ── Error State ──
  if (settingsError) {
    return (
      <div className="flex flex-col gap-8 w-full max-w-[1400px] mx-auto pb-10">
        <div>
          <h1 style={{ fontSize: 22, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Settings</h1>
          <p className="mt-1" style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Configure Devise for your organization</p>
        </div>
        <div className="flex items-center gap-2 p-4 bg-white rounded-2xl border border-[#F0F2F5]" style={{ boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}>
          <AlertTriangle size={16} className="text-[#DC2626]" />
          <span className="text-sm font-medium text-[#DC2626]">Failed to load settings: {settingsError.message}</span>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-8 w-full max-w-[1400px] mx-auto pb-10">
      
      {/* Header */}
      <div>
        <h1
          style={{
            fontSize: 22,
            fontWeight: 700,
            color: "#1A1A2E",
            fontFamily: "Inter, sans-serif",
          }}
        >
          Settings
        </h1>
        <p
          className="mt-1"
          style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}
        >
          Configure Devise for your organization
        </p>
      </div>

      <div className="flex flex-col md:flex-row items-start gap-8 w-full">
        {/* Left Nav (200px) */}
        <nav className="flex flex-col gap-1 flex-shrink-0" style={{ width: 200 }}>
          {navItems.map((item) => {
            const isActive = activeSection === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveSection(item.id)}
                className="flex items-center gap-3 w-full transition-colors duration-150 text-left"
                style={{
                  padding: "10px 16px",
                  borderRadius: 12,
                  backgroundColor: isActive ? "#FFF3EE" : "transparent",
                  color: isActive ? "#FF5C1A" : "#64748B",
                  fontFamily: "Inter, sans-serif",
                  fontWeight: isActive ? 600 : 500,
                  fontSize: 14,
                }}
                onMouseEnter={(e) => {
                  if (!isActive) e.currentTarget.style.color = "#FF5C1A";
                }}
                onMouseLeave={(e) => {
                  if (!isActive) e.currentTarget.style.color = "#64748B";
                }}
              >
                <item.icon size={18} strokeWidth={isActive ? 2 : 1.5} />
                {item.id}
              </button>
            );
          })}
        </nav>

        {/* Right Content Area */}
        <div className="flex-1 flex flex-col gap-6 w-full max-w-[800px]">
          {activeSection === "General" ? (
            <>
              {/* SECTION: Organization */}
              <div 
                className="flex flex-col gap-5 bg-white"
                style={{ borderRadius: 16, padding: "24px", border: "1px solid #F0F2F5", boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}
              >
                <h2 style={{ fontSize: 16, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                  Organization
                </h2>
                
                <div className="grid grid-cols-2 gap-5">
                  <div className="flex flex-col gap-1.5">
                    <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Org name</label>
                    <input 
                      type="text" 
                      value={orgName}
                      onChange={e => setOrgName(e.target.value)}
                      className="w-full outline-none"
                      style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
                    />
                  </div>
                  <div className="flex flex-col gap-1.5">
                    <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Industry</label>
                    <select 
                      defaultValue="Technology"
                      className="w-full outline-none bg-white cursor-pointer"
                      style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
                    >
                      <option>Technology</option>
                      <option>Finance</option>
                      <option>Healthcare</option>
                    </select>
                  </div>
                  <div className="flex flex-col gap-1.5">
                    <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Timezone</label>
                    <select 
                      defaultValue="Asia/Kolkata (IST)"
                      className="w-full outline-none bg-white cursor-pointer"
                      style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
                    >
                      <option>Asia/Kolkata (IST)</option>
                      <option>America/New_York (EST)</option>
                      <option>Europe/London (GMT)</option>
                    </select>
                  </div>
                  <div className="flex flex-col gap-1.5">
                    <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Language</label>
                    <select 
                      defaultValue="English"
                      className="w-full outline-none bg-white cursor-pointer"
                      style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
                    >
                      <option>English</option>
                      <option>Spanish</option>
                      <option>French</option>
                    </select>
                  </div>
                </div>

                <div className="flex justify-end mt-2">
                  <button 
                    onClick={handleSave}
                    disabled={isSaving}
                    className="transition-all hover:-translate-y-[1px] disabled:opacity-50 disabled:cursor-not-allowed"
                    style={{ 
                      backgroundColor: "#FF5C1A", color: "white", padding: "8px 16px", borderRadius: 8, 
                      fontSize: 14, fontWeight: 500, fontFamily: "Inter, sans-serif",
                      boxShadow: "0 1px 2px rgba(255, 92, 26, 0.2)"
                    }}
                    onMouseEnter={e => { if (!isSaving) e.currentTarget.style.backgroundColor = "#E5521A"; }}
                    onMouseLeave={e => e.currentTarget.style.backgroundColor = "#FF5C1A"}
                  >
                    {isSaving ? "Saving..." : "Save Changes"}
                  </button>
                </div>
              </div>

              {/* SECTION: Agent Configuration */}
              <div 
                className="flex flex-col gap-6 bg-white"
                style={{ borderRadius: 16, padding: "24px", border: "1px solid #F0F2F5", boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}
              >
                <div className="flex flex-col gap-1">
                  <h2 style={{ fontSize: 16, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                    Agent Configuration
                  </h2>
                  <p style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif" }}>Manage how the desktop agent monitors tool usage.</p>
                </div>

                {/* Polling Interval Slider (Mock) */}
                <div className="flex flex-col gap-2 border-b border-[#F0F2F5] pb-6">
                  <div className="flex justify-between items-end">
                    <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Detection polling interval</span>
                    <span style={{ fontSize: 13, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Current: <strong style={{color:"#1A1A2E"}}>30s</strong></span>
                  </div>
                  <div className="flex items-center gap-3 mt-1">
                    <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>10s</span>
                    <div 
                      className="relative w-full cursor-pointer h-6 flex items-center group"
                      onMouseEnter={() => setPollingHover(true)}
                      onMouseLeave={() => setPollingHover(false)}
                    >
                      <div className="w-full bg-[#E2E8F0] rounded-full" style={{ height: 4 }}>
                        <div className="bg-[#FF5C1A] rounded-full transition-all" style={{ width: "25%", height: "100%" }} />
                      </div>
                      <div 
                        className="absolute bg-white border-2 border-[#FF5C1A] rounded-full transition-all"
                        style={{
                          width: 16, height: 16, 
                          left: "25%", 
                          transform: "translate(-50%, 0)",
                          boxShadow: pollingHover ? "0 0 0 4px rgba(255,92,26,0.15)" : "0 2px 4px rgba(0,0,0,0.1)"
                        }}
                      />
                    </div>
                    <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>5min</span>
                  </div>
                </div>

                {/* Approved Tools List — now from allowed_categories */}
                <div className="flex flex-col gap-3 border-b border-[#F0F2F5] pb-6">
                  <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Allowed categories</span>
                  <div className="flex flex-wrap gap-2">
                    {allowedCategories.length === 0 && (
                      <span style={{ fontSize: 13, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>No categories configured</span>
                    )}
                    {allowedCategories.map(t => (
                      <div 
                        key={t}
                        className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg"
                        style={{ backgroundColor: "#FFF3EE", color: "#FF5C1A", fontSize: 13, fontFamily: "Inter, sans-serif", fontWeight: 500 }}
                      >
                        {t}
                        <X 
                          size={14} 
                          className="cursor-pointer hover:text-[#DC2626] transition-colors" 
                          onClick={() => handleRemoveCategory(t)}
                        />
                      </div>
                    ))}
                    <div className="flex items-center px-1">
                      <input 
                        type="text"
                        placeholder="+ Add category"
                        value={newCategory}
                        onChange={e => setNewCategory(e.target.value)}
                        onKeyDown={handleAddCategory}
                        className="outline-none bg-transparent"
                        style={{ fontSize: 13, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
                      />
                    </div>
                  </div>
                </div>

                {/* Auto Block Toggle (inverted: auto_block=true means blocking) */}
                <div className="flex items-center justify-between border-b border-[#F0F2F5] pb-6">
                  <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Auto-approve low risk tools</span>
                  <CustomToggle isOn={!autoBlock} onToggle={() => setAutoBlock(prev => !prev)} />
                </div>

                {/* Registry auto-update toggle */}
                <div className="flex items-center justify-between">
                  <div className="flex flex-col gap-0.5">
                    <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Registry auto-update</span>
                    <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Last updated 2hr ago</span>
                  </div>
                  <CustomToggle isOn={true} />
                </div>
              </div>

              {/* SECTION: Notification Preferences */}
              <div 
                className="flex flex-col gap-5 bg-white"
                style={{ borderRadius: 16, padding: "24px", border: "1px solid #F0F2F5", boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}
              >
                <h2 style={{ fontSize: 16, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                  Notification Preferences
                </h2>
                <div className="flex flex-col gap-5 mt-1">
                  
                  {/* Slack */}
                  <div className="flex items-center justify-between">
                    <div className="flex flex-col gap-1">
                      <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Slack alerts</span>
                      {slackWebhookUrl ? (
                        <span className="flex items-center gap-1.5" style={{ fontSize: 13, color: "#10B981", fontWeight: 500, fontFamily: "Inter, sans-serif" }}>
                          <span className="w-1.5 h-1.5 rounded-full bg-[#10B981]" />
                          Connected
                        </span>
                      ) : (
                        <span style={{ fontSize: 13, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>
                          No webhook configured
                        </span>
                      )}
                    </div>
                    <CustomToggle isOn={notificationSlack} onToggle={() => setNotificationSlack(prev => !prev)} />
                  </div>

                  {/* Email */}
                  <div className="flex items-center justify-between mt-1">
                    <div className="flex flex-col gap-1">
                      <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Email digest</span>
                      <span style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif" }}>
                        Daily at 9:00 AM
                      </span>
                    </div>
                    <CustomToggle isOn={notificationEmail} onToggle={() => setNotificationEmail(prev => !prev)} />
                  </div>

                  {/* Critical */}
                  <div className="flex items-center justify-between mt-1 pt-5 border-t border-[#F0F2F5]">
                    <span style={{ fontSize: 14, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Critical alerts only mode</span>
                    <CustomToggle isOn={false} />
                  </div>

                </div>
              </div>

              {/* SECTION: Budget & Threshold (from settings) */}
              {settings && (
                <div 
                  className="flex flex-col gap-5 bg-white"
                  style={{ borderRadius: 16, padding: "24px", border: "1px solid #F0F2F5", boxShadow: "0 1px 3px rgba(0,0,0,0.06)" }}
                >
                  <h2 style={{ fontSize: 16, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                    Budget & Alerts
                  </h2>
                  <div className="grid grid-cols-2 gap-5">
                    <div className="flex flex-col gap-1.5">
                      <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Monthly budget</label>
                      <div
                        className="w-full"
                        style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif", backgroundColor: "#F8FAFC" }}
                      >
                        ${settings.monthly_budget.toLocaleString()}
                      </div>
                    </div>
                    <div className="flex flex-col gap-1.5">
                      <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Alert threshold</label>
                      <div
                        className="w-full"
                        style={{ padding: "8px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif", backgroundColor: "#F8FAFC" }}
                      >
                        {settings.alert_threshold}%
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* SECTION: Danger Zone */}
              <div 
                className="flex flex-col gap-5"
                style={{ 
                  borderRadius: 16, padding: "24px", 
                  border: "1px solid #FECACA", 
                  backgroundColor: "#FFF5F5"
                }}
              >
                <div className="flex flex-col gap-1">
                  <h2 style={{ fontSize: 16, fontWeight: 600, color: "#DC2626", fontFamily: "Inter, sans-serif" }}>
                    Danger Zone
                  </h2>
                  <span style={{ fontSize: 12, color: "#DC2626", fontFamily: "Inter, sans-serif" }}>
                    These actions cannot be undone
                  </span>
                </div>

                <div className="flex flex-col sm:flex-row gap-4 mt-2">
                  <button 
                    className="flex-1 transition-colors"
                    style={{
                      border: "1px solid #FECACA", backgroundColor: "white", color: "#DC2626",
                      padding: "10px 16px", borderRadius: 8, fontSize: 14, fontWeight: 500,
                      fontFamily: "Inter, sans-serif", cursor: "pointer"
                    }}
                    onMouseEnter={e => e.currentTarget.style.backgroundColor = "#FEF2F2"}
                    onMouseLeave={e => e.currentTarget.style.backgroundColor = "white"}
                  >
                    Reset all detection data
                  </button>
                  <button 
                    className="flex-1 transition-colors"
                    style={{
                      border: "1px solid #FECACA", backgroundColor: "white", color: "#DC2626",
                      padding: "10px 16px", borderRadius: 8, fontSize: 14, fontWeight: 500,
                      fontFamily: "Inter, sans-serif", cursor: "pointer"
                    }}
                    onMouseEnter={e => e.currentTarget.style.backgroundColor = "#FEF2F2"}
                    onMouseLeave={e => e.currentTarget.style.backgroundColor = "white"}
                  >
                    Remove all agents
                  </button>
                </div>
              </div>

            </>
          ) : (
            <div className="flex items-center justify-center py-20 bg-white" style={{ borderRadius: 16, border: "1px solid #F0F2F5" }}>
              <p style={{ color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>{activeSection} settings coming soon...</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\StatsCard.tsx

```tsx
import { Card, CardContent } from "@/components/ui/card";
import { LucideIcon } from "lucide-react";

interface StatsCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: LucideIcon;
  variant?: "default" | "primary";
}

export function StatsCard({ title, value, subtitle, icon: Icon, variant = "default" }: StatsCardProps) {
  const isPrimary = variant === "primary";

  return (
    <Card className={isPrimary ? "bg-primary text-primary-foreground border-primary" : ""}>
      <CardContent className="p-5">
        <div className="flex items-center justify-between">
          <div className="space-y-1">
            <p className={`text-xs font-medium uppercase tracking-wide ${isPrimary ? "text-primary-foreground/70" : "text-muted-foreground"}`}>
              {title}
            </p>
            <p className="text-2xl font-bold">{value}</p>
            {subtitle && (
              <p className={`text-xs ${isPrimary ? "text-primary-foreground/60" : "text-muted-foreground"}`}>
                {subtitle}
              </p>
            )}
          </div>
          <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${isPrimary ? "bg-primary-foreground/20" : "bg-secondary"}`}>
            <Icon className="h-5 w-5" />
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
```

### devise-iris/frontend\src\components\dashboard\SubscriptionList.tsx

```tsx
import { Code2, X } from "lucide-react";
import { useState, useMemo } from "react";
import { useToast } from "@/components/ui/use-toast";
import { useSubscriptions } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Types ─────────────────────────────────────────────────────────────────

interface Sub {
  iconBg: string;
  icon: React.ElementType;
  iconColor: string;
  name: string;
  seats: string;
  price: string;
  badge: "active" | "zombie";
}

// ─── Color palette for subscriptions ───────────────────────────────────────

const subColors = [
  { iconBg: "#F0FFF4", iconColor: "#16A34A" },
  { iconBg: "#FFF7ED", iconColor: "#FF5C1A" },
  { iconBg: "#FEF2F2", iconColor: "#DC2626" },
  { iconBg: "#EFF6FF", iconColor: "#3B82F6" },
  { iconBg: "#F5F3FF", iconColor: "#8B5CF6" },
];

// ─── Badge ─────────────────────────────────────────────────────────────────

function Badge({ type }: { type: "active" | "zombie" }) {
  const isActive = type === "active";
  return (
    <span
      className="text-xs font-medium rounded-full px-2.5 py-0.5 flex-shrink-0"
      style={{
        backgroundColor: isActive ? "#F0FFF4" : "#FEF2F2",
        color: isActive ? "#16A34A" : "#DC2626",
        border: `1px solid ${isActive ? "#BBF7D0" : "#FECACA"}`,
        fontSize: 11,
        fontFamily: "Inter, sans-serif",
      }}
    >
      {isActive ? "Active" : "Zombie"}
    </span>
  );
}

// ─── Row ───────────────────────────────────────────────────────────────────

function SubRow({ sub, last, onClick }: { sub: Sub; last: boolean; onClick?: () => void }) {
  const Icon = sub.icon;
  return (
    <div
      onClick={onClick}
      className="flex items-center gap-3 cursor-pointer transition-colors"
      style={{
        padding: "12px 4px",
        borderBottom: last ? "none" : "1px solid #F5F5F5",
      }}
      onMouseEnter={(e) => {
        (e.currentTarget as HTMLDivElement).style.backgroundColor = "#FAFAFA";
      }}
      onMouseLeave={(e) => {
        (e.currentTarget as HTMLDivElement).style.backgroundColor = "transparent";
      }}
    >
      {/* Icon */}
      <div
        className="flex items-center justify-center rounded-xl flex-shrink-0"
        style={{ width: 38, height: 38, backgroundColor: sub.iconBg }}
      >
        <Icon size={16} strokeWidth={2} color={sub.iconColor} />
      </div>

      {/* Name + seats */}
      <div className="flex-1 min-w-0">
        <p
          className="font-semibold truncate"
          style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          {sub.name}
        </p>
        <p style={{ fontSize: 12, color: "#94A3B8", marginTop: 1 }}>{sub.seats}</p>
      </div>

      {/* Price + badge */}
      <div className="flex flex-col items-end gap-1.5 flex-shrink-0">
        <span
          className="font-semibold"
          style={{ fontSize: 13, color: "#FF5C1A", fontFamily: "Inter, sans-serif" }}
        >
          {sub.price}
        </span>
        <Badge type={sub.badge} />
      </div>
    </div>
  );
}

// ─── Exported component ───────────────────────────────────────────────────

export function SubscriptionList({ onNavigate }: { onNavigate?: (tab: string) => void }) {
  const [isAddOpen, setIsAddOpen] = useState(false);
  const { data: subscriptions, isLoading, error } = useSubscriptions();

  const topSubs: Sub[] = useMemo(() => {
    if (!subscriptions?.length) return [];
    return [...subscriptions]
      .sort((a, b) => b.cost_monthly - a.cost_monthly)
      .slice(0, 3)
      .map((item, i) => {
        const colors = subColors[i % subColors.length];
        return {
          iconBg: colors.iconBg,
          icon: Code2,
          iconColor: colors.iconColor,
          name: item.tool_name,
          seats: `${item.seats_used} of ${item.seats} seats active`,
          price: `₹${item.cost_monthly.toLocaleString("en-IN")}/mo`,
          badge: item.status === "zombie" ? "zombie" as const : "active" as const,
        };
      });
  }, [subscriptions]);

  return (
    <div
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        padding: 24,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      }}
    >
      {/* Header */}
      <div className="flex items-center justify-between mb-1">
        <p
          className="font-semibold"
          style={{ fontSize: 15, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          Top Subscriptions
        </p>
        <button
          onClick={() => setIsAddOpen(true)}
          className="font-medium transition-colors"
          style={{
            fontSize: 12,
            color: "#FF5C1A",
            border: "1px solid #FF5C1A",
            borderRadius: 999,
            padding: "4px 12px",
            backgroundColor: "transparent",
            cursor: "pointer",
            fontFamily: "Inter, sans-serif",
          }}
          onMouseEnter={(e) => {
            (e.currentTarget as HTMLButtonElement).style.backgroundColor = "#FFF3EE";
          }}
          onMouseLeave={(e) => {
            (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent";
          }}
        >
          + Add tool
        </button>
      </div>

      {/* Rows */}
      <div>
        {isLoading ? (
          // Skeleton loading rows
          Array.from({ length: 3 }).map((_, i) => (
            <div
              key={`skel-${i}`}
              className="flex items-center gap-3"
              style={{
                padding: "12px 4px",
                borderBottom: i === 2 ? "none" : "1px solid #F5F5F5",
              }}
            >
              <Skeleton className="rounded-xl flex-shrink-0" style={{ width: 38, height: 38 }} />
              <div className="flex-1 min-w-0 flex flex-col gap-1">
                <Skeleton className="w-28 h-4 rounded" />
                <Skeleton className="w-20 h-3 rounded" />
              </div>
              <div className="flex flex-col items-end gap-1.5 flex-shrink-0">
                <Skeleton className="w-20 h-4 rounded" />
                <Skeleton className="w-14 h-5 rounded-full" />
              </div>
            </div>
          ))
        ) : error ? (
          <div style={{ padding: "20px 4px", textAlign: "center" }}>
            <p style={{ fontSize: 13, color: "#DC2626" }}>
              Failed to load subscriptions
            </p>
          </div>
        ) : topSubs.length === 0 ? (
          <div style={{ padding: "20px 4px", textAlign: "center" }}>
            <p style={{ fontSize: 13, color: "#94A3B8" }}>
              No subscriptions
            </p>
          </div>
        ) : (
          topSubs.map((sub, i) => (
            <SubRow key={sub.name} sub={sub} last={i === topSubs.length - 1} onClick={() => onNavigate?.("subscriptions")} />
          ))
        )}
      </div>

      <AddSubscriptionModal isOpen={isAddOpen} onClose={() => setIsAddOpen(false)} />
    </div>
  );
}

// ─── ADD SUBSCRIPTION MODAL ─────────────────────────────────────────────────

function AddSubscriptionModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  const { toast } = useToast();
  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    toast({
      title: "Tool subscription added",
      description: "It has been recorded to your organization's ledger.",
      duration: 3000,
    });
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black/40 backdrop-blur-sm" onClick={onClose} />
      <div className="relative bg-white rounded-2xl w-[480px] p-6 shadow-[0_24px_64px_rgba(0,0,0,0.15)] animate-in fade-in zoom-in-95 duration-200 text-left">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold text-[#1A1A2E]">Add AI Tool Subscription</h2>
          <button onClick={onClose} className="p-2 text-[#94A3B8] hover:text-[#1A1A2E] hover:bg-[#F0F2F5] rounded-lg transition-colors">
            <X size={20} className="active:scale-95 transition-transform" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-5">
          <div className="flex flex-col gap-1.5">
            <label className="text-sm font-semibold text-[#1A1A2E]">Tool Name</label>
            <input 
              required
              type="text" 
              placeholder="e.g. Cursor Pro" 
              className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors"
            />
          </div>

          <div className="flex gap-4">
            <div className="flex flex-col gap-1.5 flex-1">
              <label className="text-sm font-semibold text-[#1A1A2E]">Seats Paid</label>
              <input 
                required
                type="number" 
                defaultValue={1}
                min={1}
                className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors"
              />
            </div>
            <div className="flex flex-col gap-1.5 flex-1">
              <label className="text-sm font-semibold text-[#1A1A2E]">Monthly Cost (₹)</label>
              <input 
                required
                type="number" 
                placeholder="0"
                className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors"
              />
            </div>
          </div>

          <div className="flex items-center justify-end gap-3 mt-4 pt-4 border-t border-[#F0F2F5]">
            <button 
              type="button" 
              onClick={onClose}
              className="px-5 py-2.5 text-sm font-semibold text-[#64748B] hover:text-[#1A1A2E] hover:bg-[#F8FAFC] rounded-xl transition-colors"
            >
              Cancel
            </button>
            <button 
              type="submit"
              className="px-5 py-2.5 text-sm font-semibold text-white bg-[#FF5C1A] hover:bg-[#E65318] hover:translate-y-[-1px] active:scale-[0.98] rounded-xl transition-all shadow-sm"
            >
              Add Tool
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\SubscriptionsTab.tsx

```tsx
import { useMemo } from "react";
import { Plus, AlertTriangle } from "lucide-react";
import { useSubscriptions, useSpendOverview } from "@/hooks/useDashboard";
import type { SubscriptionItem, SpendOverview } from "@/services/api";
import { Skeleton } from "@/components/ui/skeleton";

// ─── Types ─────────────────────────────────────────────────────────────────

interface Sub {
  id: string;
  name: string;
  vendor: string;
  seats: number;
  active: number;
  util: number;
  cost: string;
  status: "Active" | "Zombie" | "Expiring soon";
  cycle: string;
  renewal: string;
  bg: string;
}

// ─── Helpers ───────────────────────────────────────────────────────────────

const COLOR_PALETTE = [
  "#10A37F", "#181717", "#FF5C1A", "#D97706", "#0F172A",
  "#000000", "#8B5CF6", "#3B82F6", "#EC4899", "#10B981",
  "#4285F4", "#6366F1", "#14B8A6", "#F43F5E", "#8B5CF6",
];

function hashStringToIndex(str: string, max: number): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash + str.charCodeAt(i)) | 0;
  }
  return Math.abs(hash) % max;
}

function formatINR(amount: number): string {
  // Format as Indian locale with ₹
  return "\u20B9" + amount.toLocaleString("en-IN");
}

function formatRenewalDate(dateStr: string | null): string {
  if (!dateStr) return "\u2014";
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return "\u2014";
  const now = new Date();
  const diffMs = d.getTime() - now.getTime();
  if (diffMs < 0) return "Expired";
  const diffDays = Math.floor(diffMs / 86_400_000);
  if (diffDays < 30) return "Renews next month";
  const month = d.toLocaleString("en-US", { month: "short" });
  const year = d.getFullYear();
  return `Renews ${month} ${year}`;
}

function mapSubscriptionItem(item: SubscriptionItem): Sub {
  const util = item.seats > 0 ? Math.round((item.seats_used / item.seats) * 100) : 0;
  const statusMap: Record<SubscriptionItem["status"], Sub["status"]> = {
    active: "Active",
    zombie: "Zombie",
    trial: "Active",
    cancelled: "Zombie",
  };

  return {
    id: item.id,
    name: item.tool_name,
    vendor: item.vendor,
    seats: item.seats,
    active: item.seats_used,
    util,
    cost: `${formatINR(item.cost_monthly)}/mo`,
    status: statusMap[item.status],
    cycle: item.renewal_date ? "Annual contract" : "Monthly",
    renewal: formatRenewalDate(item.renewal_date),
    bg: COLOR_PALETTE[hashStringToIndex(item.tool_name, COLOR_PALETTE.length)],
  };
}

// ─── MAIN COMPONENT ─────────────────────────────────────────────────────────

export function SubscriptionsTab() {
  const { data: subscriptionItems, isLoading: subsLoading, error: subsError } = useSubscriptions();
  const { data: spendOverview, isLoading: spendLoading, error: spendError } = useSpendOverview();

  const isLoading = subsLoading || spendLoading;
  const error = subsError || spendError;

  const subscriptions: Sub[] = useMemo(() => {
    if (!subscriptionItems) return [];
    return subscriptionItems.map(mapSubscriptionItem);
  }, [subscriptionItems]);

  // Computed stats (fallback to spend overview, then compute from subscriptions)
  const totalMonthlySpend = spendOverview?.totalMonthlySpend ?? (subscriptionItems?.reduce((sum, s) => sum + s.cost_monthly, 0) ?? 0);
  const totalTools = subscriptions.length;
  const zombieLicenses = spendOverview?.zombieLicenses ?? subscriptions.filter(s => s.status === "Zombie").length;
  const zombieCost = spendOverview?.zombieCost ?? (subscriptionItems?.filter(s => s.status === "zombie" || s.status === "cancelled").reduce((sum, s) => sum + s.cost_monthly, 0) ?? 0);

  const CardInfo = ({ title, value, sub }: { title: string; value: string; sub: React.ReactNode }) => (
    <div
      className="flex-1 flex flex-col justify-center"
      style={{
        backgroundColor: title === "MONTHLY SPEND" ? "#FF5C1A" : "#ffffff",
        borderRadius: 20,
        padding: "20px 24px",
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        border: title === "MONTHLY SPEND" ? "none" : "1px solid #F0F2F5",
      }}
    >
      <span
        style={{
          fontSize: 12,
          fontWeight: 600,
          color: title === "MONTHLY SPEND" ? "rgba(255,255,255,0.9)" : "#94A3B8",
          letterSpacing: "0.5px",
          fontFamily: "Inter, sans-serif",
          textTransform: "uppercase",
        }}
      >
        {title}
      </span>
      <span
        className="mt-2"
        style={{
          fontSize: 36,
          fontWeight: 700,
          color: title === "MONTHLY SPEND" ? "#ffffff" : "#1A1A2E",
          fontFamily: "Inter, sans-serif",
          lineHeight: 1,
        }}
      >
        {value}
      </span>
      <div
        className="mt-3 flex items-center gap-1.5"
        style={{
          fontSize: 13,
          color: title === "MONTHLY SPEND" ? "rgba(255,255,255,0.8)" : "#64748B",
          fontFamily: "Inter, sans-serif",
        }}
      >
        {sub}
      </div>
    </div>
  );

  const getBarColor = (util: number) => {
    if (util > 70) return "#16A34A";
    if (util >= 40) return "#D97706";
    return "#DC2626";
  };

  const getActiveUsersColor = (util: number) => {
    if (util > 70) return "#16A34A";
    if (util < 40) return "#DC2626";
    return "#1A1A2E";
  };

  const getStatusBadge = (status: Sub["status"]) => {
    switch (status) {
      case "Active":
        return { bg: "#ECFDF5", text: "#10B981" };
      case "Zombie":
        return { bg: "#FEF2F2", text: "#DC2626" };
      case "Expiring soon":
        return { bg: "#FFFBEB", text: "#D97706" };
    }
  };

  // ─── Loading skeleton ──────────────────────────────────────────────────
  if (isLoading) {
    return (
      <div className="flex flex-col gap-6 w-full max-w-[1400px] mx-auto pb-10">
        <div className="flex items-center justify-between">
          <div>
            <h1 style={{ fontSize: 22, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Subscriptions</h1>
            <p className="mt-1" style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Manage all AI tool licenses and spending</p>
          </div>
          <Skeleton className="h-9 w-40 rounded-xl" />
        </div>
        <div className="flex gap-4">
          {[1, 2, 3].map(i => (
            <div key={i} className="flex-1" style={{ borderRadius: 20, padding: "20px 24px", border: "1px solid #F0F2F5" }}>
              <Skeleton className="h-3 w-24 mb-3" />
              <Skeleton className="h-9 w-28 mb-2" />
              <Skeleton className="h-3 w-32" />
            </div>
          ))}
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 16 }}>
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="flex items-center" style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 20, padding: "20px 24px", gap: 20 }}>
              <Skeleton className="h-11 w-11 rounded-full flex-shrink-0" />
              <div className="flex-1">
                <Skeleton className="h-4 w-28 mb-2" />
                <Skeleton className="h-3 w-20" />
              </div>
              <div className="flex-1">
                <Skeleton className="h-3 w-full" />
              </div>
              <div className="flex flex-col items-end gap-1">
                <Skeleton className="h-5 w-14" />
                <Skeleton className="h-5 w-20" />
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // ─── Error state ───────────────────────────────────────────────────────
  if (error) {
    return (
      <div className="flex flex-col gap-6 w-full max-w-[1400px] mx-auto pb-10">
        <div className="flex items-center justify-between">
          <div>
            <h1 style={{ fontSize: 22, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Subscriptions</h1>
            <p className="mt-1" style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Manage all AI tool licenses and spending</p>
          </div>
        </div>
        <div style={{ backgroundColor: "#FEF2F2", border: "1px solid #FECACA", borderRadius: 16, padding: "16px 20px" }}>
          <p style={{ fontSize: 14, color: "#DC2626", fontWeight: 500 }}>
            Failed to load subscriptions: {error.message}
          </p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 4 }}>
            Data will retry automatically. Check your connection if this persists.
          </p>
        </div>
      </div>
    );
  }

  // ─── Empty state ───────────────────────────────────────────────────────
  if (subscriptions.length === 0) {
    return (
      <div className="flex flex-col gap-6 w-full max-w-[1400px] mx-auto pb-10">
        <div className="flex items-center justify-between">
          <div>
            <h1 style={{ fontSize: 22, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>Subscriptions</h1>
            <p className="mt-1" style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>Manage all AI tool licenses and spending</p>
          </div>
          <button
            className="flex items-center gap-2 hover:-translate-y-[1px] transition-all duration-200"
            style={{ backgroundColor: "#FF5C1A", color: "#ffffff", padding: "8px 16px", borderRadius: 12, fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 14, boxShadow: "0 1px 3px rgba(0,0,0,0.1)" }}
            onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#E5521A")}
            onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "#FF5C1A")}
          >
            <Plus size={16} strokeWidth={2} />
            Add Subscription
          </button>
        </div>
        <div className="flex gap-4">
          <CardInfo title="MONTHLY SPEND" value={formatINR(0)} sub={<>No spend data</>} />
          <CardInfo title="TOTAL TOOLS" value="0" sub={<><span className="w-2 h-2 rounded-full bg-[#16A34A]" />No subscriptions</>} />
          <CardInfo title="WASTED SPEND" value={formatINR(0)} sub={<><span className="w-2 h-2 rounded-full bg-[#DC2626]" />0 zombie licenses</>} />
        </div>
        <div style={{ backgroundColor: "#ffffff", border: "1px solid #F0F2F5", borderRadius: 20, padding: "48px 24px" }} className="flex flex-col items-center justify-center">
          <Plus size={40} strokeWidth={1.5} color="#CBD5E1" />
          <p className="mt-4 font-medium" style={{ fontSize: 16, color: "#94A3B8" }}>No subscriptions yet</p>
          <p style={{ fontSize: 13, color: "#CBD5E1", marginTop: 4 }}>Add your first AI tool subscription to start tracking</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-6 w-full max-w-[1400px] mx-auto pb-10">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1
            style={{
              fontSize: 22,
              fontWeight: 700,
              color: "#1A1A2E",
              fontFamily: "Inter, sans-serif",
            }}
          >
            Subscriptions
          </h1>
          <p
            className="mt-1"
            style={{ fontSize: 14, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}
          >
            Manage all AI tool licenses and spending
          </p>
        </div>
        <button
          className="flex items-center gap-2 hover:-translate-y-[1px] transition-all duration-200"
          style={{
            backgroundColor: "#FF5C1A",
            color: "#ffffff",
            padding: "8px 16px",
            borderRadius: 12,
            fontFamily: "Inter, sans-serif",
            fontWeight: 500,
            fontSize: 14,
            boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
          }}
          onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#E5521A")}
          onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "#FF5C1A")}
        >
          <Plus size={16} strokeWidth={2} />
          Add Subscription
        </button>
      </div>

      {/* Stats Row */}
      <div className="flex gap-4">
        <CardInfo title="MONTHLY SPEND" value={formatINR(totalMonthlySpend)} sub={<>Across {totalTools} tools</>} />
        <CardInfo
          title="TOTAL TOOLS"
          value={String(totalTools)}
          sub={
            <>
              <span className="w-2 h-2 rounded-full bg-[#16A34A]" />
              Active subscriptions
            </>
          }
        />
        <CardInfo
          title="WASTED SPEND"
          value={formatINR(zombieCost)}
          sub={
            <>
              <span className="w-2 h-2 rounded-full bg-[#DC2626]" />
              {zombieLicenses} zombie licenses
            </>
          }
        />
      </div>

      {/* Zombie Alert Banner — only show if zombies exist */}
      {zombieLicenses > 0 && (
        <div
          className="flex items-center justify-between"
          style={{
            backgroundColor: "#FFF3EE",
            border: "1px solid #FDDCC8",
            borderRadius: 16,
            padding: "16px 20px",
          }}
        >
          <div className="flex items-center gap-3">
            <AlertTriangle size={20} color="#FF5C1A" strokeWidth={2} />
            <span
              style={{
                color: "#1A1A2E",
                fontFamily: "Inter, sans-serif",
                fontSize: 14,
                fontWeight: 500,
              }}
            >
              <span style={{ fontWeight: 700 }}>{zombieLicenses} zombie licenses detected</span> — potential savings of {formatINR(zombieCost)}/month
            </span>
          </div>
          <button
            style={{
              color: "#FF5C1A",
              fontFamily: "Inter, sans-serif",
              fontSize: 14,
              fontWeight: 600,
              background: "none",
              border: "none",
              cursor: "pointer",
            }}
          >
            Review Now &rarr;
          </button>
        </div>
      )}

      {/* Grid of Subscriptions */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2, 1fr)",
          gap: 16,
        }}
      >
        {subscriptions.map((sub) => {
          const badge = getStatusBadge(sub.status);
          return (
            <div
              key={sub.id}
              className="flex items-center transition-all duration-200 cursor-pointer hover:-translate-y-[1px]"
              style={{
                backgroundColor: "#ffffff",
                border: "1px solid #F0F2F5",
                borderRadius: 20,
                padding: "20px 24px",
                gap: 20,
                boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.boxShadow = "0 8px 24px rgba(0,0,0,0.10)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.boxShadow = "0 1px 3px rgba(0,0,0,0.06)";
              }}
            >
              {/* Left Column (Icon + Name) */}
              <div className="flex items-center gap-4 flex-1 min-w-[200px]">
                <div
                  className="flex items-center justify-center rounded-full flex-shrink-0"
                  style={{
                    width: 44,
                    height: 44,
                    backgroundColor: sub.bg,
                    color: "#ffffff",
                    fontFamily: "Inter, sans-serif",
                    fontWeight: 600,
                    fontSize: 20,
                  }}
                >
                  {sub.name.charAt(0)}
                </div>
                <div className="flex flex-col">
                  <span
                    style={{
                      fontFamily: "Inter, sans-serif",
                      fontWeight: 600,
                      fontSize: 16,
                      color: "#1A1A2E",
                      lineHeight: 1.2,
                    }}
                  >
                    {sub.name}
                  </span>
                  <span
                    className="mt-1"
                    style={{
                      fontFamily: "Inter, sans-serif",
                      fontSize: 13,
                      color: "#94A3B8",
                      lineHeight: 1.2,
                    }}
                  >
                    {sub.vendor}
                  </span>
                </div>
              </div>

              {/* Middle Section (3 Cols) */}
              <div className="flex items-start flex-1" style={{ gap: 24 }}>
                <div className="flex flex-col gap-1 w-[80px]">
                  <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>
                    Seats Paid
                  </span>
                  <span style={{ fontSize: 16, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                    {sub.seats}
                  </span>
                </div>
                <div className="flex flex-col gap-1 w-[80px]">
                  <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>
                    Active Users
                  </span>
                  <span style={{ fontSize: 16, fontWeight: 700, color: getActiveUsersColor(sub.util), fontFamily: "Inter, sans-serif" }}>
                    {sub.active}
                  </span>
                </div>
                <div className="flex flex-col gap-1 flex-1 min-w-[100px]">
                  <div className="flex items-center justify-between">
                    <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>
                      Utilization
                    </span>
                    <span style={{ fontSize: 14, fontWeight: 700, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
                      {sub.util}%
                    </span>
                  </div>
                  {/* Utilization Bar */}
                  <div
                    className="mt-1.5 w-full overflow-hidden"
                    style={{ height: 6, backgroundColor: "#F0F2F5", borderRadius: 999 }}
                  >
                    <div
                      style={{
                        width: `${sub.util}%`,
                        height: "100%",
                        backgroundColor: getBarColor(sub.util),
                        borderRadius: 999,
                      }}
                    />
                  </div>
                </div>
              </div>

              {/* Right Column (Cost + Badges) */}
              <div className="flex flex-col items-end text-right justify-center" style={{ minWidth: 140 }}>
                <div className="flex items-center gap-2 mb-1">
                  <span
                    style={{
                      backgroundColor: badge.bg,
                      color: badge.text,
                      padding: "2px 8px",
                      borderRadius: 999,
                      fontSize: 11,
                      fontWeight: 600,
                      fontFamily: "Inter, sans-serif",
                    }}
                  >
                    {sub.status}
                  </span>
                </div>
                <span
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontWeight: 700,
                    fontSize: 18,
                    color: "#1A1A2E",
                    lineHeight: 1.2,
                  }}
                >
                  {sub.cost}
                </span>
                <span
                  className="mt-0.5"
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontSize: 12,
                    color: "#94A3B8",
                  }}
                >
                  {sub.cycle}
                </span>
                <span
                  className="mt-0.5"
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontSize: 11,
                    color: "#94A3B8",
                  }}
                >
                  {sub.renewal}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\TeamTab.tsx

```tsx
import { useState, useMemo } from "react";
import { 
  UserPlus, Search, MoreHorizontal, X, User, Activity, AlertTriangle, CheckCircle2, 
  MapPin, Shield, Copy, ExternalLink, ChevronDown, Bell
} from "lucide-react";
import { Card } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip as RechartsTooltip, Cell, PieChart, Pie } from "recharts";
import { useToast } from "@/components/ui/use-toast";
import { useTeam } from "@/hooks/useDashboard";
import { inviteTeamMember } from "@/services/api";

// ─── TYPES ──────────────────────────────────────────────────────────────────

interface TeamMember {
  id: string;
  initials: string;
  name: string;
  email: string;
  department: string;
  role: string;
  toolsUsed: number;
  risk: "zero";
  lastActive: string;
}

const riskConf: Record<string, { bg: string; text: string; label: string }> = {
  high: { bg: "rgba(220,38,38,0.1)", text: "#DC2626", label: "High" },
  medium: { bg: "rgba(217,119,6,0.1)", text: "#D97706", label: "Medium" },
  low: { bg: "rgba(22,163,74,0.1)", text: "#16A34A", label: "Low" },
  zero: { bg: "transparent", text: "#C0C8D4", label: "—" },
};

// ─── HELPERS ────────────────────────────────────────────────────────────────

function deriveInitials(fullName: string): string {
  return fullName
    .split(/\s+/)
    .filter(Boolean)
    .map(w => w[0].toUpperCase())
    .slice(0, 2)
    .join("");
}

function capitalizeFirst(s: string): string {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
}

function formatDate(dateStr: string): string {
  try {
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return "—";
    return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
  } catch {
    return "—";
  }
}

// ─── MAIN COMPONENT ─────────────────────────────────────────────────────────

export function TeamTab() {
  const [searchQuery, setSearchQuery] = useState("");
  const [openMenu, setOpenMenu] = useState<string | null>(null);
  const [selectedMember, setSelectedMember] = useState<TeamMember | null>(null);
  const [isInviteOpen, setIsInviteOpen] = useState(false);

  const { data, isLoading, error } = useTeam();

  // Map API members to local TeamMember shape
  const teamMembers: TeamMember[] = useMemo(() => {
    if (!data?.members) return [];
    return data.members.map(m => ({
      id: m.id,
      initials: deriveInitials(m.full_name),
      name: m.full_name,
      email: m.email,
      department: m.department || "—",
      role: capitalizeFirst(m.role),
      toolsUsed: 0,
      risk: "zero" as const,
      lastActive: m.created_at ? formatDate(m.created_at) : "—",
    }));
  }, [data]);

  // Compute department breakdown from real data
  const deptData = useMemo(() => {
    if (!teamMembers.length) return [];
    const counts: Record<string, number> = {};
    teamMembers.forEach(m => {
      const dept = m.department || "Unknown";
      counts[dept] = (counts[dept] || 0) + 1;
    });
    return Object.entries(counts)
      .map(([name, members]) => ({ name, members }))
      .sort((a, b) => b.members - a.members);
  }, [teamMembers]);

  const filteredMembers = teamMembers.filter(m => 
    m.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
    m.email.toLowerCase().includes(searchQuery.toLowerCase()) ||
    m.department.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // ── Loading State ──
  if (isLoading) {
    return (
      <div className="flex flex-col gap-6 relative w-full pb-10">
        {/* Header skeleton */}
        <div className="flex items-center justify-between">
          <div>
            <Skeleton className="h-7 w-32 mb-2" />
            <Skeleton className="h-4 w-64" />
          </div>
          <Skeleton className="h-10 w-36 rounded-xl" />
        </div>

        {/* Stats row skeleton */}
        <div className="grid grid-cols-3 gap-4">
          {[0, 1, 2].map(i => (
            <Card key={i} className="p-5 flex flex-col justify-between border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white">
              <Skeleton className="h-3 w-28 mb-3" />
              <Skeleton className="h-8 w-16" />
            </Card>
          ))}
        </div>

        {/* Table skeleton */}
        <Card className="flex flex-col border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white rounded-2xl overflow-hidden">
          <div className="flex items-center justify-between p-5 border-b border-[#F0F2F5]">
            <Skeleton className="h-5 w-28" />
            <Skeleton className="h-9 w-60 rounded-xl" />
          </div>
          <div className="p-5 flex flex-col gap-4">
            {[0, 1, 2, 3, 4, 5].map(i => (
              <div key={i} className="flex items-center gap-4">
                <Skeleton className="w-10 h-10 rounded-full" />
                <Skeleton className="h-4 w-32" />
                <Skeleton className="h-4 w-24 ml-auto" />
                <Skeleton className="h-4 w-16" />
                <Skeleton className="h-4 w-20" />
              </div>
            ))}
          </div>
        </Card>
      </div>
    );
  }

  // ── Error State ──
  if (error) {
    return (
      <div className="flex flex-col gap-6 relative w-full pb-10">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-[22px] font-bold text-[#1A1A2E] leading-tight mb-1">Team</h1>
            <p className="text-[14px] text-[#64748B]">Manage members and their AI usage permissions</p>
          </div>
        </div>
        <Card className="p-6 border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white rounded-2xl">
          <div className="flex items-center gap-2 text-[#DC2626]">
            <AlertTriangle size={16} />
            <span className="text-sm font-medium">Failed to load team data: {error.message}</span>
          </div>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-6 relative w-full pb-10">
      
      {/* ── Header ── */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-[22px] font-bold text-[#1A1A2E] leading-tight mb-1">Team</h1>
          <p className="text-[14px] text-[#64748B]">Manage members and their AI usage permissions</p>
        </div>
        <button
          onClick={() => setIsInviteOpen(true)}
          className="flex items-center gap-2 bg-[#FF5C1A] text-white px-4 py-2 rounded-xl text-sm font-medium hover:bg-[#E65318] transition-colors"
        >
          <UserPlus size={16} />
          + Invite Member
        </button>
      </div>

      {/* ── Stats Row ── */}
      <div className="grid grid-cols-3 gap-4">
        <Card className="p-5 flex flex-col justify-between border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-[#FFF3EE]">
          <span className="text-xs font-bold tracking-wider text-[#FF5C1A] mb-3">TOTAL MEMBERS</span>
          <div className="flex items-end justify-between">
            <span className="text-3xl font-bold text-[#1A1A2E] leading-none">{teamMembers.length}</span>
            {data?.invites && data.invites.filter(inv => inv.status === "pending").length > 0 && (
              <span className="text-sm font-medium text-[#64748B] flex items-center gap-1">
                {data.invites.filter(inv => inv.status === "pending").length} pending invite{data.invites.filter(inv => inv.status === "pending").length !== 1 ? "s" : ""}
              </span>
            )}
          </div>
        </Card>
        
        <Card className="p-5 flex flex-col justify-between border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white">
          <span className="text-xs font-bold tracking-wider text-[#94A3B8] mb-3">POWER USERS</span>
          <div className="flex items-end justify-between">
            <span className="text-3xl font-bold text-[#C0C8D4] leading-none">—</span>
            <span className="text-sm text-[#64748B] flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-[#E2E8F0]" /> No data available
            </span>
          </div>
        </Card>

        <Card className="p-5 flex flex-col justify-between border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white">
          <span className="text-xs font-bold tracking-wider text-[#94A3B8] mb-3">ZERO USAGE</span>
          <div className="flex items-end justify-between">
            <span className="text-3xl font-bold text-[#C0C8D4] leading-none">—</span>
            <span className="text-sm text-[#64748B] flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-[#E2E8F0]" /> No data available
            </span>
          </div>
        </Card>
      </div>

      {/* ── Table Container ── */}
      <Card className="flex flex-col border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white rounded-2xl overflow-hidden">
        
        {/* Table Header Row */}
        <div className="flex items-center justify-between p-5 border-b border-[#F0F2F5]">
          <h2 className="text-base font-semibold text-[#1A1A2E]">All Members</h2>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-[#94A3B8]" size={16} />
            <input 
              type="text" 
              placeholder="Search members..." 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9 pr-4 py-2 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors w-[240px]"
            />
          </div>
        </div>

        {/* Table */}
        <div className="overflow-x-auto">
          {teamMembers.length === 0 ? (
            <div className="flex flex-col items-center justify-center py-16 text-center">
              <User size={32} className="text-[#C0C8D4] mb-3" />
              <p className="text-[15px] font-medium text-[#64748B]">No team members yet</p>
              <p className="text-[13px] text-[#94A3B8] mt-1">Invite your first team member to get started</p>
            </div>
          ) : (
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-[#F0F2F5]">
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">MEMBER</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">DEPARTMENT</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">ROLE</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">AI TOOLS USED</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">RISK LEVEL</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8]">LAST ACTIVE</th>
                  <th className="px-5 py-3 text-xs font-semibold tracking-wider text-[#94A3B8] text-right">ACTIONS</th>
                </tr>
              </thead>
              <tbody>
                {filteredMembers.map((m, idx) => {
                  const conf = riskConf[m.risk];
                  const isLast = idx === filteredMembers.length - 1;
                  return (
                    <tr 
                      key={m.id} 
                      onClick={() => setSelectedMember(m)}
                      className="group hover:bg-[#F8FAFC] cursor-pointer transition-colors"
                      style={{ borderBottom: isLast ? "none" : "1px solid #F0F2F5" }}
                    >
                      <td className="px-5 py-3">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 rounded-full bg-[#FF5C1A] text-white flex items-center justify-center font-bold text-sm shrink-0">
                            {m.initials}
                          </div>
                          <div className="flex flex-col">
                            <span className="font-bold text-[14px] text-[#1A1A2E] leading-tight">{m.name}</span>
                            <span className="text-[12px] text-[#94A3B8] leading-tight mt-0.5">{m.email}</span>
                          </div>
                        </div>
                      </td>
                      <td className="px-5 py-3 text-[14px] text-[#1A1A2E]">{m.department}</td>
                      <td className="px-5 py-3 text-[14px] text-[#1A1A2E]">{m.role}</td>
                      <td className="px-5 py-3 text-[14px] text-[#C0C8D4] font-medium">—</td>
                      <td className="px-5 py-3">
                        <span className="text-[#C0C8D4] font-medium">—</span>
                      </td>
                      <td className="px-5 py-3 text-[13px] text-[#64748B]">{m.lastActive}</td>
                      <td className="px-5 py-3 text-right">
                        <div className="relative inline-block" onClick={e => e.stopPropagation()}>
                          <button 
                            onClick={() => setOpenMenu(openMenu === m.id ? null : m.id)}
                            className="p-1.5 rounded-lg text-[#94A3B8] hover:text-[#1A1A2E] hover:bg-[#F0F2F5] transition-colors"
                          >
                            <MoreHorizontal size={18} />
                          </button>
                          {openMenu === m.id && (
                            <>
                              <div className="fixed inset-0 z-10" onClick={() => setOpenMenu(null)} />
                              <div className="absolute right-0 mt-1 w-48 bg-white border border-[#F0F2F5] shadow-[0_12px_24px_rgba(0,0,0,0.12)] rounded-xl py-1 z-20 text-left">
                                <button className="w-full px-4 py-2 text-sm text-[#1A1A2E] hover:bg-[#F8FAFC] text-left">View Usage Report</button>
                                <button className="w-full px-4 py-2 text-sm text-[#1A1A2E] hover:bg-[#F8FAFC] text-left">Edit Role</button>
                                <button className="w-full px-4 py-2 text-sm text-[#1A1A2E] hover:bg-[#F8FAFC] text-left">Suspend Access</button>
                                <button className="w-full px-4 py-2 text-sm text-[#DC2626] hover:bg-[#FEF2F2] text-left">Remove Member</button>
                              </div>
                            </>
                          )}
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          )}
        </div>
      </Card>

      {/* ── Bottom Section Options ── */}
      <div className="grid grid-cols-2 gap-4">
        {/* Left: Department Breakdown */}
        <Card className="p-5 border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white rounded-2xl flex flex-col">
          <h3 className="text-[16px] font-semibold text-[#1A1A2E] mb-6">Department Breakdown</h3>
          <div className="flex-1 w-full" style={{ minHeight: 250 }}>
            {deptData.length === 0 ? (
              <div className="flex items-center justify-center h-full text-[#94A3B8] text-sm">
                No department data available
              </div>
            ) : (
              <ResponsiveContainer width="100%" height="100%">
                <BarChart layout="vertical" data={deptData} margin={{ top: 0, right: 30, left: 0, bottom: 0 }}>
                  <XAxis type="number" hide />
                  <YAxis dataKey="name" type="category" axisLine={false} tickLine={false} tick={{ fill: "#64748B", fontSize: 13 }} width={90} />
                  <RechartsTooltip cursor={{ fill: "#F8FAFC" }} contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                  <Bar dataKey="members" radius={[0, 4, 4, 0]} barSize={20}>
                    {deptData.map((d, i) => (
                      <Cell key={`cell-${i}`} fill={i === 0 ? "#FF5C1A" : "#E2E8F0"} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            )}
          </div>
        </Card>

        {/* Right: AI Adoption Rate */}
        <Card className="p-5 border-none shadow-[0_2px_12px_rgba(0,0,0,0.04)] bg-white rounded-2xl flex flex-col relative">
          <h3 className="text-[16px] font-semibold text-[#1A1A2E] mb-4">AI Adoption Rate</h3>
          <div className="flex-1 w-full flex items-center justify-center relative" style={{ minHeight: 250 }}>
            <div className="flex flex-col items-center justify-center text-center">
              <span className="text-3xl font-bold text-[#C0C8D4] leading-none mb-1">—</span>
              <span className="text-xs text-[#94A3B8]">adoption data not available</span>
            </div>
          </div>
        </Card>
      </div>

      {/* ── Modals & Slide-overs ── */}
      <InviteMemberModal isOpen={isInviteOpen} onClose={() => setIsInviteOpen(false)} />
      <MemberDetailPanel member={selectedMember} onClose={() => setSelectedMember(null)} />

    </div>
  );
}

// ─── INVITE MEMBER MODAL ────────────────────────────────────────────────────

function InviteMemberModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  const { toast } = useToast();
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("member");
  const [isSubmitting, setIsSubmitting] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      await inviteTeamMember(email, role);
      toast({
        title: `Invite sent to ${email}`,
        description: "They will receive an email with instructions to join.",
        duration: 3000,
      });
      setEmail("");
      setRole("member");
      onClose();
    } catch (err: any) {
      toast({
        title: "Failed to send invite",
        description: err?.message || "Something went wrong. Please try again.",
        duration: 4000,
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black/40 backdrop-blur-sm" onClick={onClose} />
      <div className="relative bg-white rounded-2xl w-[480px] p-6 shadow-[0_24px_64px_rgba(0,0,0,0.15)] animate-in fade-in zoom-in-95 duration-200">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold text-[#1A1A2E]">Invite Team Member</h2>
          <button onClick={onClose} className="p-2 text-[#94A3B8] hover:text-[#1A1A2E] hover:bg-[#F0F2F5] rounded-lg transition-colors">
            <X size={20} className="active:scale-95 transition-transform" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-5">
          <div className="flex flex-col gap-1.5">
            <label className="text-sm font-semibold text-[#1A1A2E]">Email address</label>
            <input 
              required
              type="email" 
              placeholder="e.g. colleague@devise.ai" 
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors"
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <label className="text-sm font-semibold text-[#1A1A2E]">Department</label>
            <div className="relative">
              <ChevronDown className="absolute right-4 top-1/2 -translate-y-1/2 text-[#94A3B8] pointer-events-none" size={16} />
              <select className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm appearance-none focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors">
                <option>Engineering</option>
                <option>Design</option>
                <option>Product</option>
                <option>Marketing</option>
                <option>Finance</option>
                <option>HR</option>
              </select>
            </div>
          </div>

          <div className="flex flex-col gap-1.5">
            <label className="text-sm font-semibold text-[#1A1A2E]">Role</label>
            <div className="relative">
              <ChevronDown className="absolute right-4 top-1/2 -translate-y-1/2 text-[#94A3B8] pointer-events-none" size={16} />
              <select 
                value={role}
                onChange={e => setRole(e.target.value)}
                className="w-full px-4 py-2.5 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl text-sm appearance-none focus:outline-none focus:border-[#FF5C1A] focus:bg-white transition-colors"
              >
                <option value="member">Member</option>
                <option value="admin">Admin</option>
                <option value="viewer">Viewer</option>
              </select>
            </div>
          </div>

          <div className="flex items-center justify-end gap-3 mt-4 pt-4 border-t border-[#F0F2F5]">
            <button 
              type="button" 
              onClick={onClose}
              className="px-5 py-2.5 text-sm font-semibold text-[#64748B] hover:text-[#1A1A2E] hover:bg-[#F8FAFC] rounded-xl transition-colors"
            >
              Cancel
            </button>
            <button 
              type="submit"
              disabled={isSubmitting}
              className="px-5 py-2.5 text-sm font-semibold text-white bg-[#FF5C1A] hover:bg-[#E65318] hover:translate-y-[-1px] active:scale-[0.98] rounded-xl transition-all shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting ? "Sending..." : "Send Invite"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

// ─── MEMBER DETAIL PANEL (SLIDE-OVER) ───────────────────────────────────────

function MemberDetailPanel({ member, onClose }: { member: TeamMember | null; onClose: () => void }) {
  if (!member) return null;

  return (
    <div className="fixed inset-0 z-50">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/30 backdrop-blur-sm animate-in fade-in duration-300" 
        onClick={onClose} 
      />
      
      {/* Panel */}
      <div 
        className="absolute top-0 right-0 h-full w-[480px] bg-white border-l border-[#F0F2F5] shadow-2xl flex flex-col animate-in slide-in-from-right duration-300"
      >
        {/* Top Header Section */}
        <div className="flex flex-col items-center justify-center p-8 border-b border-[#F0F2F5] relative bg-[#FAFAFA]">
          <button 
            onClick={onClose} 
            className="absolute top-4 right-4 p-2 text-[#94A3B8] hover:text-[#1A1A2E] hover:bg-[#F0F2F5] rounded-lg transition-colors"
          >
            <X size={20} className="active:scale-95 transition-transform" />
          </button>
          
          <div className="w-16 h-16 rounded-full bg-[#FF5C1A] text-white flex items-center justify-center font-bold text-2xl shadow-md mb-4">
            {member.initials}
          </div>
          
          <h2 className="text-xl font-bold text-[#1A1A2E] leading-tight mb-1">{member.name}</h2>
          <p className="text-sm text-[#94A3B8] mb-3">{member.email}</p>
          
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 bg-white border border-[#E2E8F0] rounded-full text-[13px] font-medium text-[#1A1A2E] shadow-sm">
              {member.department}
            </span>
            <span className="px-3 py-1 bg-[#FFF3EE] border border-[#FDDCC8] rounded-full text-[13px] font-semibold text-[#FF5C1A] shadow-sm">
              {member.role}
            </span>
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-8">
          
          {/* AI Usage Summary */}
          <section>
            <h3 className="text-[13px] font-bold tracking-wider text-[#94A3B8] mb-4">AI USAGE SUMMARY</h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="p-4 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl flex flex-col justify-center">
                <span className="text-xs text-[#64748B] mb-1">Total events this month</span>
                <span className="text-xl font-bold text-[#C0C8D4]">—</span>
              </div>
              <div className="p-4 bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl flex flex-col justify-center">
                <span className="text-xs text-[#64748B] mb-1">Most used tool</span>
                <span className="text-[15px] font-bold text-[#C0C8D4]">—</span>
              </div>
            </div>
            
            <div className="mt-4 p-4 border border-[#E2E8F0] rounded-xl flex flex-col gap-2">
              <div className="flex items-center justify-between">
                <span className="text-sm font-semibold text-[#1A1A2E]">Risk Score</span>
                <span className="text-sm font-bold text-[#C0C8D4]">—</span>
              </div>
              <div className="w-full h-2 rounded-full bg-[#F0F2F5] overflow-hidden">
                <div className="h-full bg-[#E2E8F0]" style={{ width: '0%' }} />
              </div>
            </div>
          </section>

          {/* Top Tools Used */}
          <section>
            <h3 className="text-[13px] font-bold tracking-wider text-[#94A3B8] mb-4">TOP TOOLS USED</h3>
            <div className="flex flex-col items-center justify-center py-6 text-center">
              <span className="text-sm text-[#94A3B8]">No tool usage data available</span>
            </div>
          </section>

          {/* Recent Activity */}
          <section>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-[13px] font-bold tracking-wider text-[#94A3B8]">RECENT ACTIVITY</h3>
            </div>
            <div className="flex flex-col items-center justify-center py-6 text-center">
              <span className="text-sm text-[#94A3B8]">No recent activity data available</span>
            </div>
          </section>

          {/* Permissions (Toggles) */}
          <section className="mb-8">
            <h3 className="text-[13px] font-bold tracking-wider text-[#94A3B8] mb-4">PERMISSIONS</h3>
            <div className="flex flex-col gap-0 border border-[#E2E8F0] rounded-xl overflow-hidden bg-[#FAFAFA]">
              
              <PermissionToggle label="Can use approved tools" defaultOn={true} />
              <PermissionToggle label="Can request new tools" defaultOn={true} />
              <PermissionToggle label="Receives alert notifications" defaultOn={false} />
              <PermissionToggle label="Admin access" defaultOn={member.role === "Admin"} isLast />

            </div>
          </section>

        </div>
      </div>
    </div>
  );
}

// ─── HELPER: PERMISSION TOGGLE ──────────────────────────────────────────────

function PermissionToggle({ label, defaultOn, isLast }: { label: string; defaultOn: boolean; isLast?: boolean }) {
  const [isOn, setIsOn] = useState(defaultOn);
  return (
    <div className="flex items-center justify-between p-4 bg-white" style={{ borderBottom: isLast ? 'none' : '1px solid #F0F2F5' }}>
      <span className="text-[14px] font-medium text-[#1A1A2E]">{label}</span>
      <button 
        onClick={() => setIsOn(!isOn)}
        className="relative w-11 h-6 rounded-full transition-colors duration-200 ease-in-out cursor-pointer shadow-inner"
        style={{ backgroundColor: isOn ? '#16A34A' : '#E2E8F0' }}
      >
        <span 
          className="absolute left-[2px] top-[2px] w-[20px] h-[20px] bg-white rounded-full shadow transition-transform duration-200 ease-in-out"
          style={{ transform: isOn ? 'translateX(20px)' : 'translateX(0)' }}
        />
      </button>
    </div>
  );
}
```

### devise-iris/frontend\src\components\dashboard\UsageTrendChart.tsx

```tsx
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";
import { useAnalytics } from "@/hooks/useDashboard";
import { Skeleton } from "@/components/ui/skeleton";
import { useMemo } from "react";

// Custom tooltip
function CustomTooltip({ active, payload, label }: any) {
  if (!active || !payload?.length) return null;
  return (
    <div
      style={{
        backgroundColor: "#1A1A2E",
        borderRadius: 10,
        padding: "8px 14px",
        fontSize: 12,
        color: "#fff",
        boxShadow: "0 4px 16px rgba(0,0,0,0.18)",
      }}
    >
      <p style={{ fontWeight: 700, marginBottom: 4 }}>{label}</p>
      {payload.map((p: any) => (
        <p key={p.name} style={{ color: p.name === "detections" ? "#FF5C1A" : "#94A3B8" }}>
          {p.name === "detections" ? "Detections" : "Violations"}: {p.value}
        </p>
      ))}
    </div>
  );
}

export function UsageTrendChart() {
  const { data: analytics, isLoading, error } = useAnalytics();

  const chartData = useMemo(() => {
    if (!analytics?.overTime?.length) return [];
    return analytics.overTime.map((entry) => ({
      month: entry.time,
      detections: entry.count,
      violations: Math.round(entry.count * 0.4),
    }));
  }, [analytics]);

  return (
    <div
      className="flex-1 min-w-0 flex flex-col"
      style={{
        backgroundColor: "#ffffff",
        border: "1px solid #F0F2F5",
        borderRadius: 16,
        padding: 24,
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      }}
    >
      {/* Header row */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <p
            className="font-semibold"
            style={{ fontSize: 16, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
          >
            AI Usage Trend
          </p>
          <p style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>
            Detection volume over last 8 weeks
          </p>
        </div>

        {/* Legend */}
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-1.5">
            <span
              className="rounded-full"
              style={{ width: 9, height: 9, backgroundColor: "#FF5C1A", display: "inline-block" }}
            />
            <span style={{ fontSize: 12, color: "#64748B" }}>Detections</span>
          </div>
          <div className="flex items-center gap-1.5">
            <span
              className="rounded-full"
              style={{ width: 9, height: 9, backgroundColor: "#1A1A2E", display: "inline-block" }}
            />
            <span style={{ fontSize: 12, color: "#64748B" }}>Violations</span>
          </div>
        </div>
      </div>

      {/* Chart */}
      <div style={{ flex: 1 }}>
        {isLoading ? (
          <div className="flex flex-col gap-3" style={{ height: 200, justifyContent: "flex-end" }}>
            <div className="flex items-end gap-4 px-4" style={{ height: 170 }}>
              {Array.from({ length: 8 }).map((_, i) => (
                <div key={i} className="flex gap-1 items-end flex-1">
                  <Skeleton className="flex-1" style={{ height: 40 + Math.random() * 100 }} />
                  <Skeleton className="flex-1" style={{ height: 20 + Math.random() * 50 }} />
                </div>
              ))}
            </div>
            <Skeleton className="w-full" style={{ height: 14 }} />
          </div>
        ) : error ? (
          <div className="flex items-center justify-center" style={{ height: 200 }}>
            <p style={{ fontSize: 13, color: "#DC2626" }}>
              Failed to load analytics data
            </p>
          </div>
        ) : chartData.length === 0 ? (
          <div className="flex items-center justify-center" style={{ height: 200 }}>
            <p style={{ fontSize: 13, color: "#94A3B8" }}>
              No data yet
            </p>
          </div>
        ) : (
          <ResponsiveContainer width="100%" height={200}>
            <BarChart
              data={chartData}
              barCategoryGap="28%"
              barGap={4}
              margin={{ top: 4, right: 4, left: -24, bottom: 0 }}
            >
              <defs>
                {/* Diagonal hatch pattern for violations bars */}
                <pattern
                  id="hatch"
                  patternUnits="userSpaceOnUse"
                  width="5"
                  height="5"
                  patternTransform="rotate(45)"
                >
                  <rect width="5" height="5" fill="#1A1A2E" />
                  <line
                    x1="0"
                    y1="0"
                    x2="0"
                    y2="5"
                    stroke="#ffffff"
                    strokeWidth="2"
                    strokeOpacity="0.18"
                  />
                </pattern>
              </defs>

              <XAxis
                dataKey="month"
                axisLine={{ stroke: "#E2E8F0" }}
                tickLine={false}
                tick={{ fontSize: 12, fill: "#94A3B8", fontFamily: "Inter, sans-serif" }}
              />
              <YAxis
                axisLine={false}
                tickLine={false}
                tick={{ fontSize: 11, fill: "#CBD5E1", fontFamily: "Inter, sans-serif" }}
              />
              <Tooltip
                content={<CustomTooltip />}
                cursor={{ fill: "rgba(0,0,0,0.03)", radius: 4 }}
              />

              {/* Detections — solid orange */}
              <Bar
                dataKey="detections"
                radius={[5, 5, 0, 0]}
                fill="#FF5C1A"
                maxBarSize={22}
              />

              {/* Violations — hatched dark */}
              <Bar
                dataKey="violations"
                radius={[5, 5, 0, 0]}
                maxBarSize={22}
              >
                {chartData.map((_, i) => (
                  <Cell key={i} fill="url(#hatch)" />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\landing\DashboardMockups.tsx

```tsx
import { Shield, BarChart2, DollarSign, LayoutGrid, Settings, Search, User } from "lucide-react";

export const HeroDashboard = () => (
  <div className="w-full h-full bg-white flex text-[10px] md:text-xs">
    <div className="w-1/4 border-r border-gray-100 p-4 flex flex-col gap-3">
      <div className="flex items-center gap-2 mb-4">
        <div className="w-5 h-5 bg-brand-orange rounded flex items-center justify-center">
          <LayoutGrid size={12} className="text-white" />
        </div>
        <span className="font-bold text-brand-dark">Devise</span>
      </div>
      {[
        { icon: <LayoutGrid size={14} />, label: "Dashboard", active: true },
        { icon: <Shield size={14} />, label: "Oversight" },
        { icon: <BarChart2 size={14} />, label: "Pulse" },
        { icon: <DollarSign size={14} />, label: "Spend" },
        { icon: <Settings size={14} />, label: "Settings" },
      ].map((item) => (
        <div key={item.label} className={`flex items-center gap-2 p-2 rounded-lg ${item.active ? "bg-orange-50 text-brand-orange" : "text-brand-gray"}`}>
          {item.icon} <span className="font-medium">{item.label}</span>
        </div>
      ))}
    </div>
    <div className="flex-1 bg-gray-50 p-4 md:p-6">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-sm font-bold text-brand-dark">AI Tool Activity</h3>
        <div className="hidden md:flex gap-2">
          <div className="bg-white border border-gray-200 rounded px-2 py-1 flex items-center gap-2 text-gray-400">
            <Search size={10} /> Search...
          </div>
          <div className="bg-white border border-gray-200 rounded px-2 py-1">Status: All</div>
        </div>
      </div>
      <div className="bg-white rounded-xl shadow-soft overflow-hidden">
        <table className="w-full text-left">
          <thead className="bg-gray-50 border-b border-gray-100">
            <tr>
              <th className="p-3 font-semibold text-brand-gray">Tool Name</th>
              <th className="p-3 font-semibold text-brand-gray hidden md:table-cell">Users</th>
              <th className="p-3 font-semibold text-brand-gray">Risk</th>
              <th className="p-3 font-semibold text-brand-gray">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-50">
            {[
              { name: "ChatGPT", users: 47, risk: "HIGH", status: "Blocked", riskColor: "text-red-500 bg-red-50", statusColor: "text-red-500 bg-red-50" },
              { name: "Claude", users: 23, risk: "LOW", status: "Active", riskColor: "text-green-500 bg-green-50", statusColor: "text-green-500 bg-green-50" },
              { name: "Copilot", users: 89, risk: "LOW", status: "Active", riskColor: "text-green-500 bg-green-50", statusColor: "text-green-500 bg-green-50" },
              { name: "Cursor", users: 12, risk: "MED", status: "Monitor", riskColor: "text-orange-500 bg-orange-50", statusColor: "text-orange-500 bg-orange-50" },
              { name: "Midjourney", users: 8, risk: "MED", status: "Monitor", riskColor: "text-orange-500 bg-orange-50", statusColor: "text-orange-500 bg-orange-50" },
            ].map((row) => (
              <tr key={row.name}>
                <td className="p-3 font-bold text-brand-dark">{row.name}</td>
                <td className="p-3 text-brand-gray hidden md:table-cell">{row.users}</td>
                <td className="p-3"><span className={`px-2 py-0.5 rounded-full text-[8px] font-bold ${row.riskColor}`}>{row.risk}</span></td>
                <td className="p-3"><span className={`px-2 py-0.5 rounded-full text-[8px] font-bold ${row.statusColor}`}>{row.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  </div>
);

export const OversightMockup = () => (
  <div className="p-6 bg-white h-full">
    <div className="flex justify-between items-start mb-6">
      <div>
        <h4 className="text-xs font-bold text-brand-dark mb-1">Violations Feed</h4>
        <p className="text-[10px] text-brand-gray">Real-time policy enforcement</p>
      </div>
      <div className="w-12 h-12 rounded-full border-4 border-red-500 border-t-gray-200 flex items-center justify-center text-[10px] font-bold text-brand-dark">84%</div>
    </div>
    <div className="space-y-3">
      {[
        { user: "Ankit S.", tool: "ChatGPT", type: "SENSITIVE DATA", time: "2m ago" },
        { user: "Sarah L.", tool: "Midjourney", type: "UNAUTHORIZED", time: "14m ago" },
        { user: "James K.", tool: "DeepL", type: "DATA LEAK", time: "1h ago" },
      ].map((v, i) => (
        <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
          <div className="flex items-center gap-3">
            <div className="w-6 h-6 rounded-full bg-gray-200 flex items-center justify-center">
              <User size={12} />
            </div>
            <div>
              <div className="font-bold text-[10px] text-brand-dark">{v.user}</div>
              <div className="text-[8px] text-brand-gray">{v.tool} · {v.time}</div>
            </div>
          </div>
          <span className="bg-red-100 text-red-600 px-2 py-0.5 rounded text-[8px] font-black">{v.type}</span>
        </div>
      ))}
    </div>
  </div>
);

export const PulseMockup = () => (
  <div className="p-6 bg-white h-full">
    <div className="flex justify-between items-start mb-6">
      <div>
        <h4 className="text-xs font-bold text-brand-dark mb-1">AI Adoption</h4>
        <p className="text-[10px] text-brand-gray">Behavioral analytics</p>
      </div>
      <div className="w-12 h-12 rounded-full border-4 border-brand-purple border-t-gray-200 flex items-center justify-center text-[10px] font-bold text-brand-dark">73%</div>
    </div>
    <div className="space-y-3 mb-4">
      <div className="text-[10px] font-bold text-brand-dark mb-2">Top Tools by Usage</div>
      {[
        { tool: "Code Assistant", pct: 43, color: "bg-brand-purple" },
        { tool: "Writing", pct: 31, color: "bg-pink-500" },
        { tool: "Image Gen", pct: 18, color: "bg-brand-orange" },
      ].map((t) => (
        <div key={t.tool} className="flex items-center gap-2">
          <span className="text-[9px] text-brand-gray w-20">{t.tool}</span>
          <div className="flex-1 h-2 bg-gray-100 rounded-full overflow-hidden">
            <div className={`h-full ${t.color} rounded-full`} style={{ width: `${t.pct}%` }} />
          </div>
          <span className="text-[9px] font-bold text-brand-dark">{t.pct}%</span>
        </div>
      ))}
    </div>
    <div className="text-[10px] font-bold text-brand-dark mb-2">Team Leaderboard</div>
    {[
      { team: "Engineering", rate: "89%" },
      { team: "Product", rate: "72%" },
      { team: "Marketing", rate: "45%" },
    ].map((t) => (
      <div key={t.team} className="flex justify-between py-1.5 border-b border-gray-50 text-[10px]">
        <span className="text-brand-dark font-medium">{t.team}</span>
        <span className="text-brand-purple font-bold">{t.rate}</span>
      </div>
    ))}
  </div>
);

export const SpendMockup = () => (
  <div className="p-6 bg-white h-full">
    <div className="flex justify-between items-start mb-6">
      <div>
        <h4 className="text-xs font-bold text-brand-dark mb-1">Spend Overview</h4>
        <p className="text-[10px] text-brand-gray">Subscription intelligence</p>
      </div>
      <div className="text-right">
        <div className="text-lg font-bold text-brand-dark">$2,182</div>
        <div className="text-[8px] text-brand-gray">Monthly Spend</div>
      </div>
    </div>
    <div className="bg-white rounded-lg overflow-hidden">
      <table className="w-full text-[9px]">
        <thead>
          <tr className="border-b border-gray-100">
            <th className="text-left p-2 text-brand-gray font-semibold">Tool</th>
            <th className="text-left p-2 text-brand-gray font-semibold">Used</th>
            <th className="text-left p-2 text-brand-gray font-semibold">Status</th>
          </tr>
        </thead>
        <tbody>
          {[
            { tool: "Copilot", used: "67/200", status: "Zombie", zombie: true },
            { tool: "ChatGPT", used: "45/50", status: "Active", zombie: false },
            { tool: "Jasper", used: "3/25", status: "Zombie", zombie: true },
            { tool: "Notion AI", used: "89/100", status: "Active", zombie: false },
          ].map((r) => (
            <tr key={r.tool} className="border-b border-gray-50">
              <td className="p-2 font-bold text-brand-dark">{r.tool}</td>
              <td className="p-2 text-brand-gray">{r.used}</td>
              <td className="p-2">
                <span className={`px-1.5 py-0.5 rounded text-[7px] font-bold ${r.zombie ? "bg-red-50 text-red-500" : "bg-green-50 text-green-500"}`}>
                  {r.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);
```

### devise-iris/frontend\src\components\landing\Footer.tsx

```tsx
import { Link } from "react-router-dom";
import { Grid2x2 } from "lucide-react";

export const Footer = () => {
  return (
    <footer className="bg-brand-navy text-white py-20 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-5 gap-12 mb-16">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center mb-6">
              <div className="w-8 h-8 bg-brand-orange rounded-lg flex items-center justify-center">
                <Grid2x2 className="text-white w-5 h-5" />
              </div>
              <span className="ml-2 text-xl font-bold text-white">Devise</span>
            </div>
            <p className="text-gray-400 max-w-xs text-balance">
              See, understand, and govern enterprise AI. The system of record for the AI-first organization.
            </p>
          </div>

          <div>
            <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-orange">Product</h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li><Link to="/product/oversight" className="hover:text-white transition-colors">Oversight</Link></li>
              <li><Link to="/product/pulse" className="hover:text-white transition-colors">Pulse</Link></li>
              <li><Link to="/product/spend" className="hover:text-white transition-colors">Spend</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-orange">Use Cases</h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li><Link to="/use-cases" className="hover:text-white transition-colors">Adoption Scoreboard</Link></li>
              <li><Link to="/use-cases" className="hover:text-white transition-colors">Confidential Data Risks</Link></li>
              <li><Link to="/use-cases" className="hover:text-white transition-colors">Did Your Deployment Work?</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-orange">Company</h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li><Link to="/about" className="hover:text-white transition-colors">About</Link></li>
              <li><Link to="/login" className="hover:text-white transition-colors">Sign in</Link></li>
              <li><Link to="/signup" className="hover:text-white transition-colors">Create account</Link></li>
              <li><span className="hover:text-white transition-colors cursor-pointer">Security</span></li>
              <li><span className="hover:text-white transition-colors cursor-pointer">Careers</span></li>
              <li><span className="hover:text-white transition-colors cursor-pointer">Contact</span></li>
            </ul>
          </div>
        </div>

        <div className="pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-500">
          <div>© 2025 Devise, Inc. · SOC 2 · GDPR</div>
          <div className="flex gap-6">
            <span className="hover:text-white cursor-pointer">Terms</span>
            <span className="hover:text-white cursor-pointer">Privacy</span>
            <span className="hover:text-white cursor-pointer">Cookies</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
```

### devise-iris/frontend\src\components\landing\Layout.tsx

```tsx
import { ReactNode } from "react";
import { Navbar } from "./Navbar";
import { Footer } from "./Footer";

interface LayoutProps {
  children: ReactNode;
}

export const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="min-h-screen bg-brand-cream font-sans selection:bg-brand-orange/20 selection:text-brand-orange">
      <Navbar />
      <main>{children}</main>
      <Footer />
    </div>
  );
};
```

### devise-iris/frontend\src\components\landing\Navbar.tsx

```tsx
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import * as DropdownMenu from "@radix-ui/react-dropdown-menu";
import * as Dialog from "@radix-ui/react-dialog";
import {
  Grid2x2, Shield, BarChart2, DollarSign, LayoutGrid,
  TrendingUp, AlertTriangle, Menu, X, ChevronDown, Mail,
  BookOpen, FileText, Calendar, GitCompare, HelpCircle,
  Building, Lock, Briefcase, Phone, Users
} from "lucide-react";

export const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    // Only trigger scroll effect after 10px
    const handleScroll = () => setIsScrolled(window.scrollY > 10);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div className="fixed top-0 left-0 right-0 z-50">
      <nav 
        className={`transition-all duration-200 ${
          isScrolled ? "bg-white shadow-sm backdrop-blur-sm py-3" : "bg-transparent py-5"
        }`}
      >
        <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
          <Link to="/" className="flex items-center group">
            <div className="w-8 h-8 bg-brand-orange rounded-lg flex items-center justify-center transition-transform group-hover:scale-105">
              <Grid2x2 className="text-white w-5 h-5" />
            </div>
            <span className="ml-2 text-xl font-bold text-brand-dark tracking-tight">Devise</span>
          </Link>

          <div className="hidden md:flex items-center gap-8">
            {/* Product Dropdown */}
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="flex items-center gap-1 text-sm font-medium text-brand-dark hover:text-brand-orange outline-none cursor-pointer">
                Product <ChevronDown size={14} />
              </DropdownMenu.Trigger>
              <DropdownMenu.Portal>
                <DropdownMenu.Content className="bg-white rounded-2xl shadow-heavy p-2 min-w-[320px] mt-2 z-[60] animate-in fade-in slide-in-from-top-2" sideOffset={8}>
                  <DropdownMenu.Item className="outline-none" asChild>
                    <Link to="/product/oversight" className="flex items-start gap-4 p-3 rounded-xl hover:bg-brand-cream transition-colors">
                      <Shield className="text-brand-orange mt-0.5" size={20} />
                      <div>
                        <div className="font-bold text-brand-dark text-sm">Devise Oversight</div>
                        <div className="text-xs text-brand-gray">AI Governance Intelligence</div>
                      </div>
                    </Link>
                  </DropdownMenu.Item>
                  <DropdownMenu.Item className="outline-none" asChild>
                    <Link to="/product/pulse" className="flex items-start gap-4 p-3 rounded-xl hover:bg-brand-cream transition-colors">
                      <BarChart2 className="text-brand-purple mt-0.5" size={20} />
                      <div>
                        <div className="font-bold text-brand-dark text-sm">Devise Pulse</div>
                        <div className="text-xs text-brand-gray">AI Adoption Intelligence</div>
                      </div>
                    </Link>
                  </DropdownMenu.Item>
                  <DropdownMenu.Item className="outline-none" asChild>
                    <Link to="/product/spend" className="flex items-start gap-4 p-3 rounded-xl hover:bg-brand-cream transition-colors">
                      <DollarSign className="text-brand-green mt-0.5" size={20} />
                      <div>
                        <div className="font-bold text-brand-dark text-sm">Devise Spend</div>
                        <div className="text-xs text-brand-gray">AI Cost Intelligence</div>
                      </div>
                    </Link>
                  </DropdownMenu.Item>
                  <div className="h-px bg-gray-100 my-2" />
                  <div className="px-4 py-2 text-[10px] uppercase tracking-widest font-bold text-brand-gray">
                    Coverage: 3,500+ AI tools detected
                  </div>
                </DropdownMenu.Content>
              </DropdownMenu.Portal>
            </DropdownMenu.Root>

            {/* Use Cases Dropdown */}
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="flex items-center gap-1 text-sm font-medium text-brand-dark hover:text-brand-orange outline-none cursor-pointer">
                Use Cases <ChevronDown size={14} />
              </DropdownMenu.Trigger>
              <DropdownMenu.Portal>
                <DropdownMenu.Content className="bg-white rounded-2xl shadow-heavy p-6 min-w-[560px] mt-2 z-[60] animate-in fade-in slide-in-from-top-2" sideOffset={8}>
                  <div className="grid grid-cols-2 gap-8">
                    <div>
                      <div className="text-[10px] uppercase tracking-widest font-bold text-brand-gray mb-4">Featured Use Cases</div>
                      <div className="space-y-1">
                        <DropdownMenu.Item className="outline-none" asChild>
                          <Link to="/use-cases" className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark">
                            <LayoutGrid size={16} className="text-brand-orange" /> Org-wide AI adoption scoreboard
                          </Link>
                        </DropdownMenu.Item>
                        <DropdownMenu.Item className="outline-none" asChild>
                          <Link to="/use-cases" className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark">
                            <TrendingUp size={16} className="text-brand-orange" /> Did your AI deployment actually work?
                          </Link>
                        </DropdownMenu.Item>
                        <DropdownMenu.Item className="outline-none" asChild>
                          <Link to="/use-cases" className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark">
                            <AlertTriangle size={16} className="text-brand-orange" /> Confidential data sent to ChatGPT
                          </Link>
                        </DropdownMenu.Item>
                        <DropdownMenu.Item className="outline-none" asChild>
                          <Link to="/use-cases" className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark">
                            <Shield size={16} className="text-brand-orange" /> Shadow AI spreading unchecked
                          </Link>
                        </DropdownMenu.Item>
                      </div>
                    </div>
                    <div>
                      <div className="text-[10px] uppercase tracking-widest font-bold text-brand-gray mb-4">Browse by Audience</div>
                      <div className="flex flex-wrap gap-2 mb-4">
                        {["C-Suite", "Security", "Finance", "AI Leaders", "IT Admin"].map((pill) => (
                          <Link key={pill} to="/use-cases" className="bg-brand-cream text-brand-dark text-xs font-medium px-3 py-1.5 rounded-full hover:bg-brand-orange hover:text-white transition-colors">
                            {pill}
                          </Link>
                        ))}
                      </div>
                      <Link to="/use-cases" className="text-brand-orange text-sm font-medium hover:underline">
                        Browse the full library →
                      </Link>
                    </div>
                  </div>
                </DropdownMenu.Content>
              </DropdownMenu.Portal>
            </DropdownMenu.Root>

            {/* Resources Dropdown */}
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="flex items-center gap-1 text-sm font-medium text-brand-dark hover:text-brand-orange outline-none cursor-pointer">
                Resources <ChevronDown size={14} />
              </DropdownMenu.Trigger>
              <DropdownMenu.Portal>
                <DropdownMenu.Content className="bg-white rounded-2xl shadow-heavy p-6 min-w-[480px] mt-2 z-[60] animate-in fade-in slide-in-from-top-2" sideOffset={8}>
                  <div className="grid grid-cols-2 gap-8">
                    <div className="space-y-1">
                      {[
                        { icon: <BookOpen size={16} />, label: "Blog" },
                        { icon: <FileText size={16} />, label: "Guides" },
                        { icon: <FileText size={16} />, label: "White Papers" },
                        { icon: <Calendar size={16} />, label: "Events" },
                        { icon: <GitCompare size={16} />, label: "Compare" },
                      ].map((item) => (
                        <DropdownMenu.Item key={item.label} className="outline-none">
                          <span className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark cursor-pointer">
                            <span className="text-brand-gray">{item.icon}</span> {item.label}
                          </span>
                        </DropdownMenu.Item>
                      ))}
                    </div>
                    <div className="bg-brand-cream rounded-xl p-4">
                      <HelpCircle size={20} className="text-brand-orange mb-2" />
                      <div className="font-bold text-brand-dark text-sm mb-1">AI Glossary</div>
                      <div className="text-xs text-brand-gray">100+ terms explained for enterprise teams.</div>
                    </div>
                  </div>
                </DropdownMenu.Content>
              </DropdownMenu.Portal>
            </DropdownMenu.Root>

            {/* Company Dropdown */}
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="flex items-center gap-1 text-sm font-medium text-brand-dark hover:text-brand-orange outline-none cursor-pointer">
                Company <ChevronDown size={14} />
              </DropdownMenu.Trigger>
              <DropdownMenu.Portal>
                <DropdownMenu.Content className="bg-white rounded-2xl shadow-heavy p-6 min-w-[420px] mt-2 z-[60] animate-in fade-in slide-in-from-top-2" sideOffset={8}>
                  <div className="grid grid-cols-2 gap-8">
                    <div className="space-y-1">
                      <DropdownMenu.Item className="outline-none" asChild>
                        <Link to="/about" className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark">
                          <Building size={16} className="text-brand-gray" /> About
                        </Link>
                      </DropdownMenu.Item>
                      {[
                        { icon: <Lock size={16} />, label: "Security" },
                        { icon: <Briefcase size={16} />, label: "Careers" },
                        { icon: <Phone size={16} />, label: "Contact" },
                      ].map((item) => (
                        <DropdownMenu.Item key={item.label} className="outline-none">
                          <span className="flex items-center gap-3 p-2 rounded-lg hover:bg-brand-cream transition-colors text-sm text-brand-dark cursor-pointer">
                            <span className="text-brand-gray">{item.icon}</span> {item.label}
                          </span>
                        </DropdownMenu.Item>
                      ))}
                    </div>
                    <div className="bg-brand-cream rounded-xl p-4">
                      <Mail size={20} className="text-brand-orange mb-2" />
                      <div className="font-bold text-brand-dark text-sm mb-1">Talk to us</div>
                      <div className="text-xs text-brand-gray mb-3">Get in touch with our team.</div>
                      <span className="text-brand-orange text-sm font-medium cursor-pointer hover:underline">Contact sales →</span>
                    </div>
                  </div>
                </DropdownMenu.Content>
              </DropdownMenu.Portal>
            </DropdownMenu.Root>
          </div>

          <div className="flex items-center gap-4">
            <Link to="/login" className="hidden md:inline-flex bg-brand-orange text-white rounded-full text-sm px-5 py-2.5 font-semibold hover:bg-orange-600 transition-all shadow-lg shadow-brand-orange/20">
              Get Started
            </Link>

            {/* Mobile Nav Toggle */}
            <button 
              className="md:hidden p-2 text-brand-dark hover:text-brand-orange transition-colors"
              onClick={() => setMobileOpen(true)}
              aria-label="Open menu"
            >
              <Menu size={24} />
            </button>

            {/* Mobile Overlay Menu */}
            <Dialog.Root open={mobileOpen} onOpenChange={setMobileOpen}>
              <Dialog.Portal>
                <Dialog.Overlay className="fixed inset-0 bg-white/95 backdrop-blur-md z-[100] animate-in fade-in" />
                <Dialog.Content className="fixed inset-0 z-[101] p-6 flex flex-col bg-transparent overflow-y-auto w-full h-full max-h-screen">
                  <div className="flex justify-between items-center mb-8">
                    <div className="flex items-center">
                      <div className="w-8 h-8 bg-brand-orange rounded-lg flex items-center justify-center">
                        <Grid2x2 className="text-white w-5 h-5" />
                      </div>
                      <span className="ml-2 text-xl font-bold text-brand-dark">Devise</span>
                    </div>
                    <button 
                      onClick={() => setMobileOpen(false)}
                      className="p-2 text-brand-gray hover:text-brand-dark bg-gray-100 rounded-full transition-colors h-12 w-12 flex items-center justify-center"
                      aria-label="Close menu"
                    >
                        <X size={24} />
                    </button>
                  </div>
                  
                  <div className="flex flex-col gap-2 text-xl font-semibold text-brand-dark">
                    <Link to="/product/oversight" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>Oversight</Link>
                    <Link to="/product/pulse" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>Pulse</Link>
                    <Link to="/product/spend" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>Spend</Link>
                    <Link to="/use-cases" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>Use Cases</Link>
                    <Link to="/about" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>About</Link>
                    <Link to="/demo" className="py-4 hover:text-brand-orange transition-colors" onClick={() => setMobileOpen(false)}>Book a Demo</Link>
                  </div>
                  
                  <div className="mt-8 pt-8 border-t border-gray-200">
                    <Link to="/login" onClick={() => setMobileOpen(false)} className="flex items-center justify-center w-full bg-brand-orange text-white rounded-full py-4 font-semibold text-lg hover:bg-orange-600 transition-colors">
                      Get Started
                    </Link>
                  </div>
                </Dialog.Content>
              </Dialog.Portal>
            </Dialog.Root>
          </div>
        </div>
      </nav>
    </div>
  );

};
```

### devise-iris/frontend\src\components\landing\OrangeWaveBackground.tsx

```tsx
import React from "react";
import waveBg from "../../assets/image.png";

export const OrangeWaveBackground = () => {
  return (
    <div
      className="absolute inset-0 w-full h-full overflow-hidden pointer-events-none"
      style={{ zIndex: 0 }}
    >
      <img
        src={waveBg}
        alt="Background Graphic"
        className="w-full h-full object-cover object-top opacity-90"
      />
    </div>
  );
};
```

### devise-iris/frontend\src\components\layout\AccountSettingsPanel.tsx

```tsx
import { useState, useEffect } from "react";
import { X, Bell, Shield, Mail, Key, Layout, Check, AlertTriangle, User } from "lucide-react";
import { useAuth } from "@/lib/AuthContext";
import { useMe } from "@/hooks/useDashboard";
import { updateMe } from "@/services/api";
import { auth } from "@/lib/firebase";
import { updateProfile, sendPasswordResetEmail } from "firebase/auth";
import { toast } from "sonner";

interface AccountSettingsPanelProps {
  isOpen: boolean;
  onClose: () => void;
}

export function AccountSettingsPanel({ isOpen, onClose }: AccountSettingsPanelProps) {
  const { user } = useAuth();
  const { data: profile, refetch } = useMe();
  const [isClosing, setIsClosing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [isResettingPassword, setIsResettingPassword] = useState(false);

  const [fullName, setFullName] = useState("");
  const [notificationPrefs, setNotificationPrefs] = useState({
    high_risk_alerts: true,
    daily_summary: false,
    block_notifications: false
  });

  useEffect(() => {
    if (profile) {
      setFullName(profile.full_name || "");
      if (profile.notification_prefs) {
        setNotificationPrefs(profile.notification_prefs);
      }
    }
  }, [profile]);

  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === "Escape") handleClose();
    };
    if (isOpen) document.addEventListener("keydown", handleEsc);
    return () => document.removeEventListener("keydown", handleEsc);
  }, [isOpen]);

  const handleClose = () => {
    setIsClosing(true);
    setTimeout(() => {
      setIsClosing(false);
      onClose();
    }, 200);
  };

  const handleTogglePref = (key: keyof typeof notificationPrefs) => {
    setNotificationPrefs(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const handleSaveSettings = async () => {
    setIsSaving(true);
    try {
      if (fullName && fullName !== profile?.full_name) {
        if (auth.currentUser) {
          await updateProfile(auth.currentUser, { displayName: fullName });
        }
      }
      
      await updateMe({
        full_name: fullName,
        notification_prefs: notificationPrefs
      });
      await refetch();
      toast.success("Settings saved successfully");
    } catch (error) {
      console.error(error);
      toast.error("Failed to save settings");
    } finally {
      setIsSaving(false);
    }
  };

  const handlePasswordReset = async () => {
    if (!user?.email) return;
    setIsResettingPassword(true);
    try {
      await sendPasswordResetEmail(auth, user.email);
      toast.success("Password reset email sent!");
    } catch (error) {
      console.error(error);
      toast.error("Failed to send reset email");
    } finally {
      setIsResettingPassword(false);
    }
  };

  if (!isOpen && !isClosing) return null;

  return (
    <>
      <div 
        className="fixed inset-0 z-50 transition-opacity duration-200"
        style={{ 
          backgroundColor: "rgba(0,0,0,0.4)", 
          backdropFilter: "blur(4px)",
          opacity: isClosing ? 0 : 1 
        }}
        onClick={handleClose}
      />
      
      <div 
        className="fixed top-0 bottom-0 right-0 z-50 bg-white flex flex-col transition-transform duration-200"
        style={{ 
          width: 400, 
          boxShadow: "-12px 0 48px rgba(0,0,0,0.12)",
          transform: isClosing ? "translateX(100%)" : "translateX(0)" 
        }}
      >
        <div className="flex items-center justify-between p-6 border-b border-[#F0F2F5]">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-[#FFF3EE] text-[#FF5C1A]">
              <Shield size={20} />
            </div>
            <h2 style={{ fontSize: 18, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
              Account Settings
            </h2>
          </div>
          <button 
            onClick={handleClose}
            className="p-1 rounded-full transition-colors hover:bg-[#F8FAFC]"
            style={{ color: "#94A3B8" }}
          >
            <X size={20} />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-8">
          
          {/* Profile Section */}
          <section className="flex flex-col gap-4">
            <h3 className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold flex items-center gap-2">
              <User size={14} className="text-[#FF5C1A]" />
              Profile Configuration
            </h3>
            
            <div className="flex flex-col gap-4">
              <div className="flex flex-col gap-1.5">
                <label className="text-[13px] font-medium text-[#64748B]">Display Name</label>
                <input 
                  type="text" 
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  placeholder="Enter your name"
                  className="w-full px-3 py-2 border border-[#E2E8F0] rounded-lg text-sm focus:outline-none focus:border-[#FF5C1A]"
                />
              </div>

              <div className="flex flex-col gap-1.5">
                <label className="text-[13px] font-medium text-[#64748B]">Email Address</label>
                <div className="p-3 bg-[#F8FAFC] border border-[#F0F2F5] rounded-lg flex items-center justify-between">
                  <span className="text-sm text-[#64748B]">{user?.email}</span>
                  <span className="text-[10px] text-[#94A3B8]">Read Only</span>
                </div>
                <p className="text-[11px] text-[#94A3B8]">Contact admin to change your registered email.</p>
              </div>
            </div>
          </section>

          {/* Security Section */}
          <section className="flex flex-col gap-4">
            <h3 className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold flex items-center gap-2">
              <Key size={14} />
              Security & Access
            </h3>
            <div className="p-4 rounded-xl border border-[#F0F2F5] flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-[#1A1A2E]">Update Password</p>
                <p className="text-xs text-[#94A3B8]">Securely reset your account password</p>
              </div>
              <button 
                onClick={handlePasswordReset}
                disabled={isResettingPassword}
                className="px-4 py-2 rounded-lg text-sm font-semibold border border-[#E2E8F0] hover:bg-[#F8FAFC] transition-colors disabled:opacity-50"
              >
                {isResettingPassword ? "Sending..." : "Reset via Email"}
              </button>
            </div>
          </section>

          {/* Notifications Section */}
          <section className="flex flex-col gap-4">
            <h3 className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold flex items-center gap-2">
              <Bell size={14} />
              Notification Preferences
            </h3>
            <div className="flex flex-col gap-1 border border-[#F0F2F5] rounded-xl overflow-hidden text-sm">
              <NotificationToggle 
                label="High-risk Alerts" 
                description="Get instant emails for high-risk tool detections" 
                active={notificationPrefs.high_risk_alerts} 
                onToggle={() => handleTogglePref("high_risk_alerts")} 
              />
              <NotificationToggle 
                label="Daily Summary" 
                description="Receive a daily overview of activity and spend" 
                active={notificationPrefs.daily_summary} 
                onToggle={() => handleTogglePref("daily_summary")} 
              />
              <NotificationToggle 
                label="Block Notifications" 
                description="Alerts when a blocked tool is attempted" 
                active={notificationPrefs.block_notifications} 
                onToggle={() => handleTogglePref("block_notifications")} 
              />
            </div>
          </section>

          {/* Info Section */}
          <div className="p-4 rounded-xl bg-amber-50 border border-amber-100 flex gap-3 text-amber-800">
            <AlertTriangle size={18} className="shrink-0 mt-0.5" />
            <div className="flex flex-col gap-1">
              <p className="text-xs font-bold uppercase tracking-wider">Note on Privacy</p>
              <p className="text-xs leading-relaxed">
                Changes to security settings are logged and may notify the organization administrator for audit purposes.
              </p>
            </div>
          </div>

        </div>

        <div className="p-6 border-t border-[#F0F2F5] flex justify-end gap-3">
          <button 
            onClick={handleClose}
            className="transition-colors hover:bg-[#F8FAFC]"
            style={{ 
              padding: "10px 16px", borderRadius: 8, fontSize: 14, 
              fontWeight: 500, color: "#64748B", fontFamily: "Inter, sans-serif",
              border: "1px solid #E2E8F0"
            }}
          >
            Cancel
          </button>
          <button 
            onClick={handleSaveSettings}
            disabled={isSaving}
            className="transition-all hover:-translate-y-[1px] disabled:opacity-50 disabled:cursor-not-allowed group"
            style={{ 
              backgroundColor: "#FF5C1A", color: "white", padding: "10px 20px", borderRadius: 8, 
              fontSize: 14, fontWeight: 500, fontFamily: "Inter, sans-serif",
              boxShadow: "0 2px 4px rgba(255, 92, 26, 0.2)"
            }}
            onMouseEnter={e => !isSaving && (e.currentTarget.style.backgroundColor = "#E5521A")}
            onMouseLeave={e => !isSaving && (e.currentTarget.style.backgroundColor = "#FF5C1A")}
          >
            <div className="flex items-center gap-2">
              {isSaving ? "Saving..." : "Save Settings"}
              {!isSaving && <Check size={16} className="transition-transform group-hover:scale-110" />}
            </div>
          </button>
        </div>
      </div>
    </>
  );
}

function NotificationToggle({ 
  label, 
  description, 
  active, 
  onToggle 
}: { 
  label: string, 
  description: string, 
  active: boolean, 
  onToggle: () => void 
}) {
  return (
    <div 
      className="flex items-center justify-between p-4 bg-white hover:bg-[#F8FAFC] transition-colors cursor-pointer"
      onClick={onToggle}
    >
      <div className="flex flex-col gap-0.5 pr-4">
        <span className="font-semibold text-[#1A1A2E]">{label}</span>
        <span className="text-xs text-[#94A3B8]">{description}</span>
      </div>
      <div 
        className="relative flex items-center transition-colors duration-200 shrink-0"
        style={{
          width: 40, height: 22, borderRadius: 999,
          backgroundColor: active ? "#FF5C1A" : "#E2E8F0"
        }}
      >
        <div 
          className="absolute bg-white rounded-full transition-all duration-200 shadow-sm"
          style={{
            width: 18, height: 18, top: 2,
            left: active ? 20 : 2
          }}
        />
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\layout\DashboardLayout.tsx

```tsx
import { AppSidebar } from "./Sidebar";
import { TopBar } from "./TopBar";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";

interface DashboardShellProps {
  activeTab: Tab;
  onTabChange: (tab: Tab) => void;
  children?: React.ReactNode;
}

export function DashboardLayout({ activeTab, onTabChange, children }: DashboardShellProps) {
  return (
    /* Outer page — gray background */
    <div
      className="min-h-screen w-full flex items-stretch"
      style={{ backgroundColor: "#F0F2F5", padding: 24 }}
    >
      {/* White card — the entire app container */}
      <div
        className="flex flex-1 overflow-hidden"
        style={{
          backgroundColor: "#ffffff",
          borderRadius: 24,
          boxShadow: "0 8px 40px rgba(0,0,0,0.08)",
          minHeight: "calc(100vh - 48px)",
        }}
      >
        {/* Zone 1 — Left Icon Sidebar */}
        <AppSidebar activeTab={activeTab} onTabChange={onTabChange} />

        {/* Right column: Zone 2 (TopBar) + Zone 3 (Main content) */}
        <div className="flex flex-col flex-1 min-w-0">
          {/* Zone 2 — Top Navigation Bar */}
          <TopBar activeTab={activeTab} onTabChange={onTabChange} />

          {/* Zone 3 — Main Content Area */}
          <main className="flex-1 overflow-auto" style={{ padding: 24 }}>
            {children}
          </main>
        </div>
      </div>
    </div>
  );
}

```

### devise-iris/frontend\src\components\layout\HelpModal.tsx

```tsx
import { X, ExternalLink } from "lucide-react";

interface HelpModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export function HelpModal({ isOpen, onClose }: HelpModalProps) {
  if (!isOpen) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-4 transition-opacity"
      style={{ backgroundColor: "rgba(0,0,0,0.4)", backdropFilter: "blur(4px)" }}
      onClick={onClose}
    >
      <div 
        className="bg-white flex flex-col relative"
        style={{ width: "100%", maxWidth: 440, borderRadius: 16, boxShadow: "0 24px 64px rgba(0,0,0,0.15)" }}
        onClick={e => e.stopPropagation()}
      >
        <div className="flex items-center justify-between p-5 border-b border-[#F0F2F5]">
          <h2 style={{ fontSize: 18, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
            Help & Documentation
          </h2>
          <button 
            onClick={onClose}
            className="p-1 rounded-full transition-colors hover:bg-[#F8FAFC]"
            style={{ color: "#94A3B8" }}
          >
            <X size={20} />
          </button>
        </div>

        <div className="p-5 flex flex-col gap-3">
          <a
            href="https://docs.devise.ai"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between p-4 rounded-xl border border-[#E2E8F0] hover:border-[#FF5C1A] hover:bg-[#FFF3EE] transition-all group cursor-pointer"
          >
            <span style={{ fontSize: 15, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }} className="group-hover:text-[#FF5C1A] transition-colors">
              Getting Started Guide
            </span>
            <ExternalLink size={18} className="text-[#94A3B8] group-hover:text-[#FF5C1A]" />
          </a>

          <a
            href="https://docs.devise.ai/api"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between p-4 rounded-xl border border-[#E2E8F0] hover:border-[#FF5C1A] hover:bg-[#FFF3EE] transition-all group cursor-pointer"
          >
            <span style={{ fontSize: 15, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }} className="group-hover:text-[#FF5C1A] transition-colors">
              API Documentation
            </span>
            <ExternalLink size={18} className="text-[#94A3B8] group-hover:text-[#FF5C1A]" />
          </a>

          <a
            href="mailto:support@devise.ai"
            className="flex items-center justify-between p-4 rounded-xl border border-[#E2E8F0] hover:border-[#FF5C1A] hover:bg-[#FFF3EE] transition-all group cursor-pointer"
          >
            <span style={{ fontSize: 15, fontWeight: 500, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }} className="group-hover:text-[#FF5C1A] transition-colors">
              Contact Support
            </span>
            <ExternalLink size={18} className="text-[#94A3B8] group-hover:text-[#FF5C1A]" />
          </a>
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\layout\MyProfilePanel.tsx

```tsx
import { useState, useEffect } from "react";
import { X, Building2, ShieldCheck, Mail, Calendar, Activity, Database } from "lucide-react";
import { useAuth } from "@/lib/AuthContext";
import { useMe } from "@/hooks/useDashboard";
import { updateMe, getUserDetectionCount } from "@/services/api";
import { toast } from "sonner";

interface MyProfilePanelProps {
  isOpen: boolean;
  onClose: () => void;
}

export function MyProfilePanel({ isOpen, onClose }: MyProfilePanelProps) {
  const { user } = useAuth();
  const { data: profile, refetch } = useMe();
  const [isClosing, setIsClosing] = useState(false);
  const [detectionCount, setDetectionCount] = useState<number | null>(null);
  
  const [fullName, setFullName] = useState("");
  const [department, setDepartment] = useState("");
  const [isSaving, setIsSaving] = useState(false);

  useEffect(() => {
    if (profile) {
      setFullName(profile.full_name || "");
      setDepartment(profile.department || "General");
    }
  }, [profile]);

  useEffect(() => {
    if (user?.email) {
      getUserDetectionCount(user.email).then(setDetectionCount);
    }
  }, [user]);

  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === "Escape") handleClose();
    };
    if (isOpen) document.addEventListener("keydown", handleEsc);
    return () => document.removeEventListener("keydown", handleEsc);
  }, [isOpen]);

  const handleClose = () => {
    setIsClosing(true);
    setTimeout(() => {
      setIsClosing(false);
      onClose();
    }, 200);
  };

  const handleSave = async () => {
    setIsSaving(true);
    try {
      await updateMe({
        full_name: fullName,
        department: department
      });
      await refetch();
      toast.success("Profile updated successfully");
      handleClose();
    } catch (error) {
      console.error(error);
      toast.error("Failed to update profile");
    } finally {
      setIsSaving(false);
    }
  };

  const formatDate = (date: any) => {
    if (!date) return "...";
    const d = typeof date === 'string' ? new Date(date) : date.toDate();
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  };

  if (!isOpen && !isClosing) return null;

  return (
    <>
      <div 
        className="fixed inset-0 z-50 transition-opacity duration-200"
        style={{ 
          backgroundColor: "rgba(0,0,0,0.4)", 
          backdropFilter: "blur(4px)",
          opacity: isClosing ? 0 : 1 
        }}
        onClick={handleClose}
      />
      
      <div 
        className="fixed top-0 bottom-0 right-0 z-50 bg-white flex flex-col transition-transform duration-200"
        style={{ 
          width: 400, 
          boxShadow: "-12px 0 48px rgba(0,0,0,0.12)",
          transform: isClosing ? "translateX(100%)" : "translateX(0)" 
        }}
      >
        <div className="flex items-center justify-between p-6 border-b border-[#F0F2F5]">
          <h2 style={{ fontSize: 18, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
            My Profile
          </h2>
          <button 
            onClick={handleClose}
            className="p-1 rounded-full transition-colors hover:bg-[#F8FAFC]"
            style={{ color: "#94A3B8" }}
          >
            <X size={20} />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-8">
          
          <div className="flex flex-col items-center">
            <div
              className="flex items-center justify-center rounded-full mb-4 uppercase"
              style={{ 
                width: 64, height: 64, 
                backgroundColor: "#FF5C1A", 
                color: "#ffffff",
                fontFamily: "Inter, sans-serif",
                fontWeight: 700,
                fontSize: 24,
                boxShadow: "0 4px 12px rgba(255, 92, 26, 0.25)"
              }}
            >
              {profile?.full_name?.split(' ').map(n => n[0]).join('').slice(0, 2) || user?.email?.slice(0, 2) || "U"}
            </div>
            <button className="text-sm font-medium text-[#FF5C1A] hover:text-[#E5521A] transition-colors">
              Change avatar
            </button>
          </div>

          <div className="flex flex-col gap-6">
            <div className="flex flex-col gap-1.5">
              <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Full Name</label>
              <input 
                type="text" 
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full outline-none focus:border-[#FF5C1A] transition-colors"
                style={{ padding: "10px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
              />
            </div>

            <div className="flex flex-col gap-1.5">
              <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Email Address</label>
              <div className="relative">
                <input 
                  type="text" 
                  value={user?.email || ""} 
                  readOnly
                  className="w-full outline-none bg-[#F8FAFC]"
                  style={{ padding: "10px 12px 10px 36px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#64748B", fontFamily: "Inter, sans-serif", cursor: "not-allowed" }}
                />
                <Mail size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-[#94A3B8]" />
              </div>
            </div>

            <div className="flex flex-col gap-1.5">
              <label style={{ fontSize: 13, color: "#64748B", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>Department</label>
              <select 
                value={department}
                onChange={(e) => setDepartment(e.target.value)}
                className="w-full outline-none bg-white cursor-pointer focus:border-[#FF5C1A] transition-colors"
                style={{ padding: "10px 12px", border: "1px solid #E2E8F0", borderRadius: 8, fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
              >
                <option value="General">General</option>
                <option value="Engineering">Engineering</option>
                <option value="Product">Product</option>
                <option value="Design">Design</option>
                <option value="Marketing">Marketing</option>
                <option value="Operations">Operations</option>
              </select>
            </div>

            <div className="flex flex-col gap-4 p-4 rounded-xl bg-[#F8FAFC] border border-[#F0F2F5]">
              <h3 className="text-sm font-semibold text-[#1A1A2E] flex items-center gap-2">
                <Building2 size={16} className="text-[#94A3B8]" />
                Organization Details
              </h3>
              
              <div className="grid grid-cols-2 gap-4">
                <div className="flex flex-col gap-1">
                  <span className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold">Workspace</span>
                  <span className="text-sm font-medium text-[#1A1A2E] truncate">{profile?.org_name || "Personal Team"}</span>
                </div>
                <div className="flex flex-col gap-1">
                  <span className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold">Workspace ID</span>
                  <span className="text-xs font-mono text-[#64748B] truncate">{profile?.org_id || "..."}</span>
                </div>
                <div className="flex flex-col gap-1">
                  <span className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold">Role</span>
                  <div className="flex items-center gap-1.5 text-sm font-medium text-[#1A1A2E] capitalize">
                    <ShieldCheck size={14} className="text-[#FF5C1A]" />
                    {profile?.role || "Member"}
                  </div>
                </div>
                <div className="flex flex-col gap-1">
                  <span className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold">Member since</span>
                  <div className="flex items-center gap-1.5 text-sm font-medium text-[#1A1A2E]">
                    <Calendar size={14} className="text-[#94A3B8]" />
                    {formatDate(profile?.created_at)}
                  </div>
                </div>
                <div className="flex flex-col gap-1">
                  <span className="text-[11px] uppercase tracking-wider text-[#94A3B8] font-bold">Last Active</span>
                  <div className="flex items-center gap-1.5 text-sm font-medium text-[#1A1A2E]">
                    <Activity size={14} className="text-[#94A3B8]" />
                    {formatDate(profile?.last_active)}
                  </div>
                </div>
              </div>

              <div className="mt-2 pt-4 border-t border-[#E2E8F0] flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <Database size={16} className="text-[#94A3B8]" />
                </div>
                <span className="text-sm font-bold text-[#1A1A2E]">
                  {detectionCount ?? "..."}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div className="p-6 border-t border-[#F0F2F5] flex justify-end gap-3">
          <button 
            onClick={handleClose}
            className="transition-colors hover:bg-[#F8FAFC]"
            style={{ 
              padding: "10px 16px", borderRadius: 8, fontSize: 14, 
              fontWeight: 500, color: "#64748B", fontFamily: "Inter, sans-serif",
              border: "1px solid #E2E8F0"
            }}
          >
            Cancel
          </button>
          <button 
            onClick={handleSave}
            disabled={isSaving}
            className="transition-all hover:-translate-y-[1px] disabled:opacity-50 disabled:cursor-not-allowed"
            style={{ 
              backgroundColor: "#FF5C1A", color: "white", padding: "10px 20px", borderRadius: 8, 
              fontSize: 14, fontWeight: 500, fontFamily: "Inter, sans-serif",
              boxShadow: "0 2px 4px rgba(255, 92, 26, 0.2)"
            }}
            onMouseEnter={e => !isSaving && (e.currentTarget.style.backgroundColor = "#E5521A")}
            onMouseLeave={e => !isSaving && (e.currentTarget.style.backgroundColor = "#FF5C1A")}
          >
            {isSaving ? "Saving..." : "Save Changes"}
          </button>
        </div>
      </div>
    </>
  );
}
```

### devise-iris/frontend\src\components\layout\NotificationDropdown.tsx

```tsx
import { useEffect, useRef, useState } from "react";
import { AlertTriangle, ShieldAlert, Bell, Activity, Monitor } from "lucide-react";

import { NotificationItem } from "./TopBar";

interface NotificationDropdownProps {
  isOpen: boolean;
  onClose: () => void;
  notifications: NotificationItem[];
  onMarkAllRead: () => void;
  onNotificationClick: (id: number) => void;
  unreadCount?: number;
}

export function NotificationDropdown({
  isOpen, 
  onClose,
  notifications,
  onMarkAllRead,
  onNotificationClick,
  unreadCount = 0
}: NotificationDropdownProps) {
  const dropdownRef = useRef<HTMLDivElement>(null);
  const [activeTab, setActiveTab] = useState("All");

  const tabs = ["All", `Unread (${unreadCount})`, "Alerts", "System"];

  const filteredNotifs = notifications.filter((notif) => {
    if (activeTab.startsWith("Unread")) return notif.unread;
    if (activeTab === "Alerts") return notif.category === "Alerts";
    if (activeTab === "System") return notif.category === "System";
    return true; // "All"
  });

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        onClose();
      }
    };
    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    }
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      ref={dropdownRef}
      className="absolute bg-white flex flex-col z-50 overflow-hidden"
      style={{
        top: 56,
        right: 0,
        width: 380,
        borderRadius: 16,
        border: "1px solid #F0F2F5",
        boxShadow: "0 16px 48px rgba(0,0,0,0.12)",
      }}
    >
      {/* Header Row */}
      <div className="flex items-center justify-between px-4 pt-4 pb-2">
        <span
          style={{
            fontFamily: "Inter, sans-serif",
            fontWeight: 600,
            fontSize: 16,
            color: "#1A1A2E",
          }}
        >
          Notifications
        </span>
        <button
          onClick={onMarkAllRead}
          style={{
            background: "none",
            border: "none",
            color: "#FF5C1A",
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
            cursor: "pointer",
          }}
        >
          Mark all read
        </button>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-4 px-4 border-b border-[#F0F2F5]">
        {tabs.map((tab) => {
          const isActive = activeTab === tab;
          return (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className="pb-2 transition-colors relative"
              style={{
                background: "none",
                border: "none",
                fontFamily: "Inter, sans-serif",
                fontSize: 13,
                fontWeight: isActive ? 600 : 500,
                color: isActive ? "#1A1A2E" : "#94A3B8",
                cursor: "pointer",
              }}
            >
              {tab}
              {isActive && (
                <div
                  className="absolute bottom-0 left-0 right-0 rounded-t"
                  style={{ height: 2, backgroundColor: "#FF5C1A" }}
                />
              )}
            </button>
          );
        })}
      </div>

      {/* Notification Items */}
      <div 
        className="flex flex-col overflow-y-auto" 
        style={{ 
          maxHeight: 400,
          // Custom scrollbar styles
          scrollbarWidth: "thin",
          scrollbarColor: "#CBD5E1 transparent" 
        }}
      >
        {filteredNotifs.length === 0 && (
          <div className="flex flex-col items-center justify-center py-8 text-slate-400">
            <span style={{ fontSize: 13 }}>No notifications here</span>
          </div>
        )}
        {filteredNotifs.map((notif) => (
          <div
            key={notif.id}
            onClick={() => onNotificationClick(notif.id)}
            className="flex items-start transition-colors cursor-pointer"
            style={{
              padding: "12px 16px",
              gap: 12,
              opacity: notif.unread ? 1 : 0.7,
            }}
            onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#F8FAFC")}
            onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "transparent")}
          >
            {/* Left Icon Block */}
            <div className="relative shrink-0 mt-0.5">
              <div
                className="flex items-center justify-center rounded-full"
                style={{ width: 36, height: 36, backgroundColor: notif.iconBg }}
              >
                <notif.icon size={16} color="#ffffff" strokeWidth={2} />
              </div>
              {notif.unread && (
                <div
                  className="absolute"
                  style={{
                    top: 0,
                    right: 0,
                    width: 6,
                    height: 6,
                    backgroundColor: "#FF5C1A",
                    borderRadius: "50%",
                  }}
                />
              )}
            </div>

            {/* Right Content Block & Time */}
            <div className="flex flex-col flex-1 min-w-0 pr-2 pb-0.5">
              <div className="flex justify-between items-start gap-2">
                <span
                  className="truncate"
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontWeight: 600,
                    fontSize: 13,
                    color: "#1A1A2E",
                    lineHeight: 1.4,
                  }}
                >
                  {notif.title}
                </span>
                <span
                  className="shrink-0"
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontSize: 11,
                    color: "#C0C8D4",
                    lineHeight: 1.4,
                  }}
                >
                  {notif.time}
                </span>
              </div>
              <span
                className="truncate w-full mt-0.5"
                style={{
                  fontFamily: "Inter, sans-serif",
                  fontSize: 12,
                  color: "#94A3B8",
                  lineHeight: 1.4,
                }}
              >
                {notif.desc}
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* Footer */}
      <div
        className="flex items-center justify-center border-t border-[#F0F2F5]"
        style={{ padding: "12px 16px" }}
      >
        <button
          className="flex items-center justify-center"
          style={{
            background: "none",
            border: "none",
            color: "#FF5C1A",
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
            fontWeight: 500,
            cursor: "pointer",
          }}
        >
          View all alerts &rarr;
        </button>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\layout\SearchModal.tsx

```tsx
import { useState, useEffect, useRef } from "react";
import { Search, Activity } from "lucide-react";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
  onNavigate?: (tab: Tab) => void;
}

const recentEvents = [
  { id: "e1", text: "OpenAI API detected — yashm", time: "2 min ago" },
  { id: "e2", text: "GitHub Copilot active — alex", time: "15 min ago" },
  { id: "e3", text: "Midjourney usage spike — design", time: "1 hr ago" },
  { id: "e4", text: "Cursor Pro detected — sarah", time: "2 hr ago" },
  { id: "e5", text: "Notion AI disabled — system", time: "4 hr ago" },
];

const tools = [
  { id: "t1", name: "ChatGPT Enterprise", category: "LLM", color: "#10A37F" },
  { id: "t2", name: "GitHub Copilot", category: "Coding", color: "#181717" },
  { id: "t3", name: "Midjourney", category: "Image", color: "#FF5C1A" },
];

const users = [
  { id: "u1", name: "Yash M", email: "yash@devise.ai", dept: "Engineering", initial: "YM", color: "#FF5C1A" },
  { id: "u2", name: "Alex J", email: "alex@devise.ai", dept: "Product", initial: "AJ", color: "#3B82F6" },
  { id: "u3", name: "Sarah K", email: "sarah@devise.ai", dept: "Design", initial: "SK", color: "#8B5CF6" },
];

export function SearchModal({ isOpen, onClose, onNavigate }: SearchModalProps) {
  const [query, setQuery] = useState("");
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [recentSearches, setRecentSearches] = useState<string[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const saved = localStorage.getItem("devise-recent-searches");
    if (saved) {
      try { setRecentSearches(JSON.parse(saved)); } catch (e) {}
    }
  }, []);

  useEffect(() => {
    if (isOpen) {
      setQuery("");
      setSelectedIndex(0);
      setTimeout(() => inputRef.current?.focus(), 50);
    }
  }, [isOpen]);

  // Derived state
  const lowerQ = query.toLowerCase();
  const isQueryEmpty = lowerQ.trim() === "";
  
  const filteredEvents = isQueryEmpty ? [] : recentEvents.filter(e => e.text.toLowerCase().includes(lowerQ));
  const filteredTools = isQueryEmpty ? [] : tools.filter(t => t.name.toLowerCase().includes(lowerQ));
  const filteredUsers = isQueryEmpty ? [] : users.filter(u => u.name.toLowerCase().includes(lowerQ) || u.email.toLowerCase().includes(lowerQ));

  const totalResults = filteredEvents.length + filteredTools.length + filteredUsers.length;

  const flatItems: { type: string; item: any; }[] = [
    ...filteredEvents.map(item => ({ type: "event", item })),
    ...filteredTools.map(item => ({ type: "tool", item })),
    ...filteredUsers.map(item => ({ type: "user", item }))
  ];

  const handleSelect = (itemInfo: { type: string; item: any }) => {
    if (!isQueryEmpty) {
      const newRecents = [query.trim(), ...recentSearches.filter(q => q !== query.trim())].slice(0, 5);
      localStorage.setItem("devise-recent-searches", JSON.stringify(newRecents));
      setRecentSearches(newRecents);
    }

    if (onNavigate) {
      if (itemInfo.type === "event") onNavigate("live-feed");
      else if (itemInfo.type === "tool") onNavigate("subscriptions");
      else if (itemInfo.type === "user") onNavigate("devices");
    }
    onClose();
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return;

      if (e.key === "Escape") {
        onClose();
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        setSelectedIndex(prev => Math.min(prev + 1, flatItems.length > 0 ? flatItems.length - 1 : 0));
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        setSelectedIndex(prev => Math.max(prev - 1, 0));
      } else if (e.key === "Enter") {
        e.preventDefault();
        if (flatItems.length > 0 && selectedIndex >= 0 && selectedIndex < flatItems.length) {
          handleSelect(flatItems[selectedIndex]);
        } else if (isQueryEmpty && recentSearches.length > 0) {
          // If they hit enter on empty, maybe do nothing.
        }
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, selectedIndex, flatItems, onClose, isQueryEmpty, query, recentSearches, onNavigate]);

  useEffect(() => {
    setSelectedIndex(0);
  }, [query]);

  // Scroll active item into view
  useEffect(() => {
    if (scrollRef.current) {
      const activeItem = scrollRef.current.querySelector('[data-active="true"]') as HTMLElement;
      if (activeItem) {
        activeItem.scrollIntoView({ block: "nearest", behavior: "smooth" });
      }
    }
  }, [selectedIndex]);

  if (!isOpen) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-start justify-center pt-[10vh]"
      style={{ backgroundColor: "rgba(0,0,0,0.4)", backdropFilter: "blur(4px)" }}
      onClick={onClose}
    >
      <div 
        className="flex flex-col overflow-hidden bg-white relative"
        style={{ width: 600, maxHeight: 500, borderRadius: 16, boxShadow: "0 24px 64px rgba(0,0,0,0.15)" }}
        onClick={e => e.stopPropagation()}
      >
        {/* Search Input */}
        <div className="flex items-center px-4 shrink-0" style={{ borderBottom: "1px solid #F0F2F5", height: 56 }}>
          <Search size={20} color="#94A3B8" />
          <input 
            ref={inputRef}
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Search tools, users, events, devices..."
            className="flex-1 bg-transparent outline-none px-3"
            style={{ fontSize: 16, fontFamily: "Inter, sans-serif", color: "#1A1A2E" }}
          />
          <div 
            className="flex items-center justify-center rounded"
            style={{ padding: "2px 6px", border: "1px solid #E2E8F0", fontSize: 11, fontWeight: 600, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}
          >
            ESC
          </div>
        </div>

        {/* Results */}
        <div ref={scrollRef} className="flex-1 overflow-y-auto py-2">
          {isQueryEmpty ? (
            recentSearches.length === 0 ? (
              <div className="flex flex-col items-center justify-center py-12 gap-3">
                <Search size={32} color="#E2E8F0" />
                <span style={{ color: "#94A3B8", fontSize: 14, fontFamily: "Inter, sans-serif" }}>
                  Search for tools, users, and events
                </span>
              </div>
            ) : (
              <div className="mb-2">
                <div className="flex justify-between items-center px-4 py-2">
                  <span style={{ fontSize: 12, fontWeight: 600, color: "#94A3B8", fontFamily: "Inter, sans-serif", letterSpacing: "0.5px", textTransform: "uppercase" }}>
                    Recent Searches
                  </span>
                  <button 
                    onClick={() => { localStorage.removeItem("devise-recent-searches"); setRecentSearches([]); }}
                    style={{ fontSize: 11, fontWeight: 500, color: "#FF5C1A", fontFamily: "Inter, sans-serif", border: "none", background: "none", cursor: "pointer", transition: "all 0.2s" }}
                    onMouseEnter={e => e.currentTarget.style.opacity = "0.7"}
                    onMouseLeave={e => e.currentTarget.style.opacity = "1"}
                  >
                    Clear history
                  </button>
                </div>
                {recentSearches.map((rs, idx) => (
                  <div
                    key={idx}
                    className="flex items-center px-4 transition-colors duration-150 cursor-pointer"
                    style={{ height: 44 }}
                    onClick={() => setQuery(rs)}
                    onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#F8FAFC")}
                    onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "transparent")}
                  >
                    <Search size={16} color="#94A3B8" className="mr-3" />
                    <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>{rs}</span>
                  </div>
                ))}
              </div>
            )
          ) : totalResults === 0 ? (
            <div className="flex flex-col items-center justify-center py-12 gap-3">
              <Search size={32} color="#E2E8F0" />
              <span style={{ color: "#94A3B8", fontSize: 14, fontFamily: "Inter, sans-serif" }}>
                No results for '{query}'
              </span>
            </div>
          ) : (
            <>
              {filteredEvents.length > 0 && (
                <div className="mb-2">
                  <div className="px-4 py-2" style={{ fontSize: 12, fontWeight: 600, color: "#94A3B8", fontFamily: "Inter, sans-serif", letterSpacing: "0.5px", textTransform: "uppercase" }}>
                    Recent Events
                  </div>
                  {filteredEvents.map(e => {
                    const globalIndex = flatItems.findIndex(i => i.item.id === e.id);
                    const isActive = selectedIndex === globalIndex;
                    return (
                      <div
                        key={e.id}
                        data-active={isActive}
                        className="flex items-center justify-between px-4 transition-colors duration-150 cursor-pointer"
                        style={{ height: 44, backgroundColor: isActive ? "#FFF3EE" : "transparent" }}
                        onMouseEnter={() => setSelectedIndex(globalIndex)}
                        onClick={() => handleSelect({ type: "event", item: e })}
                      >
                        <div className="flex items-center gap-3">
                          <Activity size={16} color="#94A3B8" strokeWidth={2} />
                          <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>{e.text}</span>
                        </div>
                        <span style={{ fontSize: 12, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>{e.time}</span>
                      </div>
                    );
                  })}
                </div>
              )}

              {filteredTools.length > 0 && (
                <div className="mb-2">
                  <div className="px-4 py-2" style={{ fontSize: 12, fontWeight: 600, color: "#94A3B8", fontFamily: "Inter, sans-serif", letterSpacing: "0.5px", textTransform: "uppercase" }}>
                    Tools
                  </div>
                  {filteredTools.map(t => {
                    const globalIndex = flatItems.findIndex(i => i.item.id === t.id);
                    const isActive = selectedIndex === globalIndex;
                    return (
                      <div
                        key={t.id}
                        data-active={isActive}
                        className="flex items-center justify-between px-4 transition-colors duration-150 cursor-pointer"
                        style={{ height: 44, backgroundColor: isActive ? "#FFF3EE" : "transparent" }}
                        onMouseEnter={() => setSelectedIndex(globalIndex)}
                        onClick={() => handleSelect({ type: "tool", item: t })}
                      >
                        <div className="flex items-center gap-3">
                          <div className="rounded-full" style={{ width: 8, height: 8, backgroundColor: t.color }} />
                          <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>{t.name}</span>
                        </div>
                        <div 
                          className="flex items-center justify-center rounded-full"
                          style={{ padding: "2px 8px", backgroundColor: "#F8FAFC", border: "1px solid #E2E8F0", fontSize: 11, fontWeight: 500, color: "#64748B", fontFamily: "Inter, sans-serif" }}
                        >
                          {t.category}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}

              {filteredUsers.length > 0 && (
                <div className="mb-2">
                  <div className="px-4 py-2" style={{ fontSize: 12, fontWeight: 600, color: "#94A3B8", fontFamily: "Inter, sans-serif", letterSpacing: "0.5px", textTransform: "uppercase" }}>
                    Users
                  </div>
                  {filteredUsers.map(u => {
                    const globalIndex = flatItems.findIndex(i => i.item.id === u.id);
                    const isActive = selectedIndex === globalIndex;
                    return (
                      <div
                        key={u.id}
                        data-active={isActive}
                        className="flex items-center justify-between px-4 transition-colors duration-150 cursor-pointer"
                        style={{ height: 44, backgroundColor: isActive ? "#FFF3EE" : "transparent" }}
                        onMouseEnter={() => setSelectedIndex(globalIndex)}
                        onClick={() => handleSelect({ type: "user", item: u })}
                      >
                        <div className="flex items-center gap-3">
                          <div 
                            className="flex items-center justify-center rounded-full flex-shrink-0"
                            style={{ width: 24, height: 24, backgroundColor: u.color, color: "white", fontSize: 10, fontWeight: 600, fontFamily: "Inter, sans-serif" }}
                          >
                            {u.initial}
                          </div>
                          <div className="flex items-center gap-1.5">
                            <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>{u.name}</span>
                            <span style={{ fontSize: 13, color: "#94A3B8", fontFamily: "Inter, sans-serif" }}>{u.email}</span>
                          </div>
                        </div>
                        <div 
                          className="flex items-center justify-center rounded-full"
                          style={{ padding: "2px 8px", backgroundColor: "#F8FAFC", border: "1px solid #E2E8F0", fontSize: 11, fontWeight: 500, color: "#64748B", fontFamily: "Inter, sans-serif" }}
                        >
                          {u.dept}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\layout\Sidebar.tsx

```tsx
import {
  Activity,
  BarChart2,
  Monitor,
  Bell,
  Users,
  Layers,
  Settings,
  HelpCircle,
  LogOut,
  PieChart,
  Shield,
  Eye,
} from "lucide-react";
import { useState } from "react";
import { HelpModal } from "./HelpModal";
import { SignOutModal } from "./SignOutModal";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";

interface SidebarProps {
  activeTab: Tab;
  onTabChange: (tab: Tab) => void;
}

const mainIcons = [
  { id: "overview",   icon: Activity,  tab: "overview" },
  { id: "live-feed", icon: BarChart2, tab: "live-feed" },
  { id: "analytics", icon: PieChart,  tab: "analytics" },
  { id: "devices",   icon: Monitor,   tab: "devices" },
  { id: "alerts",    icon: Bell,      tab: "alerts" },
  { id: "team",      icon: Users,     tab: "team" },
  { id: "layers",    icon: Layers,    tab: "subscriptions" },
  { id: "firewall",  icon: Shield,    tab: "firewall" },
  { id: "data-risk", icon: Eye,       tab: "data-risk" },
];

export function AppSidebar({ activeTab, onTabChange }: SidebarProps) {
  const [isHelpOpen, setIsHelpOpen] = useState(false);
  const [isSignOutOpen, setIsSignOutOpen] = useState(false);

  const handleSignOutConfirm = () => {
    localStorage.clear();
    window.location.reload();
  };

  // Shared renderer for the icon buttons
  const renderIconButton = (
    id: string,
    Icon: React.ElementType,
    isActive: boolean,
    hoverColor: string,
    hoverBg: string,
    onClick?: () => void
  ) => {
    return (
      <button
        key={id}
        onClick={onClick}
        className="flex items-center justify-center transition-all"
        style={{
          width: 40, height: 40, borderRadius: 12, cursor: "pointer",
          backgroundColor: isActive ? "#FFF3EE" : "transparent",
          color: isActive ? "#FF5C1A" : "#C0C8D4",
          border: isActive ? "1px solid #FDDCC8" : "1px solid transparent",
          transitionDuration: "150ms",
        }}
        onMouseEnter={(e) => {
          if (!isActive) {
            (e.currentTarget as HTMLButtonElement).style.color = hoverColor;
            (e.currentTarget as HTMLButtonElement).style.backgroundColor = hoverBg;
          }
        }}
        onMouseLeave={(e) => {
          if (!isActive) {
            (e.currentTarget as HTMLButtonElement).style.color = "#C0C8D4";
            (e.currentTarget as HTMLButtonElement).style.backgroundColor = "transparent";
          }
        }}
        aria-label={id}
      >
        <Icon size={18} strokeWidth={1.5} />
      </button>
    );
  };

  return (
    <aside
      style={{
        width: 64, minWidth: 64, backgroundColor: "#ffffff",
        borderRight: "1px solid #F0F2F5", paddingTop: 20, paddingBottom: 20
      }}
      className="flex flex-col items-center h-full z-10"
    >
      {/* Logo */}
      <div
        className="flex items-center justify-center rounded-full mb-6 flex-shrink-0"
        style={{ width: 36, height: 36, backgroundColor: "#FF5C1A" }}
      >
        <span className="text-white font-bold text-base leading-none">D</span>
      </div>

      {/* Nav icons */}
      <div className="flex flex-col items-center w-full flex-1" style={{ gap: 8 }}>
        
        {/* Main 6 icons */}
        {mainIcons.map(({ id, icon, tab }) => {
          const isActive = tab ? activeTab === tab : false;
          
          return renderIconButton(id, icon, isActive, "#FF5C1A", "#FFF3EE", () => {
            if (tab && (["overview", "live-feed", "analytics", "devices", "alerts", "subscriptions", "team", "firewall", "data-risk"] as string[]).includes(tab)) {
              onTabChange(tab as Tab);
            }
          });
        })}

        {/* Bottom cluster (Settings + Line + Help + Logout) pushed down */}
        <div className="flex flex-col items-center w-full" style={{ marginTop: "auto", gap: 8 }}>
          {/* Settings */}
          {renderIconButton("settings", Settings, activeTab === "settings", "#FF5C1A", "#FFF3EE", () => onTabChange("settings"))}

          {/* Divider */}
          <div style={{ width: "100%", height: 1, backgroundColor: "#F0F2F5", margin: "4px 0" }} />

          {/* Help & Logout */}
          {renderIconButton("help", HelpCircle, false, "#FF5C1A", "#FFF3EE", () => setIsHelpOpen(true))}
          {renderIconButton("logout", LogOut, false, "#DC2626", "rgba(220,38,38,0.08)", () => setIsSignOutOpen(true))}
        </div>
      </div>

      <HelpModal isOpen={isHelpOpen} onClose={() => setIsHelpOpen(false)} />
      <SignOutModal isOpen={isSignOutOpen} onClose={() => setIsSignOutOpen(false)} onConfirm={handleSignOutConfirm} />
    </aside>
  );
}
```

### devise-iris/frontend\src\components\layout\SignOutModal.tsx

```tsx
import { AlertTriangle } from "lucide-react";

interface SignOutModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
}

export function SignOutModal({ isOpen, onClose, onConfirm }: SignOutModalProps) {
  if (!isOpen) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-4 transition-opacity"
      style={{ backgroundColor: "rgba(0,0,0,0.4)", backdropFilter: "blur(4px)" }}
      onClick={onClose}
    >
      <div 
        className="bg-white flex flex-col relative items-center text-center p-8"
        style={{ width: "100%", maxWidth: 400, borderRadius: 16, boxShadow: "0 24px 64px rgba(0,0,0,0.15)" }}
        onClick={e => e.stopPropagation()}
      >
        <div 
          className="flex items-center justify-center rounded-full mb-4"
          style={{ width: 48, height: 48, backgroundColor: "#FEF2F2" }}
        >
          <AlertTriangle size={24} color="#DC2626" />
        </div>
        
        <h2 className="mb-2" style={{ fontSize: 18, fontWeight: 600, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}>
          Are you sure you want to sign out?
        </h2>
        <p className="mb-8" style={{ fontSize: 14, color: "#64748B", fontFamily: "Inter, sans-serif", lineHeight: 1.5 }}>
          You will be returned to the login screen and will need to enter your credentials to access the dashboard again.
        </p>

        <div className="flex gap-3 w-full">
          <button 
            onClick={onClose}
            className="flex-1 transition-colors hover:bg-[#F8FAFC]"
            style={{ 
              padding: "10px 16px", borderRadius: 8, fontSize: 14, 
              fontWeight: 500, color: "#475569", fontFamily: "Inter, sans-serif",
              backgroundColor: "#F1F5F9",
            }}
          >
            Cancel
          </button>
          <button 
            onClick={onConfirm}
            className="flex-1 transition-all hover:-translate-y-[1px]"
            style={{ 
              backgroundColor: "#DC2626", color: "white", padding: "10px 16px", borderRadius: 8, 
              fontSize: 14, fontWeight: 500, fontFamily: "Inter, sans-serif",
              boxShadow: "0 2px 4px rgba(220, 38, 38, 0.2)"
            }}
            onMouseEnter={e => e.currentTarget.style.backgroundColor = "#B91C1C"}
            onMouseLeave={e => e.currentTarget.style.backgroundColor = "#DC2626"}
          >
            Sign Out
          </button>
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\components\layout\TopBar.tsx

```tsx
import { Search, Bell, Info, ChevronDown, AlertTriangle, ShieldAlert, Activity, Monitor } from "lucide-react";
import { useState } from "react";
import { SearchModal } from "./SearchModal";
import { NotificationDropdown } from "./NotificationDropdown";
import { UserProfileDropdown } from "./UserProfileDropdown";
import { useAuth } from "@/lib/AuthContext";
import { useMe } from "@/hooks/useDashboard";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";


export interface NotificationItem {
  id: number;
  icon: any;
  iconBg: string;
  title: string;
  desc: string;
  time: string;
  unread: boolean;
  category: "Alerts" | "System";
}

const INITIAL_NOTIFICATIONS: NotificationItem[] = [
  {
    id: 1,
    icon: AlertTriangle,
    iconBg: "#DC2626",
    title: "Critical: Finance dept used Replicate",
    desc: "Policy violation detected",
    time: "2m ago",
    unread: true,
    category: "Alerts"
  },
  {
    id: 2,
    icon: ShieldAlert,
    iconBg: "#FF5C1A",
    title: "New shadow AI tool detected",
    desc: "Character.ai first seen",
    time: "8m ago",
    unread: true,
    category: "Alerts"
  },
  {
    id: 3,
    icon: Bell,
    iconBg: "#D97706",
    title: "5 zombie licenses need review",
    desc: "₹48,000 potential savings",
    time: "1hr ago",
    unread: true,
    category: "System"
  },
  {
    id: 4,
    icon: Activity,
    iconBg: "#3B82F6",
    title: "Weekly report ready",
    desc: "247 detections this week",
    time: "2hr ago",
    unread: true,
    category: "System"
  },
  {
    id: 5,
    icon: Monitor,
    iconBg: "#16A34A",
    title: "New device enrolled",
    desc: "macbook-arjun.local added",
    time: "5hr ago",
    unread: true,
    category: "System"
  },
  {
    id: 6,
    icon: Bell,
    iconBg: "#94A3B8",
    title: "Scheduled maintenance",
    desc: "System update tonight at 2AM",
    time: "1d ago",
    unread: false,
    category: "System"
  },
  {
    id: 7,
    icon: Activity,
    iconBg: "#94A3B8",
    title: "Agent v2.4 deployed",
    desc: "Successfully updated 12 devices",
    time: "2d ago",
    unread: false,
    category: "System"
  },
  {
    id: 8,
    icon: ShieldAlert,
    iconBg: "#94A3B8",
    title: "Low risk tool approved",
    desc: "Grammarly Business added to allowed list",
    time: "3d ago",
    unread: false,
    category: "Alerts"
  },
];

interface TopBarProps {
  activeTab: Tab;
  onTabChange: (tab: Tab) => void;
}

const tabs: { id: Tab; label: string }[] = [
  { id: "overview",  label: "Overview"  },
  { id: "live-feed", label: "Live Feed" },
  { id: "analytics", label: "Analytics" },
  { id: "devices",   label: "Devices"   },
  { id: "alerts",    label: "Alerts"    },
];

export function TopBar({ activeTab, onTabChange }: TopBarProps) {
  const { user } = useAuth();
  const { data: profile } = useMe();
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [isNotifOpen, setIsNotifOpen] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  
  const [notifications, setNotifications] = useState<NotificationItem[]>(INITIAL_NOTIFICATIONS);

  // Derive unread count from notifications array passed below
  const unreadCount = notifications.filter((n) => n.unread).length;

  const handleMarkAllRead = () => {
    setNotifications(prev => prev.map(n => ({ ...n, unread: false })));
  };

  const handleNotificationClick = (id: number) => {
    setNotifications(prev => 
      prev.map(n => n.id === id ? { ...n, unread: false } : n)
    );
  };

  return (
    <header
      className="flex items-center justify-between px-6 flex-shrink-0 border-b"
      style={{ height: 72, borderColor: "#F5F5F5", backgroundColor: "#ffffff" }}
    >
      {/* Left — Greeting */}
      <div className="flex flex-col justify-center min-w-[220px]">
        <span
          className="font-bold leading-tight"
          style={{ fontSize: 22, color: "#1A1A2E", fontFamily: "Inter, sans-serif" }}
        >
          Good morning, {profile?.full_name?.split(' ')[0] || "Yash"}
        </span>
        <span
          className="leading-tight mt-0.5"
          style={{ fontSize: 13, color: "#94A3B8" }}
        >
          Monitor your AI governance across all devices
        </span>
      </div>

      {/* Center — Pill Tabs */}
      <nav className="flex items-center gap-1 bg-[#F5F7FA] rounded-full px-1.5 py-1.5">
        {tabs.map(({ id, label }) => {
          const isActive = activeTab === id;
          return (
            <button
              key={id}
              onClick={() => onTabChange(id)}
              className="transition-all duration-200 font-medium text-sm leading-none"
              style={{
                padding: "7px 18px",
                borderRadius: 999,
                backgroundColor: isActive ? "#1A1A2E" : "transparent",
                color: isActive ? "#ffffff" : "#94A3B8",
                fontFamily: "Inter, sans-serif",
              }}
              onMouseEnter={(e) => {
                if (!isActive)
                  (e.currentTarget as HTMLButtonElement).style.color = "#1A1A2E";
              }}
              onMouseLeave={(e) => {
                if (!isActive)
                  (e.currentTarget as HTMLButtonElement).style.color = "#94A3B8";
              }}
            >
              {label}
            </button>
          );
        })}
      </nav>

      {/* Right — Actions + Avatar */}
      <div className="flex items-center justify-end" style={{ gap: 20, marginRight: 24 }}>
        
        {/* Search */}
        <button
          className="flex items-center justify-center transition-colors"
          style={{ cursor: "pointer", background: "none", border: "none", color: "#94A3B8" }}
          onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.color = "#1A1A2E"; }}
          onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.color = "#94A3B8"; }}
          aria-label="Search"
          onClick={() => setIsSearchOpen(true)}
        >
          <Search size={18} strokeWidth={2} />
        </button>

        {/* Bell with orange dot */}
        <div className="relative flex items-center justify-center">
          <button
            className="flex items-center justify-center transition-colors"
            style={{ cursor: "pointer", background: "none", border: "none", color: "#94A3B8" }}
            onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.color = "#1A1A2E"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.color = "#94A3B8"; }}
            aria-label="Notifications"
            onClick={() => setIsNotifOpen(!isNotifOpen)}
          >
            <Bell size={18} strokeWidth={2} />
            {unreadCount > 0 && (
              <span
                className="absolute rounded-full"
                style={{ 
                  top: 0, 
                  right: 0, 
                  width: 8, 
                  height: 8, 
                  backgroundColor: "#FF5C1A" 
                }}
              />
            )}
          </button>
          <NotificationDropdown 
            isOpen={isNotifOpen} 
            onClose={() => setIsNotifOpen(false)}
            notifications={notifications}
            onMarkAllRead={handleMarkAllRead}
            onNotificationClick={handleNotificationClick}
            unreadCount={unreadCount}
          />
        </div>

        {/* Info */}
        <button
          className="flex items-center justify-center transition-colors"
          style={{ cursor: "pointer", background: "none", border: "none", color: "#94A3B8" }}
          onMouseEnter={e => { (e.currentTarget as HTMLButtonElement).style.color = "#1A1A2E"; }}
          onMouseLeave={e => { (e.currentTarget as HTMLButtonElement).style.color = "#94A3B8"; }}
          aria-label="Info"
        >
          <Info size={18} strokeWidth={2} />
        </button>

        {/* Vertical Divider */}
        <div style={{ width: 1, height: 28, backgroundColor: "#F0F2F5", margin: "0 4px" }} />

        {/* Avatar + name */}
        <div className="relative flex items-center">
          <div 
            className="flex items-center transition-colors select-none" 
            style={{ gap: 10, cursor: "pointer", borderRadius: 12, padding: "4px 8px" }}
            onMouseEnter={e => { (e.currentTarget as HTMLDivElement).style.backgroundColor = "#F8FAFC"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLDivElement).style.backgroundColor = "transparent"; }}
            onClick={() => setIsProfileOpen(!isProfileOpen)}
          >
            <div
              className="flex items-center justify-center rounded-full flex-shrink-0"
              style={{ 
                width: 36, height: 36, 
                backgroundColor: "#FF5C1A", 
                color: "#ffffff",
                fontFamily: "Inter, sans-serif",
                fontWeight: 600,
                fontSize: 13,
                letterSpacing: "0.5px"
              }}
            >
              {profile?.full_name?.split(' ').map(n => n[0]).join('').slice(0, 2) || user?.email?.slice(0, 2).toUpperCase() || "U"}
            </div>
            <div className="flex flex-col text-left">
              <span
                className="font-semibold"
                style={{ fontSize: 14, color: "#1A1A2E", lineHeight: 1.2, fontFamily: "Inter, sans-serif" }}
              >
                {profile?.full_name || user?.email?.split('@')[0] || "User"}
              </span>
              <span
                style={{ fontSize: 12, color: "#94A3B8", lineHeight: 1.2, fontFamily: "Inter, sans-serif" }}
              >
                {user?.email || "..."}
              </span>
            </div>
            <ChevronDown size={16} strokeWidth={2} style={{ color: "#94A3B8", marginLeft: 4 }} />
          </div>
          <UserProfileDropdown 
            isOpen={isProfileOpen} 
            onClose={() => setIsProfileOpen(false)} 
            onTabChange={onTabChange}
          />
        </div>
      </div>

      <SearchModal isOpen={isSearchOpen} onClose={() => setIsSearchOpen(false)} onNavigate={onTabChange} />
    </header>
  );
}

```

### devise-iris/frontend\src\components\layout\UserProfileDropdown.tsx

```tsx
import { useEffect, useRef, useState } from "react";
import { User, Settings, Layers, HelpCircle, Moon, LogOut } from "lucide-react";
import { MyProfilePanel } from "./MyProfilePanel";
import { AccountSettingsPanel } from "./AccountSettingsPanel";
import { HelpModal } from "./HelpModal";
import { SignOutModal } from "./SignOutModal";
import { useAuth } from "@/lib/AuthContext";
import { useMe } from "@/hooks/useDashboard";
import { updateMe } from "@/services/api";

type Tab = "overview" | "live-feed" | "analytics" | "devices" | "alerts" | "subscriptions" | "settings" | "team" | "firewall" | "data-risk";

interface UserProfileDropdownProps {
  isOpen: boolean;
  onClose: () => void;
  onTabChange: (tab: Tab) => void;
}

export function UserProfileDropdown({ isOpen, onClose, onTabChange }: UserProfileDropdownProps) {
  const { user, signOut } = useAuth();
  const { data: profile, isLoading } = useMe();
  const dropdownRef = useRef<HTMLDivElement>(null);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const [isAccountOpen, setIsAccountOpen] = useState(false);
  const [isHelpOpen, setIsHelpOpen] = useState(false);
  const [isSignOutOpen, setIsSignOutOpen] = useState(false);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        onClose();
      }
    };
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }
    };

    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
      document.addEventListener("keydown", handleEsc);
    }
    
    // Read dark mode initial state
    const savedTheme = localStorage.getItem("devise-theme");
    if (savedTheme === "dark" || document.documentElement.classList.contains("dark")) {
      setIsDarkMode(true);
    }

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("keydown", handleEsc);
    };
  }, [isOpen, onClose]);

  const toggleDarkMode = async () => {
    const newDarkMode = !isDarkMode;
    setIsDarkMode(newDarkMode);
    
    // UI update
    if (newDarkMode) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("devise-theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("devise-theme", "light");
    }

    // Sync to Firestore
    try {
      await updateMe({ dark_mode: newDarkMode });
    } catch (error) {
      console.error("Failed to sync dark mode to Firestore:", error);
    }
  };

  const handleSignOutConfirm = async () => {
    localStorage.clear();
    await signOut();
    window.location.href = "/login";
  };

  return (
    <>
      {/* Modals are rendered outside the open check so they don't unmount when dropdown closes */}
      <MyProfilePanel isOpen={isProfileOpen} onClose={() => setIsProfileOpen(false)} />
      <AccountSettingsPanel isOpen={isAccountOpen} onClose={() => setIsAccountOpen(false)} />
      <HelpModal isOpen={isHelpOpen} onClose={() => setIsHelpOpen(false)} />
      <SignOutModal isOpen={isSignOutOpen} onClose={() => setIsSignOutOpen(false)} onConfirm={handleSignOutConfirm} />

      {isOpen && (
        <div
          ref={dropdownRef}
          className="absolute bg-white flex flex-col z-40 overflow-hidden"
          style={{
        top: 56,
        right: 24,
        width: 260,
        borderRadius: 16,
        border: "1px solid #F0F2F5",
        boxShadow: "0 16px 48px rgba(0,0,0,0.12)",
      }}
    >
      {/* Top Section */}
      <div 
        className="flex flex-col items-center justify-center pt-5 pb-[12px] border-b border-[#F0F2F5]"
      >
        <div
          className="flex items-center justify-center rounded-full mb-3 uppercase"
          style={{ 
            width: 48, height: 48, 
            backgroundColor: "#FF5C1A", 
            color: "#ffffff",
            fontFamily: "Inter, sans-serif",
            fontWeight: 700,
            fontSize: 18,
            boxShadow: "0 2px 8px rgba(255, 92, 26, 0.25)"
          }}
        >
          {profile?.full_name?.split(' ').map(n => n[0]).join('').slice(0, 2) || user?.email?.slice(0, 2) || "U"}
        </div>
        <span
          style={{
            fontFamily: "Inter, sans-serif",
            fontWeight: 600,
            fontSize: 15,
            color: "#1A1A2E",
            lineHeight: 1.2,
          }}
        >
          {profile?.full_name || user?.displayName || "User"}
        </span>
        <span
          className="mt-0.5 mb-2"
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
            color: "#94A3B8",
            lineHeight: 1.2,
          }}
        >
          {user?.email || "..."}
        </span>
        <span
          className="capitalize"
          style={{
            backgroundColor: "#FFF3EE",
            color: "#FF5C1A",
            border: "1px solid #FDDCC8",
            borderRadius: 9999,
            padding: "2px 8px",
            fontSize: 12,
            fontFamily: "Inter, sans-serif",
            fontWeight: 500,
          }}
        >
          {profile?.role || "Member"}
        </span>
      </div>

      {/* Menu Items */}
      <div className="flex flex-col p-2 gap-0.5" onClick={(e) => e.stopPropagation()}>
        
        <MenuItem icon={User} label="My Profile" onClick={() => { setIsProfileOpen(true); onClose(); }} />
        <MenuItem icon={Settings} label="Account Settings" onClick={() => { setIsAccountOpen(true); onClose(); }} />
        <MenuItem icon={Layers} label="Subscription" onClick={() => { onTabChange("subscriptions"); onClose(); }} />
        <MenuItem icon={HelpCircle} label="Help & Documentation" onClick={() => { setIsHelpOpen(true); onClose(); }} />
        
        <div style={{ height: 1, backgroundColor: "#F0F2F5", margin: "4px 0" }} />
        
        {/* Dark Mode Toggle */}
        <div
          className="flex items-center group cursor-pointer"
          style={{
            height: 40, padding: "0 16px", borderRadius: 8, transition: "background-color 150ms",
          }}
          onMouseEnter={e => e.currentTarget.style.backgroundColor = "#F8FAFC"}
          onMouseLeave={e => e.currentTarget.style.backgroundColor = "transparent"}
          onClick={toggleDarkMode}
        >
          <div className="flex items-center gap-[10px] flex-1">
            <Moon 
              size={16} 
              className="text-[#94A3B8] transition-colors group-hover:text-[#FF5C1A]"
              strokeWidth={2}
            />
            <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>
              Dark Mode
            </span>
          </div>
          
          <div 
            className="relative flex items-center transition-colors duration-200"
            style={{
              width: 36, height: 20, borderRadius: 999,
              backgroundColor: isDarkMode ? "#FF5C1A" : "#E2E8F0"
            }}
          >
            <div 
              className="absolute bg-white rounded-full transition-all duration-200 shadow-sm"
              style={{
                width: 16, height: 16, top: 2,
                left: isDarkMode ? 18 : 2
              }}
            />
          </div>
        </div>

        <div style={{ height: 1, backgroundColor: "#F0F2F5", margin: "4px 0" }} />

        {/* Log Out */}
        <div
          className="flex items-center gap-[10px] cursor-pointer"
          style={{
            height: 40, padding: "0 16px", borderRadius: 8, transition: "background-color 150ms",
          }}
          onMouseEnter={e => e.currentTarget.style.backgroundColor = "#FEF2F2"}
          onMouseLeave={e => e.currentTarget.style.backgroundColor = "transparent"}
          onClick={() => { setIsSignOutOpen(true); onClose(); }}
        >
          <LogOut size={16} color="#DC2626" strokeWidth={2} />
          <span style={{ fontSize: 14, color: "#DC2626", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>
            Sign Out
          </span>
        </div>

      </div>
        </div>
      )}
    </>
  );
}

// Helper for standard menu items
function MenuItem({ 
  icon: Icon, 
  label, 
  onClick 
}: { 
  icon: React.ElementType, 
  label: string, 
  onClick: () => void 
}) {
  return (
    <div
      className="flex items-center gap-[10px] group cursor-pointer"
      style={{
        height: 40, padding: "0 16px", borderRadius: 8, transition: "background-color 150ms",
      }}
      onMouseEnter={e => e.currentTarget.style.backgroundColor = "#F8FAFC"}
      onMouseLeave={e => e.currentTarget.style.backgroundColor = "transparent"}
      onClick={onClick}
    >
      <Icon 
        size={16} 
        className="text-[#94A3B8] transition-colors group-hover:text-[#FF5C1A]" 
        strokeWidth={2} 
      />
      <span style={{ fontSize: 14, color: "#1A1A2E", fontFamily: "Inter, sans-serif", fontWeight: 500 }}>
        {label}
      </span>
    </div>
  );
}
```

### devise-iris/frontend\src\components\ui\accordion.tsx

```tsx
import * as React from "react";
import * as AccordionPrimitive from "@radix-ui/react-accordion";
import { ChevronDown } from "lucide-react";

import { cn } from "@/lib/utils";

const Accordion = AccordionPrimitive.Root;

const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item ref={ref} className={cn("border-b", className)} {...props} />
));
AccordionItem.displayName = "AccordionItem";

const AccordionTrigger = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Header className="flex">
    <AccordionPrimitive.Trigger
      ref={ref}
      className={cn(
        "flex flex-1 items-center justify-between py-4 font-medium transition-all hover:underline [&[data-state=open]>svg]:rotate-180",
        className,
      )}
      {...props}
    >
      {children}
      <ChevronDown className="h-4 w-4 shrink-0 transition-transform duration-200" />
    </AccordionPrimitive.Trigger>
  </AccordionPrimitive.Header>
));
AccordionTrigger.displayName = AccordionPrimitive.Trigger.displayName;

const AccordionContent = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Content
    ref={ref}
    className="overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down"
    {...props}
  >
    <div className={cn("pb-4 pt-0", className)}>{children}</div>
  </AccordionPrimitive.Content>
));

AccordionContent.displayName = AccordionPrimitive.Content.displayName;

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent };
```

### devise-iris/frontend\src\components\ui\alert-dialog.tsx

```tsx
import * as React from "react";
import * as AlertDialogPrimitive from "@radix-ui/react-alert-dialog";

import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

const AlertDialog = AlertDialogPrimitive.Root;

const AlertDialogTrigger = AlertDialogPrimitive.Trigger;

const AlertDialogPortal = AlertDialogPrimitive.Portal;

const AlertDialogOverlay = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className,
    )}
    {...props}
    ref={ref}
  />
));
AlertDialogOverlay.displayName = AlertDialogPrimitive.Overlay.displayName;

const AlertDialogContent = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Content>
>(({ className, ...props }, ref) => (
  <AlertDialogPortal>
    <AlertDialogOverlay />
    <AlertDialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className,
      )}
      {...props}
    />
  </AlertDialogPortal>
));
AlertDialogContent.displayName = AlertDialogPrimitive.Content.displayName;

const AlertDialogHeader = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col space-y-2 text-center sm:text-left", className)} {...props} />
);
AlertDialogHeader.displayName = "AlertDialogHeader";

const AlertDialogFooter = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2", className)} {...props} />
);
AlertDialogFooter.displayName = "AlertDialogFooter";

const AlertDialogTitle = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Title ref={ref} className={cn("text-lg font-semibold", className)} {...props} />
));
AlertDialogTitle.displayName = AlertDialogPrimitive.Title.displayName;

const AlertDialogDescription = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Description ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
));
AlertDialogDescription.displayName = AlertDialogPrimitive.Description.displayName;

const AlertDialogAction = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Action>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Action>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Action ref={ref} className={cn(buttonVariants(), className)} {...props} />
));
AlertDialogAction.displayName = AlertDialogPrimitive.Action.displayName;

const AlertDialogCancel = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Cancel>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Cancel>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Cancel
    ref={ref}
    className={cn(buttonVariants({ variant: "outline" }), "mt-2 sm:mt-0", className)}
    {...props}
  />
));
AlertDialogCancel.displayName = AlertDialogPrimitive.Cancel.displayName;

export {
  AlertDialog,
  AlertDialogPortal,
  AlertDialogOverlay,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
};
```

### devise-iris/frontend\src\components\ui\alert.tsx

```tsx
import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const alertVariants = cva(
  "relative w-full rounded-lg border p-4 [&>svg~*]:pl-7 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive: "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
);

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div ref={ref} role="alert" className={cn(alertVariants({ variant }), className)} {...props} />
));
Alert.displayName = "Alert";

const AlertTitle = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h5 ref={ref} className={cn("mb-1 font-medium leading-none tracking-tight", className)} {...props} />
  ),
);
AlertTitle.displayName = "AlertTitle";

const AlertDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("text-sm [&_p]:leading-relaxed", className)} {...props} />
  ),
);
AlertDescription.displayName = "AlertDescription";

export { Alert, AlertTitle, AlertDescription };
```

### devise-iris/frontend\src\components\ui\aspect-ratio.tsx

```tsx
import * as AspectRatioPrimitive from "@radix-ui/react-aspect-ratio";

const AspectRatio = AspectRatioPrimitive.Root;

export { AspectRatio };
```

### devise-iris/frontend\src\components\ui\avatar.tsx

```tsx
import * as React from "react";
import * as AvatarPrimitive from "@radix-ui/react-avatar";

import { cn } from "@/lib/utils";

const Avatar = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Root
    ref={ref}
    className={cn("relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full", className)}
    {...props}
  />
));
Avatar.displayName = AvatarPrimitive.Root.displayName;

const AvatarImage = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Image>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Image>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Image ref={ref} className={cn("aspect-square h-full w-full", className)} {...props} />
));
AvatarImage.displayName = AvatarPrimitive.Image.displayName;

const AvatarFallback = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Fallback>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Fallback>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Fallback
    ref={ref}
    className={cn("flex h-full w-full items-center justify-center rounded-full bg-muted", className)}
    {...props}
  />
));
AvatarFallback.displayName = AvatarPrimitive.Fallback.displayName;

export { Avatar, AvatarImage, AvatarFallback };
```

### devise-iris/frontend\src\components\ui\badge.tsx

```tsx
import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default: "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        secondary: "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive: "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
);

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement>, VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />;
}

export { Badge, badgeVariants };
```

### devise-iris/frontend\src\components\ui\breadcrumb.tsx

```tsx
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { ChevronRight, MoreHorizontal } from "lucide-react";

import { cn } from "@/lib/utils";

const Breadcrumb = React.forwardRef<
  HTMLElement,
  React.ComponentPropsWithoutRef<"nav"> & {
    separator?: React.ReactNode;
  }
>(({ ...props }, ref) => <nav ref={ref} aria-label="breadcrumb" {...props} />);
Breadcrumb.displayName = "Breadcrumb";

const BreadcrumbList = React.forwardRef<HTMLOListElement, React.ComponentPropsWithoutRef<"ol">>(
  ({ className, ...props }, ref) => (
    <ol
      ref={ref}
      className={cn(
        "flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5",
        className,
      )}
      {...props}
    />
  ),
);
BreadcrumbList.displayName = "BreadcrumbList";

const BreadcrumbItem = React.forwardRef<HTMLLIElement, React.ComponentPropsWithoutRef<"li">>(
  ({ className, ...props }, ref) => (
    <li ref={ref} className={cn("inline-flex items-center gap-1.5", className)} {...props} />
  ),
);
BreadcrumbItem.displayName = "BreadcrumbItem";

const BreadcrumbLink = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentPropsWithoutRef<"a"> & {
    asChild?: boolean;
  }
>(({ asChild, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a";

  return <Comp ref={ref} className={cn("transition-colors hover:text-foreground", className)} {...props} />;
});
BreadcrumbLink.displayName = "BreadcrumbLink";

const BreadcrumbPage = React.forwardRef<HTMLSpanElement, React.ComponentPropsWithoutRef<"span">>(
  ({ className, ...props }, ref) => (
    <span
      ref={ref}
      role="link"
      aria-disabled="true"
      aria-current="page"
      className={cn("font-normal text-foreground", className)}
      {...props}
    />
  ),
);
BreadcrumbPage.displayName = "BreadcrumbPage";

const BreadcrumbSeparator = ({ children, className, ...props }: React.ComponentProps<"li">) => (
  <li role="presentation" aria-hidden="true" className={cn("[&>svg]:size-3.5", className)} {...props}>
    {children ?? <ChevronRight />}
  </li>
);
BreadcrumbSeparator.displayName = "BreadcrumbSeparator";

const BreadcrumbEllipsis = ({ className, ...props }: React.ComponentProps<"span">) => (
  <span
    role="presentation"
    aria-hidden="true"
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More</span>
  </span>
);
BreadcrumbEllipsis.displayName = "BreadcrumbElipssis";

export {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbEllipsis,
};
```

### devise-iris/frontend\src\components\ui\button.tsx

```tsx
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  },
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return <Comp className={cn(buttonVariants({ variant, size, className }))} ref={ref} {...props} />;
  },
);
Button.displayName = "Button";

export { Button, buttonVariants };
```

### devise-iris/frontend\src\components\ui\calendar.tsx

```tsx
import * as React from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { DayPicker } from "react-day-picker";

import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

export type CalendarProps = React.ComponentProps<typeof DayPicker>;

function Calendar({ className, classNames, showOutsideDays = true, ...props }: CalendarProps) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3", className)}
      classNames={{
        months: "flex flex-col sm:flex-row space-y-4 sm:space-x-4 sm:space-y-0",
        month: "space-y-4",
        caption: "flex justify-center pt-1 relative items-center",
        caption_label: "text-sm font-medium",
        nav: "space-x-1 flex items-center",
        nav_button: cn(
          buttonVariants({ variant: "outline" }),
          "h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100",
        ),
        nav_button_previous: "absolute left-1",
        nav_button_next: "absolute right-1",
        table: "w-full border-collapse space-y-1",
        head_row: "flex",
        head_cell: "text-muted-foreground rounded-md w-9 font-normal text-[0.8rem]",
        row: "flex w-full mt-2",
        cell: "h-9 w-9 text-center text-sm p-0 relative [&:has([aria-selected].day-range-end)]:rounded-r-md [&:has([aria-selected].day-outside)]:bg-accent/50 [&:has([aria-selected])]:bg-accent first:[&:has([aria-selected])]:rounded-l-md last:[&:has([aria-selected])]:rounded-r-md focus-within:relative focus-within:z-20",
        day: cn(buttonVariants({ variant: "ghost" }), "h-9 w-9 p-0 font-normal aria-selected:opacity-100"),
        day_range_end: "day-range-end",
        day_selected:
          "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
        day_today: "bg-accent text-accent-foreground",
        day_outside:
          "day-outside text-muted-foreground opacity-50 aria-selected:bg-accent/50 aria-selected:text-muted-foreground aria-selected:opacity-30",
        day_disabled: "text-muted-foreground opacity-50",
        day_range_middle: "aria-selected:bg-accent aria-selected:text-accent-foreground",
        day_hidden: "invisible",
        ...classNames,
      }}
      components={{
        IconLeft: ({ ..._props }) => <ChevronLeft className="h-4 w-4" />,
        IconRight: ({ ..._props }) => <ChevronRight className="h-4 w-4" />,
      }}
      {...props}
    />
  );
}
Calendar.displayName = "Calendar";

export { Calendar };
```

### devise-iris/frontend\src\components\ui\card.tsx

```tsx
import * as React from "react";

import { cn } from "@/lib/utils";

const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("rounded-lg border bg-card text-card-foreground shadow-sm", className)} {...props} />
));
Card.displayName = "Card";

const CardHeader = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("flex flex-col space-y-1.5 p-6", className)} {...props} />
  ),
);
CardHeader.displayName = "CardHeader";

const CardTitle = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h3 ref={ref} className={cn("text-2xl font-semibold leading-none tracking-tight", className)} {...props} />
  ),
);
CardTitle.displayName = "CardTitle";

const CardDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => (
    <p ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
  ),
);
CardDescription.displayName = "CardDescription";

const CardContent = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />,
);
CardContent.displayName = "CardContent";

const CardFooter = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("flex items-center p-6 pt-0", className)} {...props} />
  ),
);
CardFooter.displayName = "CardFooter";

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent };
```

### devise-iris/frontend\src\components\ui\carousel.tsx

```tsx
import * as React from "react";
import useEmblaCarousel, { type UseEmblaCarouselType } from "embla-carousel-react";
import { ArrowLeft, ArrowRight } from "lucide-react";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";

type CarouselApi = UseEmblaCarouselType[1];
type UseCarouselParameters = Parameters<typeof useEmblaCarousel>;
type CarouselOptions = UseCarouselParameters[0];
type CarouselPlugin = UseCarouselParameters[1];

type CarouselProps = {
  opts?: CarouselOptions;
  plugins?: CarouselPlugin;
  orientation?: "horizontal" | "vertical";
  setApi?: (api: CarouselApi) => void;
};

type CarouselContextProps = {
  carouselRef: ReturnType<typeof useEmblaCarousel>[0];
  api: ReturnType<typeof useEmblaCarousel>[1];
  scrollPrev: () => void;
  scrollNext: () => void;
  canScrollPrev: boolean;
  canScrollNext: boolean;
} & CarouselProps;

const CarouselContext = React.createContext<CarouselContextProps | null>(null);

function useCarousel() {
  const context = React.useContext(CarouselContext);

  if (!context) {
    throw new Error("useCarousel must be used within a <Carousel />");
  }

  return context;
}

const Carousel = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement> & CarouselProps>(
  ({ orientation = "horizontal", opts, setApi, plugins, className, children, ...props }, ref) => {
    const [carouselRef, api] = useEmblaCarousel(
      {
        ...opts,
        axis: orientation === "horizontal" ? "x" : "y",
      },
      plugins,
    );
    const [canScrollPrev, setCanScrollPrev] = React.useState(false);
    const [canScrollNext, setCanScrollNext] = React.useState(false);

    const onSelect = React.useCallback((api: CarouselApi) => {
      if (!api) {
        return;
      }

      setCanScrollPrev(api.canScrollPrev());
      setCanScrollNext(api.canScrollNext());
    }, []);

    const scrollPrev = React.useCallback(() => {
      api?.scrollPrev();
    }, [api]);

    const scrollNext = React.useCallback(() => {
      api?.scrollNext();
    }, [api]);

    const handleKeyDown = React.useCallback(
      (event: React.KeyboardEvent<HTMLDivElement>) => {
        if (event.key === "ArrowLeft") {
          event.preventDefault();
          scrollPrev();
        } else if (event.key === "ArrowRight") {
          event.preventDefault();
          scrollNext();
        }
      },
      [scrollPrev, scrollNext],
    );

    React.useEffect(() => {
      if (!api || !setApi) {
        return;
      }

      setApi(api);
    }, [api, setApi]);

    React.useEffect(() => {
      if (!api) {
        return;
      }

      onSelect(api);
      api.on("reInit", onSelect);
      api.on("select", onSelect);

      return () => {
        api?.off("select", onSelect);
      };
    }, [api, onSelect]);

    return (
      <CarouselContext.Provider
        value={{
          carouselRef,
          api: api,
          opts,
          orientation: orientation || (opts?.axis === "y" ? "vertical" : "horizontal"),
          scrollPrev,
          scrollNext,
          canScrollPrev,
          canScrollNext,
        }}
      >
        <div
          ref={ref}
          onKeyDownCapture={handleKeyDown}
          className={cn("relative", className)}
          role="region"
          aria-roledescription="carousel"
          {...props}
        >
          {children}
        </div>
      </CarouselContext.Provider>
    );
  },
);
Carousel.displayName = "Carousel";

const CarouselContent = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => {
    const { carouselRef, orientation } = useCarousel();

    return (
      <div ref={carouselRef} className="overflow-hidden">
        <div
          ref={ref}
          className={cn("flex", orientation === "horizontal" ? "-ml-4" : "-mt-4 flex-col", className)}
          {...props}
        />
      </div>
    );
  },
);
CarouselContent.displayName = "CarouselContent";

const CarouselItem = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => {
    const { orientation } = useCarousel();

    return (
      <div
        ref={ref}
        role="group"
        aria-roledescription="slide"
        className={cn("min-w-0 shrink-0 grow-0 basis-full", orientation === "horizontal" ? "pl-4" : "pt-4", className)}
        {...props}
      />
    );
  },
);
CarouselItem.displayName = "CarouselItem";

const CarouselPrevious = React.forwardRef<HTMLButtonElement, React.ComponentProps<typeof Button>>(
  ({ className, variant = "outline", size = "icon", ...props }, ref) => {
    const { orientation, scrollPrev, canScrollPrev } = useCarousel();

    return (
      <Button
        ref={ref}
        variant={variant}
        size={size}
        className={cn(
          "absolute h-8 w-8 rounded-full",
          orientation === "horizontal"
            ? "-left-12 top-1/2 -translate-y-1/2"
            : "-top-12 left-1/2 -translate-x-1/2 rotate-90",
          className,
        )}
        disabled={!canScrollPrev}
        onClick={scrollPrev}
        {...props}
      >
        <ArrowLeft className="h-4 w-4" />
        <span className="sr-only">Previous slide</span>
      </Button>
    );
  },
);
CarouselPrevious.displayName = "CarouselPrevious";

const CarouselNext = React.forwardRef<HTMLButtonElement, React.ComponentProps<typeof Button>>(
  ({ className, variant = "outline", size = "icon", ...props }, ref) => {
    const { orientation, scrollNext, canScrollNext } = useCarousel();

    return (
      <Button
        ref={ref}
        variant={variant}
        size={size}
        className={cn(
          "absolute h-8 w-8 rounded-full",
          orientation === "horizontal"
            ? "-right-12 top-1/2 -translate-y-1/2"
            : "-bottom-12 left-1/2 -translate-x-1/2 rotate-90",
          className,
        )}
        disabled={!canScrollNext}
        onClick={scrollNext}
        {...props}
      >
        <ArrowRight className="h-4 w-4" />
        <span className="sr-only">Next slide</span>
      </Button>
    );
  },
);
CarouselNext.displayName = "CarouselNext";

export { type CarouselApi, Carousel, CarouselContent, CarouselItem, CarouselPrevious, CarouselNext };
```

### devise-iris/frontend\src\components\ui\chart.tsx

```tsx
import * as React from "react";
import * as RechartsPrimitive from "recharts";

import { cn } from "@/lib/utils";

// Format: { THEME_NAME: CSS_SELECTOR }
const THEMES = { light: "", dark: ".dark" } as const;

export type ChartConfig = {
  [k in string]: {
    label?: React.ReactNode;
    icon?: React.ComponentType;
  } & ({ color?: string; theme?: never } | { color?: never; theme: Record<keyof typeof THEMES, string> });
};

type ChartContextProps = {
  config: ChartConfig;
};

const ChartContext = React.createContext<ChartContextProps | null>(null);

function useChart() {
  const context = React.useContext(ChartContext);

  if (!context) {
    throw new Error("useChart must be used within a <ChartContainer />");
  }

  return context;
}

const ChartContainer = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    config: ChartConfig;
    children: React.ComponentProps<typeof RechartsPrimitive.ResponsiveContainer>["children"];
  }
>(({ id, className, children, config, ...props }, ref) => {
  const uniqueId = React.useId();
  const chartId = `chart-${id || uniqueId.replace(/:/g, "")}`;

  return (
    <ChartContext.Provider value={{ config }}>
      <div
        data-chart={chartId}
        ref={ref}
        className={cn(
          "flex aspect-video justify-center text-xs [&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-none [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-sector]:outline-none [&_.recharts-surface]:outline-none",
          className,
        )}
        {...props}
      >
        <ChartStyle id={chartId} config={config} />
        <RechartsPrimitive.ResponsiveContainer>{children}</RechartsPrimitive.ResponsiveContainer>
      </div>
    </ChartContext.Provider>
  );
});
ChartContainer.displayName = "Chart";

const ChartStyle = ({ id, config }: { id: string; config: ChartConfig }) => {
  const colorConfig = Object.entries(config).filter(([_, config]) => config.theme || config.color);

  if (!colorConfig.length) {
    return null;
  }

  return (
    <style
      dangerouslySetInnerHTML={{
        __html: Object.entries(THEMES)
          .map(
            ([theme, prefix]) => `
${prefix} [data-chart=${id}] {
${colorConfig
  .map(([key, itemConfig]) => {
    const color = itemConfig.theme?.[theme as keyof typeof itemConfig.theme] || itemConfig.color;
    return color ? `  --color-${key}: ${color};` : null;
  })
  .join("\n")}
}
`,
          )
          .join("\n"),
      }}
    />
  );
};

const ChartTooltip = RechartsPrimitive.Tooltip;

const ChartTooltipContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<typeof RechartsPrimitive.Tooltip> &
    React.ComponentProps<"div"> & {
      hideLabel?: boolean;
      hideIndicator?: boolean;
      indicator?: "line" | "dot" | "dashed";
      nameKey?: string;
      labelKey?: string;
    }
>(
  (
    {
      active,
      payload,
      className,
      indicator = "dot",
      hideLabel = false,
      hideIndicator = false,
      label,
      labelFormatter,
      labelClassName,
      formatter,
      color,
      nameKey,
      labelKey,
    },
    ref,
  ) => {
    const { config } = useChart();

    const tooltipLabel = React.useMemo(() => {
      if (hideLabel || !payload?.length) {
        return null;
      }

      const [item] = payload;
      const key = `${labelKey || item.dataKey || item.name || "value"}`;
      const itemConfig = getPayloadConfigFromPayload(config, item, key);
      const value =
        !labelKey && typeof label === "string"
          ? config[label as keyof typeof config]?.label || label
          : itemConfig?.label;

      if (labelFormatter) {
        return <div className={cn("font-medium", labelClassName)}>{labelFormatter(value, payload)}</div>;
      }

      if (!value) {
        return null;
      }

      return <div className={cn("font-medium", labelClassName)}>{value}</div>;
    }, [label, labelFormatter, payload, hideLabel, labelClassName, config, labelKey]);

    if (!active || !payload?.length) {
      return null;
    }

    const nestLabel = payload.length === 1 && indicator !== "dot";

    return (
      <div
        ref={ref}
        className={cn(
          "grid min-w-[8rem] items-start gap-1.5 rounded-lg border border-border/50 bg-background px-2.5 py-1.5 text-xs shadow-xl",
          className,
        )}
      >
        {!nestLabel ? tooltipLabel : null}
        <div className="grid gap-1.5">
          {payload.map((item, index) => {
            const key = `${nameKey || item.name || item.dataKey || "value"}`;
            const itemConfig = getPayloadConfigFromPayload(config, item, key);
            const indicatorColor = color || item.payload.fill || item.color;

            return (
              <div
                key={item.dataKey}
                className={cn(
                  "flex w-full flex-wrap items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5 [&>svg]:text-muted-foreground",
                  indicator === "dot" && "items-center",
                )}
              >
                {formatter && item?.value !== undefined && item.name ? (
                  formatter(item.value, item.name, item, index, item.payload)
                ) : (
                  <>
                    {itemConfig?.icon ? (
                      <itemConfig.icon />
                    ) : (
                      !hideIndicator && (
                        <div
                          className={cn("shrink-0 rounded-[2px] border-[--color-border] bg-[--color-bg]", {
                            "h-2.5 w-2.5": indicator === "dot",
                            "w-1": indicator === "line",
                            "w-0 border-[1.5px] border-dashed bg-transparent": indicator === "dashed",
                            "my-0.5": nestLabel && indicator === "dashed",
                          })}
                          style={
                            {
                              "--color-bg": indicatorColor,
                              "--color-border": indicatorColor,
                            } as React.CSSProperties
                          }
                        />
                      )
                    )}
                    <div
                      className={cn(
                        "flex flex-1 justify-between leading-none",
                        nestLabel ? "items-end" : "items-center",
                      )}
                    >
                      <div className="grid gap-1.5">
                        {nestLabel ? tooltipLabel : null}
                        <span className="text-muted-foreground">{itemConfig?.label || item.name}</span>
                      </div>
                      {item.value && (
                        <span className="font-mono font-medium tabular-nums text-foreground">
                          {item.value.toLocaleString()}
                        </span>
                      )}
                    </div>
                  </>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  },
);
ChartTooltipContent.displayName = "ChartTooltip";

const ChartLegend = RechartsPrimitive.Legend;

const ChartLegendContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> &
    Pick<RechartsPrimitive.LegendProps, "payload" | "verticalAlign"> & {
      hideIcon?: boolean;
      nameKey?: string;
    }
>(({ className, hideIcon = false, payload, verticalAlign = "bottom", nameKey }, ref) => {
  const { config } = useChart();

  if (!payload?.length) {
    return null;
  }

  return (
    <div
      ref={ref}
      className={cn("flex items-center justify-center gap-4", verticalAlign === "top" ? "pb-3" : "pt-3", className)}
    >
      {payload.map((item) => {
        const key = `${nameKey || item.dataKey || "value"}`;
        const itemConfig = getPayloadConfigFromPayload(config, item, key);

        return (
          <div
            key={item.value}
            className={cn("flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3 [&>svg]:text-muted-foreground")}
          >
            {itemConfig?.icon && !hideIcon ? (
              <itemConfig.icon />
            ) : (
              <div
                className="h-2 w-2 shrink-0 rounded-[2px]"
                style={{
                  backgroundColor: item.color,
                }}
              />
            )}
            {itemConfig?.label}
          </div>
        );
      })}
    </div>
  );
});
ChartLegendContent.displayName = "ChartLegend";

// Helper to extract item config from a payload.
function getPayloadConfigFromPayload(config: ChartConfig, payload: unknown, key: string) {
  if (typeof payload !== "object" || payload === null) {
    return undefined;
  }

  const payloadPayload =
    "payload" in payload && typeof payload.payload === "object" && payload.payload !== null
      ? payload.payload
      : undefined;

  let configLabelKey: string = key;

  if (key in payload && typeof payload[key as keyof typeof payload] === "string") {
    configLabelKey = payload[key as keyof typeof payload] as string;
  } else if (
    payloadPayload &&
    key in payloadPayload &&
    typeof payloadPayload[key as keyof typeof payloadPayload] === "string"
  ) {
    configLabelKey = payloadPayload[key as keyof typeof payloadPayload] as string;
  }

  return configLabelKey in config ? config[configLabelKey] : config[key as keyof typeof config];
}

export { ChartContainer, ChartTooltip, ChartTooltipContent, ChartLegend, ChartLegendContent, ChartStyle };
```

### devise-iris/frontend\src\components\ui\checkbox.tsx

```tsx
import * as React from "react";
import * as CheckboxPrimitive from "@radix-ui/react-checkbox";
import { Check } from "lucide-react";

import { cn } from "@/lib/utils";

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>
>(({ className, ...props }, ref) => (
  <CheckboxPrimitive.Root
    ref={ref}
    className={cn(
      "peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
      className,
    )}
    {...props}
  >
    <CheckboxPrimitive.Indicator className={cn("flex items-center justify-center text-current")}>
      <Check className="h-4 w-4" />
    </CheckboxPrimitive.Indicator>
  </CheckboxPrimitive.Root>
));
Checkbox.displayName = CheckboxPrimitive.Root.displayName;

export { Checkbox };
```

### devise-iris/frontend\src\components\ui\collapsible.tsx

```tsx
import * as CollapsiblePrimitive from "@radix-ui/react-collapsible";

const Collapsible = CollapsiblePrimitive.Root;

const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger;

const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent;

export { Collapsible, CollapsibleTrigger, CollapsibleContent };
```

### devise-iris/frontend\src\components\ui\command.tsx

```tsx
import * as React from "react";
import { type DialogProps } from "@radix-ui/react-dialog";
import { Command as CommandPrimitive } from "cmdk";
import { Search } from "lucide-react";

import { cn } from "@/lib/utils";
import { Dialog, DialogContent } from "@/components/ui/dialog";

const Command = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive>
>(({ className, ...props }, ref) => (
  <CommandPrimitive
    ref={ref}
    className={cn(
      "flex h-full w-full flex-col overflow-hidden rounded-md bg-popover text-popover-foreground",
      className,
    )}
    {...props}
  />
));
Command.displayName = CommandPrimitive.displayName;

interface CommandDialogProps extends DialogProps {}

const CommandDialog = ({ children, ...props }: CommandDialogProps) => {
  return (
    <Dialog {...props}>
      <DialogContent className="overflow-hidden p-0 shadow-lg">
        <Command className="[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground [&_[cmdk-group]:not([hidden])_~[cmdk-group]]:pt-0 [&_[cmdk-group]]:px-2 [&_[cmdk-input-wrapper]_svg]:h-5 [&_[cmdk-input-wrapper]_svg]:w-5 [&_[cmdk-input]]:h-12 [&_[cmdk-item]]:px-2 [&_[cmdk-item]]:py-3 [&_[cmdk-item]_svg]:h-5 [&_[cmdk-item]_svg]:w-5">
          {children}
        </Command>
      </DialogContent>
    </Dialog>
  );
};

const CommandInput = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Input>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Input>
>(({ className, ...props }, ref) => (
  <div className="flex items-center border-b px-3" cmdk-input-wrapper="">
    <Search className="mr-2 h-4 w-4 shrink-0 opacity-50" />
    <CommandPrimitive.Input
      ref={ref}
      className={cn(
        "flex h-11 w-full rounded-md bg-transparent py-3 text-sm outline-none placeholder:text-muted-foreground disabled:cursor-not-allowed disabled:opacity-50",
        className,
      )}
      {...props}
    />
  </div>
));

CommandInput.displayName = CommandPrimitive.Input.displayName;

const CommandList = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.List>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.List
    ref={ref}
    className={cn("max-h-[300px] overflow-y-auto overflow-x-hidden", className)}
    {...props}
  />
));

CommandList.displayName = CommandPrimitive.List.displayName;

const CommandEmpty = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Empty>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Empty>
>((props, ref) => <CommandPrimitive.Empty ref={ref} className="py-6 text-center text-sm" {...props} />);

CommandEmpty.displayName = CommandPrimitive.Empty.displayName;

const CommandGroup = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Group>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Group>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Group
    ref={ref}
    className={cn(
      "overflow-hidden p-1 text-foreground [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-xs [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground",
      className,
    )}
    {...props}
  />
));

CommandGroup.displayName = CommandPrimitive.Group.displayName;

const CommandSeparator = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Separator ref={ref} className={cn("-mx-1 h-px bg-border", className)} {...props} />
));
CommandSeparator.displayName = CommandPrimitive.Separator.displayName;

const CommandItem = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Item>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[disabled=true]:pointer-events-none data-[selected='true']:bg-accent data-[selected=true]:text-accent-foreground data-[disabled=true]:opacity-50",
      className,
    )}
    {...props}
  />
));

CommandItem.displayName = CommandPrimitive.Item.displayName;

const CommandShortcut = ({ className, ...props }: React.HTMLAttributes<HTMLSpanElement>) => {
  return <span className={cn("ml-auto text-xs tracking-widest text-muted-foreground", className)} {...props} />;
};
CommandShortcut.displayName = "CommandShortcut";

export {
  Command,
  CommandDialog,
  CommandInput,
  CommandList,
  CommandEmpty,
  CommandGroup,
  CommandItem,
  CommandShortcut,
  CommandSeparator,
};
```

### devise-iris/frontend\src\components\ui\context-menu.tsx

```tsx
import * as React from "react";
import * as ContextMenuPrimitive from "@radix-ui/react-context-menu";
import { Check, ChevronRight, Circle } from "lucide-react";

import { cn } from "@/lib/utils";

const ContextMenu = ContextMenuPrimitive.Root;

const ContextMenuTrigger = ContextMenuPrimitive.Trigger;

const ContextMenuGroup = ContextMenuPrimitive.Group;

const ContextMenuPortal = ContextMenuPrimitive.Portal;

const ContextMenuSub = ContextMenuPrimitive.Sub;

const ContextMenuRadioGroup = ContextMenuPrimitive.RadioGroup;

const ContextMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubTrigger> & {
    inset?: boolean;
  }
>(({ className, inset, children, ...props }, ref) => (
  <ContextMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[state=open]:bg-accent data-[state=open]:text-accent-foreground focus:bg-accent focus:text-accent-foreground",
      inset && "pl-8",
      className,
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </ContextMenuPrimitive.SubTrigger>
));
ContextMenuSubTrigger.displayName = ContextMenuPrimitive.SubTrigger.displayName;

const ContextMenuSubContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className,
    )}
    {...props}
  />
));
ContextMenuSubContent.displayName = ContextMenuPrimitive.SubContent.displayName;

const ContextMenuContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Portal>
    <ContextMenuPrimitive.Content
      ref={ref}
      className={cn(
        "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md animate-in fade-in-80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className,
      )}
      {...props}
    />
  </ContextMenuPrimitive.Portal>
));
ContextMenuContent.displayName = ContextMenuPrimitive.Content.displayName;

const ContextMenuItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Item> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      inset && "pl-8",
      className,
    )}
    {...props}
  />
));
ContextMenuItem.displayName = ContextMenuPrimitive.Item.displayName;

const ContextMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <ContextMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.CheckboxItem>
));
ContextMenuCheckboxItem.displayName = ContextMenuPrimitive.CheckboxItem.displayName;

const ContextMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <ContextMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.RadioItem>
));
ContextMenuRadioItem.displayName = ContextMenuPrimitive.RadioItem.displayName;

const ContextMenuLabel = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Label> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold text-foreground", inset && "pl-8", className)}
    {...props}
  />
));
ContextMenuLabel.displayName = ContextMenuPrimitive.Label.displayName;

const ContextMenuSeparator = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Separator ref={ref} className={cn("-mx-1 my-1 h-px bg-border", className)} {...props} />
));
ContextMenuSeparator.displayName = ContextMenuPrimitive.Separator.displayName;

const ContextMenuShortcut = ({ className, ...props }: React.HTMLAttributes<HTMLSpanElement>) => {
  return <span className={cn("ml-auto text-xs tracking-widest text-muted-foreground", className)} {...props} />;
};
ContextMenuShortcut.displayName = "ContextMenuShortcut";

export {
  ContextMenu,
  ContextMenuTrigger,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuCheckboxItem,
  ContextMenuRadioItem,
  ContextMenuLabel,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuGroup,
  ContextMenuPortal,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuRadioGroup,
};
```

### devise-iris/frontend\src\components\ui\dialog.tsx

```tsx
import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";

import { cn } from "@/lib/utils";

const Dialog = DialogPrimitive.Root;

const DialogTrigger = DialogPrimitive.Trigger;

const DialogPortal = DialogPrimitive.Portal;

const DialogClose = DialogPrimitive.Close;

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className,
    )}
    {...props}
  />
));
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName;

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className,
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity data-[state=open]:bg-accent data-[state=open]:text-muted-foreground hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
));
DialogContent.displayName = DialogPrimitive.Content.displayName;

const DialogHeader = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col space-y-1.5 text-center sm:text-left", className)} {...props} />
);
DialogHeader.displayName = "DialogHeader";

const DialogFooter = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2", className)} {...props} />
);
DialogFooter.displayName = "DialogFooter";

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold leading-none tracking-tight", className)}
    {...props}
  />
));
DialogTitle.displayName = DialogPrimitive.Title.displayName;

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
));
DialogDescription.displayName = DialogPrimitive.Description.displayName;

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogClose,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
};
```

### devise-iris/frontend\src\components\ui\drawer.tsx

```tsx
import * as React from "react";
import { Drawer as DrawerPrimitive } from "vaul";

import { cn } from "@/lib/utils";

const Drawer = ({ shouldScaleBackground = true, ...props }: React.ComponentProps<typeof DrawerPrimitive.Root>) => (
  <DrawerPrimitive.Root shouldScaleBackground={shouldScaleBackground} {...props} />
);
Drawer.displayName = "Drawer";

const DrawerTrigger = DrawerPrimitive.Trigger;

const DrawerPortal = DrawerPrimitive.Portal;

const DrawerClose = DrawerPrimitive.Close;

const DrawerOverlay = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Overlay ref={ref} className={cn("fixed inset-0 z-50 bg-black/80", className)} {...props} />
));
DrawerOverlay.displayName = DrawerPrimitive.Overlay.displayName;

const DrawerContent = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DrawerPortal>
    <DrawerOverlay />
    <DrawerPrimitive.Content
      ref={ref}
      className={cn(
        "fixed inset-x-0 bottom-0 z-50 mt-24 flex h-auto flex-col rounded-t-[10px] border bg-background",
        className,
      )}
      {...props}
    >
      <div className="mx-auto mt-4 h-2 w-[100px] rounded-full bg-muted" />
      {children}
    </DrawerPrimitive.Content>
  </DrawerPortal>
));
DrawerContent.displayName = "DrawerContent";

const DrawerHeader = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("grid gap-1.5 p-4 text-center sm:text-left", className)} {...props} />
);
DrawerHeader.displayName = "DrawerHeader";

const DrawerFooter = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("mt-auto flex flex-col gap-2 p-4", className)} {...props} />
);
DrawerFooter.displayName = "DrawerFooter";

const DrawerTitle = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold leading-none tracking-tight", className)}
    {...props}
  />
));
DrawerTitle.displayName = DrawerPrimitive.Title.displayName;

const DrawerDescription = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Description ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
));
DrawerDescription.displayName = DrawerPrimitive.Description.displayName;

export {
  Drawer,
  DrawerPortal,
  DrawerOverlay,
  DrawerTrigger,
  DrawerClose,
  DrawerContent,
  DrawerHeader,
  DrawerFooter,
  DrawerTitle,
  DrawerDescription,
};
```

### devise-iris/frontend\src\components\ui\dropdown-menu.tsx

```tsx
import * as React from "react";
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu";
import { Check, ChevronRight, Circle } from "lucide-react";

import { cn } from "@/lib/utils";

const DropdownMenu = DropdownMenuPrimitive.Root;

const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger;

const DropdownMenuGroup = DropdownMenuPrimitive.Group;

const DropdownMenuPortal = DropdownMenuPrimitive.Portal;

const DropdownMenuSub = DropdownMenuPrimitive.Sub;

const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup;

const DropdownMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubTrigger> & {
    inset?: boolean;
  }
>(({ className, inset, children, ...props }, ref) => (
  <DropdownMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[state=open]:bg-accent focus:bg-accent",
      inset && "pl-8",
      className,
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </DropdownMenuPrimitive.SubTrigger>
));
DropdownMenuSubTrigger.displayName = DropdownMenuPrimitive.SubTrigger.displayName;

const DropdownMenuSubContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className,
    )}
    {...props}
  />
));
DropdownMenuSubContent.displayName = DropdownMenuPrimitive.SubContent.displayName;

const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className,
      )}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
));
DropdownMenuContent.displayName = DropdownMenuPrimitive.Content.displayName;

const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none transition-colors data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      inset && "pl-8",
      className,
    )}
    {...props}
  />
));
DropdownMenuItem.displayName = DropdownMenuPrimitive.Item.displayName;

const DropdownMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <DropdownMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.CheckboxItem>
));
DropdownMenuCheckboxItem.displayName = DropdownMenuPrimitive.CheckboxItem.displayName;

const DropdownMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <DropdownMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.RadioItem>
));
DropdownMenuRadioItem.displayName = DropdownMenuPrimitive.RadioItem.displayName;

const DropdownMenuLabel = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Label> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold", inset && "pl-8", className)}
    {...props}
  />
));
DropdownMenuLabel.displayName = DropdownMenuPrimitive.Label.displayName;

const DropdownMenuSeparator = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Separator ref={ref} className={cn("-mx-1 my-1 h-px bg-muted", className)} {...props} />
));
DropdownMenuSeparator.displayName = DropdownMenuPrimitive.Separator.displayName;

const DropdownMenuShortcut = ({ className, ...props }: React.HTMLAttributes<HTMLSpanElement>) => {
  return <span className={cn("ml-auto text-xs tracking-widest opacity-60", className)} {...props} />;
};
DropdownMenuShortcut.displayName = "DropdownMenuShortcut";

export {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuPortal,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuRadioGroup,
};
```

### devise-iris/frontend\src\components\ui\form.tsx

```tsx
import * as React from "react";
import * as LabelPrimitive from "@radix-ui/react-label";
import { Slot } from "@radix-ui/react-slot";
import { Controller, ControllerProps, FieldPath, FieldValues, FormProvider, useFormContext } from "react-hook-form";

import { cn } from "@/lib/utils";
import { Label } from "@/components/ui/label";

const Form = FormProvider;

type FormFieldContextValue<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  name: TName;
};

const FormFieldContext = React.createContext<FormFieldContextValue>({} as FormFieldContextValue);

const FormField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  );
};

const useFormField = () => {
  const fieldContext = React.useContext(FormFieldContext);
  const itemContext = React.useContext(FormItemContext);
  const { getFieldState, formState } = useFormContext();

  const fieldState = getFieldState(fieldContext.name, formState);

  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>");
  }

  const { id } = itemContext;

  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  };
};

type FormItemContextValue = {
  id: string;
};

const FormItemContext = React.createContext<FormItemContextValue>({} as FormItemContextValue);

const FormItem = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => {
    const id = React.useId();

    return (
      <FormItemContext.Provider value={{ id }}>
        <div ref={ref} className={cn("space-y-2", className)} {...props} />
      </FormItemContext.Provider>
    );
  },
);
FormItem.displayName = "FormItem";

const FormLabel = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root>
>(({ className, ...props }, ref) => {
  const { error, formItemId } = useFormField();

  return <Label ref={ref} className={cn(error && "text-destructive", className)} htmlFor={formItemId} {...props} />;
});
FormLabel.displayName = "FormLabel";

const FormControl = React.forwardRef<React.ElementRef<typeof Slot>, React.ComponentPropsWithoutRef<typeof Slot>>(
  ({ ...props }, ref) => {
    const { error, formItemId, formDescriptionId, formMessageId } = useFormField();

    return (
      <Slot
        ref={ref}
        id={formItemId}
        aria-describedby={!error ? `${formDescriptionId}` : `${formDescriptionId} ${formMessageId}`}
        aria-invalid={!!error}
        {...props}
      />
    );
  },
);
FormControl.displayName = "FormControl";

const FormDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => {
    const { formDescriptionId } = useFormField();

    return <p ref={ref} id={formDescriptionId} className={cn("text-sm text-muted-foreground", className)} {...props} />;
  },
);
FormDescription.displayName = "FormDescription";

const FormMessage = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, children, ...props }, ref) => {
    const { error, formMessageId } = useFormField();
    const body = error ? String(error?.message) : children;

    if (!body) {
      return null;
    }

    return (
      <p ref={ref} id={formMessageId} className={cn("text-sm font-medium text-destructive", className)} {...props}>
        {body}
      </p>
    );
  },
);
FormMessage.displayName = "FormMessage";

export { useFormField, Form, FormItem, FormLabel, FormControl, FormDescription, FormMessage, FormField };
```

### devise-iris/frontend\src\components\ui\hover-card.tsx

```tsx
import * as React from "react";
import * as HoverCardPrimitive from "@radix-ui/react-hover-card";

import { cn } from "@/lib/utils";

const HoverCard = HoverCardPrimitive.Root;

const HoverCardTrigger = HoverCardPrimitive.Trigger;

const HoverCardContent = React.forwardRef<
  React.ElementRef<typeof HoverCardPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof HoverCardPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <HoverCardPrimitive.Content
    ref={ref}
    align={align}
    sideOffset={sideOffset}
    className={cn(
      "z-50 w-64 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className,
    )}
    {...props}
  />
));
HoverCardContent.displayName = HoverCardPrimitive.Content.displayName;

export { HoverCard, HoverCardTrigger, HoverCardContent };
```

### devise-iris/frontend\src\components\ui\input-otp.tsx

```tsx
import * as React from "react";
import { OTPInput, OTPInputContext } from "input-otp";
import { Dot } from "lucide-react";

import { cn } from "@/lib/utils";

const InputOTP = React.forwardRef<React.ElementRef<typeof OTPInput>, React.ComponentPropsWithoutRef<typeof OTPInput>>(
  ({ className, containerClassName, ...props }, ref) => (
    <OTPInput
      ref={ref}
      containerClassName={cn("flex items-center gap-2 has-[:disabled]:opacity-50", containerClassName)}
      className={cn("disabled:cursor-not-allowed", className)}
      {...props}
    />
  ),
);
InputOTP.displayName = "InputOTP";

const InputOTPGroup = React.forwardRef<React.ElementRef<"div">, React.ComponentPropsWithoutRef<"div">>(
  ({ className, ...props }, ref) => <div ref={ref} className={cn("flex items-center", className)} {...props} />,
);
InputOTPGroup.displayName = "InputOTPGroup";

const InputOTPSlot = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div"> & { index: number }
>(({ index, className, ...props }, ref) => {
  const inputOTPContext = React.useContext(OTPInputContext);
  const { char, hasFakeCaret, isActive } = inputOTPContext.slots[index];

  return (
    <div
      ref={ref}
      className={cn(
        "relative flex h-10 w-10 items-center justify-center border-y border-r border-input text-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md",
        isActive && "z-10 ring-2 ring-ring ring-offset-background",
        className,
      )}
      {...props}
    >
      {char}
      {hasFakeCaret && (
        <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
          <div className="animate-caret-blink h-4 w-px bg-foreground duration-1000" />
        </div>
      )}
    </div>
  );
});
InputOTPSlot.displayName = "InputOTPSlot";

const InputOTPSeparator = React.forwardRef<React.ElementRef<"div">, React.ComponentPropsWithoutRef<"div">>(
  ({ ...props }, ref) => (
    <div ref={ref} role="separator" {...props}>
      <Dot />
    </div>
  ),
);
InputOTPSeparator.displayName = "InputOTPSeparator";

export { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator };
```

### devise-iris/frontend\src\components\ui\input.tsx

```tsx
import * as React from "react";

import { cn } from "@/lib/utils";

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className,
        )}
        ref={ref}
        {...props}
      />
    );
  },
);
Input.displayName = "Input";

export { Input };
```

### devise-iris/frontend\src\components\ui\label.tsx

```tsx
import * as React from "react";
import * as LabelPrimitive from "@radix-ui/react-label";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const labelVariants = cva("text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70");

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> & VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root ref={ref} className={cn(labelVariants(), className)} {...props} />
));
Label.displayName = LabelPrimitive.Root.displayName;

export { Label };
```

### devise-iris/frontend\src\components\ui\menubar.tsx

```tsx
import * as React from "react";
import * as MenubarPrimitive from "@radix-ui/react-menubar";
import { Check, ChevronRight, Circle } from "lucide-react";

import { cn } from "@/lib/utils";

const MenubarMenu = MenubarPrimitive.Menu;

const MenubarGroup = MenubarPrimitive.Group;

const MenubarPortal = MenubarPrimitive.Portal;

const MenubarSub = MenubarPrimitive.Sub;

const MenubarRadioGroup = MenubarPrimitive.RadioGroup;

const Menubar = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Root
    ref={ref}
    className={cn("flex h-10 items-center space-x-1 rounded-md border bg-background p-1", className)}
    {...props}
  />
));
Menubar.displayName = MenubarPrimitive.Root.displayName;

const MenubarTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-3 py-1.5 text-sm font-medium outline-none data-[state=open]:bg-accent data-[state=open]:text-accent-foreground focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    {...props}
  />
));
MenubarTrigger.displayName = MenubarPrimitive.Trigger.displayName;

const MenubarSubTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubTrigger> & {
    inset?: boolean;
  }
>(({ className, inset, children, ...props }, ref) => (
  <MenubarPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[state=open]:bg-accent data-[state=open]:text-accent-foreground focus:bg-accent focus:text-accent-foreground",
      inset && "pl-8",
      className,
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </MenubarPrimitive.SubTrigger>
));
MenubarSubTrigger.displayName = MenubarPrimitive.SubTrigger.displayName;

const MenubarSubContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className,
    )}
    {...props}
  />
));
MenubarSubContent.displayName = MenubarPrimitive.SubContent.displayName;

const MenubarContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Content>
>(({ className, align = "start", alignOffset = -4, sideOffset = 8, ...props }, ref) => (
  <MenubarPrimitive.Portal>
    <MenubarPrimitive.Content
      ref={ref}
      align={align}
      alignOffset={alignOffset}
      sideOffset={sideOffset}
      className={cn(
        "z-50 min-w-[12rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className,
      )}
      {...props}
    />
  </MenubarPrimitive.Portal>
));
MenubarContent.displayName = MenubarPrimitive.Content.displayName;

const MenubarItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Item> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      inset && "pl-8",
      className,
    )}
    {...props}
  />
));
MenubarItem.displayName = MenubarPrimitive.Item.displayName;

const MenubarCheckboxItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <MenubarPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.CheckboxItem>
));
MenubarCheckboxItem.displayName = MenubarPrimitive.CheckboxItem.displayName;

const MenubarRadioItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <MenubarPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.RadioItem>
));
MenubarRadioItem.displayName = MenubarPrimitive.RadioItem.displayName;

const MenubarLabel = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Label> & {
    inset?: boolean;
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold", inset && "pl-8", className)}
    {...props}
  />
));
MenubarLabel.displayName = MenubarPrimitive.Label.displayName;

const MenubarSeparator = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Separator ref={ref} className={cn("-mx-1 my-1 h-px bg-muted", className)} {...props} />
));
MenubarSeparator.displayName = MenubarPrimitive.Separator.displayName;

const MenubarShortcut = ({ className, ...props }: React.HTMLAttributes<HTMLSpanElement>) => {
  return <span className={cn("ml-auto text-xs tracking-widest text-muted-foreground", className)} {...props} />;
};
MenubarShortcut.displayname = "MenubarShortcut";

export {
  Menubar,
  MenubarMenu,
  MenubarTrigger,
  MenubarContent,
  MenubarItem,
  MenubarSeparator,
  MenubarLabel,
  MenubarCheckboxItem,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarPortal,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarGroup,
  MenubarSub,
  MenubarShortcut,
};
```

### devise-iris/frontend\src\components\ui\navigation-menu.tsx

```tsx
import * as React from "react";
import * as NavigationMenuPrimitive from "@radix-ui/react-navigation-menu";
import { cva } from "class-variance-authority";
import { ChevronDown } from "lucide-react";

import { cn } from "@/lib/utils";

const NavigationMenu = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Root
    ref={ref}
    className={cn("relative z-10 flex max-w-max flex-1 items-center justify-center", className)}
    {...props}
  >
    {children}
    <NavigationMenuViewport />
  </NavigationMenuPrimitive.Root>
));
NavigationMenu.displayName = NavigationMenuPrimitive.Root.displayName;

const NavigationMenuList = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.List>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.List
    ref={ref}
    className={cn("group flex flex-1 list-none items-center justify-center space-x-1", className)}
    {...props}
  />
));
NavigationMenuList.displayName = NavigationMenuPrimitive.List.displayName;

const NavigationMenuItem = NavigationMenuPrimitive.Item;

const navigationMenuTriggerStyle = cva(
  "group inline-flex h-10 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground focus:outline-none disabled:pointer-events-none disabled:opacity-50 data-[active]:bg-accent/50 data-[state=open]:bg-accent/50",
);

const NavigationMenuTrigger = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Trigger
    ref={ref}
    className={cn(navigationMenuTriggerStyle(), "group", className)}
    {...props}
  >
    {children}{" "}
    <ChevronDown
      className="relative top-[1px] ml-1 h-3 w-3 transition duration-200 group-data-[state=open]:rotate-180"
      aria-hidden="true"
    />
  </NavigationMenuPrimitive.Trigger>
));
NavigationMenuTrigger.displayName = NavigationMenuPrimitive.Trigger.displayName;

const NavigationMenuContent = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Content
    ref={ref}
    className={cn(
      "left-0 top-0 w-full data-[motion^=from-]:animate-in data-[motion^=to-]:animate-out data-[motion^=from-]:fade-in data-[motion^=to-]:fade-out data-[motion=from-end]:slide-in-from-right-52 data-[motion=from-start]:slide-in-from-left-52 data-[motion=to-end]:slide-out-to-right-52 data-[motion=to-start]:slide-out-to-left-52 md:absolute md:w-auto",
      className,
    )}
    {...props}
  />
));
NavigationMenuContent.displayName = NavigationMenuPrimitive.Content.displayName;

const NavigationMenuLink = NavigationMenuPrimitive.Link;

const NavigationMenuViewport = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Viewport>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Viewport>
>(({ className, ...props }, ref) => (
  <div className={cn("absolute left-0 top-full flex justify-center")}>
    <NavigationMenuPrimitive.Viewport
      className={cn(
        "origin-top-center relative mt-1.5 h-[var(--radix-navigation-menu-viewport-height)] w-full overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-90 md:w-[var(--radix-navigation-menu-viewport-width)]",
        className,
      )}
      ref={ref}
      {...props}
    />
  </div>
));
NavigationMenuViewport.displayName = NavigationMenuPrimitive.Viewport.displayName;

const NavigationMenuIndicator = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Indicator>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Indicator>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Indicator
    ref={ref}
    className={cn(
      "top-full z-[1] flex h-1.5 items-end justify-center overflow-hidden data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:fade-in",
      className,
    )}
    {...props}
  >
    <div className="relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm bg-border shadow-md" />
  </NavigationMenuPrimitive.Indicator>
));
NavigationMenuIndicator.displayName = NavigationMenuPrimitive.Indicator.displayName;

export {
  navigationMenuTriggerStyle,
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuContent,
  NavigationMenuTrigger,
  NavigationMenuLink,
  NavigationMenuIndicator,
  NavigationMenuViewport,
};
```

### devise-iris/frontend\src\components\ui\pagination.tsx

```tsx
import * as React from "react";
import { ChevronLeft, ChevronRight, MoreHorizontal } from "lucide-react";

import { cn } from "@/lib/utils";
import { ButtonProps, buttonVariants } from "@/components/ui/button";

const Pagination = ({ className, ...props }: React.ComponentProps<"nav">) => (
  <nav
    role="navigation"
    aria-label="pagination"
    className={cn("mx-auto flex w-full justify-center", className)}
    {...props}
  />
);
Pagination.displayName = "Pagination";

const PaginationContent = React.forwardRef<HTMLUListElement, React.ComponentProps<"ul">>(
  ({ className, ...props }, ref) => (
    <ul ref={ref} className={cn("flex flex-row items-center gap-1", className)} {...props} />
  ),
);
PaginationContent.displayName = "PaginationContent";

const PaginationItem = React.forwardRef<HTMLLIElement, React.ComponentProps<"li">>(({ className, ...props }, ref) => (
  <li ref={ref} className={cn("", className)} {...props} />
));
PaginationItem.displayName = "PaginationItem";

type PaginationLinkProps = {
  isActive?: boolean;
} & Pick<ButtonProps, "size"> &
  React.ComponentProps<"a">;

const PaginationLink = ({ className, isActive, size = "icon", ...props }: PaginationLinkProps) => (
  <a
    aria-current={isActive ? "page" : undefined}
    className={cn(
      buttonVariants({
        variant: isActive ? "outline" : "ghost",
        size,
      }),
      className,
    )}
    {...props}
  />
);
PaginationLink.displayName = "PaginationLink";

const PaginationPrevious = ({ className, ...props }: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink aria-label="Go to previous page" size="default" className={cn("gap-1 pl-2.5", className)} {...props}>
    <ChevronLeft className="h-4 w-4" />
    <span>Previous</span>
  </PaginationLink>
);
PaginationPrevious.displayName = "PaginationPrevious";

const PaginationNext = ({ className, ...props }: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink aria-label="Go to next page" size="default" className={cn("gap-1 pr-2.5", className)} {...props}>
    <span>Next</span>
    <ChevronRight className="h-4 w-4" />
  </PaginationLink>
);
PaginationNext.displayName = "PaginationNext";

const PaginationEllipsis = ({ className, ...props }: React.ComponentProps<"span">) => (
  <span aria-hidden className={cn("flex h-9 w-9 items-center justify-center", className)} {...props}>
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More pages</span>
  </span>
);
PaginationEllipsis.displayName = "PaginationEllipsis";

export {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
};
```

### devise-iris/frontend\src\components\ui\popover.tsx

```tsx
import * as React from "react";
import * as PopoverPrimitive from "@radix-ui/react-popover";

import { cn } from "@/lib/utils";

const Popover = PopoverPrimitive.Root;

const PopoverTrigger = PopoverPrimitive.Trigger;

const PopoverContent = React.forwardRef<
  React.ElementRef<typeof PopoverPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof PopoverPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <PopoverPrimitive.Portal>
    <PopoverPrimitive.Content
      ref={ref}
      align={align}
      sideOffset={sideOffset}
      className={cn(
        "z-50 w-72 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className,
      )}
      {...props}
    />
  </PopoverPrimitive.Portal>
));
PopoverContent.displayName = PopoverPrimitive.Content.displayName;

export { Popover, PopoverTrigger, PopoverContent };
```

### devise-iris/frontend\src\components\ui\progress.tsx

```tsx
import * as React from "react";
import * as ProgressPrimitive from "@radix-ui/react-progress";

import { cn } from "@/lib/utils";

const Progress = React.forwardRef<
  React.ElementRef<typeof ProgressPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ProgressPrimitive.Root>
>(({ className, value, ...props }, ref) => (
  <ProgressPrimitive.Root
    ref={ref}
    className={cn("relative h-4 w-full overflow-hidden rounded-full bg-secondary", className)}
    {...props}
  >
    <ProgressPrimitive.Indicator
      className="h-full w-full flex-1 bg-primary transition-all"
      style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
    />
  </ProgressPrimitive.Root>
));
Progress.displayName = ProgressPrimitive.Root.displayName;

export { Progress };
```

### devise-iris/frontend\src\components\ui\radio-group.tsx

```tsx
import * as React from "react";
import * as RadioGroupPrimitive from "@radix-ui/react-radio-group";
import { Circle } from "lucide-react";

import { cn } from "@/lib/utils";

const RadioGroup = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Root>
>(({ className, ...props }, ref) => {
  return <RadioGroupPrimitive.Root className={cn("grid gap-2", className)} {...props} ref={ref} />;
});
RadioGroup.displayName = RadioGroupPrimitive.Root.displayName;

const RadioGroupItem = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Item>
>(({ className, ...props }, ref) => {
  return (
    <RadioGroupPrimitive.Item
      ref={ref}
      className={cn(
        "aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
        className,
      )}
      {...props}
    >
      <RadioGroupPrimitive.Indicator className="flex items-center justify-center">
        <Circle className="h-2.5 w-2.5 fill-current text-current" />
      </RadioGroupPrimitive.Indicator>
    </RadioGroupPrimitive.Item>
  );
});
RadioGroupItem.displayName = RadioGroupPrimitive.Item.displayName;

export { RadioGroup, RadioGroupItem };
```

### devise-iris/frontend\src\components\ui\resizable.tsx

```tsx
import { GripVertical } from "lucide-react";
import * as ResizablePrimitive from "react-resizable-panels";

import { cn } from "@/lib/utils";

const ResizablePanelGroup = ({ className, ...props }: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) => (
  <ResizablePrimitive.PanelGroup
    className={cn("flex h-full w-full data-[panel-group-direction=vertical]:flex-col", className)}
    {...props}
  />
);

const ResizablePanel = ResizablePrimitive.Panel;

const ResizableHandle = ({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean;
}) => (
  <ResizablePrimitive.PanelResizeHandle
    className={cn(
      "relative flex w-px items-center justify-center bg-border after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:-translate-y-1/2 data-[panel-group-direction=vertical]:after:translate-x-0 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring focus-visible:ring-offset-1 [&[data-panel-group-direction=vertical]>div]:rotate-90",
      className,
    )}
    {...props}
  >
    {withHandle && (
      <div className="z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border">
        <GripVertical className="h-2.5 w-2.5" />
      </div>
    )}
  </ResizablePrimitive.PanelResizeHandle>
);

export { ResizablePanelGroup, ResizablePanel, ResizableHandle };
```

### devise-iris/frontend\src\components\ui\scroll-area.tsx

```tsx
import * as React from "react";
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area";

import { cn } from "@/lib/utils";

const ScrollArea = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <ScrollAreaPrimitive.Root ref={ref} className={cn("relative overflow-hidden", className)} {...props}>
    <ScrollAreaPrimitive.Viewport className="h-full w-full rounded-[inherit]">{children}</ScrollAreaPrimitive.Viewport>
    <ScrollBar />
    <ScrollAreaPrimitive.Corner />
  </ScrollAreaPrimitive.Root>
));
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName;

const ScrollBar = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({ className, orientation = "vertical", ...props }, ref) => (
  <ScrollAreaPrimitive.ScrollAreaScrollbar
    ref={ref}
    orientation={orientation}
    className={cn(
      "flex touch-none select-none transition-colors",
      orientation === "vertical" && "h-full w-2.5 border-l border-l-transparent p-[1px]",
      orientation === "horizontal" && "h-2.5 flex-col border-t border-t-transparent p-[1px]",
      className,
    )}
    {...props}
  >
    <ScrollAreaPrimitive.ScrollAreaThumb className="relative flex-1 rounded-full bg-border" />
  </ScrollAreaPrimitive.ScrollAreaScrollbar>
));
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName;

export { ScrollArea, ScrollBar };
```

### devise-iris/frontend\src\components\ui\select.tsx

```tsx
import * as React from "react";
import * as SelectPrimitive from "@radix-ui/react-select";
import { Check, ChevronDown, ChevronUp } from "lucide-react";

import { cn } from "@/lib/utils";

const Select = SelectPrimitive.Root;

const SelectGroup = SelectPrimitive.Group;

const SelectValue = SelectPrimitive.Value;

const SelectTrigger = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1",
      className,
    )}
    {...props}
  >
    {children}
    <SelectPrimitive.Icon asChild>
      <ChevronDown className="h-4 w-4 opacity-50" />
    </SelectPrimitive.Icon>
  </SelectPrimitive.Trigger>
));
SelectTrigger.displayName = SelectPrimitive.Trigger.displayName;

const SelectScrollUpButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollUpButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollUpButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollUpButton
    ref={ref}
    className={cn("flex cursor-default items-center justify-center py-1", className)}
    {...props}
  >
    <ChevronUp className="h-4 w-4" />
  </SelectPrimitive.ScrollUpButton>
));
SelectScrollUpButton.displayName = SelectPrimitive.ScrollUpButton.displayName;

const SelectScrollDownButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollDownButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollDownButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollDownButton
    ref={ref}
    className={cn("flex cursor-default items-center justify-center py-1", className)}
    {...props}
  >
    <ChevronDown className="h-4 w-4" />
  </SelectPrimitive.ScrollDownButton>
));
SelectScrollDownButton.displayName = SelectPrimitive.ScrollDownButton.displayName;

const SelectContent = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Content>
>(({ className, children, position = "popper", ...props }, ref) => (
  <SelectPrimitive.Portal>
    <SelectPrimitive.Content
      ref={ref}
      className={cn(
        "relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        position === "popper" &&
          "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
        className,
      )}
      position={position}
      {...props}
    >
      <SelectScrollUpButton />
      <SelectPrimitive.Viewport
        className={cn(
          "p-1",
          position === "popper" &&
            "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)]",
        )}
      >
        {children}
      </SelectPrimitive.Viewport>
      <SelectScrollDownButton />
    </SelectPrimitive.Content>
  </SelectPrimitive.Portal>
));
SelectContent.displayName = SelectPrimitive.Content.displayName;

const SelectLabel = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Label>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Label ref={ref} className={cn("py-1.5 pl-8 pr-2 text-sm font-semibold", className)} {...props} />
));
SelectLabel.displayName = SelectPrimitive.Label.displayName;

const SelectItem = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Item>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground",
      className,
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <SelectPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </SelectPrimitive.ItemIndicator>
    </span>

    <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
  </SelectPrimitive.Item>
));
SelectItem.displayName = SelectPrimitive.Item.displayName;

const SelectSeparator = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Separator ref={ref} className={cn("-mx-1 my-1 h-px bg-muted", className)} {...props} />
));
SelectSeparator.displayName = SelectPrimitive.Separator.displayName;

export {
  Select,
  SelectGroup,
  SelectValue,
  SelectTrigger,
  SelectContent,
  SelectLabel,
  SelectItem,
  SelectSeparator,
  SelectScrollUpButton,
  SelectScrollDownButton,
};
```

### devise-iris/frontend\src\components\ui\separator.tsx

```tsx
import * as React from "react";
import * as SeparatorPrimitive from "@radix-ui/react-separator";

import { cn } from "@/lib/utils";

const Separator = React.forwardRef<
  React.ElementRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(({ className, orientation = "horizontal", decorative = true, ...props }, ref) => (
  <SeparatorPrimitive.Root
    ref={ref}
    decorative={decorative}
    orientation={orientation}
    className={cn("shrink-0 bg-border", orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]", className)}
    {...props}
  />
));
Separator.displayName = SeparatorPrimitive.Root.displayName;

export { Separator };
```

### devise-iris/frontend\src\components\ui\sheet.tsx

```tsx
import * as SheetPrimitive from "@radix-ui/react-dialog";
import { cva, type VariantProps } from "class-variance-authority";
import { X } from "lucide-react";
import * as React from "react";

import { cn } from "@/lib/utils";

const Sheet = SheetPrimitive.Root;

const SheetTrigger = SheetPrimitive.Trigger;

const SheetClose = SheetPrimitive.Close;

const SheetPortal = SheetPrimitive.Portal;

const SheetOverlay = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className,
    )}
    {...props}
    ref={ref}
  />
));
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName;

const sheetVariants = cva(
  "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:duration-300 data-[state=open]:duration-500",
  {
    variants: {
      side: {
        top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
        bottom:
          "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
        left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
        right:
          "inset-y-0 right-0 h-full w-3/4  border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
      },
    },
    defaultVariants: {
      side: "right",
    },
  },
);

interface SheetContentProps
  extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
    VariantProps<typeof sheetVariants> {}

const SheetContent = React.forwardRef<React.ElementRef<typeof SheetPrimitive.Content>, SheetContentProps>(
  ({ side = "right", className, children, ...props }, ref) => (
    <SheetPortal>
      <SheetOverlay />
      <SheetPrimitive.Content ref={ref} className={cn(sheetVariants({ side }), className)} {...props}>
        {children}
        <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity data-[state=open]:bg-secondary hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none">
          <X className="h-4 w-4" />
          <span className="sr-only">Close</span>
        </SheetPrimitive.Close>
      </SheetPrimitive.Content>
    </SheetPortal>
  ),
);
SheetContent.displayName = SheetPrimitive.Content.displayName;

const SheetHeader = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col space-y-2 text-center sm:text-left", className)} {...props} />
);
SheetHeader.displayName = "SheetHeader";

const SheetFooter = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2", className)} {...props} />
);
SheetFooter.displayName = "SheetFooter";

const SheetTitle = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Title ref={ref} className={cn("text-lg font-semibold text-foreground", className)} {...props} />
));
SheetTitle.displayName = SheetPrimitive.Title.displayName;

const SheetDescription = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Description ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
));
SheetDescription.displayName = SheetPrimitive.Description.displayName;

export {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetOverlay,
  SheetPortal,
  SheetTitle,
  SheetTrigger,
};
```

### devise-iris/frontend\src\components\ui\sidebar.tsx

```tsx
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { VariantProps, cva } from "class-variance-authority";
import { PanelLeft } from "lucide-react";

import { useIsMobile } from "@/hooks/use-mobile";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import { Sheet, SheetContent } from "@/components/ui/sheet";
import { Skeleton } from "@/components/ui/skeleton";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";

const SIDEBAR_COOKIE_NAME = "sidebar:state";
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7;
const SIDEBAR_WIDTH = "16rem";
const SIDEBAR_WIDTH_MOBILE = "18rem";
const SIDEBAR_WIDTH_ICON = "3rem";
const SIDEBAR_KEYBOARD_SHORTCUT = "b";

type SidebarContext = {
  state: "expanded" | "collapsed";
  open: boolean;
  setOpen: (open: boolean) => void;
  openMobile: boolean;
  setOpenMobile: (open: boolean) => void;
  isMobile: boolean;
  toggleSidebar: () => void;
};

const SidebarContext = React.createContext<SidebarContext | null>(null);

function useSidebar() {
  const context = React.useContext(SidebarContext);
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.");
  }

  return context;
}

const SidebarProvider = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    defaultOpen?: boolean;
    open?: boolean;
    onOpenChange?: (open: boolean) => void;
  }
>(({ defaultOpen = true, open: openProp, onOpenChange: setOpenProp, className, style, children, ...props }, ref) => {
  const isMobile = useIsMobile();
  const [openMobile, setOpenMobile] = React.useState(false);

  // This is the internal state of the sidebar.
  // We use openProp and setOpenProp for control from outside the component.
  const [_open, _setOpen] = React.useState(defaultOpen);
  const open = openProp ?? _open;
  const setOpen = React.useCallback(
    (value: boolean | ((value: boolean) => boolean)) => {
      const openState = typeof value === "function" ? value(open) : value;
      if (setOpenProp) {
        setOpenProp(openState);
      } else {
        _setOpen(openState);
      }

      // This sets the cookie to keep the sidebar state.
      document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`;
    },
    [setOpenProp, open],
  );

  // Helper to toggle the sidebar.
  const toggleSidebar = React.useCallback(() => {
    return isMobile ? setOpenMobile((open) => !open) : setOpen((open) => !open);
  }, [isMobile, setOpen, setOpenMobile]);

  // Adds a keyboard shortcut to toggle the sidebar.
  React.useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === SIDEBAR_KEYBOARD_SHORTCUT && (event.metaKey || event.ctrlKey)) {
        event.preventDefault();
        toggleSidebar();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [toggleSidebar]);

  // We add a state so that we can do data-state="expanded" or "collapsed".
  // This makes it easier to style the sidebar with Tailwind classes.
  const state = open ? "expanded" : "collapsed";

  const contextValue = React.useMemo<SidebarContext>(
    () => ({
      state,
      open,
      setOpen,
      isMobile,
      openMobile,
      setOpenMobile,
      toggleSidebar,
    }),
    [state, open, setOpen, isMobile, openMobile, setOpenMobile, toggleSidebar],
  );

  return (
    <SidebarContext.Provider value={contextValue}>
      <TooltipProvider delayDuration={0}>
        <div
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH,
              "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
              ...style,
            } as React.CSSProperties
          }
          className={cn("group/sidebar-wrapper flex min-h-svh w-full has-[[data-variant=inset]]:bg-sidebar", className)}
          ref={ref}
          {...props}
        >
          {children}
        </div>
      </TooltipProvider>
    </SidebarContext.Provider>
  );
});
SidebarProvider.displayName = "SidebarProvider";

const Sidebar = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    side?: "left" | "right";
    variant?: "sidebar" | "floating" | "inset";
    collapsible?: "offcanvas" | "icon" | "none";
  }
>(({ side = "left", variant = "sidebar", collapsible = "offcanvas", className, children, ...props }, ref) => {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar();

  if (collapsible === "none") {
    return (
      <div
        className={cn("flex h-full w-[--sidebar-width] flex-col bg-sidebar text-sidebar-foreground", className)}
        ref={ref}
        {...props}
      >
        {children}
      </div>
    );
  }

  if (isMobile) {
    return (
      <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
        <SheetContent
          data-sidebar="sidebar"
          data-mobile="true"
          className="w-[--sidebar-width] bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
          side={side}
        >
          <div className="flex h-full w-full flex-col">{children}</div>
        </SheetContent>
      </Sheet>
    );
  }

  return (
    <div
      ref={ref}
      className="group peer hidden text-sidebar-foreground md:block"
      data-state={state}
      data-collapsible={state === "collapsed" ? collapsible : ""}
      data-variant={variant}
      data-side={side}
    >
      {/* This is what handles the sidebar gap on desktop */}
      <div
        className={cn(
          "relative h-svh w-[--sidebar-width] bg-transparent transition-[width] duration-200 ease-linear",
          "group-data-[collapsible=offcanvas]:w-0",
          "group-data-[side=right]:rotate-180",
          variant === "floating" || variant === "inset"
            ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4))]"
            : "group-data-[collapsible=icon]:w-[--sidebar-width-icon]",
        )}
      />
      <div
        className={cn(
          "fixed inset-y-0 z-10 hidden h-svh w-[--sidebar-width] transition-[left,right,width] duration-200 ease-linear md:flex",
          side === "left"
            ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
            : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
          // Adjust the padding for floating and inset variants.
          variant === "floating" || variant === "inset"
            ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4)_+2px)]"
            : "group-data-[collapsible=icon]:w-[--sidebar-width-icon] group-data-[side=left]:border-r group-data-[side=right]:border-l",
          className,
        )}
        {...props}
      >
        <div
          data-sidebar="sidebar"
          className="flex h-full w-full flex-col bg-sidebar group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:border-sidebar-border group-data-[variant=floating]:shadow"
        >
          {children}
        </div>
      </div>
    </div>
  );
});
Sidebar.displayName = "Sidebar";

const SidebarTrigger = React.forwardRef<React.ElementRef<typeof Button>, React.ComponentProps<typeof Button>>(
  ({ className, onClick, ...props }, ref) => {
    const { toggleSidebar } = useSidebar();

    return (
      <Button
        ref={ref}
        data-sidebar="trigger"
        variant="ghost"
        size="icon"
        className={cn("h-7 w-7", className)}
        onClick={(event) => {
          onClick?.(event);
          toggleSidebar();
        }}
        {...props}
      >
        <PanelLeft />
        <span className="sr-only">Toggle Sidebar</span>
      </Button>
    );
  },
);
SidebarTrigger.displayName = "SidebarTrigger";

const SidebarRail = React.forwardRef<HTMLButtonElement, React.ComponentProps<"button">>(
  ({ className, ...props }, ref) => {
    const { toggleSidebar } = useSidebar();

    return (
      <button
        ref={ref}
        data-sidebar="rail"
        aria-label="Toggle Sidebar"
        tabIndex={-1}
        onClick={toggleSidebar}
        title="Toggle Sidebar"
        className={cn(
          "absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] group-data-[side=left]:-right-4 group-data-[side=right]:left-0 hover:after:bg-sidebar-border sm:flex",
          "[[data-side=left]_&]:cursor-w-resize [[data-side=right]_&]:cursor-e-resize",
          "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
          "group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full group-data-[collapsible=offcanvas]:hover:bg-sidebar",
          "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
          "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
          className,
        )}
        {...props}
      />
    );
  },
);
SidebarRail.displayName = "SidebarRail";

const SidebarInset = React.forwardRef<HTMLDivElement, React.ComponentProps<"main">>(({ className, ...props }, ref) => {
  return (
    <main
      ref={ref}
      className={cn(
        "relative flex min-h-svh flex-1 flex-col bg-background",
        "peer-data-[variant=inset]:min-h-[calc(100svh-theme(spacing.4))] md:peer-data-[variant=inset]:m-2 md:peer-data-[state=collapsed]:peer-data-[variant=inset]:ml-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow",
        className,
      )}
      {...props}
    />
  );
});
SidebarInset.displayName = "SidebarInset";

const SidebarInput = React.forwardRef<React.ElementRef<typeof Input>, React.ComponentProps<typeof Input>>(
  ({ className, ...props }, ref) => {
    return (
      <Input
        ref={ref}
        data-sidebar="input"
        className={cn(
          "h-8 w-full bg-background shadow-none focus-visible:ring-2 focus-visible:ring-sidebar-ring",
          className,
        )}
        {...props}
      />
    );
  },
);
SidebarInput.displayName = "SidebarInput";

const SidebarHeader = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return <div ref={ref} data-sidebar="header" className={cn("flex flex-col gap-2 p-2", className)} {...props} />;
});
SidebarHeader.displayName = "SidebarHeader";

const SidebarFooter = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return <div ref={ref} data-sidebar="footer" className={cn("flex flex-col gap-2 p-2", className)} {...props} />;
});
SidebarFooter.displayName = "SidebarFooter";

const SidebarSeparator = React.forwardRef<React.ElementRef<typeof Separator>, React.ComponentProps<typeof Separator>>(
  ({ className, ...props }, ref) => {
    return (
      <Separator
        ref={ref}
        data-sidebar="separator"
        className={cn("mx-2 w-auto bg-sidebar-border", className)}
        {...props}
      />
    );
  },
);
SidebarSeparator.displayName = "SidebarSeparator";

const SidebarContent = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="content"
      className={cn(
        "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
        className,
      )}
      {...props}
    />
  );
});
SidebarContent.displayName = "SidebarContent";

const SidebarGroup = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="group"
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      {...props}
    />
  );
});
SidebarGroup.displayName = "SidebarGroup";

const SidebarGroupLabel = React.forwardRef<HTMLDivElement, React.ComponentProps<"div"> & { asChild?: boolean }>(
  ({ className, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "div";

    return (
      <Comp
        ref={ref}
        data-sidebar="group-label"
        className={cn(
          "flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium text-sidebar-foreground/70 outline-none ring-sidebar-ring transition-[margin,opa] duration-200 ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
          "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
          className,
        )}
        {...props}
      />
    );
  },
);
SidebarGroupLabel.displayName = "SidebarGroupLabel";

const SidebarGroupAction = React.forwardRef<HTMLButtonElement, React.ComponentProps<"button"> & { asChild?: boolean }>(
  ({ className, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";

    return (
      <Comp
        ref={ref}
        data-sidebar="group-action"
        className={cn(
          "absolute right-3 top-3.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
          // Increases the hit area of the button on mobile.
          "after:absolute after:-inset-2 after:md:hidden",
          "group-data-[collapsible=icon]:hidden",
          className,
        )}
        {...props}
      />
    );
  },
);
SidebarGroupAction.displayName = "SidebarGroupAction";

const SidebarGroupContent = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(
  ({ className, ...props }, ref) => (
    <div ref={ref} data-sidebar="group-content" className={cn("w-full text-sm", className)} {...props} />
  ),
);
SidebarGroupContent.displayName = "SidebarGroupContent";

const SidebarMenu = React.forwardRef<HTMLUListElement, React.ComponentProps<"ul">>(({ className, ...props }, ref) => (
  <ul ref={ref} data-sidebar="menu" className={cn("flex w-full min-w-0 flex-col gap-1", className)} {...props} />
));
SidebarMenu.displayName = "SidebarMenu";

const SidebarMenuItem = React.forwardRef<HTMLLIElement, React.ComponentProps<"li">>(({ className, ...props }, ref) => (
  <li ref={ref} data-sidebar="menu-item" className={cn("group/menu-item relative", className)} {...props} />
));
SidebarMenuItem.displayName = "SidebarMenuItem";

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-none ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-[[data-sidebar=menu-action]]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:!size-8 group-data-[collapsible=icon]:!p-2 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
        outline:
          "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]",
      },
      size: {
        default: "h-8 text-sm",
        sm: "h-7 text-xs",
        lg: "h-12 text-sm group-data-[collapsible=icon]:!p-0",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  },
);

const SidebarMenuButton = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean;
    isActive?: boolean;
    tooltip?: string | React.ComponentProps<typeof TooltipContent>;
  } & VariantProps<typeof sidebarMenuButtonVariants>
>(({ asChild = false, isActive = false, variant = "default", size = "default", tooltip, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "button";
  const { isMobile, state } = useSidebar();

  const button = (
    <Comp
      ref={ref}
      data-sidebar="menu-button"
      data-size={size}
      data-active={isActive}
      className={cn(sidebarMenuButtonVariants({ variant, size }), className)}
      {...props}
    />
  );

  if (!tooltip) {
    return button;
  }

  if (typeof tooltip === "string") {
    tooltip = {
      children: tooltip,
    };
  }

  return (
    <Tooltip>
      <TooltipTrigger asChild>{button}</TooltipTrigger>
      <TooltipContent side="right" align="center" hidden={state !== "collapsed" || isMobile} {...tooltip} />
    </Tooltip>
  );
});
SidebarMenuButton.displayName = "SidebarMenuButton";

const SidebarMenuAction = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean;
    showOnHover?: boolean;
  }
>(({ className, asChild = false, showOnHover = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "button";

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-action"
      className={cn(
        "absolute right-1 top-1.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform peer-hover/menu-button:text-sidebar-accent-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 after:md:hidden",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        showOnHover &&
          "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 peer-data-[active=true]/menu-button:text-sidebar-accent-foreground md:opacity-0",
        className,
      )}
      {...props}
    />
  );
});
SidebarMenuAction.displayName = "SidebarMenuAction";

const SidebarMenuBadge = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      data-sidebar="menu-badge"
      className={cn(
        "pointer-events-none absolute right-1 flex h-5 min-w-5 select-none items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums text-sidebar-foreground",
        "peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[active=true]/menu-button:text-sidebar-accent-foreground",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        className,
      )}
      {...props}
    />
  ),
);
SidebarMenuBadge.displayName = "SidebarMenuBadge";

const SidebarMenuSkeleton = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    showIcon?: boolean;
  }
>(({ className, showIcon = false, ...props }, ref) => {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`;
  }, []);

  return (
    <div
      ref={ref}
      data-sidebar="menu-skeleton"
      className={cn("flex h-8 items-center gap-2 rounded-md px-2", className)}
      {...props}
    >
      {showIcon && <Skeleton className="size-4 rounded-md" data-sidebar="menu-skeleton-icon" />}
      <Skeleton
        className="h-4 max-w-[--skeleton-width] flex-1"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  );
});
SidebarMenuSkeleton.displayName = "SidebarMenuSkeleton";

const SidebarMenuSub = React.forwardRef<HTMLUListElement, React.ComponentProps<"ul">>(
  ({ className, ...props }, ref) => (
    <ul
      ref={ref}
      data-sidebar="menu-sub"
      className={cn(
        "mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l border-sidebar-border px-2.5 py-0.5",
        "group-data-[collapsible=icon]:hidden",
        className,
      )}
      {...props}
    />
  ),
);
SidebarMenuSub.displayName = "SidebarMenuSub";

const SidebarMenuSubItem = React.forwardRef<HTMLLIElement, React.ComponentProps<"li">>(({ ...props }, ref) => (
  <li ref={ref} {...props} />
));
SidebarMenuSubItem.displayName = "SidebarMenuSubItem";

const SidebarMenuSubButton = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentProps<"a"> & {
    asChild?: boolean;
    size?: "sm" | "md";
    isActive?: boolean;
  }
>(({ asChild = false, size = "md", isActive, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a";

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-sub-button"
      data-size={size}
      data-active={isActive}
      className={cn(
        "flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-md px-2 text-sidebar-foreground outline-none ring-sidebar-ring aria-disabled:pointer-events-none aria-disabled:opacity-50 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground",
        "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
        size === "sm" && "text-xs",
        size === "md" && "text-sm",
        "group-data-[collapsible=icon]:hidden",
        className,
      )}
      {...props}
    />
  );
});
SidebarMenuSubButton.displayName = "SidebarMenuSubButton";

export {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInput,
  SidebarInset,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
};
```

### devise-iris/frontend\src\components\ui\skeleton.tsx

```tsx
import { cn } from "@/lib/utils";

function Skeleton({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn("animate-pulse rounded-md bg-muted", className)} {...props} />;
}

export { Skeleton };
```

### devise-iris/frontend\src\components\ui\slider.tsx

```tsx
import * as React from "react";
import * as SliderPrimitive from "@radix-ui/react-slider";

import { cn } from "@/lib/utils";

const Slider = React.forwardRef<
  React.ElementRef<typeof SliderPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SliderPrimitive.Root>
>(({ className, ...props }, ref) => (
  <SliderPrimitive.Root
    ref={ref}
    className={cn("relative flex w-full touch-none select-none items-center", className)}
    {...props}
  >
    <SliderPrimitive.Track className="relative h-2 w-full grow overflow-hidden rounded-full bg-secondary">
      <SliderPrimitive.Range className="absolute h-full bg-primary" />
    </SliderPrimitive.Track>
    <SliderPrimitive.Thumb className="block h-5 w-5 rounded-full border-2 border-primary bg-background ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" />
  </SliderPrimitive.Root>
));
Slider.displayName = SliderPrimitive.Root.displayName;

export { Slider };
```

### devise-iris/frontend\src\components\ui\sonner.tsx

```tsx
import { useTheme } from "next-themes";
import { Toaster as Sonner, toast } from "sonner";

type ToasterProps = React.ComponentProps<typeof Sonner>;

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme();

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
          description: "group-[.toast]:text-muted-foreground",
          actionButton: "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
          cancelButton: "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground",
        },
      }}
      {...props}
    />
  );
};

export { Toaster, toast };
```

### devise-iris/frontend\src\components\ui\switch.tsx

```tsx
import * as React from "react";
import * as SwitchPrimitives from "@radix-ui/react-switch";

import { cn } from "@/lib/utils";

const Switch = React.forwardRef<
  React.ElementRef<typeof SwitchPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof SwitchPrimitives.Root>
>(({ className, ...props }, ref) => (
  <SwitchPrimitives.Root
    className={cn(
      "peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors data-[state=checked]:bg-primary data-[state=unchecked]:bg-input focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50",
      className,
    )}
    {...props}
    ref={ref}
  >
    <SwitchPrimitives.Thumb
      className={cn(
        "pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0",
      )}
    />
  </SwitchPrimitives.Root>
));
Switch.displayName = SwitchPrimitives.Root.displayName;

export { Switch };
```

### devise-iris/frontend\src\components\ui\table.tsx

```tsx
import * as React from "react";

import { cn } from "@/lib/utils";

const Table = React.forwardRef<HTMLTableElement, React.HTMLAttributes<HTMLTableElement>>(
  ({ className, ...props }, ref) => (
    <div className="relative w-full overflow-auto">
      <table ref={ref} className={cn("w-full caption-bottom text-sm", className)} {...props} />
    </div>
  ),
);
Table.displayName = "Table";

const TableHeader = React.forwardRef<HTMLTableSectionElement, React.HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => <thead ref={ref} className={cn("[&_tr]:border-b", className)} {...props} />,
);
TableHeader.displayName = "TableHeader";

const TableBody = React.forwardRef<HTMLTableSectionElement, React.HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <tbody ref={ref} className={cn("[&_tr:last-child]:border-0", className)} {...props} />
  ),
);
TableBody.displayName = "TableBody";

const TableFooter = React.forwardRef<HTMLTableSectionElement, React.HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <tfoot ref={ref} className={cn("border-t bg-muted/50 font-medium [&>tr]:last:border-b-0", className)} {...props} />
  ),
);
TableFooter.displayName = "TableFooter";

const TableRow = React.forwardRef<HTMLTableRowElement, React.HTMLAttributes<HTMLTableRowElement>>(
  ({ className, ...props }, ref) => (
    <tr
      ref={ref}
      className={cn("border-b transition-colors data-[state=selected]:bg-muted hover:bg-muted/50", className)}
      {...props}
    />
  ),
);
TableRow.displayName = "TableRow";

const TableHead = React.forwardRef<HTMLTableCellElement, React.ThHTMLAttributes<HTMLTableCellElement>>(
  ({ className, ...props }, ref) => (
    <th
      ref={ref}
      className={cn(
        "h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0",
        className,
      )}
      {...props}
    />
  ),
);
TableHead.displayName = "TableHead";

const TableCell = React.forwardRef<HTMLTableCellElement, React.TdHTMLAttributes<HTMLTableCellElement>>(
  ({ className, ...props }, ref) => (
    <td ref={ref} className={cn("p-4 align-middle [&:has([role=checkbox])]:pr-0", className)} {...props} />
  ),
);
TableCell.displayName = "TableCell";

const TableCaption = React.forwardRef<HTMLTableCaptionElement, React.HTMLAttributes<HTMLTableCaptionElement>>(
  ({ className, ...props }, ref) => (
    <caption ref={ref} className={cn("mt-4 text-sm text-muted-foreground", className)} {...props} />
  ),
);
TableCaption.displayName = "TableCaption";

export { Table, TableHeader, TableBody, TableFooter, TableHead, TableRow, TableCell, TableCaption };
```

### devise-iris/frontend\src\components\ui\tabs.tsx

```tsx
import * as React from "react";
import * as TabsPrimitive from "@radix-ui/react-tabs";

import { cn } from "@/lib/utils";

const Tabs = TabsPrimitive.Root;

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
      className,
    )}
    {...props}
  />
));
TabsList.displayName = TabsPrimitive.List.displayName;

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
      className,
    )}
    {...props}
  />
));
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName;

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className,
    )}
    {...props}
  />
));
TabsContent.displayName = TabsPrimitive.Content.displayName;

export { Tabs, TabsList, TabsTrigger, TabsContent };
```

### devise-iris/frontend\src\components\ui\textarea.tsx

```tsx
import * as React from "react";

import { cn } from "@/lib/utils";

export interface TextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}

const Textarea = React.forwardRef<HTMLTextAreaElement, TextareaProps>(({ className, ...props }, ref) => {
  return (
    <textarea
      className={cn(
        "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
        className,
      )}
      ref={ref}
      {...props}
    />
  );
});
Textarea.displayName = "Textarea";

export { Textarea };
```

### devise-iris/frontend\src\components\ui\toast.tsx

```tsx
import * as React from "react";
import * as ToastPrimitives from "@radix-ui/react-toast";
import { cva, type VariantProps } from "class-variance-authority";
import { X } from "lucide-react";

import { cn } from "@/lib/utils";

const ToastProvider = ToastPrimitives.Provider;

const ToastViewport = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Viewport>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Viewport>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Viewport
    ref={ref}
    className={cn(
      "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]",
      className,
    )}
    {...props}
  />
));
ToastViewport.displayName = ToastPrimitives.Viewport.displayName;

const toastVariants = cva(
  "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)] data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[swipe=end]:animate-out data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full data-[state=open]:slide-in-from-top-full data-[state=open]:sm:slide-in-from-bottom-full",
  {
    variants: {
      variant: {
        default: "border bg-background text-foreground",
        destructive: "destructive group border-destructive bg-destructive text-destructive-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
);

const Toast = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Root> & VariantProps<typeof toastVariants>
>(({ className, variant, ...props }, ref) => {
  return <ToastPrimitives.Root ref={ref} className={cn(toastVariants({ variant }), className)} {...props} />;
});
Toast.displayName = ToastPrimitives.Root.displayName;

const ToastAction = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Action>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Action>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Action
    ref={ref}
    className={cn(
      "inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors group-[.destructive]:border-muted/40 hover:bg-secondary group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 group-[.destructive]:focus:ring-destructive disabled:pointer-events-none disabled:opacity-50",
      className,
    )}
    {...props}
  />
));
ToastAction.displayName = ToastPrimitives.Action.displayName;

const ToastClose = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Close>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Close>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Close
    ref={ref}
    className={cn(
      "absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity group-hover:opacity-100 group-[.destructive]:text-red-300 hover:text-foreground group-[.destructive]:hover:text-red-50 focus:opacity-100 focus:outline-none focus:ring-2 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600",
      className,
    )}
    toast-close=""
    {...props}
  >
    <X className="h-4 w-4" />
  </ToastPrimitives.Close>
));
ToastClose.displayName = ToastPrimitives.Close.displayName;

const ToastTitle = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Title>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Title>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Title ref={ref} className={cn("text-sm font-semibold", className)} {...props} />
));
ToastTitle.displayName = ToastPrimitives.Title.displayName;

const ToastDescription = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Description>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Description>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Description ref={ref} className={cn("text-sm opacity-90", className)} {...props} />
));
ToastDescription.displayName = ToastPrimitives.Description.displayName;

type ToastProps = React.ComponentPropsWithoutRef<typeof Toast>;

type ToastActionElement = React.ReactElement<typeof ToastAction>;

export {
  type ToastProps,
  type ToastActionElement,
  ToastProvider,
  ToastViewport,
  Toast,
  ToastTitle,
  ToastDescription,
  ToastClose,
  ToastAction,
};
```

### devise-iris/frontend\src\components\ui\toaster.tsx

```tsx
import { useToast } from "@/hooks/use-toast";
import { Toast, ToastClose, ToastDescription, ToastProvider, ToastTitle, ToastViewport } from "@/components/ui/toast";

export function Toaster() {
  const { toasts } = useToast();

  return (
    <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        return (
          <Toast key={id} {...props}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && <ToastDescription>{description}</ToastDescription>}
            </div>
            {action}
            <ToastClose />
          </Toast>
        );
      })}
      <ToastViewport />
    </ToastProvider>
  );
}
```

### devise-iris/frontend\src\components\ui\toggle-group.tsx

```tsx
import * as React from "react";
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group";
import { type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";
import { toggleVariants } from "@/components/ui/toggle";

const ToggleGroupContext = React.createContext<VariantProps<typeof toggleVariants>>({
  size: "default",
  variant: "default",
});

const ToggleGroup = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Root> & VariantProps<typeof toggleVariants>
>(({ className, variant, size, children, ...props }, ref) => (
  <ToggleGroupPrimitive.Root ref={ref} className={cn("flex items-center justify-center gap-1", className)} {...props}>
    <ToggleGroupContext.Provider value={{ variant, size }}>{children}</ToggleGroupContext.Provider>
  </ToggleGroupPrimitive.Root>
));

ToggleGroup.displayName = ToggleGroupPrimitive.Root.displayName;

const ToggleGroupItem = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Item> & VariantProps<typeof toggleVariants>
>(({ className, children, variant, size, ...props }, ref) => {
  const context = React.useContext(ToggleGroupContext);

  return (
    <ToggleGroupPrimitive.Item
      ref={ref}
      className={cn(
        toggleVariants({
          variant: context.variant || variant,
          size: context.size || size,
        }),
        className,
      )}
      {...props}
    >
      {children}
    </ToggleGroupPrimitive.Item>
  );
});

ToggleGroupItem.displayName = ToggleGroupPrimitive.Item.displayName;

export { ToggleGroup, ToggleGroupItem };
```

### devise-iris/frontend\src\components\ui\toggle.tsx

```tsx
import * as React from "react";
import * as TogglePrimitive from "@radix-ui/react-toggle";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const toggleVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors hover:bg-muted hover:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline: "border border-input bg-transparent hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-10 px-3",
        sm: "h-9 px-2.5",
        lg: "h-11 px-5",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  },
);

const Toggle = React.forwardRef<
  React.ElementRef<typeof TogglePrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof TogglePrimitive.Root> & VariantProps<typeof toggleVariants>
>(({ className, variant, size, ...props }, ref) => (
  <TogglePrimitive.Root ref={ref} className={cn(toggleVariants({ variant, size, className }))} {...props} />
));

Toggle.displayName = TogglePrimitive.Root.displayName;

export { Toggle, toggleVariants };
```

### devise-iris/frontend\src\components\ui\tooltip.tsx

```tsx
import * as React from "react";
import * as TooltipPrimitive from "@radix-ui/react-tooltip";

import { cn } from "@/lib/utils";

const TooltipProvider = TooltipPrimitive.Provider;

const Tooltip = TooltipPrimitive.Root;

const TooltipTrigger = TooltipPrimitive.Trigger;

const TooltipContent = React.forwardRef<
  React.ElementRef<typeof TooltipPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TooltipPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <TooltipPrimitive.Content
    ref={ref}
    sideOffset={sideOffset}
    className={cn(
      "z-50 overflow-hidden rounded-md border bg-popover px-3 py-1.5 text-sm text-popover-foreground shadow-md animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className,
    )}
    {...props}
  />
));
TooltipContent.displayName = TooltipPrimitive.Content.displayName;

export { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider };
```

### devise-iris/frontend\src\components\ui\use-toast.ts

```ts
import { useToast, toast } from "@/hooks/use-toast";

export { useToast, toast };
```

### devise-iris/frontend\src\data\mockData.backup.ts

```ts
// Mock data for Devise Dashboard

export interface DetectionEvent {
  event_id: string;
  user_id: string;
  user_email: string;
  department: string;
  device_id: string;
  tool_name: string;
  domain: string;
  category: string;
  vendor: string;
  risk_level: "low" | "medium" | "high";
  source: string;
  process_name: string;
  process_path: string;
  is_approved: boolean;
  timestamp: string;
  connection_frequency?: number;
  high_frequency?: boolean;
  bytes_read?: number;
  bytes_write?: number;
}

export interface HeartbeatEvent {
  event_type: "heartbeat";
  device_id: string;
  agent_version: string;
  queue_depth: number;
  last_detection_time: string | null;
  os_version: string;
  restart_detected: boolean;
  timestamp: string;
}

export interface TamperAlert {
  type: "tamper_alert";
  device_id: string;
  expected_hash: string;
  actual_hash: string;
  timestamp: string;
}

export interface AgentGapEvent {
  event_type: "agent_gap";
  device_id: string;
  gap_seconds: number;
  last_seen: string;
  suspicious: boolean;
  timestamp: string;
}

const now = new Date();
const ago = (minutes: number) => new Date(now.getTime() - minutes * 60000).toISOString();

const devices = [
  "03479922-d748-5ca6-aaf9-31f1f7e93c28",
  "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "f9e8d7c6-b5a4-3210-fedc-ba0987654321",
  "11223344-5566-7788-99aa-bbccddeeff00",
  "deadbeef-cafe-babe-face-123456789abc",
];

const users = [
  { id: "yashm", email: "yash.m@company.com", dept: "Engineering" },
  { id: "sarahk", email: "sarah.k@company.com", dept: "Product" },
  { id: "mikej", email: "mike.j@company.com", dept: "Design" },
  { id: "emilyw", email: "emily.w@company.com", dept: "Marketing" },
  { id: "alexr", email: "alex.r@company.com", dept: "Engineering" },
];

let eventId = 0;
const eid = () => `evt-${String(++eventId).padStart(4, "0")}-${Math.random().toString(36).slice(2, 10)}`;

export const mockDetectionEvents: DetectionEvent[] = [
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "OpenAI ChatGPT", domain: "chat.openai.com", category: "chat", vendor: "OpenAI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(2), connection_frequency: 3 },
  { event_id: eid(), user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1], tool_name: "Claude", domain: "claude.ai", category: "chat", vendor: "Anthropic", risk_level: "medium", source: "desktop", process_name: "firefox.exe", process_path: "C:\\Program Files\\Mozilla Firefox\\firefox.exe", is_approved: true, timestamp: ago(5) },
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "OpenAI API", domain: "api.openai.com", category: "api", vendor: "OpenAI", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(8), connection_frequency: 15, high_frequency: true, bytes_read: 2048000, bytes_write: 512000 },
  { event_id: eid(), user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2], tool_name: "Midjourney", domain: "midjourney.com", category: "image", vendor: "Midjourney", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(12) },
  { event_id: eid(), user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4], tool_name: "GitHub Copilot", domain: "copilot.github.com", category: "coding", vendor: "Microsoft", risk_level: "low", source: "desktop", process_name: "Code.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", is_approved: true, timestamp: ago(15) },
  { event_id: eid(), user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3], tool_name: "Jasper", domain: "jasper.ai", category: "productivity", vendor: "Jasper", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(18) },
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "Anthropic API", domain: "api.anthropic.com", category: "api", vendor: "Anthropic", risk_level: "high", source: "desktop", process_name: "node.exe", process_path: "C:\\Program Files\\nodejs\\node.exe", is_approved: false, timestamp: ago(22), connection_frequency: 8 },
  { event_id: eid(), user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1], tool_name: "Perplexity", domain: "perplexity.ai", category: "search", vendor: "Perplexity", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(30) },
  { event_id: eid(), user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2], tool_name: "DALL-E", domain: "labs.openai.com", category: "image", vendor: "OpenAI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(35) },
  { event_id: eid(), user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4], tool_name: "Cursor", domain: "cursor.sh", category: "coding", vendor: "Anysphere", risk_level: "medium", source: "desktop", process_name: "Cursor.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Cursor\\Cursor.exe", is_approved: false, timestamp: ago(40) },
  { event_id: eid(), user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3], tool_name: "Grammarly", domain: "grammarly.com", category: "productivity", vendor: "Grammarly", risk_level: "low", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(45) },
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "Google Gemini", domain: "gemini.google.com", category: "chat", vendor: "Google", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(55) },
  { event_id: eid(), user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1], tool_name: "Notion AI", domain: "notion.so", category: "productivity", vendor: "Notion", risk_level: "low", source: "desktop", process_name: "Notion.exe", process_path: "C:\\Users\\sarahk\\AppData\\Local\\Programs\\Notion\\Notion.exe", is_approved: true, timestamp: ago(60) },
  { event_id: eid(), user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4], tool_name: "DeepSeek", domain: "deepseek.com", category: "chat", vendor: "DeepSeek", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(70) },
  { event_id: eid(), user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2], tool_name: "Leonardo AI", domain: "leonardo.ai", category: "image", vendor: "Leonardo AI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(80) },
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "Replicate", domain: "replicate.com", category: "api", vendor: "Replicate", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(90), connection_frequency: 12, high_frequency: true },
  { event_id: eid(), user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3], tool_name: "ElevenLabs", domain: "elevenlabs.io", category: "audio", vendor: "ElevenLabs", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(100) },
  { event_id: eid(), user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4], tool_name: "Tabnine", domain: "tabnine.com", category: "coding", vendor: "Tabnine", risk_level: "medium", source: "desktop", process_name: "Code.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", is_approved: false, timestamp: ago(120) },
  { event_id: eid(), user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1], tool_name: "Runway", domain: "runwayml.com", category: "video", vendor: "Runway", risk_level: "high", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(140) },
  { event_id: eid(), user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0], tool_name: "Groq", domain: "groq.com", category: "api", vendor: "Groq", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(160) },
];

export const mockHeartbeats: HeartbeatEvent[] = [
  { event_type: "heartbeat", device_id: devices[0], agent_version: "1.0.0", queue_depth: 0, last_detection_time: ago(2), os_version: "Windows 11", restart_detected: false, timestamp: ago(1) },
  { event_type: "heartbeat", device_id: devices[1], agent_version: "1.0.0", queue_depth: 2, last_detection_time: ago(5), os_version: "Windows 10", restart_detected: false, timestamp: ago(3) },
  { event_type: "heartbeat", device_id: devices[2], agent_version: "0.9.8", queue_depth: 0, last_detection_time: ago(12), os_version: "macOS 14.2", restart_detected: false, timestamp: ago(4) },
  { event_type: "heartbeat", device_id: devices[3], agent_version: "1.0.0", queue_depth: 5, last_detection_time: ago(18), os_version: "Windows 11", restart_detected: true, timestamp: ago(8) },
  { event_type: "heartbeat", device_id: devices[4], agent_version: "1.0.1", queue_depth: 0, last_detection_time: ago(15), os_version: "macOS 15.0", restart_detected: false, timestamp: ago(2) },
];

export const mockTamperAlerts: TamperAlert[] = [
  { type: "tamper_alert", device_id: devices[3], expected_hash: "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6", actual_hash: "e5f6a7b8c9d0e1f2a3b4c5d6a1b2c3d4", timestamp: ago(45) },
  { type: "tamper_alert", device_id: devices[1], expected_hash: "1234567890abcdef1234567890abcdef", actual_hash: "fedcba0987654321fedcba0987654321", timestamp: ago(200) },
];

export const mockAgentGaps: AgentGapEvent[] = [
  { event_type: "agent_gap", device_id: devices[3], gap_seconds: 3600, last_seen: ago(120), suspicious: true, timestamp: ago(60) },
  { event_type: "agent_gap", device_id: devices[1], gap_seconds: 900, last_seen: ago(50), suspicious: false, timestamp: ago(35) },
];

// Derived stats
export const getStats = () => {
  const events = mockDetectionEvents;
  return {
    totalDetections: events.length,
    uniqueTools: new Set(events.map(e => e.tool_name)).size,
    highRiskCount: events.filter(e => e.risk_level === "high").length,
    unapprovedCount: events.filter(e => !e.is_approved).length,
    onlineDevices: mockHeartbeats.filter(h => {
      const diff = (Date.now() - new Date(h.timestamp).getTime()) / 60000;
      return diff < 6;
    }).length,
    totalDevices: mockHeartbeats.length,
    activeAlerts: mockTamperAlerts.length + mockAgentGaps.filter(g => g.suspicious).length + events.filter(e => e.risk_level === "high" && !e.is_approved).length,
  };
};

// Chart data helpers
export const getDetectionsByTool = () => {
  const counts: Record<string, number> = {};
  mockDetectionEvents.forEach(e => { counts[e.tool_name] = (counts[e.tool_name] || 0) + 1; });
  return Object.entries(counts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count).slice(0, 8);
};

export const getDetectionsByCategory = () => {
  const counts: Record<string, number> = {};
  mockDetectionEvents.forEach(e => { counts[e.category] = (counts[e.category] || 0) + 1; });
  return Object.entries(counts).map(([name, value]) => ({ name, value }));
};

export const getDetectionsOverTime = () => {
  const buckets: Record<string, number> = {};
  mockDetectionEvents.forEach(e => {
    const hour = new Date(e.timestamp).getHours();
    const label = `${hour.toString().padStart(2, "0")}:00`;
    buckets[label] = (buckets[label] || 0) + 1;
  });
  return Object.entries(buckets).map(([time, count]) => ({ time, count })).sort((a, b) => a.time.localeCompare(b.time));
};

export const getTopProcesses = () => {
  const counts: Record<string, number> = {};
  mockDetectionEvents.forEach(e => { counts[e.process_name] = (counts[e.process_name] || 0) + 1; });
  return Object.entries(counts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count);
};
```

### devise-iris/frontend\src\data\mockData.ts

```ts
/**
 * Type definitions for Devise Dashboard data models.
 *
 * NOTE: Mock data has been moved to mockData.backup.ts.
 * All runtime data now comes from the API via hooks in useDashboard.ts.
 */

export interface DetectionEvent {
  event_id: string;
  user_id: string;
  user_email: string;
  department: string;
  device_id: string;
  tool_name: string;
  domain: string;
  category: string;
  vendor: string;
  risk_level: "low" | "medium" | "high";
  source: string;
  process_name: string;
  process_path: string;
  is_approved: boolean;
  timestamp: string;
  connection_frequency?: number;
  high_frequency?: boolean;
  bytes_read?: number;
  bytes_write?: number;
}

export interface HeartbeatEvent {
  event_type: "heartbeat";
  device_id: string;
  agent_version: string;
  queue_depth: number;
  last_detection_time: string | null;
  os_version: string;
  restart_detected: boolean;
  timestamp: string;
}

export interface TamperAlert {
  type: "tamper_alert";
  device_id: string;
  expected_hash: string;
  actual_hash: string;
  timestamp: string;
}

export interface AgentGapEvent {
  event_type: "agent_gap";
  device_id: string;
  gap_seconds: number;
  last_seen: string;
  suspicious: boolean;
  timestamp: string;
}
```

### devise-iris/frontend\src\hooks\use-mobile.tsx

```tsx
import * as React from "react";

const MOBILE_BREAKPOINT = 768;

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined);

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`);
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    };
    mql.addEventListener("change", onChange);
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    return () => mql.removeEventListener("change", onChange);
  }, []);

  return !!isMobile;
}
```

### devise-iris/frontend\src\hooks\use-toast.ts

```ts
import * as React from "react";

import type { ToastActionElement, ToastProps } from "@/components/ui/toast";

const TOAST_LIMIT = 1;
const TOAST_REMOVE_DELAY = 1000000;

type ToasterToast = ToastProps & {
  id: string;
  title?: React.ReactNode;
  description?: React.ReactNode;
  action?: ToastActionElement;
};

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST",
} as const;

let count = 0;

function genId() {
  count = (count + 1) % Number.MAX_SAFE_INTEGER;
  return count.toString();
}

type ActionType = typeof actionTypes;

type Action =
  | {
      type: ActionType["ADD_TOAST"];
      toast: ToasterToast;
    }
  | {
      type: ActionType["UPDATE_TOAST"];
      toast: Partial<ToasterToast>;
    }
  | {
      type: ActionType["DISMISS_TOAST"];
      toastId?: ToasterToast["id"];
    }
  | {
      type: ActionType["REMOVE_TOAST"];
      toastId?: ToasterToast["id"];
    };

interface State {
  toasts: ToasterToast[];
}

const toastTimeouts = new Map<string, ReturnType<typeof setTimeout>>();

const addToRemoveQueue = (toastId: string) => {
  if (toastTimeouts.has(toastId)) {
    return;
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId);
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    });
  }, TOAST_REMOVE_DELAY);

  toastTimeouts.set(toastId, timeout);
};

export const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "ADD_TOAST":
      return {
        ...state,
        toasts: [action.toast, ...state.toasts].slice(0, TOAST_LIMIT),
      };

    case "UPDATE_TOAST":
      return {
        ...state,
        toasts: state.toasts.map((t) => (t.id === action.toast.id ? { ...t, ...action.toast } : t)),
      };

    case "DISMISS_TOAST": {
      const { toastId } = action;

      // ! Side effects ! - This could be extracted into a dismissToast() action,
      // but I'll keep it here for simplicity
      if (toastId) {
        addToRemoveQueue(toastId);
      } else {
        state.toasts.forEach((toast) => {
          addToRemoveQueue(toast.id);
        });
      }

      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === toastId || toastId === undefined
            ? {
                ...t,
                open: false,
              }
            : t,
        ),
      };
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return {
          ...state,
          toasts: [],
        };
      }
      return {
        ...state,
        toasts: state.toasts.filter((t) => t.id !== action.toastId),
      };
  }
};

const listeners: Array<(state: State) => void> = [];

let memoryState: State = { toasts: [] };

function dispatch(action: Action) {
  memoryState = reducer(memoryState, action);
  listeners.forEach((listener) => {
    listener(memoryState);
  });
}

type Toast = Omit<ToasterToast, "id">;

function toast({ ...props }: Toast) {
  const id = genId();

  const update = (props: ToasterToast) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    });
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id });

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open) => {
        if (!open) dismiss();
      },
    },
  });

  return {
    id: id,
    dismiss,
    update,
  };
}

function useToast() {
  const [state, setState] = React.useState<State>(memoryState);

  React.useEffect(() => {
    listeners.push(setState);
    return () => {
      const index = listeners.indexOf(setState);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    };
  }, [state]);

  return {
    ...state,
    toast,
    dismiss: (toastId?: string) => dispatch({ type: "DISMISS_TOAST", toastId }),
  };
}

export { useToast, toast };
```

### devise-iris/frontend\src\hooks\useDashboard.ts

```ts
import { useQuery } from "@tanstack/react-query";
import { useAuth } from "@/lib/AuthContext";
import {
  fetchEvents,
  fetchHeartbeats,
  fetchStats,
  fetchAlerts,
  fetchAnalytics,
  fetchSubscriptions,
  fetchSpendOverview,
  fetchTeam,
  fetchSettings,
  fetchMe,
  type StatsResponse,
  type AlertItem,
  type AnalyticsResponse,
  type EventsResponse,
  type SubscriptionItem,
  type SpendOverview,
  type TeamResponse,
  type OrgSettings,
  type UserProfile,
} from "@/services/api";
import type { HeartbeatEvent } from "@/data/mockData";

/**
 * Polling intervals (user-specified):
 *   Events:       10s
 *   Stats:        30s
 *   Heartbeats:   30s
 *   Alerts:       30s
 *   Analytics:    60s
 *   Subscriptions:60s
 *
 * All hooks are gated by `enabled: !!session` so they never fire
 * before auth is ready (prevents 401 race → sign-out loop).
 */

export function useEvents(category?: string, riskLevel?: string) {
  const { session } = useAuth();
  return useQuery<EventsResponse, Error>({
    queryKey: ["events", category, riskLevel],
    queryFn: () => fetchEvents(category, riskLevel),
    enabled: !!session,
    refetchInterval: 10_000,
    staleTime: 8_000,
    retry: 2,
  });
}

export function useStats() {
  const { session } = useAuth();
  return useQuery<StatsResponse, Error>({
    queryKey: ["stats"],
    queryFn: fetchStats,
    enabled: !!session,
    refetchInterval: 30_000,
    staleTime: 25_000,
    retry: 2,
  });
}

export function useHeartbeats() {
  const { session } = useAuth();
  return useQuery<HeartbeatEvent[], Error>({
    queryKey: ["heartbeats"],
    queryFn: fetchHeartbeats,
    enabled: !!session,
    refetchInterval: 30_000,
    staleTime: 25_000,
    retry: 2,
  });
}

export function useAlerts() {
  const { session } = useAuth();
  return useQuery<AlertItem[], Error>({
    queryKey: ["alerts"],
    queryFn: fetchAlerts,
    enabled: !!session,
    refetchInterval: 30_000,
    staleTime: 25_000,
    retry: 2,
  });
}

export function useAnalytics() {
  const { session } = useAuth();
  return useQuery<AnalyticsResponse, Error>({
    queryKey: ["analytics"],
    queryFn: fetchAnalytics,
    enabled: !!session,
    refetchInterval: 60_000,
    staleTime: 55_000,
    retry: 2,
  });
}

export function useSubscriptions() {
  const { session } = useAuth();
  return useQuery<SubscriptionItem[], Error>({
    queryKey: ["subscriptions"],
    queryFn: fetchSubscriptions,
    enabled: !!session,
    refetchInterval: 60_000,
    staleTime: 55_000,
    retry: 2,
  });
}

export function useSpendOverview() {
  const { session } = useAuth();
  return useQuery<SpendOverview, Error>({
    queryKey: ["spend-overview"],
    queryFn: fetchSpendOverview,
    enabled: !!session,
    refetchInterval: 60_000,
    staleTime: 55_000,
    retry: 2,
  });
}

export function useTeam() {
  const { session } = useAuth();
  return useQuery<TeamResponse, Error>({
    queryKey: ["team"],
    queryFn: fetchTeam,
    enabled: !!session,
    refetchInterval: 60_000,
    staleTime: 55_000,
    retry: 2,
  });
}

export function useSettings() {
  const { session } = useAuth();
  return useQuery<OrgSettings, Error>({
    queryKey: ["settings"],
    queryFn: fetchSettings,
    enabled: !!session,
    staleTime: 60_000,
    retry: 2,
  });
}

export function useMe() {
  const { session } = useAuth();
  return useQuery<UserProfile, Error>({
    queryKey: ["me"],
    queryFn: fetchMe,
    enabled: !!session,
    staleTime: 300_000,
    retry: 2,
  });
}
```

### devise-iris/frontend\src\lib\aiToolsRegistry.ts

```ts
export interface AITool {
  tool_name: string;
  domain: string;
  category: "chat" | "coding" | "api" | "image" | "audio" | "video" | "search" | "productivity";
  vendor: string;
  risk_level: "low" | "medium" | "high";
  is_approved: boolean;
}

export const aiToolsRegistry: AITool[] = [
  { tool_name: "OpenAI ChatGPT", domain: "openai.com", category: "chat", vendor: "OpenAI", risk_level: "medium", is_approved: true },
  { tool_name: "OpenAI ChatGPT", domain: "chat.openai.com", category: "chat", vendor: "OpenAI", risk_level: "medium", is_approved: true },
  { tool_name: "OpenAI API", domain: "api.openai.com", category: "api", vendor: "OpenAI", risk_level: "high", is_approved: false },
  { tool_name: "OpenAI Platform", domain: "platform.openai.com", category: "api", vendor: "OpenAI", risk_level: "high", is_approved: true },
  { tool_name: "Anthropic", domain: "anthropic.com", category: "chat", vendor: "Anthropic", risk_level: "medium", is_approved: true },
  { tool_name: "Claude", domain: "claude.ai", category: "chat", vendor: "Anthropic", risk_level: "medium", is_approved: true },
  { tool_name: "Anthropic API", domain: "api.anthropic.com", category: "api", vendor: "Anthropic", risk_level: "high", is_approved: false },
  { tool_name: "Anthropic Console", domain: "console.anthropic.com", category: "api", vendor: "Anthropic", risk_level: "high", is_approved: true },
  { tool_name: "Microsoft Copilot", domain: "copilot.microsoft.com", category: "coding", vendor: "Microsoft", risk_level: "low", is_approved: true },
  { tool_name: "GitHub", domain: "github.com", category: "coding", vendor: "Microsoft", risk_level: "low", is_approved: true },
  { tool_name: "GitHub API", domain: "api.github.com", category: "api", vendor: "Microsoft", risk_level: "high", is_approved: false },
  { tool_name: "Google Gemini", domain: "gemini.google.com", category: "chat", vendor: "Google", risk_level: "medium", is_approved: true },
  { tool_name: "Google AI Studio", domain: "aistudio.google.com", category: "api", vendor: "Google", risk_level: "high", is_approved: true },
  { tool_name: "Google AI API", domain: "generativelanguage.googleapis.com", category: "api", vendor: "Google", risk_level: "high", is_approved: false },
  { tool_name: "Meta AI", domain: "ai.meta.com", category: "chat", vendor: "Meta", risk_level: "medium", is_approved: true },
  { tool_name: "Meta Llama", domain: "llama.meta.com", category: "api", vendor: "Meta", risk_level: "high", is_approved: true },
  { tool_name: "Replicate", domain: "replicate.com", category: "api", vendor: "Replicate", risk_level: "high", is_approved: false },
  { tool_name: "Hugging Face", domain: "huggingface.co", category: "api", vendor: "Hugging Face", risk_level: "high", is_approved: false },
  { tool_name: "Cohere", domain: "cohere.com", category: "api", vendor: "Cohere", risk_level: "high", is_approved: false },
  { tool_name: "Midjourney", domain: "midjourney.com", category: "image", vendor: "Midjourney", risk_level: "medium", is_approved: false },
  { tool_name: "Stability AI", domain: "stability.ai", category: "image", vendor: "Stability AI", risk_level: "high", is_approved: false },
  { tool_name: "DALL-E", domain: "labs.openai.com", category: "image", vendor: "OpenAI", risk_level: "medium", is_approved: true },
  { tool_name: "ElevenLabs", domain: "elevenlabs.io", category: "audio", vendor: "ElevenLabs", risk_level: "medium", is_approved: false },
  { tool_name: "Runway", domain: "runwayml.com", category: "video", vendor: "Runway", risk_level: "high", is_approved: false },
  { tool_name: "Perplexity", domain: "perplexity.ai", category: "search", vendor: "Perplexity", risk_level: "medium", is_approved: false },
  { tool_name: "You.com", domain: "you.com", category: "search", vendor: "You.com", risk_level: "medium", is_approved: false },
  { tool_name: "Notion AI", domain: "notion.so", category: "productivity", vendor: "Notion", risk_level: "low", is_approved: true },
  { tool_name: "Jasper", domain: "jasper.ai", category: "productivity", vendor: "Jasper", risk_level: "medium", is_approved: false },
  { tool_name: "Grammarly", domain: "grammarly.com", category: "productivity", vendor: "Grammarly", risk_level: "low", is_approved: true },
  { tool_name: "GitHub Copilot", domain: "copilot.github.com", category: "coding", vendor: "Microsoft", risk_level: "low", is_approved: true },
  { tool_name: "Tabnine", domain: "tabnine.com", category: "coding", vendor: "Tabnine", risk_level: "medium", is_approved: false },
  { tool_name: "Codeium", domain: "codeium.com", category: "coding", vendor: "Codeium", risk_level: "medium", is_approved: false },
  { tool_name: "Cursor", domain: "cursor.sh", category: "coding", vendor: "Anysphere", risk_level: "medium", is_approved: false },
  { tool_name: "AWS Bedrock", domain: "bedrock.amazonaws.com", category: "api", vendor: "AWS", risk_level: "high", is_approved: true },
  { tool_name: "Azure OpenAI", domain: "openai.azure.com", category: "api", vendor: "Microsoft", risk_level: "high", is_approved: true },
  { tool_name: "Google Vertex AI", domain: "aiplatform.googleapis.com", category: "api", vendor: "Google", risk_level: "high", is_approved: true },
  { tool_name: "Mistral AI", domain: "mistral.ai", category: "api", vendor: "Mistral", risk_level: "high", is_approved: false },
  { tool_name: "Together AI", domain: "together.ai", category: "api", vendor: "Together AI", risk_level: "high", is_approved: false },
  { tool_name: "Groq", domain: "groq.com", category: "api", vendor: "Groq", risk_level: "high", is_approved: false },
  { tool_name: "Ollama", domain: "ollama.ai", category: "api", vendor: "Ollama", risk_level: "low", is_approved: true },
  { tool_name: "LM Studio", domain: "lmstudio.ai", category: "api", vendor: "LM Studio", risk_level: "low", is_approved: true },
  { tool_name: "Writesonic", domain: "writesonic.com", category: "productivity", vendor: "Writesonic", risk_level: "medium", is_approved: false },
  { tool_name: "Copy.ai", domain: "copy.ai", category: "productivity", vendor: "Copy.ai", risk_level: "medium", is_approved: false },
  { tool_name: "Synthesia", domain: "synthesia.io", category: "video", vendor: "Synthesia", risk_level: "high", is_approved: false },
  { tool_name: "Descript", domain: "descript.com", category: "audio", vendor: "Descript", risk_level: "medium", is_approved: false },
  { tool_name: "Whisper API", domain: "whisper.openai.com", category: "audio", vendor: "OpenAI", risk_level: "high", is_approved: false },
  { tool_name: "Leonardo AI", domain: "leonardo.ai", category: "image", vendor: "Leonardo AI", risk_level: "medium", is_approved: false },
  { tool_name: "Poe", domain: "poe.com", category: "chat", vendor: "Quora", risk_level: "medium", is_approved: false },
  { tool_name: "Character.AI", domain: "character.ai", category: "chat", vendor: "Character.AI", risk_level: "medium", is_approved: false },
  { tool_name: "Phind", domain: "phind.com", category: "search", vendor: "Phind", risk_level: "medium", is_approved: false },
  { tool_name: "DeepSeek", domain: "deepseek.com", category: "chat", vendor: "DeepSeek", risk_level: "medium", is_approved: false },
  { tool_name: "DeepSeek API", domain: "api.deepseek.com", category: "api", vendor: "DeepSeek", risk_level: "high", is_approved: false },
  { tool_name: "Suno AI", domain: "suno.ai", category: "audio", vendor: "Suno", risk_level: "medium", is_approved: false },
  { tool_name: "Udio", domain: "udio.com", category: "audio", vendor: "Udio", risk_level: "medium", is_approved: false },
  { tool_name: "Ideogram", domain: "ideogram.ai", category: "image", vendor: "Ideogram", risk_level: "medium", is_approved: false },
  { tool_name: "Lovable", domain: "lovable.dev", category: "coding", vendor: "Lovable", risk_level: "medium", is_approved: false },
  { tool_name: "Bolt", domain: "bolt.new", category: "coding", vendor: "StackBlitz", risk_level: "medium", is_approved: false },
  { tool_name: "v0", domain: "v0.dev", category: "coding", vendor: "Vercel", risk_level: "medium", is_approved: false },
  { tool_name: "Replit AI", domain: "replit.com", category: "coding", vendor: "Replit", risk_level: "medium", is_approved: false },
  { tool_name: "Vercel AI", domain: "sdk.vercel.ai", category: "api", vendor: "Vercel", risk_level: "high", is_approved: false },
  { tool_name: "Fireworks AI", domain: "fireworks.ai", category: "api", vendor: "Fireworks", risk_level: "high", is_approved: false },
  { tool_name: "Anyscale", domain: "anyscale.com", category: "api", vendor: "Anyscale", risk_level: "high", is_approved: false },
];

export const categories = [...new Set(aiToolsRegistry.map(t => t.category))];
export const vendors = [...new Set(aiToolsRegistry.map(t => t.vendor))];
export const riskLevels: AITool["risk_level"][] = ["low", "medium", "high"];
```

### devise-iris/frontend\src\lib\AuthContext.tsx

```tsx
import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";
import { 
  onAuthStateChanged, 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword, 
  signOut as firebaseSignOut,
  updateProfile,
  type User 
} from "firebase/auth";
import { doc, setDoc, getDoc, serverTimestamp } from "firebase/firestore";
import { updateLastActive } from "@/services/api";
import { auth, db } from "@/lib/firebase";

interface AuthContextType {
  user: User | null;
  session: User | null; // Alias for compatibility
  loading: boolean;
  signIn: (email: string, password: string) => Promise<{ error: Error | null }>;
  signUp: (email: string, password: string, fullName?: string) => Promise<{ error: Error | null }>;
  signOut: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (firebaseUser) => {
      setUser(firebaseUser);
      if (firebaseUser) {
        // Update last_active on login
        await updateLastActive();
        
        // Initial theme sync from Firestore
        const profileRef = doc(db, "profiles", firebaseUser.uid);
        const profileSnap = await getDoc(profileRef);
        if (profileSnap.exists()) {
          const data = profileSnap.data();
          if (data.dark_mode !== undefined) {
            const isDark = data.dark_mode;
            document.documentElement.classList.toggle("dark", isDark);
            localStorage.setItem("theme", isDark ? "dark" : "light");
          }
        }
      }
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  const signIn = async (email: string, password: string) => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      return { error: null };
    } catch (error) {
      return { error: error as Error };
    }
  };

  const signUp = async (email: string, password: string, fullName?: string) => {
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      if (fullName && user) {
        await updateProfile(user, { displayName: fullName });
      }

      // Create initial Firestore profile and organization for the new user
      if (user) {
        const orgId = `org_${user.uid.slice(0, 8)}`;
        
        // 1. Create Organization
        await setDoc(doc(db, "organizations", orgId), {
          id: orgId,
          name: `${fullName || 'My'}'s Team`,
          slug: orgId,
          created_at: new Date().toISOString()
        });

        // 2. Create User Profile
        await setDoc(doc(db, "profiles", user.uid), {
          id: user.uid,
          email: user.email,
          full_name: fullName || "",
          org_id: orgId,
          role: "admin",
          department: "General",
          created_at: new Date().toISOString()
        });

        // 3. Create Default Org Settings
        await setDoc(doc(db, "org_settings", orgId), {
          id: orgId,
          org_id: orgId,
          monthly_budget: 1000,
          alert_threshold: 80,
          auto_block: false,
          allowed_categories: ["AI Assistant", "Development"],
          blocked_domains: [],
          notification_email: true,
          notification_slack: false
        });
      }

      return { error: null };
    } catch (error) {
      console.error("Signup error:", error);
      return { error: error as Error };
    }
  };

  const signOut = async () => {
    try {
      if (user) {
        await updateLastActive();
      }
    } catch (e) {
      console.error("Failed to update last_active on sign out", e);
    }
    await firebaseSignOut(auth);
  };

  return (
    <AuthContext.Provider value={{ user, session: user, loading, signIn, signUp, signOut }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
```

### devise-iris/frontend\src\lib\firebase.ts

```ts
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBju5m5jdhrlMBeUjnxSqMJUS4Hs8jpGDg",
  authDomain: "steadfast-wares-481309-m5.firebaseapp.com",
  projectId: "steadfast-wares-481309-m5",
  storageBucket: "steadfast-wares-481309-m5.firebasestorage.app",
  messagingSenderId: "1017722427416",
  appId: "1:1017722427416:web:ed0a9b4f3ab392bf4acb6d",
  measurementId: "G-1D8PQZKEY0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const analytics = getAnalytics(app);
```

### devise-iris/frontend\src\lib\utils.ts

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

### devise-iris/frontend\src\pages\Alerts.tsx

```tsx
import { AlertTriangle, Shield, Clock } from "lucide-react";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { StatsCard } from "@/components/dashboard/StatsCard";
import { AlertsList } from "@/components/dashboard/AlertsList";
import { useStats, useAlerts } from "@/hooks/useDashboard";

const Alerts = () => {
  const { data: stats } = useStats();
  const { data: alerts = [] } = useAlerts();

  const tamperCount = alerts.filter(a => a.type === "tamper").length;
  const agentGapCount = alerts.filter(a => a.type === "agent_gap").length;

  return (
    <DashboardLayout title="Alerts">
      <div className="space-y-6">
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
          <StatsCard title="Active Alerts" value={stats?.activeAlerts ?? "—"} icon={AlertTriangle} variant="primary" />
          <StatsCard title="Tamper Alerts" value={tamperCount} icon={Shield} />
          <StatsCard title="Agent Gaps" value={agentGapCount} icon={Clock} />
          <StatsCard title="High Risk Unapproved" value={stats?.highRiskCount ?? "—"} icon={AlertTriangle} />
        </div>

        <AlertsList />
      </div>
    </DashboardLayout>
  );
};

export default Alerts;
```

### devise-iris/frontend\src\pages\Analytics.tsx

```tsx
import { Activity, Shield, AlertTriangle, Ban } from "lucide-react";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { StatsCard } from "@/components/dashboard/StatsCard";
import { AnalyticsCharts } from "@/components/dashboard/AnalyticsCharts";
import { useStats } from "@/hooks/useDashboard";

const Analytics = () => {
  const { data: stats } = useStats();

  return (
    <DashboardLayout title="Analytics">
      <div className="space-y-6">
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
          <StatsCard title="Total Detections" value={stats?.totalDetections ?? "—"} icon={Activity} variant="primary" />
          <StatsCard title="Unique Tools" value={stats?.uniqueTools ?? "—"} icon={Shield} />
          <StatsCard title="High Risk" value={stats?.highRiskCount ?? "—"} icon={AlertTriangle} />
          <StatsCard title="Unapproved" value={stats?.unapprovedCount ?? "—"} icon={Ban} />
        </div>

        <AnalyticsCharts />
      </div>
    </DashboardLayout>
  );
};

export default Analytics;
```

### devise-iris/frontend\src\pages\Devices.tsx

```tsx
import { Monitor, Wifi, WifiOff, AlertTriangle } from "lucide-react";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { StatsCard } from "@/components/dashboard/StatsCard";
import { DevicesTable } from "@/components/dashboard/DevicesTable";
import { useStats } from "@/hooks/useDashboard";

const Devices = () => {
  const { data: stats } = useStats();

  return (
    <DashboardLayout title="Devices">
      <div className="space-y-6">
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
          <StatsCard title="Total Devices" value={stats?.totalDevices ?? "—"} icon={Monitor} variant="primary" />
          <StatsCard title="Online" value={stats?.onlineDevices ?? "—"} icon={Wifi} subtitle="Last 6 min" />
          <StatsCard title="Offline" value={stats ? stats.totalDevices - stats.onlineDevices : "—"} icon={WifiOff} />
          <StatsCard title="Active Alerts" value={stats?.activeAlerts ?? "—"} icon={AlertTriangle} />
        </div>

        <DevicesTable />
      </div>
    </DashboardLayout>
  );
};

export default Devices;
```

### devise-iris/frontend\src\pages\Index.tsx

```tsx
// Update this page (the content is just a fallback if you fail to update the page)

const Index = () => {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background">
      <div className="text-center">
        <h1 className="mb-4 text-4xl font-bold">Welcome to Your Blank App</h1>
        <p className="text-xl text-muted-foreground">Start building your amazing project here!</p>
      </div>
    </div>
  );
};

export default Index;
```

### devise-iris/frontend\src\pages\LiveFeed.tsx

```tsx
import { useState, useMemo } from "react";
import { Activity, Shield, AlertTriangle, Ban } from "lucide-react";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { StatsCard } from "@/components/dashboard/StatsCard";
import { LiveFeedTable } from "@/components/dashboard/LiveFeedTable";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { categories, riskLevels } from "@/lib/aiToolsRegistry";
import { useEvents, useStats } from "@/hooks/useDashboard";

const LiveFeed = () => {
  const [categoryFilter, setCategoryFilter] = useState<string>("all");
  const [riskFilter, setRiskFilter] = useState<string>("all");

  const { data: eventsData, isLoading } = useEvents(categoryFilter, riskFilter);
  const { data: stats } = useStats();

  const events = useMemo(() => eventsData?.events ?? [], [eventsData]);

  return (
    <DashboardLayout title="Live Feed">
      <div className="space-y-6">
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
          <StatsCard title="Total Detections" value={stats?.totalDetections ?? "—"} icon={Activity} variant="primary" subtitle="Last 24h" />
          <StatsCard title="Unique Tools" value={stats?.uniqueTools ?? "—"} icon={Shield} subtitle="Active tools" />
          <StatsCard title="High Risk" value={stats?.highRiskCount ?? "—"} icon={AlertTriangle} subtitle="Needs review" />
          <StatsCard title="Unapproved" value={stats?.unapprovedCount ?? "—"} icon={Ban} subtitle="Not sanctioned" />
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <Select value={categoryFilter} onValueChange={setCategoryFilter}>
            <SelectTrigger className="w-[150px] h-9 text-sm">
              <SelectValue placeholder="Category" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Categories</SelectItem>
              {categories.map(c => (
                <SelectItem key={c} value={c} className="capitalize">{c}</SelectItem>
              ))}
            </SelectContent>
          </Select>

          <Select value={riskFilter} onValueChange={setRiskFilter}>
            <SelectTrigger className="w-[140px] h-9 text-sm">
              <SelectValue placeholder="Risk Level" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Risks</SelectItem>
              {riskLevels.map(r => (
                <SelectItem key={r} value={r} className="capitalize">{r}</SelectItem>
              ))}
            </SelectContent>
          </Select>

          {isLoading && (
            <span className="text-xs text-muted-foreground animate-pulse">Refreshing…</span>
          )}
        </div>

        <LiveFeedTable events={events} />
      </div>
    </DashboardLayout>
  );
};

export default LiveFeed;
```

### devise-iris/frontend\src\pages\LoginPage.tsx

```tsx
import { useState } from "react";
import { Link } from "react-router-dom";
import { Grid2x2, Eye, EyeOff, ChevronLeft, Loader2 } from "lucide-react";
import { useAuth } from "@/lib/AuthContext";
import { useNavigate } from "react-router-dom";

export function LoginPage() {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const { signIn } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please fill in all fields");
      return;
    }
    setError("");
    setLoading(true);
    
    try {
      const { error: authError } = await signIn(email, password);
      if (authError) {
        setError(authError.message);
      } else {
        navigate("/dashboard");
      }
    } catch (err: any) {
      setError("An unexpected error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen w-screen overflow-hidden grid grid-cols-1 lg:grid-cols-2">
      {/* LEFT PANEL */}
      <div className="hidden lg:block relative overflow-hidden bg-[#0A0E1A]">
        {/* Background Image */}
        <img
          src="/src/assets/login-image.png"
          alt="Premium background"
          className="absolute inset-0 w-full h-full object-cover opacity-80"
        />

        {/* TOP LEFT RECTANGLE LOGO */}
        <div className="absolute top-0 left-0 p-8 flex items-center gap-2 z-10">
          <div className="w-8 h-8 bg-[#F04E23] rounded-lg flex items-center justify-center">
            <Grid2x2 className="text-white w-4 h-4" />
          </div>
          <span className="text-white font-bold text-lg">Devise</span>
        </div>


      </div>

      {/* RIGHT PANEL */}
      <div className="bg-white flex flex-col items-center justify-center px-8 md:px-16 lg:px-20 relative">
        {/* BACK TO HOME (MOBILE) */}
        <Link
          to="/"
          className="absolute top-8 left-8 flex items-center gap-1 text-xs text-gray-400 hover:text-gray-600 z-10 lg:ml-0"
        >
          <ChevronLeft className="w-3 h-3" />
          Back to home
        </Link>

        {/* FORM CONTAINER */}
        <div className="max-w-md w-full">
          {/* MOBILE LOGO */}
          <div className="lg:hidden flex items-center gap-2 mb-8">
            <div className="w-8 h-8 bg-[#F04E23] rounded-lg flex items-center justify-center">
              <Grid2x2 className="text-white w-4 h-4" />
            </div>
            <span className="text-[#1A1A1A] font-bold text-lg">Devise</span>
          </div>

          <div className="mb-8">
            <h1 className="text-3xl font-bold text-[#1A1A1A] mb-1">Welcome back</h1>
            <p className="text-sm text-gray-500">Sign in to your Devise account</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 mb-1.5 block">
                Work Email
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@company.com"
                className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
              />
            </div>

            <div>
              <div className="flex justify-between items-center mb-1.5">
                <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 block">
                  Password
                </label>
                <Link to="#" className="text-xs text-[#F04E23] hover:underline">
                  Forgot password?
                </Link>
              </div>
              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
              {error && <p className="text-xs text-red-500 mt-1">{error}</p>}
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-[#F04E23] text-white rounded-xl py-3.5 font-semibold text-sm mt-2 hover:bg-orange-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {loading && <Loader2 className="w-4 h-4 animate-spin" />}
              {loading ? "Signing In..." : "Sign In"}
            </button>
          </form>

          <div className="flex items-center gap-3 my-4 text-gray-100">
            <div className="flex-1 h-px bg-gray-100" />
            <span className="text-xs text-gray-400">or</span>
            <div className="flex-1 h-px bg-gray-100" />
          </div>

          <button className="w-full border border-gray-200 rounded-xl py-3.5 flex items-center justify-center gap-3 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
            <svg viewBox="0 0 24 24" className="w-[18px] h-[18px]">
              <path
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                fill="#4285F4"
              />
              <path
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                fill="#34A853"
              />
              <path
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"
                fill="#FBBC05"
              />
              <path
                d="M12 5.38c1.62 0 3.06.56 4.21 1.66l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                fill="#EA4335"
              />
            </svg>
            Continue with Google
          </button>

          <p className="text-center text-sm text-gray-500 mt-6">
            Don't have an account?
            <Link to="/signup" className="text-[#F04E23] font-medium hover:underline ml-1">
              Sign up
            </Link>
          </p>

          <p className="text-center text-xs text-gray-400 mt-8">
            By signing in you agree to our{" "}
            <Link to="#" className="text-gray-400 hover:text-[#F04E23] underline transition-colors">
              Terms of Service
            </Link>{" "}
            and{" "}
            <Link to="#" className="text-gray-400 hover:text-[#F04E23] underline transition-colors">
              Privacy Policy
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\pages\NotFound.tsx

```tsx
import { useLocation } from "react-router-dom";
import { useEffect } from "react";

const NotFound = () => {
  const location = useLocation();

  useEffect(() => {
    console.error("404 Error: User attempted to access non-existent route:", location.pathname);
  }, [location.pathname]);

  return (
    <div className="flex min-h-screen items-center justify-center bg-muted">
      <div className="text-center">
        <h1 className="mb-4 text-4xl font-bold">404</h1>
        <p className="mb-4 text-xl text-muted-foreground">Oops! Page not found</p>
        <a href="/" className="text-primary underline hover:text-primary/90">
          Return to Home
        </a>
      </div>
    </div>
  );
};

export default NotFound;
```

### devise-iris/frontend\src\pages\SignupPage.tsx

```tsx
import { useState, useMemo } from "react";
import { Link } from "react-router-dom";
import { Grid2x2, Eye, EyeOff, ChevronLeft, ShieldCheck, Lock, Eye as EyeIcon, Loader2 } from "lucide-react";
import { useAuth } from "@/lib/AuthContext";
import { useNavigate } from "react-router-dom";

export function SignupPage() {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    company: "",
    password: "",
  });

  const passwordStrength = useMemo(() => {
    const len = formData.password.length;
    if (len === 0) return 0;
    if (len < 4) return 1;
    if (len < 8) return 2;
    if (len < 12) return 3;
    return 4;
  }, [formData.password]);

  const strengthColor = ["bg-gray-100", "bg-red-500", "bg-orange-500", "bg-yellow-500", "bg-green-500"][passwordStrength];

  const { signUp } = useAuth();
  const navigate = useNavigate();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const { error: authError } = await signUp(formData.email, formData.password, formData.fullName);
      if (authError) {
        setError(authError.message);
      } else {
        navigate("/dashboard");
      }
    } catch (err: any) {
      setError("An unexpected error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen w-screen overflow-hidden grid grid-cols-1 lg:grid-cols-2">
      {/* LEFT PANEL */}
      <div className="hidden lg:block relative overflow-hidden bg-[#0A0E1A]">
        <img
          src="/src/assets/login-image.png"
          alt="Premium background"
          className="absolute inset-0 w-full h-full object-cover opacity-80"
        />

        <div className="absolute top-0 left-0 p-8 flex items-center gap-2 z-10">
          <div className="w-8 h-8 bg-[#F04E23] rounded-lg flex items-center justify-center">
            <Grid2x2 className="text-white w-4 h-4" />
          </div>
          <span className="text-white font-bold text-lg">Devise</span>
        </div>


      </div>

      {/* RIGHT PANEL */}
      <div className="bg-white flex flex-col items-center justify-center px-8 md:px-16 lg:px-20 relative overflow-y-auto">
        <Link
          to="/"
          className="absolute top-8 left-8 flex items-center gap-1 text-xs text-gray-400 hover:text-gray-600 z-10"
        >
          <ChevronLeft className="w-3 h-3" />
          Back to home
        </Link>

        <div className="max-w-md w-full py-12">
          <div className="lg:hidden flex items-center gap-2 mb-8">
            <div className="w-8 h-8 bg-[#F04E23] rounded-lg flex items-center justify-center">
              <Grid2x2 className="text-white w-4 h-4" />
            </div>
            <span className="text-[#1A1A1A] font-bold text-lg">Devise</span>
          </div>

          <div className="mb-8">
            <h1 className="text-3xl font-bold text-[#1A1A1A] mb-1">Get started free</h1>
            <p className="text-sm text-gray-500">Create your Devise account</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 mb-1.5 block">
                Full Name
              </label>
              <input
                type="text"
                required
                value={formData.fullName}
                onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
                placeholder="Priya Sharma"
                className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
              />
            </div>

            <div>
              <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 mb-1.5 block">
                Work Email
              </label>
              <input
                type="email"
                required
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                placeholder="you@company.com"
                className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
              />
            </div>

            <div>
              <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 mb-1.5 block">
                Company
              </label>
              <input
                type="text"
                required
                value={formData.company}
                onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                placeholder="Acme Corp"
                className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
              />
            </div>

            <div>
              <label className="text-xs font-semibold uppercase tracking-widest text-gray-500 mb-1.5 block">
                Password
              </label>
              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  required
                  value={formData.password}
                  onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                  placeholder="Min. 8 characters"
                  className="w-full border border-gray-200 rounded-xl px-4 py-3.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:border-[#F04E23] focus:ring-1 focus:ring-[#F04E23] transition-colors"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
              
              {/* Strength Indicator */}
              <div className="flex gap-1.5 mt-2">
                {[1, 2, 3, 4].map((step) => (
                  <div
                    key={step}
                    className={`h-1 flex-1 rounded-full transition-colors duration-300 ${
                      passwordStrength >= step ? strengthColor : "bg-gray-100"
                    }`}
                  />
                ))}
              </div>
            </div>
            {error && <p className="text-xs text-red-500 mt-1 text-center">{error}</p>}


            <button
              type="submit"
              disabled={loading}
              className="w-full bg-[#F04E23] text-white rounded-xl py-3.5 font-semibold text-sm mt-2 hover:bg-orange-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {loading && <Loader2 className="w-4 h-4 animate-spin" />}
              {loading ? "Creating Account..." : "Create Account"}
            </button>
          </form>

          <div className="flex items-center gap-3 my-4 text-gray-100">
            <div className="flex-1 h-px bg-gray-100" />
            <span className="text-xs text-gray-400">or</span>
            <div className="flex-1 h-px bg-gray-100" />
          </div>

          <button className="w-full border border-gray-200 rounded-xl py-3.5 flex items-center justify-center gap-3 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
            <svg viewBox="0 0 24 24" className="w-[18px] h-[18px]">
              <path
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                fill="#4285F4"
              />
              <path
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                fill="#34A853"
              />
              <path
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"
                fill="#FBBC05"
              />
              <path
                d="M12 5.38c1.62 0 3.06.56 4.21 1.66l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                fill="#EA4335"
              />
            </svg>
            Sign up with Google
          </button>

          <p className="text-center text-sm text-gray-500 mt-6">
            Already have an account?
            <Link to="/login" className="text-[#F04E23] font-medium hover:underline ml-1">
              Sign in
            </Link>
          </p>

          <div className="flex items-center justify-center gap-6 mt-8">
            <div className="flex items-center gap-1.5 text-[10px] sm:text-xs text-gray-400">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>SOC 2 Certified</span>
            </div>
            <div className="flex items-center gap-1.5 text-[10px] sm:text-xs text-gray-400">
              <Lock className="w-3.5 h-3.5" />
              <span>256-bit encryption</span>
            </div>
            <div className="flex items-center gap-1.5 text-[10px] sm:text-xs text-gray-400">
              <EyeIcon className="w-3.5 h-3.5" />
              <span>No card required</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### devise-iris/frontend\src\pages\landing\AboutPage.tsx

```tsx
import { Eye, Shield, Building, Globe } from "lucide-react";
import { Layout } from "../../components/landing/Layout";

export const AboutPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="pt-32 pb-24 px-6 max-w-4xl mx-auto text-center">
        <h1 className="text-5xl md:text-6xl font-bold text-brand-dark leading-tight">
          The Future of AI Is Governed. Or It Isn&apos;t.
        </h1>
        <p className="text-xl text-brand-gray mt-6 max-w-2xl mx-auto">
          Every enterprise will need a system of record for AI — just like they have one for finance, HR, and security. Devise is that system.
        </p>

        <div className="mt-12 bg-white rounded-2xl shadow-lg p-6 border-l-4 border-brand-orange max-w-2xl mx-auto text-left">
          <p className="text-brand-dark text-lg font-medium italic">
            &ldquo;You can&apos;t govern what you can&apos;t see. We make it visible.&rdquo;
          </p>
        </div>
      </section>

      {/* Mission */}
      <section className="py-24 px-6 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold text-brand-dark mb-6">Our Mission</h2>
        <p className="text-brand-gray text-lg leading-relaxed">
          Devise was built because enterprise AI adoption has outpaced every governance framework that exists. We exist to close that gap — giving security, finance, and AI leaders the real-time visibility they need to operate confidently in an AI-first world.
        </p>
      </section>

      {/* Values */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {[
            { icon: <Eye />, title: "Transparency", desc: "We believe enterprises deserve full visibility into their AI usage — no blind spots." },
            { icon: <Shield />, title: "Security-First", desc: "Every design decision starts with the question: how does this protect our customers?" },
            { icon: <Building />, title: "Enterprise-Grade", desc: "Built for the compliance, scale, and reliability demands of large organizations." },
            { icon: <Globe />, title: "India-Built", desc: "Proudly built in India, for global enterprises navigating the AI era." },
          ].map((v, i) => (
            <div key={i} className="bg-white rounded-2xl shadow-lg p-8">
              <div className="text-brand-orange mb-4">{v.icon}</div>
              <h4 className="text-lg font-bold text-brand-dark mb-3">{v.title}</h4>
              <p className="text-brand-gray text-sm leading-relaxed">{v.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Dark CTA */}
      <section className="mx-6 md:mx-auto max-w-5xl rounded-2xl bg-brand-navy text-white py-16 px-8 mb-24 text-center">
        <h2 className="text-3xl font-bold mb-4">Join us in building the future of AI governance.</h2>
        <p className="text-gray-400 mb-8">We&apos;re hiring across engineering, design, and go-to-market.</p>
        <button className="bg-brand-orange text-white rounded-full px-8 py-3 font-semibold hover:bg-orange-600 transition-colors">
          View Careers
        </button>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\pages\landing\DemoPage.tsx

```tsx
import { useState } from "react";
import { CheckCircle, Shield } from "lucide-react";
import { Layout } from "../../components/landing/Layout";

export const DemoPage = () => {
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <Layout>
      <section className="relative overflow-hidden pt-32 pb-24 px-6">
        <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-[radial-gradient(circle,_#F04E23_0%,_transparent_70%)] opacity-[0.6] blur-3xl -z-10 pointer-events-none" />
        <div className="absolute bottom-0 right-0 w-[400px] h-[400px] bg-[radial-gradient(circle,_#F04E23_0%,_transparent_70%)] opacity-[0.6] blur-3xl -z-10 pointer-events-none" />

        <div className="max-w-4xl mx-auto text-center relative z-10 mb-16">
          <h1 className="text-5xl font-bold text-brand-dark">Book a 30-Minute Demo</h1>
          <p className="text-xl text-brand-gray mt-4">See Devise reveal your organization&apos;s complete AI landscape.</p>
        </div>

        <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 relative z-10">
          {/* Form */}
          <div className="bg-white rounded-2xl shadow-lg p-8">
            {submitted ? (
              <div className="text-center py-16">
                <CheckCircle className="text-brand-green mx-auto mb-4" size={48} />
                <h3 className="text-2xl font-bold text-brand-dark mb-2">Demo Booked!</h3>
                <p className="text-brand-gray">We&apos;ll be in touch within 24 hours.</p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <input type="text" placeholder="First Name" required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm" />
                  <input type="text" placeholder="Last Name" required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm" />
                </div>
                <input type="email" placeholder="Work Email" required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm" />
                <input type="text" placeholder="Company Name" required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm" />
                <select required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm text-brand-gray">
                  <option value="">Company Size</option>
                  <option>&lt;50</option>
                  <option>50-200</option>
                  <option>200-500</option>
                  <option>500-2000</option>
                  <option>2000+</option>
                </select>
                <select required className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm text-brand-gray">
                  <option value="">Your Role</option>
                  <option>CISO</option>
                  <option>CFO</option>
                  <option>Head of AI</option>
                  <option>IT Admin</option>
                  <option>Other</option>
                </select>
                <textarea placeholder="Message (optional)" rows={3} className="border border-gray-200 rounded-lg px-4 py-3 w-full focus:outline-none focus:border-brand-orange text-sm" />
                <button type="submit" className="w-full bg-brand-orange text-white rounded-full py-3 font-semibold hover:bg-orange-600 transition-colors">
                  Book Demo →
                </button>
              </form>
            )}
          </div>

          {/* Info */}
          <div className="bg-white rounded-2xl shadow-lg p-8">
            <h3 className="text-xl font-bold text-brand-dark mb-6">What you&apos;ll see in the demo</h3>
            <div className="space-y-4 mb-8">
              {[
                "Live AI tool detection across a simulated org (browser + desktop)",
                "Real-time Oversight violations feed and policy alerts",
                "Pulse adoption heatmap and Spend zombie license detection",
              ].map((item) => (
                <div key={item} className="flex items-start gap-3 text-sm text-brand-dark font-medium">
                  <CheckCircle className="text-brand-orange shrink-0 mt-0.5" size={18} /> {item}
                </div>
              ))}
            </div>
            <div className="h-px bg-gray-200 mb-6" />
            <p className="text-brand-gray text-sm mb-6">No credit card required. No installation before the call.</p>
            <div className="flex flex-wrap gap-3">
              {["SOC 2", "GDPR", "30 min"].map((badge) => (
                <span key={badge} className="bg-brand-cream rounded-full px-4 py-1.5 text-xs font-medium text-brand-dark flex items-center gap-1.5">
                  <Shield size={12} className="text-brand-orange" /> {badge}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\pages\landing\Index.tsx

```tsx
// Update this page (the content is just a fallback if you fail to update the page)

const Index = () => {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background">
      <div className="text-center">
        <h1 className="mb-4 text-4xl font-bold">Welcome to Your Blank App</h1>
        <p className="text-xl text-muted-foreground">Start building your amazing project here!</p>
      </div>
    </div>
  );
};

export default Index;
```

### devise-iris/frontend\src\pages\landing\LandingPage.tsx

```tsx
import { Link } from "react-router-dom";
import * as Accordion from "@radix-ui/react-accordion";
import * as Tabs from "@radix-ui/react-tabs";
import {
  Shield, BarChart2, DollarSign, Layers, ShieldOff,
  AlertOctagon, Rocket, Search, Brain, Zap, CheckCircle,
  ArrowRight, Plus, Minus, Star, Cpu, Eye, Settings,
  FileText, Map, Server, Globe, Lock, Clock, Key, X
} from "lucide-react";
import { Layout } from "../../components/landing/Layout";
import { OrangeWaveBackground } from "../../components/landing/OrangeWaveBackground";
import { HeroDashboard, OversightMockup, PulseMockup, SpendMockup } from "../../components/landing/DashboardMockups";
import heroDashboard from "@/assets/hero-dashboard.png";

export const LandingPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="relative pt-32 pb-24 px-6 bg-transparent">
        <OrangeWaveBackground />

        <div className="max-w-4xl mx-auto text-center relative" style={{ zIndex: 1 }}>

          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold text-brand-dark leading-tight mt-6">
            The System of Record for Enterprise AI
          </h1>

          <p className="text-xl md:text-2xl text-brand-gray font-medium mt-4">
            See Every Tool. Govern Every Risk. Control Every Rupee.
          </p>

          <p className="text-base md:text-lg text-brand-gray max-w-2xl mx-auto mt-4 leading-relaxed">
            Devise installs a lightweight agent on employee devices to surface every AI tool
            in use — and turns that invisible usage into security, compliance, adoption, and
            cost intelligence that leaders can act on.
          </p>

          <div className="flex flex-wrap gap-4 justify-center mt-8">
            <Link to="/login" className="border-2 border-brand-dark text-brand-dark rounded-full px-6 py-2.5 font-medium hover:bg-brand-dark hover:text-white transition-colors">
              Get Started
            </Link>
            <Link to="/demo" className="bg-brand-orange text-white rounded-full px-6 py-2.5 font-medium hover:bg-orange-600 transition-colors shadow-lg shadow-brand-orange/20 flex items-center gap-2">
              Book a Demo <ArrowRight size={16} />
            </Link>
          </div>

        </div>

        {/* Hero Image */}
        <div className="mt-16 max-w-5xl mx-auto relative z-10 group">
          <div className="absolute -inset-1 bg-gradient-to-r from-brand-orange to-brand-purple rounded-2xl blur opacity-10 group-hover:opacity-20 transition duration-1000" />
          <div className="relative bg-white rounded-2xl shadow-2xl overflow-hidden border border-white/20">
            <img src={heroDashboard} alt="Devise AI Tool Activity Dashboard" className="w-full" />
          </div>
          <div className="absolute -top-4 -left-4 w-12 h-12 bg-green-700 rounded-xl shadow-heavy flex items-center justify-center text-white font-bold text-sm">XLS</div>
          <div className="absolute -top-4 -right-4 w-12 h-12 bg-blue-700 rounded-xl shadow-heavy flex items-center justify-center text-white font-bold text-sm">SAP</div>
          <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-red-600 rounded-xl shadow-heavy flex items-center justify-center text-white font-bold text-sm">INF</div>
          <div className="absolute -bottom-4 -left-4 w-12 h-12 bg-blue-500 rounded-xl shadow-heavy flex items-center justify-center text-white font-bold text-sm">OK</div>
        </div>
      </section>


      {/* Problem Section */}
      <section className="py-32 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-[0.2em] text-brand-orange mb-6">The Challenge</div>
        <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16">
          <h2 className="text-4xl md:text-[3.2rem] font-bold text-brand-dark leading-[1.15] max-w-xl">
            Enterprise AI is now three problems at once
          </h2>
          <p className="text-brand-gray text-lg max-w-xs leading-relaxed">
            Most companies can&apos;t answer basic questions about any of them. Can you?
          </p>
        </div>

        {/* Spreadsheet mockup */}
        <div className="bg-white shadow-xl rounded-2xl p-6 max-w-3xl mx-auto relative border border-gray-100">
          <div className="bg-gray-50 rounded-xl p-5 space-y-2.5">
            {[1, 2, 3].map((row) => (
              <div key={row} className="flex gap-2.5">
                {[1, 2, 3, 4].map((col) => (
                  <div key={col} className="flex-1 h-9 bg-gray-200/80 rounded-md" />
                ))}
              </div>
            ))}
            <div className="flex gap-2.5 pt-1">
              {[1, 2].map((col) => (
                <div key={col} className="flex-1 h-7 bg-gray-300/70 rounded-md" />
              ))}
            </div>
          </div>
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-red-400 text-[120px] font-black opacity-60 select-none" style={{ lineHeight: 1 }}>✕</span>
          </div>
        </div>
        <p className="text-center text-brand-gray text-sm mt-4">
          Organisations tried. Emails, surveys, and spreadsheets can&apos;t track this for you.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-20">
          {[
            { icon: <Layers className="w-7 h-7" />, title: "Fragmented Systems", desc: "Your AI tools are scattered across departments with no central view." },
            { icon: <ShieldOff className="w-7 h-7" />, title: "No Policy Enforcement", desc: "Violations go undetected until something goes wrong — no audit trail." },
            { icon: <BarChart2 className="w-7 h-7" />, title: "Zero Adoption Clarity", desc: "2,000 employees using AI, 4 separate trackers, no single source of truth." },
            { icon: <AlertOctagon className="w-7 h-7" />, title: "Reactive, Not Proactive", desc: "Your team discovers shadow AI incidents after the fact, not before." },
          ].map((item, i) => (
            <div key={i} className="p-7 rounded-2xl bg-white border border-gray-100 shadow-soft hover:shadow-heavy transition-all duration-300 group">
              <div className="text-brand-orange mb-5 group-hover:scale-110 transition-transform">{item.icon}</div>
              <h4 className="text-base font-bold text-brand-dark mb-2">{item.title}</h4>
              <p className="text-brand-gray text-sm leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Missing Link */}
      <section className="py-32 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <div className="inline-block text-xs font-semibold uppercase tracking-[0.2em] text-brand-orange bg-brand-orange/10 px-4 py-1.5 rounded-full mb-6">The Missing Link in Your Stack</div>
            <h2 className="text-4xl md:text-5xl font-bold text-brand-dark max-w-3xl mx-auto leading-tight">
              We automate the high-friction work of AI governance, adoption, and spend.
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-12 gap-5">
            {/* Large feature card */}
            <div className="md:col-span-7 bg-brand-navy rounded-3xl p-8 md:p-10 text-white relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-64 h-64 bg-brand-orange/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />
              <div className="relative">
                <div className="flex items-center gap-2 mb-4">
                  <Shield className="w-5 h-5 text-brand-orange" />
                  <span className="text-xs font-bold uppercase tracking-wider text-brand-orange">Oversight</span>
                </div>
                <h3 className="text-2xl font-bold mb-3">Integrated AI Visibility & Policy Enforcement</h3>
                <p className="text-gray-400 text-sm leading-relaxed mb-8 max-w-md">Detect every AI tool in real time, across browsers and desktop apps. Policy violations surface instantly.</p>
                <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl overflow-hidden h-52">
                  <OversightMockup />
                </div>
              </div>
            </div>

            {/* Stacked right cards */}
            <div className="md:col-span-5 flex flex-col gap-5">
              <div className="flex-1 bg-white rounded-3xl border border-gray-100 p-8 shadow-soft group hover:shadow-heavy transition-all duration-300">
                <div className="flex items-center gap-2 mb-4">
                  <BarChart2 className="w-5 h-5 text-brand-purple" />
                  <span className="text-xs font-bold uppercase tracking-wider text-brand-purple">Pulse</span>
                </div>
                <h3 className="text-lg font-bold text-brand-dark mb-2">Real-time AI Adoption Management</h3>
                <p className="text-brand-gray text-sm leading-relaxed">Track which teams are adopting AI, which tools are winning, and where your program needs attention.</p>
              </div>
              <div className="flex-1 bg-white rounded-3xl border border-gray-100 p-8 shadow-soft group hover:shadow-heavy transition-all duration-300">
                <div className="flex items-center gap-2 mb-4">
                  <DollarSign className="w-5 h-5 text-brand-green" />
                  <span className="text-xs font-bold uppercase tracking-wider text-brand-green">Spend</span>
                </div>
                <h3 className="text-lg font-bold text-brand-dark mb-2">AI Cost & Subscription Intelligence</h3>
                <p className="text-brand-gray text-sm leading-relaxed">Map AI usage to subscriptions. Detect zombie licenses. Report ROI with real numbers.</p>
              </div>
            </div>

            {/* Full-width audit trail */}
            <div className="md:col-span-12 bg-brand-dark rounded-3xl p-8 md:p-10 text-white">
              <div className="flex flex-col md:flex-row md:items-start gap-8">
                <div className="md:w-1/3">
                  <div className="flex items-center gap-2 mb-4">
                    <Eye className="w-5 h-5 text-brand-orange" />
                    <span className="text-xs font-bold uppercase tracking-wider text-brand-orange">Audit Trail</span>
                  </div>
                  <h3 className="text-xl font-bold mb-2">Live AI Monitoring</h3>
                  <p className="text-gray-400 text-sm leading-relaxed">Every AI interaction logged, timestamped, and mapped. Regulatory-ready from day one.</p>
                </div>
                <div className="md:w-2/3 bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-5 space-y-3">
                  {[
                    { name: "Priya M.", tool: "ChatGPT", dept: "Engineering", time: "10:32 AM", badge: "ALERT" },
                    { name: "David R.", tool: "Copilot", dept: "Product", time: "10:28 AM", badge: "OK" },
                    { name: "Lin W.", tool: "Midjourney", dept: "Design", time: "10:15 AM", badge: "ALERT" },
                    { name: "Sam K.", tool: "Claude", dept: "Legal", time: "10:02 AM", badge: "OK" },
                  ].map((item, i) => (
                    <div key={i} className="flex justify-between items-center text-xs py-2 border-b border-white/5 last:border-0">
                      <div className="flex items-center gap-3">
                        <div className="w-7 h-7 rounded-full bg-gradient-to-br from-gray-600 to-gray-700 flex items-center justify-center text-[10px] font-bold">{item.name.charAt(0)}</div>
                        <div>
                          <span className="font-semibold block">{item.name}</span>
                          <span className="text-gray-500 text-[10px]">{item.dept}</span>
                        </div>
                      </div>
                      <span className="text-gray-400 hidden md:block">{item.tool}</span>
                      <div className="flex items-center gap-3">
                        <span className="text-gray-500">{item.time}</span>
                        <span className={`px-2 py-0.5 rounded-full text-[9px] font-bold ${item.badge === "ALERT" ? "bg-brand-orange/20 text-brand-orange" : "bg-green-500/15 text-green-400"}`}>{item.badge}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4">How It Works</div>
        <h2 className="text-4xl font-bold text-brand-dark mb-2">See. Understand. Act.</h2>
        <p className="text-brand-gray max-w-2xl">
          Devise turns invisible AI usage into visible intelligence — without changing how your teams work.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mt-12">
          {[
            { num: "01", icon: <Rocket className="w-6 h-6" />, title: "Deploy", desc: "IT deploys the Devise agent via Jamf, Intune, Kandji, or SCCM. No network changes. No employee action. Under 30 minutes." },
            { num: "02", icon: <Search className="w-6 h-6" />, title: "Detect", desc: "Every AI tool — browser or desktop — identified against our registry of 3,500+ tools and logged in real time." },
            { num: "03", icon: <Brain className="w-6 h-6" />, title: "Analyze", desc: "The risk engine, adoption engine, and cost engine process events and surface intelligence for each stakeholder." },
            { num: "04", icon: <Zap className="w-6 h-6" />, title: "Act", desc: "Role-specific dashboards give your CISO, CFO, and AI Lead exactly what they need to make confident decisions." },
          ].map((step) => (
            <div key={step.num} className="bg-white rounded-2xl shadow-lg p-6">
              <div className="text-brand-orange mb-4">{step.icon}</div>
              <div className="text-[10px] font-bold text-brand-gray mb-1">{step.num}</div>
              <h4 className="text-lg font-bold text-brand-dark mb-2">{step.title}</h4>
              <p className="text-brand-gray text-sm leading-relaxed">{step.desc}</p>
            </div>
          ))}
        </div>

      </section>

      {/* Stats */}
      <section className="bg-white py-20 px-6">
        <div className="max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-6">
          {[
            { num: "80%", label: "of employees use unapproved AI tools" },
            { num: "86%", label: "of orgs are blind to AI data flows" },
            { num: "30%+", label: "of AI budget wasted on unused licenses" },
            { num: "3,500+", label: "AI tools detected automatically" },
          ].map((stat) => (
            <div key={stat.num} className="bg-white rounded-2xl shadow-md p-6 lg:p-8 text-center border border-gray-100 hover:shadow-lg hover:-translate-y-1 transition-all duration-200 flex flex-col justify-center">
              <div className="text-4xl md:text-5xl lg:text-6xl font-bold text-brand-orange tracking-tight whitespace-nowrap">{stat.num}</div>
              <p className="text-sm text-brand-gray mt-3 max-w-[140px] mx-auto leading-snug">{stat.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 3 Modules */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4">The Solution</div>
        <h2 className="text-4xl font-bold text-brand-dark">One deployment. Complete visibility.</h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <ModuleCard
            tag="Devise Oversight"
            title="AI Governance & Risk Intelligence"
            desc="Surface policy exposure and compliance gaps using real behavioral data — not questionnaires."
            borderColor="border-l-brand-orange"
            tagBg="bg-orange-50"
            tagText="text-brand-orange"
            accentColor="text-brand-orange"
            items={["Complete visibility into AI data flows", "OWASP / NIST / RMF framework mapping", "Shadow AI detection", "Defensible audit trail", "Real-time Slack & email alerts"]}
            ctaText="Get a Demo →"
            ctaLink="/demo"
          />
          <ModuleCard
            tag="Devise Pulse"
            title="AI Adoption Intelligence"
            desc="Replace stale surveys with real behavioral data about how AI is actually being adopted across your organization."
            borderColor="border-l-brand-purple"
            tagBg="bg-purple-50"
            tagText="text-brand-purple"
            accentColor="text-brand-purple"
            items={["Adoption rate by team and department", "Power user identification", "Tool preference tracking", "Training gap surfacing", "Weekly executive reports"]}
            ctaText="Learn more →"
            ctaLink="/product/pulse"
          />
          <ModuleCard
            tag="Devise Spend"
            title="AI Cost Intelligence"
            desc="Connect actual usage to subscription costs. Eliminate zombie licenses and duplicate spend. Justify AI ROI."
            borderColor="border-l-brand-green"
            tagBg="bg-green-50"
            tagText="text-brand-green"
            accentColor="text-brand-green"
            items={["Centralized subscription view", "Zombie license detection", "Duplicate subscription flagging", "Cost attribution by team", "Budget forecasting"]}
            ctaText="Learn more →"
            ctaLink="/product/spend"
          />
        </div>
      </section>

      {/* Why Devise Comparison */}
      <section className="bg-white py-24 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4">Why Devise</div>
          <h2 className="text-4xl font-bold text-brand-dark mb-4">Everything in one deployment</h2>
          <p className="text-brand-gray text-lg max-w-2xl mx-auto mb-12">
            Competitors address one problem. Devise addresses all three simultaneously from a single lightweight agent.
          </p>

          <div className="overflow-x-auto rounded-2xl shadow-lg border border-gray-100">
            <table className="w-full text-left border-collapse min-w-[800px]">
              <thead>
                <tr className="bg-brand-orange text-white">
                  <th className="py-6 px-6 font-semibold text-sm uppercase tracking-wide border-b border-orange-600">Feature</th>
                  <th className="py-6 px-6 font-semibold text-sm uppercase tracking-wide border-b border-orange-600 bg-orange-600/80 text-center relative w-1/4">
                    Devise
                    <div className="absolute -bottom-3 left-1/2 -translate-x-1/2 bg-white text-brand-orange text-[10px] font-bold px-3 py-1 rounded-full shadow-sm flex items-center gap-1">
                      <Star size={10} fill="currentColor" /> Recommended
                    </div>
                  </th>
                  <th className="py-6 px-6 font-semibold text-sm uppercase tracking-wide border-b border-orange-600 text-center w-48">SaaS Mgmt</th>
                  <th className="py-6 px-6 font-semibold text-sm uppercase tracking-wide border-b border-orange-600 text-center w-48">Manual Audits</th>
                  <th className="py-6 px-6 font-semibold text-sm uppercase tracking-wide border-b border-orange-600 text-center w-48">Point Solutions</th>
                </tr>
              </thead>
              <tbody className="bg-white">
                {[
                  { feature: "Real-time AI detection", devise: "yes", saas: "no", manual: "no", point: "partial" },
                  { feature: "No vendor integrations needed", devise: "yes", saas: "no", manual: "yes", point: "no" },
                  { feature: "Governance + Adoption + Cost in one", devise: "yes", saas: "partial", manual: "no", point: "no" },
                  { feature: "Detects shadow AI", devise: "yes", saas: "no", manual: "no", point: "partial" },
                  { feature: "Zero user workflow change", devise: "yes", saas: "no", manual: "no", point: "no" },
                  { feature: "Desktop app coverage", devise: "yes", saas: "no", manual: "no", point: "no" },
                  { feature: "NIST / OWASP framework mapping", devise: "yes", saas: "no", manual: "no", point: "partial" },
                  { feature: "On-premise deployment option", devise: "yes", saas: "partial", manual: "yes", point: "partial" },
                ].map((row, idx) => (
                  <tr key={idx} className={idx % 2 === 0 ? "bg-white" : "bg-gray-50 border-y border-gray-100"}>
                    <td className="py-5 px-6 font-medium text-brand-dark text-sm border-r border-gray-100">{row.feature}</td>
                    <td className="py-5 px-6 text-center border-r border-gray-100 bg-orange-50/50">
                      <CheckCircle className="text-green-600 w-5 h-5 mx-auto" />
                    </td>
                    <td className="py-5 px-6 text-center border-r border-gray-100">
                      {row.saas === "no" ? <X className="text-red-400 w-5 h-5 mx-auto" /> : row.saas === "yes" ? <CheckCircle className="text-green-600 w-5 h-5 mx-auto" /> : <Minus className="text-gray-300 w-5 h-5 mx-auto" />}
                    </td>
                    <td className="py-5 px-6 text-center border-r border-gray-100">
                      {row.manual === "no" ? <X className="text-red-400 w-5 h-5 mx-auto" /> : row.manual === "yes" ? <CheckCircle className="text-green-600 w-5 h-5 mx-auto" /> : <Minus className="text-gray-300 w-5 h-5 mx-auto" />}
                    </td>
                    <td className="py-5 px-6 text-center">
                      {row.point === "no" ? <X className="text-red-400 w-5 h-5 mx-auto" /> : row.point === "yes" ? <CheckCircle className="text-green-600 w-5 h-5 mx-auto" /> : <Minus className="text-gray-300 w-5 h-5 mx-auto" />}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Role Tabs */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4 text-center">Built for Your Role</div>
        <h2 className="text-4xl font-bold text-brand-dark text-center">Built for how enterprise teams work</h2>

        <Tabs.Root defaultValue="ciso" className="w-full mt-12">
          <Tabs.List className="flex justify-center gap-8 border-b border-gray-200 mb-12">
            {[
              { value: "ciso", label: "CISO / Security" },
              { value: "cfo", label: "CFO / Finance" },
              { value: "ai", label: "Head of AI" },
            ].map((tab) => (
              <Tabs.Trigger
                key={tab.value}
                value={tab.value}
                className="pb-4 text-sm font-bold text-brand-gray hover:text-brand-dark data-[state=active]:text-brand-orange data-[state=active]:border-b-2 data-[state=active]:border-brand-orange transition-all outline-none"
              >
                {tab.label}
              </Tabs.Trigger>
            ))}
          </Tabs.List>

          <Tabs.Content value="ciso" className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center animate-in fade-in duration-500">
            <div>
              <h3 className="text-3xl font-bold text-brand-dark mb-6">You can&apos;t manage AI risk without real visibility.</h3>
              <p className="text-brand-gray text-lg mb-8">Devise gives security teams a real-time audit trail, policy enforcement engine, and defensible compliance story — without requiring any integrations with AI vendors.</p>
              <div className="text-xs font-semibold uppercase tracking-widest text-brand-gray mb-4">Questions you can answer:</div>
              <div className="space-y-4">
                {["Is sensitive data leaving our network via AI tools?", "Which employees are using unauthorized tools today?", "Can we demonstrate compliance to regulators?"].map((q) => (
                  <div key={q} className="flex items-center gap-3 font-bold text-brand-dark">
                    <ArrowRight className="text-brand-orange shrink-0" size={18} /> {q}
                  </div>
                ))}
              </div>
            </div>
            <div className="bg-white rounded-2xl shadow-heavy overflow-hidden border border-gray-100">
              <OversightMockup />
            </div>
          </Tabs.Content>

          <Tabs.Content value="cfo" className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center animate-in fade-in duration-500">
            <div>
              <h3 className="text-3xl font-bold text-brand-dark mb-6">Stop paying for AI nobody uses.</h3>
              <p className="text-brand-gray text-lg mb-8">Devise connects actual AI usage to your subscriptions so finance can eliminate waste, justify spend, and forecast accurately.</p>
              <div className="text-xs font-semibold uppercase tracking-widest text-brand-gray mb-4">Questions you can answer:</div>
              <div className="space-y-4">
                {["Which tools are we paying for that nobody uses?", "What's our actual ROI on AI investment?", "How do I attribute AI costs by team?"].map((q) => (
                  <div key={q} className="flex items-center gap-3 font-bold text-brand-dark">
                    <ArrowRight className="text-brand-orange shrink-0" size={18} /> {q}
                  </div>
                ))}
              </div>
            </div>
            <div className="bg-white rounded-2xl shadow-heavy overflow-hidden border border-gray-100">
              <SpendMockup />
            </div>
          </Tabs.Content>

          <Tabs.Content value="ai" className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center animate-in fade-in duration-500">
            <div>
              <h3 className="text-3xl font-bold text-brand-dark mb-6">Run your AI program with real data, not surveys.</h3>
              <p className="text-brand-gray text-lg mb-8">Devise replaces stale survey data with behavioral adoption metrics — so you can show the board that your AI transformation program is actually working.</p>
              <div className="text-xs font-semibold uppercase tracking-widest text-brand-gray mb-4">Questions you can answer:</div>
              <div className="space-y-4">
                {["Are we actually adopting AI or just talking about it?", "Which teams are leading vs lagging?", "Where should I invest training budget?"].map((q) => (
                  <div key={q} className="flex items-center gap-3 font-bold text-brand-dark">
                    <ArrowRight className="text-brand-orange shrink-0" size={18} /> {q}
                  </div>
                ))}
              </div>
            </div>
            <div className="bg-white rounded-2xl shadow-heavy overflow-hidden border border-gray-100">
              <PulseMockup />
            </div>
          </Tabs.Content>
        </Tabs.Root>
      </section>

      {/* Enterprise Ready */}
      <section className="bg-white py-24 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4 text-center">Enterprise Ready</div>
          <h2 className="text-4xl font-bold text-brand-dark text-center mb-12">Built for enterprise requirements</h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { icon: <Shield />, title: "SOC 2 Type I Certified", desc: "Independently audited security controls." },
              { icon: <Key />, title: "SSO & SCIM Integration", desc: "Okta, Azure AD, OneLogin, Google Workspace." },
              { icon: <Server />, title: "On-Premises Option", desc: "All data within your own infrastructure." },
              { icon: <Globe />, title: "GDPR Compliant", desc: "Full European data protection compliance." },
              { icon: <Lock />, title: "End-to-End Encryption", desc: "AES-256 in transit and at rest." },
              { icon: <Clock />, title: "Configurable Retention", desc: "Set retention policies to match compliance needs." },
            ].map((item, i) => (
              <div key={i} className="border border-gray-100 rounded-2xl p-6 shadow-soft">
                <div className="text-brand-orange mb-3">{item.icon}</div>
                <h4 className="font-bold text-brand-dark mb-1">{item.title}</h4>
                <p className="text-brand-gray text-sm">{item.desc}</p>
              </div>
            ))}
          </div>

          <div className="flex flex-wrap gap-4 justify-center mt-10">
            {["SOC 2 Type II", "GDPR Compliant", "Open Source Core", "Self-Host Option"].map((badge) => (
              <span key={badge} className="bg-brand-cream rounded-full px-4 py-1.5 text-sm font-medium text-brand-dark">{badge}</span>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-24 px-6 max-w-2xl mx-auto">
        <h2 className="text-4xl font-bold text-brand-dark text-center mb-16">Frequently Asked Questions</h2>
        <Accordion.Root type="single" collapsible defaultValue="q1">
          {[
            { value: "q1", q: "What is Devise?", a: "Devise is an enterprise AI governance platform that installs a lightweight agent on employee devices to detect every AI tool in use — and turns that usage into security, compliance, adoption, and cost intelligence." },
            { value: "q2", q: "How does it work?", a: "A browser extension and desktop agent monitor AI tool usage at the network and navigation layer. No conversation content is ever captured — only which tool was used, by whom, and when. Events flow into the Devise dashboard in real time." },
            { value: "q3", q: "What data does it collect?", a: "Tool name, domain, user identity, department, timestamp, and source (browser or desktop). We deliberately never capture conversation content, keystrokes, clipboard data, or any user-generated input." },
            { value: "q4", q: "Is it legal?", a: "Yes. Monitoring company-owned devices with employee disclosure is lawful under GDPR and applicable labour law. Devise is SOC 2 Type I certified and architected for GDPR compliance." },
            { value: "q5", q: "How do I get support?", a: "Email us at support@devise.ai or book a demo to speak directly with our team." },
          ].map((faq) => (
            <Accordion.Item key={faq.value} value={faq.value} className="border-b border-gray-200 last:border-b-0 group">
              <Accordion.Header>
                <Accordion.Trigger className="flex w-full items-center justify-between py-5 px-0 text-left font-medium text-brand-dark text-base hover:text-brand-orange transition-colors outline-none cursor-pointer">
                  {faq.q}
                  <Plus className="text-brand-orange w-5 h-5 flex-shrink-0 group-data-[state=open]:hidden" />
                  <Minus className="text-brand-orange w-5 h-5 flex-shrink-0 group-data-[state=closed]:hidden" />
                </Accordion.Trigger>
              </Accordion.Header>
              <Accordion.Content className="text-brand-gray text-sm leading-relaxed pb-5 overflow-hidden transition-all duration-200 ease-in-out data-[state=open]:animate-accordion-down data-[state=closed]:animate-accordion-up">
                {faq.a}
              </Accordion.Content>
            </Accordion.Item>
          ))}
        </Accordion.Root>
      </section>

      {/* Final CTA */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto bg-brand-navy rounded-[2.5rem] p-12 md:p-20 text-center relative overflow-hidden group">
          <div className="absolute top-0 right-0 w-96 h-96 bg-brand-orange/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 group-hover:bg-brand-orange/20 transition-colors duration-700" />
          <div className="absolute bottom-0 left-0 w-96 h-96 bg-brand-purple/10 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2 group-hover:bg-brand-purple/20 transition-colors duration-700" />
          
          <div className="relative z-10">
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6 leading-tight">
              Ready to govern your <span className="text-brand-orange">AI landscape?</span>
            </h2>
            <p className="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-10">
              Join 200+ enterprise teams using Devise to surface every AI tool and 
              turn invisible usage into intelligence.
            </p>
            <div className="flex flex-wrap gap-4 justify-center">
              <Link to="/login" className="bg-brand-orange text-white rounded-full px-10 py-4 font-bold text-lg hover:bg-orange-600 transition-all shadow-xl shadow-brand-orange/20 hover:scale-105 active:scale-95">
                Get Started Free
              </Link>
              <Link to="/demo" className="bg-white/10 text-white backdrop-blur-md border border-white/20 rounded-full px-10 py-4 font-bold text-lg hover:bg-white/20 transition-all hover:scale-105 active:scale-95">
                Book a Demo
              </Link>
            </div>
          </div>
        </div>
      </section>

    </Layout>
  );
};

const ModuleCard = ({ tag, title, desc, borderColor, tagBg, tagText, accentColor, items, ctaText, ctaLink }: {
  tag: string; title: string; desc: string; borderColor: string; tagBg: string; tagText: string; accentColor: string; items: string[]; ctaText: string; ctaLink?: string;
}) => (
  <div className={`bg-white p-8 rounded-2xl shadow-lg border-l-4 ${borderColor} hover:shadow-heavy transition-all`}>
    <div className={`inline-block px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest mb-6 ${tagBg} ${tagText}`}>
      {tag}
    </div>
    <h3 className="text-2xl font-bold text-brand-dark mb-4">{title}</h3>
    <p className="text-brand-gray text-sm mb-8 leading-relaxed">{desc}</p>
    <ul className="space-y-4 mb-8">
      {items.map((item) => (
        <li key={item} className="flex items-start gap-3 text-sm font-medium text-brand-dark">
          <CheckCircle className={`${accentColor} shrink-0`} size={18} />
          {item}
        </li>
      ))}
    </ul>
    {ctaLink ? (
      <Link to={ctaLink} className={`font-bold ${accentColor} flex items-center gap-2 hover:translate-x-1 transition-transform`}>
        {ctaText}
      </Link>
    ) : (
      <button className={`font-bold ${accentColor} flex items-center gap-2 hover:translate-x-1 transition-transform`}>
        {ctaText}
      </button>
    )}
  </div>
);
```

### devise-iris/frontend\src\pages\landing\NotFound.tsx

```tsx
import { useLocation } from "react-router-dom";
import { useEffect } from "react";

const NotFound = () => {
  const location = useLocation();

  useEffect(() => {
    console.error("404 Error: User attempted to access non-existent route:", location.pathname);
  }, [location.pathname]);

  return (
    <div className="flex min-h-screen items-center justify-center bg-muted">
      <div className="text-center">
        <h1 className="mb-4 text-4xl font-bold">404</h1>
        <p className="mb-4 text-xl text-muted-foreground">Oops! Page not found</p>
        <a href="/" className="text-primary underline hover:text-primary/90">
          Return to Home
        </a>
      </div>
    </div>
  );
};

export default NotFound;
```

### devise-iris/frontend\src\pages\landing\OversightPage.tsx

```tsx
import { Link } from "react-router-dom";
import {
  Eye, AlertTriangle, Settings, Map, Shield, FileText,
  ChevronRight, ArrowRight, CheckCircle
} from "lucide-react";
import { Layout } from "../../components/landing/Layout";
import oversightDashboard from "@/assets/oversight-dashboard.png";

export const OversightPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="relative overflow-hidden pt-32 pb-24 px-6">
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-[radial-gradient(circle,_#F04E23_0%,_transparent_70%)] opacity-[0.4] blur-3xl -z-10 pointer-events-none" />
        <div className="absolute top-20 right-0 w-[300px] h-[300px] bg-[radial-gradient(circle,_#F04E23_0%,_transparent_70%)] opacity-[0.3] blur-3xl -z-10 pointer-events-none" />

        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-block px-3 py-1 rounded-full text-xs font-black uppercase tracking-widest mb-6 bg-orange-50 text-brand-orange">
            Devise Oversight
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-brand-dark leading-tight">
            AI Governance & Risk Intelligence
          </h1>
          <p className="text-xl text-brand-gray mt-4 max-w-2xl mx-auto">
            Surface policy exposure and compliance gaps using real usage data.
          </p>
          <div className="flex flex-wrap gap-4 justify-center mt-8">
            <Link to="/demo" className="bg-brand-orange text-white rounded-full px-6 py-2.5 font-medium hover:bg-orange-600 transition-colors shadow-lg shadow-brand-orange/20">
              Book a Demo
            </Link>
            <button className="border border-brand-dark text-brand-dark rounded-full px-6 py-2.5 font-medium hover:bg-brand-dark hover:text-white transition-colors">
              See all features
            </button>
          </div>
        </div>

        <div className="mt-16 max-w-5xl mx-auto relative z-10">
          <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
            <img src={oversightDashboard} alt="Devise Oversight Dashboard" className="w-full" />
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4 text-center">Features</div>
        <h2 className="text-4xl font-bold text-brand-dark text-center mb-12">Complete governance toolkit</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            { icon: <Eye />, title: "Real-time AI Visibility", desc: "See every AI tool used across your entire organization in real time." },
            { icon: <AlertTriangle />, title: "Shadow AI Detection", desc: "Automatically detect unauthorized AI tools before they cause incidents." },
            { icon: <Settings />, title: "Policy Rule Engine", desc: "Create and enforce granular AI usage policies by team, tool, or data type." },
            { icon: <Map />, title: "Framework Mapping", desc: "Map findings to OWASP LLM Top 10, NIST AI RMF, ISO 42001, and EU AI Act." },
            { icon: <Shield />, title: "Data Sensitivity Flagging", desc: "Detect when sensitive data is shared with AI tools and alert instantly." },
            { icon: <FileText />, title: "Defensible Audit Trail", desc: "Complete, tamper-proof logs for regulatory review and compliance audits." },
          ].map((f, i) => (
            <div key={i} className="bg-white rounded-2xl shadow-lg p-6">
              <div className="text-brand-orange mb-4">{f.icon}</div>
              <h4 className="font-bold text-brand-dark mb-2">{f.title}</h4>
              <p className="text-brand-gray text-sm">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 3-Step Flow */}
      <section className="py-16 px-6 max-w-3xl mx-auto">
        <div className="flex flex-col md:flex-row items-center gap-4 justify-center">
          {["Detect", "Classify", "Alert"].map((step, i) => (
            <div key={step} className="flex items-center gap-4">
              <div className="bg-white rounded-2xl shadow-lg px-8 py-6 text-center">
                <div className="text-brand-orange font-bold text-lg">{step}</div>
              </div>
              {i < 2 && <ChevronRight className="text-brand-gray hidden md:block" size={24} />}
            </div>
          ))}
        </div>
      </section>

      {/* Compliance Frameworks */}
      <section className="py-24 px-6 max-w-5xl mx-auto">
        <h2 className="text-3xl font-bold text-brand-dark text-center mb-12">Compliance Frameworks Supported</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {["OWASP LLM Top 10", "NIST AI RMF", "ISO 42001", "EU AI Act"].map((fw) => (
            <div key={fw} className="bg-white rounded-2xl shadow-lg p-6 text-center">
              <Shield className="text-brand-orange mx-auto mb-3" size={24} />
              <div className="font-bold text-brand-dark text-sm">{fw}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Who Uses It */}
      <section className="py-16 px-6 max-w-4xl mx-auto">
        <h3 className="text-xl font-bold text-brand-dark text-center mb-8">Who uses Oversight</h3>
        <div className="flex flex-wrap gap-3 justify-center">
          {["CISO", "Compliance Officer", "Legal", "Security Team", "Internal Audit"].map((role) => (
            <span key={role} className="bg-white rounded-full px-5 py-2 text-sm shadow-soft text-brand-dark font-medium">{role}</span>
          ))}
        </div>
      </section>

      {/* Dark CTA */}
      <section className="mx-6 md:mx-auto max-w-5xl rounded-2xl bg-brand-navy text-white py-16 px-8 mb-24 text-center">
        <h2 className="text-3xl font-bold mb-4">Ready to govern your AI landscape?</h2>
        <p className="text-gray-400 mb-8">See Devise Oversight in action with a personalized demo.</p>
        <Link to="/demo" className="bg-brand-orange text-white rounded-full px-8 py-3 font-semibold hover:bg-orange-600 transition-colors shadow-lg shadow-brand-orange/20 inline-block">
          Book a Demo
        </Link>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\pages\landing\PulsePage.tsx

```tsx
import { Link } from "react-router-dom";
import { HelpCircle, CheckCircle, BarChart2, Users, TrendingUp } from "lucide-react";
import { Layout } from "../../components/landing/Layout";
import pulseDashboard from "@/assets/pulse-dashboard.png";

export const PulsePage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="relative overflow-hidden pt-32 pb-24 px-6">
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-block px-3 py-1 rounded-full text-xs font-black uppercase tracking-widest mb-6 bg-purple-50 text-brand-purple">
            Devise Pulse
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-brand-dark leading-tight">
            AI Adoption & Usage Analytics
          </h1>
          <p className="text-xl text-brand-gray mt-4 max-w-2xl mx-auto">
            Replace stale surveys with real behavioral adoption data.
          </p>
          <div className="flex flex-wrap gap-4 justify-center mt-8">
            <Link to="/demo" className="bg-brand-purple text-white rounded-full px-6 py-2.5 font-medium hover:bg-purple-700 transition-colors shadow-lg shadow-brand-purple/20">
              Book a Demo
            </Link>
            <Link to="/login" className="border border-brand-dark text-brand-dark rounded-full px-6 py-2.5 font-medium hover:bg-brand-dark hover:text-white transition-colors">
              Get Started
            </Link>
          </div>
        </div>

        <div className="mt-16 max-w-5xl mx-auto relative z-10">
          <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
            <img src={pulseDashboard} alt="Devise Pulse Dashboard" className="w-full" />
          </div>
        </div>
      </section>

      {/* Question Cards */}
      <section className="py-24 px-6 max-w-5xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            "Are we actually adopting AI or just talking about it?",
            "Which teams are leading vs lagging?",
            "Which tools are becoming the company default?",
            "Where should we invest in training?",
            "Who are our internal AI champions?",
          ].map((q, i) => (
            <div key={i} className="bg-white rounded-xl shadow-soft p-6">
              <HelpCircle className="text-brand-purple mb-3" size={20} />
              <p className="text-brand-dark font-medium text-sm">{q}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Features + Who Uses */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-16">
          <div>
            <h2 className="text-3xl font-bold text-brand-dark mb-8">Features</h2>
            <ul className="space-y-4">
              {[
                "Adoption rate by tool, team, and department",
                "Trend tracking over time",
                "Team leaderboard",
                "Power user identification",
                "Training gap surfacing",
                "Weekly executive reports",
              ].map((f) => (
                <li key={f} className="flex items-start gap-3 text-brand-dark font-medium">
                  <CheckCircle className="text-brand-purple shrink-0" size={18} /> {f}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h2 className="text-3xl font-bold text-brand-dark mb-8">Who uses Pulse</h2>
            <div className="flex flex-wrap gap-3">
              {["CHRO", "AI Transformation Lead", "L&D Team", "Department Heads", "CEO"].map((role) => (
                <span key={role} className="bg-white rounded-full px-5 py-2 text-sm shadow-soft text-brand-dark font-medium">{role}</span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Dark CTA */}
      <section className="mx-6 md:mx-auto max-w-5xl rounded-2xl bg-brand-navy text-white py-16 px-8 mb-24 text-center">
        <h2 className="text-3xl font-bold mb-4">See real adoption data, not survey estimates.</h2>
        <p className="text-gray-400 mb-8">Book a demo to see Devise Pulse in action.</p>
        <Link to="/demo" className="bg-brand-purple text-white rounded-full px-8 py-3 font-semibold hover:bg-purple-700 transition-colors shadow-lg shadow-brand-purple/20 inline-block">
          Book a Demo
        </Link>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\pages\landing\SpendPage.tsx

```tsx
import { Link } from "react-router-dom";
import { CheckCircle, DollarSign } from "lucide-react";
import { Layout } from "../../components/landing/Layout";
import spendDashboard from "@/assets/spend-dashboard.png";

export const SpendPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="relative overflow-hidden pt-32 pb-24 px-6">
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-block px-3 py-1 rounded-full text-xs font-black uppercase tracking-widest mb-6 bg-green-50 text-brand-green">
            Devise Spend
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-brand-dark leading-tight">
            AI Cost Intelligence & Optimization
          </h1>
          <p className="text-xl text-brand-gray mt-4 max-w-2xl mx-auto">
            Eliminate waste. Justify investment. Control every rupee.
          </p>
          <div className="flex flex-wrap gap-4 justify-center mt-8">
            <Link to="/demo" className="bg-brand-orange text-white rounded-full px-6 py-2.5 font-medium hover:bg-orange-600 transition-colors shadow-lg shadow-brand-orange/20">
              Book a Demo
            </Link>
            <Link to="/login" className="border border-brand-dark text-brand-dark rounded-full px-6 py-2.5 font-medium hover:bg-brand-dark hover:text-white transition-colors">
              Get Started
            </Link>
          </div>
        </div>

        <div className="mt-16 max-w-5xl mx-auto relative z-10">
          <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
            <img src={spendDashboard} alt="Devise Spend Dashboard" className="w-full" />
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 px-6 max-w-5xl mx-auto">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          {[
            { num: "30%+", label: "AI budget wasted" },
            { num: "78%", label: "unexpected charges" },
            { num: "40+", label: "tools per org" },
            { num: "₹12Cr/yr", label: "annual potential savings" },
          ].map((s) => (
            <div key={s.num} className="bg-white rounded-2xl shadow-lg p-6">
              <div className="text-3xl md:text-4xl font-bold text-brand-orange">{s.num}</div>
              <p className="text-sm text-brand-gray mt-2">{s.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Features + Who Uses */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-16">
          <div>
            <h2 className="text-3xl font-bold text-brand-dark mb-8">Features</h2>
            <ul className="space-y-4">
              {[
                "Centralized subscription view",
                "Zombie license detection",
                "Duplicate subscription flagging",
                "Cost attribution by team",
                "Budget forecasting",
                "ROI reports",
              ].map((f) => (
                <li key={f} className="flex items-start gap-3 text-brand-dark font-medium">
                  <CheckCircle className="text-brand-green shrink-0" size={18} /> {f}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h2 className="text-3xl font-bold text-brand-dark mb-8">Who uses Spend</h2>
            <div className="flex flex-wrap gap-3">
              {["CFO", "IT Procurement", "Finance Team", "Department Budget Owners"].map((role) => (
                <span key={role} className="bg-white rounded-full px-5 py-2 text-sm shadow-soft text-brand-dark font-medium">{role}</span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Dark CTA */}
      <section className="mx-6 md:mx-auto max-w-5xl rounded-2xl bg-brand-navy text-white py-16 px-8 mb-24 text-center">
        <h2 className="text-3xl font-bold mb-4">Stop wasting money on AI nobody uses.</h2>
        <p className="text-gray-400 mb-8">See Devise Spend eliminate waste in your first demo.</p>
        <Link to="/demo" className="bg-brand-orange text-white rounded-full px-8 py-3 font-semibold hover:bg-orange-600 transition-colors shadow-lg shadow-brand-orange/20 inline-block">
          Book a Demo
        </Link>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\pages\landing\UseCasesPage.tsx

```tsx
import { useState } from "react";
import { Link } from "react-router-dom";
import {
  LayoutGrid, TrendingUp, AlertTriangle, DollarSign, Users, Shield,
  ArrowRight, Briefcase, Eye, Lock, Settings
} from "lucide-react";
import { Layout } from "../../components/landing/Layout";

const useCases = [
  { tag: "C-Suite", color: "bg-orange-50 text-brand-orange", icon: <LayoutGrid size={20} />, title: "Org-wide AI adoption scoreboard", desc: "The board wants to know 'where are we on AI?' You need a real answer — not a survey estimate or gut feeling." },
  { tag: "C-Suite", color: "bg-orange-50 text-brand-orange", icon: <TrendingUp size={20} />, title: "Did your AI deployment actually work?", desc: "You approved a major AI tool rollout. Six weeks later, someone asks if it's working. You don't have an answer." },
  { tag: "Security", color: "bg-red-50 text-red-500", icon: <AlertTriangle size={20} />, title: "Confidential data sent to ChatGPT", desc: "A senior analyst pastes a confidential client email thread into ChatGPT. The data left your network instantly." },
  { tag: "Finance", color: "bg-green-50 text-brand-green", icon: <DollarSign size={20} />, title: "Zombie licenses draining budget", desc: "Paying for 200 Copilot seats. Only 67 engineers use it. That's ₹1.2L wasted every month." },
  { tag: "AI Leaders", color: "bg-purple-50 text-brand-purple", icon: <Users size={20} />, title: "Finding your internal AI champions", desc: "Which employees are power users who can drive adoption? You have no way to know." },
  { tag: "IT Admin", color: "bg-gray-100 text-brand-gray", icon: <Shield size={20} />, title: "Shadow AI spreading across the org", desc: "Every month, new AI tools appear in your network. You find out about them when something goes wrong." },
];

const filters = ["All", "C-Suite", "Security", "Finance", "AI Leaders", "IT Admin"];

const audiences = [
  { icon: <Eye />, title: "CEO / Head of AI", desc: "Need real adoption data to report to the board." },
  { icon: <DollarSign />, title: "CFO / Finance", desc: "Need to eliminate AI subscription waste." },
  { icon: <Shield />, title: "CISO / Security", desc: "Need visibility into shadow AI and data risks." },
  { icon: <Settings />, title: "IT Admin", desc: "Need control over tool sprawl and access." },
  { icon: <Lock />, title: "Compliance", desc: "Need defensible audit trails for regulators." },
];

export const UseCasesPage = () => {
  const [activeFilter, setActiveFilter] = useState("All");

  const filtered = activeFilter === "All" ? useCases : useCases.filter((uc) => uc.tag === activeFilter);

  return (
    <Layout>
      <section className="pt-32 pb-24 px-6 max-w-7xl mx-auto">
        <div className="text-xs font-semibold uppercase tracking-widest text-brand-orange mb-4">Use Cases</div>
        <h1 className="text-5xl font-bold text-brand-dark mb-4">Real situations. Real answers.</h1>
        <p className="text-brand-gray text-lg max-w-2xl">
          Every use case maps to a question a leader is actually asking right now.
        </p>

        <div className="flex flex-wrap gap-3 mt-10">
          {filters.map((f) => (
            <button
              key={f}
              onClick={() => setActiveFilter(f)}
              className={`rounded-full px-4 py-1.5 text-sm font-medium transition-colors ${
                activeFilter === f
                  ? "bg-brand-orange text-white"
                  : "bg-white text-brand-dark shadow-soft hover:shadow-heavy"
              }`}
            >
              {f}
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
          {filtered.map((uc, i) => (
            <div key={i} className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center gap-3 mb-4">
                <span className={`px-3 py-1 rounded-full text-xs font-bold ${uc.color}`}>{uc.tag}</span>
                <span className="text-brand-orange">{uc.icon}</span>
              </div>
              <h3 className="text-lg font-bold text-brand-dark mb-3">{uc.title}</h3>
              <p className="text-brand-gray text-sm mb-4 leading-relaxed">{uc.desc}</p>
              <button className="text-brand-orange font-medium text-sm flex items-center gap-1 hover:translate-x-1 transition-transform">
                See how it works <ArrowRight size={14} />
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* By Audience */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <h2 className="text-3xl font-bold text-brand-dark text-center mb-12">By Audience</h2>
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          {audiences.map((a, i) => (
            <div key={i} className="bg-white rounded-2xl shadow-lg p-6 text-center">
              <div className="text-brand-orange mx-auto mb-3 flex justify-center">{a.icon}</div>
              <h4 className="font-bold text-brand-dark text-sm mb-2">{a.title}</h4>
              <p className="text-brand-gray text-xs">{a.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Dark CTA */}
      <section className="mx-6 md:mx-auto max-w-5xl rounded-2xl bg-brand-navy text-white py-16 px-8 mb-24 text-center">
        <h2 className="text-3xl font-bold mb-4">See how Devise solves your challenge.</h2>
        <p className="text-gray-400 mb-8">Book a 30-minute demo tailored to your role.</p>
        <Link to="/demo" className="bg-brand-orange text-white rounded-full px-8 py-3 font-semibold hover:bg-orange-600 transition-colors inline-block">
          Book a Demo
        </Link>
      </section>
    </Layout>
  );
};
```

### devise-iris/frontend\src\services\api.ts

```ts
/**
 * Devise Dashboard — API service layer (Firebase Edition)
 * Backend: None (Serverless / Direct Firestore)
 * Auth: Firebase SDK
 */

import { 
  collection, 
  query, 
  where, 
  getDocs, 
  getDoc, 
  doc, 
  setDoc, 
  deleteDoc,
  orderBy,
  limit as firestoreLimit,
  Timestamp,
  onSnapshot,
  addDoc,
  serverTimestamp
} from "firebase/firestore";
import { db, auth } from "@/lib/firebase";
import type { DetectionEvent, HeartbeatEvent } from "@/data/mockData";

// ---------------------------------------------------------------------------
// Response types
// ---------------------------------------------------------------------------
export interface EventsResponse {
  total: number;
  events: DetectionEvent[];
}

export interface StatsResponse {
  totalDetections: number;
  uniqueTools: number;
  highRiskCount: number;
  unapprovedCount: number;
  onlineDevices: number;
  totalDevices: number;
  activeAlerts: number;
}

export interface AlertItem {
  id: string;
  type: "high_risk" | "unapproved" | "tamper" | "agent_gap" | "high_frequency";
  title: string;
  description: string;
  timestamp: string;
  severity: "low" | "medium" | "high";
}

export interface AnalyticsResponse {
  byTool: { name: string; count: number }[];
  byCategory: { name: string; value: number }[];
  overTime: { time: string; count: number }[];
  topProcesses: { name: string; count: number }[];
}

export interface SubscriptionItem {
  id: string;
  tool_name: string;
  vendor: string;
  seats: number;
  seats_used: number;
  cost_monthly: number;
  currency: string;
  status: "active" | "zombie" | "cancelled" | "trial";
  renewal_date: string | null;
  created_at: string;
}

export interface SpendOverview {
  totalMonthlySpend: number;
  monthlyBudget: number;
  budgetRemaining: number;
  zombieLicenses: number;
  zombieCost: number;
}

export interface TeamResponse {
  members: {
    id: string;
    full_name: string;
    email: string;
    department: string;
    role: string;
    avatar_url: string | null;
    created_at: string;
  }[];
  invites: {
    id: string;
    email: string;
    role: string;
    status: string;
    created_at: string;
    expires_at: string;
  }[];
}

export interface OrgSettings {
  id: string;
  org_id: string;
  monthly_budget: number;
  alert_threshold: number;
  auto_block: boolean;
  allowed_categories: string[];
  blocked_domains: string[];
  notification_email: boolean;
  notification_slack: boolean;
  slack_webhook_url: string | null;
}

export interface UserProfile {
  id: string;
  org_id: string;
  full_name: string;
  email: string;
  department: string;
  role: string;
  avatar_url: string | null;
  org_name: string;
  org_slug: string;
  created_at?: string | Timestamp;
  last_active?: string | Timestamp;
  dark_mode?: boolean;
  notification_prefs?: {
    high_risk_alerts: boolean;
    daily_summary: boolean;
    block_notifications: boolean;
  };
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
async function getOrgId(): Promise<string> {
  const user = auth.currentUser;
  if (!user) throw new Error("Not authenticated");
  
  const profileRef = doc(db, "profiles", user.uid);
  const profileDoc = await getDoc(profileRef);
  
  if (!profileDoc.exists()) {
    // Lazy creation for users who signed up before the fix
    console.log("Profile missing, creating default...");
    const orgId = `org_${user.uid.slice(0, 8)}`;
    
    // Create Organization
    await setDoc(doc(db, "organizations", orgId), {
      id: orgId,
      name: `${user.displayName || 'My'}'s Team`,
      slug: orgId,
      created_at: new Date().toISOString()
    });

    // Create User Profile
    await setDoc(profileRef, {
      id: user.uid,
      email: user.email,
      full_name: user.displayName || "",
      org_id: orgId,
      role: "admin",
      department: "General",
      created_at: new Date().toISOString()
    });

    // Create Default Org Settings
    await setDoc(doc(db, "org_settings", orgId), {
      id: orgId,
      org_id: orgId,
      monthly_budget: 1000,
      alert_threshold: 80,
      auto_block: false,
      allowed_categories: ["AI Assistant", "Development"],
      blocked_domains: [],
      notification_email: true,
      notification_slack: false
    });

    return orgId;
  }
  
  return profileDoc.data().org_id;
}

/**
 * Normalizes any timestamp (Firestore Timestamp or string) to an ISO string.
 * This ensures consistency across the dashboard and fixes "Invalid Date" errors.
 */
function normalizeDate(ts: any): string {
  if (!ts) return new Date().toISOString();
  if (ts instanceof Timestamp) return ts.toDate().toISOString();
  if (typeof ts === 'string') {
    const d = new Date(ts);
    return isNaN(d.getTime()) ? new Date().toISOString() : d.toISOString();
  }
  return new Date().toISOString();
}

// Stub for now (not used in direct Firestore version)
export function setApiToken(_token: string | null) {}

// ---------------------------------------------------------------------------
// Fetchers
// ---------------------------------------------------------------------------
export const fetchEvents = async (
  category?: string,
  riskLevel?: string,
  limit = 200,
  _offset = 0
): Promise<EventsResponse> => {
  const orgId = await getOrgId();
  let q = query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    orderBy("timestamp", "desc"),
    firestoreLimit(limit)
  );

  if (category && category !== "all") {
    q = query(q, where("category", "==", category));
  }
  if (riskLevel && riskLevel !== "all") {
    q = query(q, where("risk_level", "==", riskLevel));
  }

  const snapshot = await getDocs(q);
  const events = snapshot.docs.map(d => {
    const data = d.data();
    return { 
      ...data, 
      event_id: d.id,
      timestamp: normalizeDate(data.timestamp),
      department: (!data.department || data.department === "Unknown") ? "General" : data.department
    } as DetectionEvent;
  });

  return {
    total: events.length,
    events
  };
};

export const fetchHeartbeats = async (): Promise<HeartbeatEvent[]> => {
  const orgId = await getOrgId();
  const q = query(
    collection(db, "heartbeats"),
    where("org_id", "==", orgId),
    orderBy("timestamp", "desc")
  );
  const snapshot = await getDocs(q);
  return snapshot.docs.map(doc => doc.data() as HeartbeatEvent);
};

export const fetchStats = async (): Promise<StatsResponse> => {
  const orgId = await getOrgId();
  
  // In a real app with huge data, we'd use aggregation queries or cloud functions.
  // For V1-V2, we process on the client or fetch a summary doc.
  const eventsSnap = await getDocs(query(collection(db, "detection_events"), where("org_id", "==", orgId)));
  const heartbeatsSnap = await getDocs(query(collection(db, "heartbeats"), where("org_id", "==", orgId)));
  
  // Wrap index-prone queries in try-catch to prevent crashing the whole stats load
  let tamperSnap: any = { size: 0, docs: [] };
  let gapSnap: any = { size: 0, docs: [] };
  
  try {
    tamperSnap = await getDocs(query(collection(db, "tamper_alerts"), where("org_id", "==", orgId)));
  } catch (e) {
    console.warn("Tamper alerts query failed (missing index?)", e);
  }
  
  try {
    gapSnap = await getDocs(query(collection(db, "agent_gaps"), where("org_id", "==", orgId), where("suspicious", "==", true)));
  } catch (e) {
    console.warn("Agent gaps query failed (missing index?)", e);
  }

  const now = new Date();
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();
  const sixMinsAgo = new Date(now.getTime() - 6 * 60000).toISOString();
  
  const tools = new Set();
  let highRiskCount = 0;
  let unapprovedCount = 0;
  let highRiskUnapproved = 0;
  let todayDetections = 0;

  eventsSnap.docs.forEach(d => {
    const data = d.data();
    const ts = normalizeDate(data.timestamp);

    tools.add(data.tool_name);
    if (data.risk_level === "high") highRiskCount++;
    if (!data.is_approved) unapprovedCount++;
    if (data.risk_level === "high" && !data.is_approved) highRiskUnapproved++;
    if (ts && ts >= todayStart) todayDetections++;
  });

  const onlineDevices = heartbeatsSnap.docs.filter(d => {
    const data = d.data();
    const ts = normalizeDate(data.timestamp);
    return ts && ts >= sixMinsAgo;
  }).length;

  return {
    totalDetections: todayDetections, // Label in UI is "Events Today"
    uniqueTools: tools.size,
    highRiskCount,
    unapprovedCount,
    onlineDevices,
    totalDevices: heartbeatsSnap.size,
    activeAlerts: tamperSnap.size + gapSnap.size + highRiskUnapproved
  };
};

export const fetchAlerts = async (): Promise<AlertItem[]> => {
  const orgId = await getOrgId();
  const alerts: AlertItem[] = [];

  // High-risk unapproved
  const hrSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("risk_level", "==", "high"),
    where("is_approved", "==", false)
  ));
  hrSnap.forEach(d => {
    const r = d.data();
    alerts.push({
      id: `hr-${r.event_id}`,
      type: "high_risk",
      title: `High-risk unapproved tool: ${r.tool_name || "Unknown"}`,
      description: `${r.user_id || "?"} accessed ${r.domain || "?"} via ${r.process_name || "?"}`,
      timestamp: normalizeDate(r.timestamp),
      severity: "high"
    });
  });

  // Tamper alerts
  const taSnap = await getDocs(query(collection(db, "tamper_alerts"), where("org_id", "==", orgId)));
  taSnap.forEach(d => {
    const r = d.data();
    alerts.push({
      id: `ta-${r.device_id}-${r.timestamp}`,
      type: "tamper",
      title: "Agent binary tampered",
      description: `Device ${String(r.device_id).slice(0, 8)}… — hash mismatch detected`,
      timestamp: normalizeDate(r.timestamp),
      severity: "high"
    });
  });

  // Dismissed filter
  const dismissedSnap = await getDocs(query(collection(db, "dismissed_alerts"), where("org_id", "==", orgId)));
  const dismissedIds = new Set(dismissedSnap.docs.map(d => d.data().alert_id));

  return alerts
    .filter(a => !dismissedIds.has(a.id))
    .sort((a, b) => (b.timestamp || "").localeCompare(a.timestamp || ""));
};

export const fetchAnalytics = async (): Promise<AnalyticsResponse> => {
  const orgId = await getOrgId();
  const eventsSnap = await getDocs(query(collection(db, "detection_events"), where("org_id", "==", orgId)));
  
  const toolCounts: Record<string, number> = {};
  const catCounts: Record<string, number> = {};
  const procCounts: Record<string, number> = {};
  const timeCounts: Record<string, number> = {};

  eventsSnap.docs.forEach(d => {
    const e = d.data();
    const tn = e.tool_name || "Unknown";
    toolCounts[tn] = (toolCounts[tn] || 0) + 1;
    
    const cat = e.category || "Unknown";
    catCounts[cat] = (catCounts[cat] || 0) + 1;
    
    const proc = e.process_name || "Unknown";
    procCounts[proc] = (procCounts[proc] || 0) + 1;
    
    const ts = normalizeDate(e.timestamp);
      
    if (ts && ts.length >= 13) {
      // ISO format: YYYY-MM-DDTHH:mm:ss.sssZ
      const hour = ts.substring(11, 13) + ":00";
      timeCounts[hour] = (timeCounts[hour] || 0) + 1;
    }
  });

  return {
    byTool: Object.entries(toolCounts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count).slice(0, 8),
    byCategory: Object.entries(catCounts).map(([name, value]) => ({ name, value })).sort((a, b) => b.value - a.value),
    overTime: Object.entries(timeCounts).map(([time, count]) => ({ time, count })).sort((a, b) => a.time.localeCompare(b.time)),
    topProcesses: Object.entries(procCounts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count).slice(0, 10),
  };
};

export const fetchSubscriptions = async (): Promise<SubscriptionItem[]> => {
  const orgId = await getOrgId();
  const q = query(collection(db, "subscriptions"), where("org_id", "==", orgId), orderBy("tool_name"));
  const snapshot = await getDocs(q);
  return snapshot.docs.map(doc => doc.data() as SubscriptionItem);
};

export const fetchSpendOverview = async (): Promise<SpendOverview> => {
  const orgId = await getOrgId();
  const subsSnap = await getDocs(query(collection(db, "subscriptions"), where("org_id", "==", orgId)));
  const settingsDoc = await getDoc(doc(db, "org_settings", orgId));

  const subs = subsSnap.docs.map(d => d.data());
  const activeSubs = subs.filter(s => s.status === "active");
  const totalMonthlySpend = activeSubs.reduce((acc, s) => acc + (Number(s.cost_monthly) || 0), 0);
  
  const zombies = subs.filter(s => s.status === "zombie");
  const zombieCost = zombies.reduce((acc, s) => acc + (Number(s.cost_monthly) || 0), 0);
  
  const budget = settingsDoc.exists() ? (Number(settingsDoc.data().monthly_budget) || 0) : 0;

  return {
    totalMonthlySpend,
    monthlyBudget: budget,
    budgetRemaining: budget - totalMonthlySpend,
    zombieLicenses: zombies.length,
    zombieCost
  };
};

export const fetchTeam = async (): Promise<TeamResponse> => {
  const orgId = await getOrgId();
  const membersSnap = await getDocs(query(collection(db, "profiles"), where("org_id", "==", orgId)));
  const invitesSnap = await getDocs(query(collection(db, "team_invites"), where("org_id", "==", orgId)));
  
  return {
    members: membersSnap.docs.map(d => ({ id: d.id, ...d.data() } as any)),
    invites: invitesSnap.docs.map(d => ({ id: d.id, ...d.data() } as any))
  };
};

export const fetchSettings = async (): Promise<OrgSettings> => {
  const orgId = await getOrgId();
  const res = await getDoc(doc(db, "org_settings", orgId));
  if (!res.exists()) throw new Error("Settings not found");
  return { id: res.id, ...res.data() } as OrgSettings;
};

export const fetchMe = async (): Promise<UserProfile> => {
  const user = auth.currentUser;
  if (!user) throw new Error("Not authenticated");
  
  const profileDoc = await getDoc(doc(db, "profiles", user.uid));
  if (!profileDoc.exists()) throw new Error("Profile not found");
  
  const data = profileDoc.data();
  const orgId = data.org_id;
  
  if (orgId) {
    const orgDoc = await getDoc(doc(db, "organizations", orgId));
    if (orgDoc.exists()) {
      const orgData = orgDoc.data();
      data.org_name = orgData.name || "";
      data.org_slug = orgData.slug || "";
    }
  }
  
  return { id: profileDoc.id, ...data } as UserProfile;
};

// ---------------------------------------------------------------------------
// Mutations
// ---------------------------------------------------------------------------
export const updateMe = async (data: Partial<UserProfile>): Promise<{ status: string }> => {
  const user = auth.currentUser;
  if (!user) throw new Error("Not authenticated");
  
  const profileRef = doc(db, "profiles", user.uid);
  await setDoc(profileRef, data, { merge: true });
  return { status: "updated" };
};

export const updateLastActive = async (): Promise<void> => {
  const user = auth.currentUser;
  if (!user) return;
  
  const profileRef = doc(db, "profiles", user.uid);
  await setDoc(profileRef, {
    last_active: serverTimestamp()
  }, { merge: true });
};

export const getUserDetectionCount = async (email: string): Promise<number> => {
  const orgId = await getOrgId();
  const q = query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("user_id", "==", email) // Assuming user_id field in events stores email
  );
  const snap = await getDocs(q);
  return snap.size;
};

export const dismissAlert = async (alertId: string): Promise<{ status: string; id: string }> => {
  const orgId = await getOrgId();
  const user = auth.currentUser;
  
  await setDoc(doc(db, "dismissed_alerts", alertId), {
    alert_id: alertId,
    org_id: orgId,
    action: "dismissed",
    dismissed_by: user?.uid,
    timestamp: new Date().toISOString()
  });
  
  return { status: "dismissed", id: alertId };
};

export const resolveAlert = async (alertId: string): Promise<{ status: string; id: string }> => {
  // Logic could vary, for now same as dismiss or update a status field
  return dismissAlert(alertId);
};

export const inviteTeamMember = async (email: string, role: string = "member"): Promise<{ status: string; email: string }> => {
  const orgId = await getOrgId();
  const id = `inv_${Date.now()}`;
  
  await setDoc(doc(db, "team_invites", id), {
    email,
    role,
    org_id: orgId,
    status: "pending",
    created_at: new Date().toISOString(),
    expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString()
  });
  
  return { status: "invited", email };
};

export const updateSettings = async (settings: Partial<OrgSettings>): Promise<{ status: string }> => {
  const orgId = await getOrgId();
  await setDoc(doc(db, "org_settings", orgId), settings, { merge: true });
  return { status: "updated" };
};

// ---------------------------------------------------------------------------
// AI FIREWALL
// ---------------------------------------------------------------------------
export interface FirewallRule {
  id: string;
  tool_name: string;
  domain: string;
  status: "allowed" | "blocked";
  updated_at: string;
  updated_by: string;
  block_count: number;
}

export interface BlockEvent {
  id: string;
  event_id: string;
  tool_name: string;
  domain: string;
  user_id: string;
  device_id: string;
  timestamp: string;
  block_reason: string | null;
  policy_matched: string | null;
  org_id: string;
}

export interface FirewallStats {
  blockedToday: number;
  blockEventsThisWeek: number;
  policyViolations: number;
  complianceScore: number;
}

export const fetchFirewallRules = async (): Promise<FirewallRule[]> => {
  const orgId = await getOrgId();
  const snap = await getDocs(
    collection(db, "org_settings", orgId, "firewall_rules")
  );
  return snap.docs.map(d => {
    const data = d.data();
    return { 
      id: d.id, 
      ...data,
      updated_at: normalizeDate(data.updated_at)
    } as FirewallRule;
  });
};

export const updateFirewallRule = async (
  rule: Omit<FirewallRule, "id" | "block_count" | "updated_at" | "updated_by">
): Promise<{ status: string }> => {
  const orgId = await getOrgId();
  const user = auth.currentUser;
  const ruleId = rule.tool_name.replace(/\s+/g, "_").toLowerCase();
  await setDoc(
    doc(db, "org_settings", orgId, "firewall_rules", ruleId),
    {
      ...rule,
      updated_at: new Date().toISOString(),
      updated_by: user?.email || "unknown",
      block_count: 0,
    },
    { merge: true }
  );
  return { status: "updated" };
};

export const deleteFirewallRule = async (toolName: string): Promise<void> => {
  const orgId = await getOrgId();
  const ruleId = toolName.replace(/\s+/g, "_").toLowerCase();
  await deleteDoc(doc(db, "org_settings", orgId, "firewall_rules", ruleId));
};

export const fetchBlockEvents = async (limitN = 100): Promise<BlockEvent[]> => {
  const orgId = await getOrgId();
  const q = query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("event_type", "==", "blocked"),
    orderBy("timestamp", "desc"),
    firestoreLimit(limitN)
  );
  const snap = await getDocs(q);
  return snap.docs.map(d => {
    const data = d.data();
    return { 
      id: d.id, 
      ...data,
      timestamp: normalizeDate(data.timestamp)
    } as BlockEvent;
  });
};

export const fetchFirewallStats = async (): Promise<FirewallStats> => {
  const orgId = await getOrgId();
  const now = new Date();
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();
  const weekStart = new Date(now.getTime() - 7 * 24 * 3600 * 1000).toISOString();

  const allBlocksSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("event_type", "==", "blocked")
  ));

  const allEventsSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId)
  ));

  const allBlocks = allBlocksSnap.docs.map(d => {
    const data = d.data();
    return {
      ...data,
      timestamp: normalizeDate(data.timestamp)
    };
  });
  const blockedToday = allBlocks.filter(e => (e.timestamp || "") >= todayStart).length;
  const blockEventsThisWeek = allBlocks.filter(e => (e.timestamp || "") >= weekStart).length;
  
  const rulesSnap = await getDocs(collection(db, "org_settings", orgId, "firewall_rules"));
  const totalRules = rulesSnap.size;
  const allowedRules = rulesSnap.docs.filter(d => d.data().status === "allowed").length;
  const complianceScore = totalRules > 0 ? Math.round((allowedRules / totalRules) * 100) : 100;

  return {
    blockedToday,
    blockEventsThisWeek,
    policyViolations: allBlocks.length,
    complianceScore,
  };
};

// Auto-populate firewall rules from detected events
export const syncFirewallRulesFromEvents = async (): Promise<void> => {
  const orgId = await getOrgId();
  const eventsSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId)
  ));

  const existingSnap = await getDocs(collection(db, "org_settings", orgId, "firewall_rules"));
  const existingIds = new Set(existingSnap.docs.map(d => d.id));

  const toolsSeen: Record<string, { tool_name: string; domain: string }> = {};
  eventsSnap.docs.forEach(d => {
    const e = d.data();
    if (e.tool_name) {
      const ruleId = e.tool_name.replace(/\s+/g, "_").toLowerCase();
      if (!toolsSeen[ruleId]) toolsSeen[ruleId] = { tool_name: e.tool_name, domain: e.domain || "" };
    }
  });

  const user = auth.currentUser;
  const batch: Promise<void>[] = [];
  for (const [ruleId, info] of Object.entries(toolsSeen)) {
    if (!existingIds.has(ruleId)) {
      batch.push(setDoc(
        doc(db, "org_settings", orgId, "firewall_rules", ruleId),
        {
          tool_name: info.tool_name,
          domain: info.domain,
          status: "allowed",
          updated_at: new Date().toISOString(),
          updated_by: user?.email || "system",
          block_count: 0,
        }
      ));
    }
  }
  await Promise.all(batch);
};

// ---------------------------------------------------------------------------
// DATA SENSITIVITY
// ---------------------------------------------------------------------------
export type SensitivityFlag =
  | "SOURCE_CODE"
  | "FILE_UPLOAD"
  | "LARGE_PASTE"
  | "FINANCIAL_KEYWORDS"
  | "CREDENTIALS_PATTERN";

export interface SensitivityEvent {
  id: string;
  event_id: string;
  tool_name: string;
  domain: string;
  user_id: string;
  device_id: string;
  timestamp: string;
  sensitivity_flag: SensitivityFlag;
  sensitivity_score: number;
  window_title: string | null;
  paste_size_chars: number | null;
  file_name: string | null;
  org_id: string;
  reviewed: boolean;
}

export interface EmployeeRiskScore {
  id: string;
  user_email: string;
  risk_score: number;
  high_risk_events: number;
  medium_risk_events: number;
  last_incident: string;
  top_sensitivity_type: string;
  updated_at: string;
}

export interface DataRiskStats {
  highRiskToday: number;
  employeesWithRisk: number;
  mostCommonType: string;
  orgRiskScore: number;
}

export const fetchSensitivityEvents = async (
  flag?: SensitivityFlag,
  limitN = 100
): Promise<SensitivityEvent[]> => {
  const orgId = await getOrgId();
  let q = query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("sensitivity_flag", "!=", null),
    orderBy("sensitivity_flag"),
    orderBy("timestamp", "desc"),
    firestoreLimit(limitN)
  );
  const snap = await getDocs(q);
  const events = snap.docs
    .map(d => {
      const data = d.data();
      return { 
        id: d.id, 
        ...data,
        timestamp: normalizeDate(data.timestamp)
      } as SensitivityEvent;
    })
    .filter(e => !flag || e.sensitivity_flag === flag);
  return events;
};

export const fetchEmployeeRiskScores = async (): Promise<EmployeeRiskScore[]> => {
  const orgId = await getOrgId();
  const snap = await getDocs(
    collection(db, "risk_scores", orgId, "employees")
  );
  return snap.docs
    .map(d => ({ id: d.id, ...d.data() } as EmployeeRiskScore))
    .sort((a, b) => b.risk_score - a.risk_score);
};

export const fetchDataRiskStats = async (): Promise<DataRiskStats> => {
  const orgId = await getOrgId();
  const now = new Date();
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();

  const allSensitiveSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("sensitivity_flag", "!=", null)
  ));

  const all = allSensitiveSnap.docs.map(d => d.data());
  const highRiskToday = all.filter(e => 
    (e.timestamp || "") >= todayStart && (e.sensitivity_score || 0) >= 70
  ).length;
  
  const employeeSet = new Set(all.map(e => e.user_id).filter(Boolean));
  
  const flagCounts: Record<string, number> = {};
  all.forEach(e => {
    if (e.sensitivity_flag) flagCounts[e.sensitivity_flag] = (flagCounts[e.sensitivity_flag] || 0) + 1;
  });
  const mostCommonType = Object.entries(flagCounts).sort((a, b) => b[1] - a[1])[0]?.[0] || "—";
  
  const avgScore = all.length > 0
    ? Math.round(all.reduce((s, e) => s + (e.sensitivity_score || 0), 0) / all.length)
    : 0;

  return {
    highRiskToday,
    employeesWithRisk: employeeSet.size,
    mostCommonType,
    orgRiskScore: avgScore,
  };
};

export const markSensitivityEventReviewed = async (eventDocId: string): Promise<void> => {
  await setDoc(doc(db, "detection_events", eventDocId), { reviewed: true }, { merge: true });
};

export const subscribeToHighRiskEvents = (
  orgId: string,
  callback: (events: SensitivityEvent[]) => void
): (() => void) => {
  const q = query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("sensitivity_flag", "!=", null),
    orderBy("sensitivity_flag"),
    orderBy("timestamp", "desc"),
    firestoreLimit(20)
  );
  return onSnapshot(q, snap => {
    const events = snap.docs
      .map(d => ({ id: d.id, ...d.data() } as SensitivityEvent))
      .filter(e => (e.sensitivity_score || 0) >= 60);
    callback(events);
  });
};

// Rebuild employee risk scores from sensitivity events (client-side)
export const rebuildEmployeeRiskScores = async (): Promise<void> => {
  const orgId = await getOrgId();
  const eventsSnap = await getDocs(query(
    collection(db, "detection_events"),
    where("org_id", "==", orgId),
    where("sensitivity_flag", "!=", null)
  ));

  const byEmployee: Record<string, SensitivityEvent[]> = {};
  eventsSnap.docs.forEach(d => {
    const e = { id: d.id, ...d.data() } as SensitivityEvent;
    const key = e.user_id || "unknown";
    if (!byEmployee[key]) byEmployee[key] = [];
    byEmployee[key].push(e);
  });

  const batch: Promise<void>[] = [];
  for (const [email, events] of Object.entries(byEmployee)) {
    const highRisk = events.filter(e => (e.sensitivity_score || 0) >= 70).length;
    const medRisk  = events.filter(e => (e.sensitivity_score || 0) >= 40 && (e.sensitivity_score || 0) < 70).length;
    const avgScore = Math.round(events.reduce((s, e) => s + (e.sensitivity_score || 0), 0) / events.length);
    const sorted   = events.sort((a, b) => b.timestamp.localeCompare(a.timestamp));
    const flagCounts: Record<string, number> = {};
    events.forEach(e => { flagCounts[e.sensitivity_flag] = (flagCounts[e.sensitivity_flag] || 0) + 1; });
    const topType = Object.entries(flagCounts).sort((a, b) => b[1] - a[1])[0]?.[0] || "";

    const scoreId = email.replace(/[^a-zA-Z0-9]/g, "_");
    batch.push(setDoc(
      doc(db, "risk_scores", orgId, "employees", scoreId),
      {
        user_email: email,
        risk_score: avgScore,
        high_risk_events: highRisk,
        medium_risk_events: medRisk,
        last_incident: typeof sorted[0]?.timestamp === 'string' ? sorted[0].timestamp : (sorted[0]?.timestamp as any)?.toDate?.()?.toISOString() || "",
        top_sensitivity_type: topType,
        updated_at: new Date().toISOString(),
      }
    ));
  }
  await Promise.all(batch);
};
```

### devise-iris/frontend\src\test\example.test.ts

```ts
import { describe, it, expect } from "vitest";

describe("example", () => {
  it("should pass", () => {
    expect(true).toBe(true);
  });
});
```

### devise-iris/frontend\src\test\setup.ts

```ts
import "@testing-library/jest-dom";

Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: (query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => {},
  }),
});
```

### devise-agent/build-arm64.spec

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

### devise-agent/build-x86_64.spec

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

### devise-agent/build.spec

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
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### devise-agent/config.py

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

### devise-agent/deduplicator.py

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

### devise-agent/detector.py

```py
"""Network connection detection module for Devise Desktop Agent."""

import logging
import psutil
from typing import List, Dict, Optional, Set
from datetime import datetime


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

    def __init__(self, poll_interval: int = 30, process_resolver=None):
        """Initialize network detector.

        Args:
            poll_interval: Polling interval in seconds (default 30)
            process_resolver: Optional ProcessResolver for process info
        """
        self._poll_interval = poll_interval
        self._seen_connections: Set[str] = set()
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

    def get_established_connections(self) -> List[Dict[str, any]]:
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

    def run_detection_cycle(self) -> List[Dict[str, any]]:
        """Run a single detection cycle.

        Returns:
            List of new connections not seen in previous cycle
        """
        current_connections = self.get_established_connections()

        # Create unique key for each connection
        new_connections = []
        for conn in current_connections:
            conn_key = f"{conn['remote_addr']}:{conn['remote_port']}:{conn.get('pid', 'unknown')}"

            if conn_key not in self._seen_connections:
                self._seen_connections.add(conn_key)

                # Add process info if resolver available
                if self._process_resolver and conn.get("pid"):
                    process_info = self.get_process_info(conn["pid"])
                    conn["process_name"] = process_info["process_name"]
                    conn["process_path"] = process_info["process_path"]

                new_connections.append(conn)

        # Limit cache size to prevent memory growth
        if len(self._seen_connections) > 10000:
            self._seen_connections = set(list(self._seen_connections)[-5000:])

        return new_connections


def create_detector(poll_interval: int = 30, process_resolver=None) -> NetworkDetector:
    """Create a network detector instance.

    Args:
        poll_interval: Polling interval in seconds
        process_resolver: Optional ProcessResolver

    Returns:
        NetworkDetector instance
    """
    return NetworkDetector(poll_interval, process_resolver)
```

### devise-agent/dns_resolver.py

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

### devise-agent/doh_resolver.py

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
            from .dns_resolver import DNSResolver

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

### devise-agent/event_builder.py

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
        "timestamp",
    ]

    def __init__(self, identity: Dict[str, str], device_id: str):
        """Initialize event builder.

        Args:
            identity: User identity dict from identity module
            device_id: Device ID from config
        """
        self._identity = identity
        self._device_id = device_id

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
            "timestamp": datetime.now(timezone.utc).isoformat(),
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


def create_event_builder(identity: Dict[str, str], device_id: str) -> EventBuilder:
    """Create an event builder instance.

    Args:
        identity: User identity dict
        device_id: Device ID

    Returns:
        EventBuilder instance
    """
    return EventBuilder(identity, device_id)
```

### devise-agent/frequency_tracker.py

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

### devise-agent/heartbeat.py

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

### devise-agent/identity.py

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
from .config import get_config


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

### devise-agent/liveness_monitor.py

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

### devise-agent/main.py

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
        from .config import get_config, ConfigPoller
        from .identity import get_identity
        from .detector import create_detector
        from .process_resolver import create_process_resolver
        from .dns_resolver import create_resolver
        from .registry import create_registry
        from .deduplicator import create_deduplicator
        from .event_builder import create_event_builder
        from .reporter import create_reporter
        from .queue import create_event_queue
        from .heartbeat import create_heartbeat_sender
        from .frequency_tracker import FrequencyTracker
        from .liveness_monitor import LivenessMonitor
        from .tamper_guard import TamperGuard

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
        self._queue = create_event_queue(
            encrypted=True,
            api_key=_api_key,
            device_id=_device_id,
        )

        # Initialize DNS resolver — DoH if enabled (FR-09), else system DNS
        if self._config.doh_enabled:
            try:
                from .doh_resolver import create_doh_resolver

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
            self._config.poll_interval, process_resolver=self._process_resolver
        )
        self._registry = create_registry(update_url=self._config.registry_update_url)
        self._deduplicator = create_deduplicator(self._config.deduplication_window)
        self._event_builder = create_event_builder(
            self._identity_resolver.identity,
            _device_id,
        )

        # Initialize reporter with queue for FR-17 (retry logic)
        self._reporter = create_reporter(
            _api_key,
            self._config.event_endpoint,
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
        if self._config_poller and self._config_poller.should_poll():
            try:
                await self._config_poller.fetch_config()
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

        # Resolve hostname via reverse DNS (DoH or system DNS)
        hostname = self._dns_resolver.reverse_lookup(remote_ip)

        if not hostname:
            logger.debug(f"No hostname for IP: {remote_ip}")
            return

        # Match against registry
        entry = self._registry.find_match(hostname)

        if not entry:
            logger.debug(f"No registry match for: {hostname}")
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
        if self._config_poller:
            await self._config_poller.start()

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
            if self._config_poller:
                await self._config_poller.stop()

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

### devise-agent/process_resolver.py

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

### devise-agent/queue.py

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
from queue import Queue
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

# Queue capacity
MAX_QUEUE_SIZE = 10000
BATCH_SIZE = 100

# Backoff intervals in seconds
BACKOFF_INTERVALS = [30, 60, 120, 300]
MAX_RETRIES = 4


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
            event_json = json.dumps(event)
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

            event_json = json.dumps(event)
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

### devise-agent/registry.py

```py
"""AI Tools Registry module for Devise Desktop Agent."""

import json
import logging
import os
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
        self._load_registry(registry_path)

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

### devise-agent/reporter.py

```py
"""HTTP reporter module for Devise Desktop Agent.

Provides retry logic with exponential backoff and offline queue integration.
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

import httpx


logger = logging.getLogger(__name__)

# Backoff intervals in seconds
BACKOFF_INTERVALS = [30, 60, 120, 300]
MAX_RETRIES = 4
BATCH_SIZE = 100


class Reporter:
    """HTTP event reporter to backend API with retry logic."""

    def __init__(
        self,
        api_key: str,
        endpoint: str,
        timeout: float = 10.0,
        queue=None,
    ):
        """Initialize reporter.

        Args:
            api_key: Device API key for authentication
            endpoint: Full API endpoint URL
            timeout: Request timeout in seconds
            queue: Optional EventQueue for offline buffering
        """
        self._api_key = api_key
        self._endpoint = endpoint
        self._timeout = timeout
        self._queue = queue
        self._client: Optional[httpx.AsyncClient] = None

    def set_queue(self, queue) -> None:
        """Set the event queue for offline buffering.

        Args:
            queue: EventQueue instance
        """
        self._queue = queue

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create async HTTP client.

        Returns:
            httpx AsyncClient instance
        """
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=self._timeout,
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                    "Content-Type": "application/json",
                },
            )
        return self._client

    async def _check_connectivity(self) -> bool:
        """Check if backend is reachable.

        Returns:
            True if backend is reachable
        """
        try:
            client = await self._get_client()
            # Try a lightweight request to check connectivity
            response = await client.head(self._endpoint, timeout=5.0)
            return response.status_code < 500
        except Exception:
            return False

    async def report_event(self, event: Dict[str, Any]) -> bool:
        """Report event to backend with retry logic.

        Args:
            event: Event dict to send

        Returns:
            True if successful, False otherwise
        """
        for attempt in range(MAX_RETRIES + 1):
            try:
                client = await self._get_client()
                response = await client.post(self._endpoint, json=event)
                response.raise_for_status()

                logger.debug(f"Event reported successfully: {event.get('event_id')}")
                return True

            except httpx.HTTPStatusError as e:
                # Non-retryable client errors (4xx)
                if 400 <= e.response.status_code < 500:
                    logger.warning(
                        f"Client error reporting event: {e.response.status_code}"
                    )
                    return False

                # Server errors (5xx) - retry
                logger.warning(
                    f"Server error (attempt {attempt + 1}): {e.response.status_code}"
                )

            except httpx.RequestError as e:
                logger.warning(f"Request error (attempt {attempt + 1}): {e}")

            except Exception as e:
                logger.warning(f"Unexpected error (attempt {attempt + 1}): {e}")

            # Check if we should retry
            if attempt < MAX_RETRIES:
                backoff = BACKOFF_INTERVALS[attempt]
                logger.info(f"Retrying in {backoff}s...")
                await asyncio.sleep(backoff)
            else:
                # All retries exhausted
                logger.warning(
                    f"Event reporting failed after {MAX_RETRIES + 1} attempts"
                )

        # All retries exhausted - try to queue if available
        if self._queue:
            logger.info("Queueing event for later retry")
            self._queue.enqueue(event)
            return False

        return False

    async def report_events(self, events: List[Dict[str, Any]]) -> Dict[str, int]:
        """Report multiple events to backend.

        Args:
            events: List of event dicts

        Returns:
            Dict with success/failure counts
        """
        results = {"success": 0, "failure": 0, "queued": 0}

        # Check connectivity first
        connected = await self._check_connectivity()

        if not connected:
            # Queue all events if offline
            if self._queue:
                for event in events:
                    self._queue.enqueue(event)
                results["queued"] = len(events)
                logger.info(f"Offline - queued {len(events)} events")
                return results
            else:
                logger.warning("Offline and no queue available")

        # Try to send batch
        if len(events) > BATCH_SIZE:
            # Split into batches
            for i in range(0, len(events), BATCH_SIZE):
                batch = events[i : i + BATCH_SIZE]
                batch_result = await self._send_batch(batch)
                results["success"] += batch_result["success"]
                results["failure"] += batch_result["failure"]
        else:
            batch_result = await self._send_batch(events)
            results["success"] = batch_result["success"]
            results["failure"] = batch_result["failure"]

        logger.info(
            f"Batch report: {results['success']} success, "
            f"{results['failure']} failed, {results['queued']} queued"
        )
        return results

    async def _send_batch(self, events: List[Dict[str, Any]]) -> Dict[str, int]:
        """Send a batch of events.

        Args:
            events: List of event dicts

        Returns:
            Dict with success/failure counts
        """
        results = {"success": 0, "failure": 0}

        for event in events:
            if await self.report_event(event):
                results["success"] += 1
            else:
                results["failure"] += 1

        return results

    async def flush_queue(self) -> Dict[str, int]:
        """Flush events from queue to backend.

        Returns:
            Dict with success/failure counts
        """
        if not self._queue:
            return {"success": 0, "failure": 0, "skipped": 0}

        results = {"success": 0, "failure": 0, "skipped": 0}

        # Check connectivity
        if not await self._check_connectivity():
            logger.info("Backend unreachable, skipping queue flush")
            results["skipped"] = self._queue.get_queue_depth()
            return results

        # Get pending events
        pending = self._queue.get_pending(limit=BATCH_SIZE)

        if not pending:
            logger.debug("No pending events to flush")
            return results

        logger.info(f"Flushing {len(pending)} events from queue")

        # Send events
        success_ids = []
        failed_ids = []

        for event in pending:
            queue_id = event.get("_queue_id")
            if await self.report_event(event):
                if queue_id:
                    success_ids.append(queue_id)
            else:
                if queue_id:
                    failed_ids.append(queue_id)

        # Mark events as processed
        if success_ids:
            self._queue.mark_success(success_ids)
            results["success"] = len(success_ids)

        if failed_ids:
            self._queue.mark_failed(failed_ids)
            results["failure"] = len(failed_ids)

        logger.info(
            f"Queue flush: {results['success']} sent, {results['failure']} failed"
        )

        return results

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "Reporter":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()


def create_reporter(
    api_key: str,
    endpoint: str,
    timeout: float = 10.0,
    queue=None,
) -> Reporter:
    """Create a reporter instance.

    Args:
        api_key: Device API key
        endpoint: API endpoint URL
        timeout: Request timeout
        queue: Optional EventQueue

    Returns:
        Reporter instance
    """
    return Reporter(api_key, endpoint, timeout, queue)
```

### devise-agent/requirements.txt

```txt
psutil>=5.9.0
dnspython>=2.4.0
APScheduler>=3.10.0
httpx>=0.25.0
python-dotenv>=1.0.0
PyInstaller>=6.0.0
pysqlcipher3>=1.0.3
keyring>=24.0.0

```

### devise-agent/tamper_guard.py

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

### devise-agent/__init__.py

```py
# Devise Desktop Agent
```

### devise-agent/data\ai_tools_registry.json

```json
{
  "version": "1.0.0",
  "updated_at": "2026-03-06",
  "tools": [
    {"domain": "openai.com", "tool_name": "OpenAI ChatGPT", "category": "chat", "vendor": "OpenAI", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "chat.openai.com", "tool_name": "OpenAI ChatGPT", "category": "chat", "vendor": "OpenAI", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "api.openai.com", "tool_name": "OpenAI API", "category": "api", "vendor": "OpenAI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "platform.openai.com", "tool_name": "OpenAI Platform", "category": "api", "vendor": "OpenAI", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "anthropic.com", "tool_name": "Anthropic Claude", "category": "chat", "vendor": "Anthropic", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "claude.ai", "tool_name": "Anthropic Claude", "category": "chat", "vendor": "Anthropic", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "api.anthropic.com", "tool_name": "Anthropic Claude API", "category": "api", "vendor": "Anthropic", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "console.anthropic.com", "tool_name": "Anthropic Console", "category": "api", "vendor": "Anthropic", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "copilot.microsoft.com", "tool_name": "Microsoft Copilot", "category": "coding", "vendor": "Microsoft", "risk_level": "low", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "github.com", "tool_name": "GitHub Copilot", "category": "coding", "vendor": "Microsoft", "risk_level": "low", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "api.github.com", "tool_name": "GitHub API", "category": "api", "vendor": "Microsoft", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "gemini.google.com", "tool_name": "Google Gemini", "category": "chat", "vendor": "Google", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "aistudio.google.com", "tool_name": "Google AI Studio", "category": "api", "vendor": "Google", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "generativelanguage.googleapis.com", "tool_name": "Google Gemini API", "category": "api", "vendor": "Google", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "makersuite.google.com", "tool_name": "Google MakerSuite", "category": "api", "vendor": "Google", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "claude.claude.ai", "tool_name": "Claude Enterprise", "category": "chat", "vendor": "Anthropic", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "ai.meta.com", "tool_name": "Meta AI", "category": "chat", "vendor": "Meta", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "meta.ai", "tool_name": "Meta AI", "category": "chat", "vendor": "Meta", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "llama.meta.com", "tool_name": "Meta Llama", "category": "api", "vendor": "Meta", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "replicate.com", "tool_name": "Replicate", "category": "api", "vendor": "Replicate", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.replicate.com", "tool_name": "Replicate API", "category": "api", "vendor": "Replicate", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "huggingface.co", "tool_name": "Hugging Face", "category": "api", "vendor": "Hugging Face", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.huggingface.co", "tool_name": "Hugging Face Inference API", "category": "api", "vendor": "Hugging Face", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "inference.huggingface.co", "tool_name": "Hugging Face Inference", "category": "api", "vendor": "Hugging Face", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "cohere.com", "tool_name": "Cohere", "category": "api", "vendor": "Cohere", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.cohere.ai", "tool_name": "Cohere API", "category": "api", "vendor": "Cohere", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "ai21.com", "tool_name": "AI21 Labs", "category": "api", "vendor": "AI21 Labs", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.ai21.com", "tool_name": "AI21 API", "category": "api", "vendor": "AI21 Labs", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "together.ai", "tool_name": "Together AI", "category": "api", "vendor": "Together AI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.together.xyz", "tool_name": "Together AI API", "category": "api", "vendor": "Together AI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "mistral.ai", "tool_name": "Mistral AI", "category": "api", "vendor": "Mistral AI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.mistral.ai", "tool_name": "Mistral API", "category": "api", "vendor": "Mistral AI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "perplexity.ai", "tool_name": "Perplexity AI", "category": "research", "vendor": "Perplexity", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "www.perplexity.ai", "tool_name": "Perplexity AI", "category": "research", "vendor": "Perplexity", "risk_level": "medium", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "api.perplexity.ai", "tool_name": "Perplexity API", "category": "api", "vendor": "Perplexity", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "writesonic.com", "tool_name": "Writesonic", "category": "chat", "vendor": "Writesonic", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "jasper.ai", "tool_name": "Jasper AI", "category": "chat", "vendor": "Jasper", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "copy.ai", "tool_name": "Copy.ai", "category": "chat", "vendor": "Copy.ai", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "character.ai", "tool_name": "Character AI", "category": "chat", "vendor": "Character AI", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "www.character.ai", "tool_name": "Character AI", "category": "chat", "vendor": "Character AI", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "poe.com", "tool_name": "Poe AI", "category": "chat", "vendor": "Quora", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "www.poe.com", "tool_name": "Poe AI", "category": "chat", "vendor": "Quora", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "kimi.kimi.com", "tool_name": "Kimi", "category": "chat", "vendor": "Moonshot AI", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "www.kimi.com", "tool_name": "Kimi", "category": "chat", "vendor": "Moonshot AI", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "cursor.sh", "tool_name": "Cursor IDE", "category": "coding", "vendor": "Anysphere", "risk_level": "low", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "cursor.sh", "tool_name": "Cursor IDE", "category": "coding", "vendor": "Anysphere", "risk_level": "low", "enterprise_flag": true, "api_domain_flag": false},
    {"domain": "api.cursor.sh", "tool_name": "Cursor API", "category": "api", "vendor": "Anysphere", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "windsor.ai", "tool_name": "Windsor AI", "category": "api", "vendor": "Windsor AI", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "openrouter.ai", "tool_name": "OpenRouter", "category": "api", "vendor": "OpenRouter", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "api.openrouter.ai", "tool_name": "OpenRouter API", "category": "api", "vendor": "OpenRouter", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "cloudflare.com", "tool_name": "Cloudflare Workers AI", "category": "api", "vendor": "Cloudflare", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "workers.cloudflare.com", "tool_name": "Cloudflare Workers", "category": "api", "vendor": "Cloudflare", "risk_level": "high", "enterprise_flag": false, "api_domain_flag": true},
    {"domain": "vertexai.googleapis.com", "tool_name": "Google Vertex AI", "category": "api", "vendor": "Google", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "aiplatform.googleapis.com", "tool_name": "Google AI Platform", "category": "api", "vendor": "Google", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "azure.com", "tool_name": "Azure OpenAI", "category": "api", "vendor": "Microsoft", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "openai.azure.com", "tool_name": "Azure OpenAI", "category": "api", "vendor": "Microsoft", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "cognitiveservices.azure.com", "tool_name": "Azure Cognitive Services", "category": "api", "vendor": "Microsoft", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "aws.amazon.com", "tool_name": "AWS AI Services", "category": "api", "vendor": "Amazon", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "bedrock.amazonaws.com", "tool_name": "AWS Bedrock", "category": "api", "vendor": "Amazon", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "sagemaker.amazonaws.com", "tool_name": "AWS SageMaker", "category": "api", "vendor": "Amazon", "risk_level": "high", "enterprise_flag": true, "api_domain_flag": true},
    {"domain": "you.com", "tool_name": "You.com AI", "category": "research", "vendor": "You.com", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false},
    {"domain": "www.you.com", "tool_name": "You.com AI", "category": "research", "vendor": "You.com", "risk_level": "medium", "enterprise_flag": false, "api_domain_flag": false}
  ]
}
```

### devise-agent/data\binary_hash.txt

```txt
a2a4eff8d0b0c845284c607d50a3b5b966ac5a3121736a2e38e165bd6644d9fe
```

### devise-agent/data\cdn_ip_ranges.json

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

### devise-agent/installers\linux\devise-agent.service

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

### devise-agent/installers\linux\install.sh

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

### devise-agent/installers\macos\com.devise.agent.plist

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

### devise-agent/installers\windows\install-service.ps1

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

### devise-agent/installers\windows\uninstall-service.ps1

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

