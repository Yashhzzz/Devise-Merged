# Devise Iris Dashboard — Frontend Overview

This document provides a comprehensive overview of the **Devise Iris** frontend architecture, built with React, Vite, and tailwind. The frontend connects to the local Node.js backend to display rich, real-time AI usage data.

---

## 🏗️ 1. Architecture Stack

The Devise Iris frontend is a modern Single Page Application (SPA).

*   **Framework:** React 18
*   **Build Tool:** Vite (Starts on port `8081`)
*   **Styling:** Tailwind CSS (Utility-first styling, highly responsive)
*   **Icons:** Lucide React (Clean, scalable SVG icons)
*   **Charts:** Recharts (Responsive D3-based charting library)
*   **Routing:** React Router DOM (Client-side routing for seamless navigation)
*   **State Management:** Custom React Hooks (`useDashboard.ts`, `useFirewall.ts`, etc.) mapping to REST API calls.

---

## 📂 2. Directory Structure

The frontend code resides in `devise-iris/frontend/src/`. Here is the core layout:

```text
src/
├── components/          # Reusable UI building blocks
│   ├── dashboard/       # Main dashboard tabs (Live Feed, Analytics, etc.)
│   ├── ui/              # Generic, atomic components (Buttons, Input, Switch, Badges)
│   ├── layout/          # Structural components (Sidebar, TopNav, AppLayout)
│   └── TopNav.tsx       # The top navigation bar
├── hooks/               # Custom React hooks containing business logic
│   ├── useDashboard.ts  # Fetches core stats, events, and heartbeats
│   ├── useDataRisk.ts   # Fetches sensitivity/DLP events and risk scores
│   ├── useFirewall.ts   # Fetches/mutates blocking rules and stats
│   ├── useSubscriptions.ts # Fetches spend, budget, and subscription data
│   └── useTeam.ts       # Fetches team members and invites
├── lib/                 # Utilities and third-party integrations
│   ├── AuthContext.tsx  # Authentication state provider (Currently points to Firebase Auth)
│   ├── utils.ts         # Helper functions (e.g., date formatting, class merging)
│   └── firebase.ts      # (Deprecated for data, still used for Login/Auth)
├── pages/               # Top-level page components (Route destinations)
│   ├── DashboardPage.tsx# The main container holding all dashboard tabs
│   ├── LoginPage.tsx    # Authentication page
│   └── LandingPage.tsx  # The public marketing page
├── services/            # API interaction layer
│   └── api.ts           # The central hub for all network requests to the backend (localhost:3001)
├── App.tsx              # Root component defining routes and context providers
└── main.tsx             # Application entry point (Mounts React to the DOM)
```

---

## 🔌 3. Data Flow & API Integration

The frontend operates using a standard **Service -> Hook -> Component** pattern. It has been entirely decoupled from Firebase for data fetching and now relies on a local Express backend.

### The Service Layer (`src/services/api.ts`)
This file is the single source of truth for all data interactions. It defines TypeScript interfaces for all data models (e.g., `DetectionEvent`, `HeartbeatEvent`, `FirewallRule`) and exports async functions that wrap `fetch()` calls to `http://localhost:3001/api`.

*Example flow:*
1. `fetchEvents()` calls `GET /api/events`.
2. It receives JSON.
3. It throws an error if the status is not `200 OK`.

### The Hook Layer (`src/hooks/`)
To keep components clean, data fetching logic is encapsulated in custom hooks. These hooks manage `loading`, `error`, and `data` states.

*Example flow:*
1. `useDashboard()` is called by a component.
2. Inside the hook, `useEffect` triggers `fetchEvents()` from `api.ts`.
3. The hook sets `loading: true`, waits for data, sets the `data` state, and sets `loading: false`.

### The Component Layer (`src/components/dashboard/`)
Components subscribe to hooks and render UI based on the returned state.

---

## 🧩 4. Key Dashboard Tabs (Components)

The dashboard is split into several distinct "Tabs," all injected into `DashboardPage.tsx` based on the active routing state.

1.  **Overview Tab (`OverviewTab.tsx`)**
    *   The "Home" screen. Displays high-level metric cards (Total Detections, High Risk, Online Devices) and summary charts.
    *   **Data Source:** `useDashboard()` -> `fetchStats()`, `fetchAnalytics()`

2.  **Live Feed Tab (`LiveFeedTab.tsx`)**
    *   A real-time table of all AI activity. Highlights risk levels with color-coded badges and indicates if an event was blocked by the firewall.
    *   **Data Source:** `useDashboard()` -> `fetchEvents()`

3.  **Analytics Tab (`AnalyticsTab.tsx`)**
    *   Detailed visualizations using Recharts. Shows usage over time, breakdowns by category, and the most heavily used tools.
    *   **Data Source:** `useDashboard()` -> `fetchAnalytics()`

4.  **AI Firewall Tab (`FirewallTab.tsx`)**
    *   The policy enforcement center. Allows admins to flip a switch to "Block" or "Allow" specific domains/tools. Displays compliance scores.
    *   **Data Source:** `useFirewall()` -> `fetchFirewallRules()`, `updateFirewallRule()`

5.  **Devices Tab (`DevicesTab.tsx`)**
    *   Lists all machines running the Devise Agent. Shows OS versions, agent versions, and online/offline status based on recent heartbeats.
    *   **Data Source:** `useDashboard()` -> `fetchHeartbeats()`

6.  **Data Risk / DLP Tab (`DataRiskTab.tsx`)**
    *   Focuses on sensitive data exposure (e.g., pasted Source Code, Financial phrasing). Shows employee risk scores based on their activity.
    *   **Data Source:** `useDataRisk()` -> `fetchSensitivityEvents()`, `fetchEmployeeRiskScores()`

7.  **Spend / Subscriptions Tab (`SubscriptionsTab.tsx`)**
    *   Tracks financial metrics. Identifies "zombie" licenses (paid but unused), tracks total monthly spend against budget, and lists active subscriptions.
    *   **Data Source:** `useSubscriptions()` -> `fetchSpendOverview()`, `fetchSubscriptions()`

---

## 🎨 5. UI & Styling Principles

*   **Dark Mode First:** The dashboard leans heavily on dark-mode aesthetics using Tailwind's `bg-gray-900`, `text-gray-100`, and subtle borders (`border-gray-800`), creating a premium, focused environment.
*   **Atomic Design:** Common UI elements (Buttons, Badges, Modals) are extracted into `src/components/ui/` to ensure consistency across all complex tabs.
*   **Responsive:** Layouts utilize Flexbox and CSS Grid to ensure the dashboard remains usable on smaller screens, though it is optimized for desktop viewing.
*   **Visual Hierarchy:** Color is used sparingly but effectively: Red for High Risk/Blocked, Yellow for Warnings, Green for Allowed/Online, and muted grays for secondary information.

---

## 🚀 6. Running the Frontend

To run the frontend locally and connect it to the backend:

1.  Ensure the backend is running on port `3001` (`node server.js` in `devise-iris/backend`).
2.  Navigate to `devise-iris/frontend`.
3.  Install dependencies: `npm install`
4.  Start the development server:
    ```bash
    npm run dev
    ```
5.  Open `http://localhost:8081` in your browser.
