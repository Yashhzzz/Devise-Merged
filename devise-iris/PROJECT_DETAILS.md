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
