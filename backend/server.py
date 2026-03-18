"""
Devise Backend — FastAPI
Serves dashboard data + ingests agent events → Firestore
"""

import json
import os
import logging
from datetime import datetime, timezone
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Header, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from google.oauth2 import service_account
from google.auth.transport.requests import Request as GoogleRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Devise Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Firestore helpers ────────────────────────────────────────────────────────


def get_firestore_token() -> str:
    sa_json = json.loads(os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON", "{}"))
    if not sa_json:
        raise HTTPException(
            status_code=500, detail="FIREBASE_SERVICE_ACCOUNT_JSON not configured"
        )
    credentials = service_account.Credentials.from_service_account_info(
        sa_json, scopes=["https://www.googleapis.com/auth/datastore"]
    )
    credentials.refresh(GoogleRequest())
    return credentials.token


def project_id() -> str:
    pid = os.environ.get("FIREBASE_PROJECT_ID", "")
    if not pid:
        raise HTTPException(
            status_code=500, detail="FIREBASE_PROJECT_ID not configured"
        )
    return pid


def fs_url(collection: str, doc_id: str = None) -> str:
    base = f"https://firestore.googleapis.com/v1/projects/{project_id()}/databases/(default)/documents/{collection}"
    return f"{base}/{doc_id}" if doc_id else base


def to_fs_value(val):
    if val is None:
        return {"nullValue": None}
    if isinstance(val, bool):
        return {"booleanValue": val}
    if isinstance(val, int):
        return {"integerValue": str(val)}
    if isinstance(val, float):
        return {"doubleValue": val}
    if isinstance(val, str):
        return {"stringValue": val}
    if isinstance(val, dict):
        return {"mapValue": {"fields": {k: to_fs_value(v) for k, v in val.items()}}}
    if isinstance(val, list):
        return {"arrayValue": {"values": [to_fs_value(v) for v in val]}}
    return {"stringValue": str(val)}


def to_fs_fields(d: dict) -> dict:
    return {k: to_fs_value(v) for k, v in d.items() if v is not None}


def from_fs_value(val: dict):
    if not val:
        return None
    if "stringValue" in val:
        return val["stringValue"]
    if "integerValue" in val:
        return int(val["integerValue"])
    if "doubleValue" in val:
        return float(val["doubleValue"])
    if "booleanValue" in val:
        return val["booleanValue"]
    if "nullValue" in val:
        return None
    if "mapValue" in val:
        return from_fs_doc(val["mapValue"].get("fields", {}))
    if "arrayValue" in val:
        return [from_fs_value(v) for v in val["arrayValue"].get("values", [])]
    return None


def from_fs_doc(fields: dict) -> dict:
    return {k: from_fs_value(v) for k, v in fields.items()}


async def fs_get_collection(collection: str, filters: list = None) -> List[dict]:
    """Fetch all docs from a Firestore collection."""
    try:
        token = get_firestore_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        if filters:
            url = f"https://firestore.googleapis.com/v1/projects/{project_id()}/databases/(default)/documents:runQuery"
            body = {
                "structuredQuery": {
                    "from": [{"collectionId": collection}],
                    "where": {"compositeFilter": {"op": "AND", "filters": filters}}
                    if len(filters) > 1
                    else filters[0],
                }
            }
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(url, json=body, headers=headers)
            if resp.status_code != 200:
                return []
            results = []
            for item in resp.json():
                if "document" in item:
                    doc = item["document"]
                    data = from_fs_doc(doc.get("fields", {}))
                    data["_id"] = doc["name"].split("/")[-1]
                    results.append(data)
            return results
        else:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.get(fs_url(collection), headers=headers)
            if resp.status_code != 200:
                return []
            docs = resp.json().get("documents", [])
            results = []
            for doc in docs:
                data = from_fs_doc(doc.get("fields", {}))
                data["_id"] = doc["name"].split("/")[-1]
                results.append(data)
            return results
    except Exception as e:
        logger.error(f"Firestore get error: {e}")
        return []


async def fs_write(collection: str, data: dict, doc_id: str = None) -> bool:
    try:
        token = get_firestore_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        body = {"fields": to_fs_fields(data)}
        async with httpx.AsyncClient(timeout=10.0) as client:
            if doc_id:
                resp = await client.patch(
                    fs_url(collection, doc_id), json=body, headers=headers
                )
            else:
                resp = await client.post(fs_url(collection), json=body, headers=headers)
        return resp.status_code in (200, 201)
    except Exception as e:
        logger.error(f"Firestore write error: {e}")
        return False


async def fs_get_subcollection(
    parent_collection: str, parent_id: str, subcollection: str
) -> List[dict]:
    try:
        token = get_firestore_token()
        headers = {"Authorization": f"Bearer {token}"}
        url = f"https://firestore.googleapis.com/v1/projects/{project_id()}/databases/(default)/documents/{parent_collection}/{parent_id}/{subcollection}"
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url, headers=headers)
        if resp.status_code != 200:
            return []
        docs = resp.json().get("documents", [])
        results = []
        for doc in docs:
            data = from_fs_doc(doc.get("fields", {}))
            data["id"] = doc["name"].split("/")[-1]
            results.append(data)
        return results
    except Exception as e:
        logger.error(f"Firestore subcollection error: {e}")
        return []


# ── Auth dependency ────────────────────────────────────────────────────────


def verify_device_key(x_device_key: str = Header(None)):
    expected = os.environ.get("DEVICE_API_KEY", "")
    if not x_device_key or x_device_key != expected:
        raise HTTPException(status_code=401, detail="Unauthorized")


async def get_org_id_from_header(x_org_id: str = Header(None)) -> str:
    """Dashboard endpoints pass org_id via header or we get it from auth."""
    if x_org_id:
        return x_org_id
    orgs = await fs_get_collection("organizations")
    if orgs:
        return orgs[0].get("_id", orgs[0].get("id", ""))
    raise HTTPException(status_code=400, detail="No org found")


# ── Health endpoint ────────────────────────────────────────────────────────


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "devise-backend", "version": "1.0.0"}


# ── Agent Ingest Endpoints ─────────────────────────────────────────────────


class EventPayload(BaseModel):
    event_type: str = "detection"
    event_id: Optional[str] = None
    org_id: str
    device_id: str
    user_id: Optional[str] = None
    user_email: Optional[str] = None
    department: Optional[str] = "General"
    tool_name: Optional[str] = None
    domain: Optional[str] = None
    category: Optional[str] = None
    vendor: Optional[str] = None
    risk_level: Optional[str] = "low"
    source: Optional[str] = "desktop"
    process_name: Optional[str] = None
    process_path: Optional[str] = None
    is_approved: Optional[bool] = True
    timestamp: Optional[str] = None
    connection_frequency: Optional[int] = None
    high_frequency: Optional[bool] = None
    bytes_read: Optional[int] = None
    bytes_write: Optional[int] = None
    sensitivity_flag: Optional[str] = None
    sensitivity_score: Optional[int] = None
    window_title: Optional[str] = None
    paste_size_chars: Optional[int] = None
    file_name: Optional[str] = None
    reviewed: Optional[bool] = False
    agent_version: Optional[str] = None
    os_version: Optional[str] = None
    queue_depth: Optional[int] = None
    restart_detected: Optional[bool] = None
    last_detection_time: Optional[str] = None
    gap_seconds: Optional[float] = None
    suspicious: Optional[bool] = None
    hostname: Optional[str] = None
    status: Optional[str] = None


@app.post("/api/event")
async def ingest_event(payload: EventPayload, _=Depends(verify_device_key)):
    data = {k: v for k, v in payload.dict().items() if v is not None}
    if "timestamp" not in data:
        data["timestamp"] = datetime.now(timezone.utc).isoformat()

    event_type = data.get("event_type", "detection")

    if event_type == "heartbeat":
        success = await fs_write("heartbeats", data, doc_id=data["device_id"])
    elif event_type == "agent_gap":
        success = await fs_write("agent_gaps", data)
    else:
        doc_id = data.get("event_id")
        success = await fs_write("detection_events", data, doc_id=doc_id)

    if not success:
        raise HTTPException(status_code=500, detail="Firestore write failed")
    return {"status": "ok", "event_type": event_type}


class HeartbeatPayload(BaseModel):
    device_id: str
    org_id: str
    agent_version: Optional[str] = "1.0.0"
    os_version: Optional[str] = None
    queue_depth: Optional[int] = 0
    restart_detected: Optional[bool] = False
    last_detection_time: Optional[str] = None
    timestamp: Optional[str] = None
    status: Optional[str] = "active"
    user_email: Optional[str] = None
    hostname: Optional[str] = None


@app.post("/api/heartbeat")
async def ingest_heartbeat(payload: HeartbeatPayload, _=Depends(verify_device_key)):
    data = {k: v for k, v in payload.dict().items() if v is not None}
    if "timestamp" not in data:
        data["timestamp"] = datetime.now(timezone.utc).isoformat()
    data["status"] = "active"
    success = await fs_write("heartbeats", data, doc_id=data["device_id"])
    if not success:
        raise HTTPException(status_code=500, detail="Firestore write failed")
    return {"status": "ok", "device_id": data["device_id"]}


# ── Dashboard Query Endpoints ─────────────────────────────────────────────


@app.get("/api/events")
async def get_events(
    category: Optional[str] = None,
    risk_level: Optional[str] = None,
    limit: int = 200,
    x_org_id: str = Header(None),
):
    events = await fs_get_collection("detection_events")
    events = [e for e in events if e.get("org_id") == x_org_id] if x_org_id else events
    if category and category != "all":
        events = [e for e in events if e.get("category") == category]
    if risk_level and risk_level != "all":
        events = [e for e in events if e.get("risk_level") == risk_level]
    events.sort(key=lambda e: e.get("timestamp", ""), reverse=True)
    return {"total": len(events), "events": events[:limit]}


@app.get("/api/stats")
async def get_stats(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    heartbeats = await fs_get_collection("heartbeats")

    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]
        heartbeats = [h for h in heartbeats if h.get("org_id") == x_org_id]

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

    tools = set()
    high_risk = 0
    unapproved = 0
    today_count = 0

    for e in events:
        tools.add(e.get("tool_name", ""))
        if e.get("risk_level") == "high":
            high_risk += 1
        if not e.get("is_approved", True):
            unapproved += 1
        ts = e.get("timestamp", "")
        if ts >= today_start:
            today_count += 1

    online = sum(1 for h in heartbeats if h.get("status") == "active")

    return {
        "totalDetections": today_count,
        "uniqueTools": len(tools),
        "highRiskCount": high_risk,
        "unapprovedCount": unapproved,
        "onlineDevices": online,
        "totalDevices": len(heartbeats),
        "activeAlerts": high_risk + unapproved,
    }


@app.get("/api/alerts")
async def get_alerts(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]

    alerts = []
    for e in events:
        if e.get("risk_level") == "high" and not e.get("is_approved", True):
            alerts.append(
                {
                    "id": f"hr-{e.get('event_id', e.get('_id', ''))}",
                    "type": "high_risk",
                    "title": f"High-risk unapproved tool: {e.get('tool_name', 'Unknown')}",
                    "description": f"{e.get('user_email', '?')} accessed {e.get('domain', '?')} via {e.get('process_name', '?')}",
                    "timestamp": e.get("timestamp", ""),
                    "severity": "high",
                }
            )
        if e.get("event_type") == "blocked":
            alerts.append(
                {
                    "id": f"bl-{e.get('event_id', e.get('_id', ''))}",
                    "type": "unapproved",
                    "title": f"Blocked tool access: {e.get('tool_name', 'Unknown')}",
                    "description": f"{e.get('user_email', '?')} tried to access {e.get('domain', '?')}",
                    "timestamp": e.get("timestamp", ""),
                    "severity": "high",
                }
            )
        if e.get("sensitivity_flag"):
            alerts.append(
                {
                    "id": f"sens-{e.get('event_id', e.get('_id', ''))}",
                    "type": "high_risk",
                    "title": f"Sensitive data detected: {e.get('sensitivity_flag', '')}",
                    "description": f"{e.get('tool_name', '?')} — score: {e.get('sensitivity_score', 0)}",
                    "timestamp": e.get("timestamp", ""),
                    "severity": "medium"
                    if e.get("sensitivity_score", 0) < 80
                    else "high",
                }
            )

    alerts.sort(key=lambda a: a.get("timestamp", ""), reverse=True)
    return alerts[:50]


@app.get("/api/analytics")
async def get_analytics(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]

    tool_counts = {}
    cat_counts = {}
    proc_counts = {}
    time_counts = {}

    for e in events:
        tn = e.get("tool_name", "Unknown")
        tool_counts[tn] = tool_counts.get(tn, 0) + 1
        cat = e.get("category", "Unknown")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        proc = e.get("process_name", "Unknown")
        proc_counts[proc] = proc_counts.get(proc, 0) + 1
        ts = e.get("timestamp", "")
        if len(ts) >= 13:
            hour = ts[11:13] + ":00"
            time_counts[hour] = time_counts.get(hour, 0) + 1

    return {
        "byTool": sorted(
            [{"name": k, "count": v} for k, v in tool_counts.items()],
            key=lambda x: -x["count"],
        )[:8],
        "byCategory": sorted(
            [{"name": k, "value": v} for k, v in cat_counts.items()],
            key=lambda x: -x["value"],
        ),
        "overTime": sorted(
            [{"time": k, "count": v} for k, v in time_counts.items()],
            key=lambda x: x["time"],
        ),
        "topProcesses": sorted(
            [{"name": k, "count": v} for k, v in proc_counts.items()],
            key=lambda x: -x["count"],
        )[:10],
    }


@app.get("/api/heartbeats")
async def get_heartbeats(x_org_id: str = Header(None)):
    heartbeats = await fs_get_collection("heartbeats")
    if x_org_id:
        heartbeats = [h for h in heartbeats if h.get("org_id") == x_org_id]
    return heartbeats


@app.get("/api/subscriptions")
async def get_subscriptions(x_org_id: str = Header(None)):
    subs = await fs_get_collection("subscriptions")
    if x_org_id:
        subs = [s for s in subs if s.get("org_id") == x_org_id]
    return subs


@app.get("/api/spend")
async def get_spend(x_org_id: str = Header(None)):
    subs = await fs_get_collection("subscriptions")
    if x_org_id:
        subs = [s for s in subs if s.get("org_id") == x_org_id]

    settings_docs = await fs_get_collection("org_settings")
    settings = next((s for s in settings_docs if s.get("org_id") == x_org_id), {})

    active = [s for s in subs if s.get("status") == "active"]
    zombies = [s for s in subs if s.get("status") == "zombie"]
    total_spend = sum(float(s.get("cost_monthly", 0)) for s in active)
    zombie_cost = sum(float(s.get("cost_monthly", 0)) for s in zombies)
    budget = float(settings.get("monthly_budget", 0))

    return {
        "totalMonthlySpend": total_spend,
        "monthlyBudget": budget,
        "budgetRemaining": budget - total_spend,
        "zombieLicenses": len(zombies),
        "zombieCost": zombie_cost,
    }


@app.get("/api/team")
async def get_team(x_org_id: str = Header(None)):
    members = await fs_get_collection("profiles")
    invites = await fs_get_collection("team_invites")
    if x_org_id:
        members = [m for m in members if m.get("org_id") == x_org_id]
        invites = [i for i in invites if i.get("org_id") == x_org_id]
    return {"members": members, "invites": invites}


@app.get("/api/settings")
async def get_settings(x_org_id: str = Header(None)):
    docs = await fs_get_collection("org_settings")
    if x_org_id:
        doc = next((d for d in docs if d.get("org_id") == x_org_id), None)
        if doc:
            return doc
    return docs[0] if docs else {}


@app.put("/api/settings")
async def update_settings(settings: dict, x_org_id: str = Header(None)):
    if not x_org_id:
        raise HTTPException(status_code=400, detail="org_id required")
    await fs_write("org_settings", {**settings, "org_id": x_org_id}, doc_id=x_org_id)
    return {"status": "updated"}


@app.get("/api/me")
async def get_me(x_user_id: str = Header(None), x_org_id: str = Header(None)):
    if not x_user_id:
        return {
            "id": "demo",
            "org_id": x_org_id or "",
            "full_name": "Demo User",
            "email": "demo@company.com",
            "department": "Engineering",
            "role": "admin",
            "avatar_url": None,
            "org_name": "Devise",
            "org_slug": "devise",
        }
    profiles = await fs_get_collection("profiles")
    profile = next(
        (p for p in profiles if p.get("_id") == x_user_id or p.get("id") == x_user_id),
        None,
    )
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    orgs = await fs_get_collection("organizations")
    org = next((o for o in orgs if o.get("_id") == profile.get("org_id")), {})
    profile["org_name"] = org.get("name", "")
    profile["org_slug"] = org.get("slug", "")
    return profile


@app.put("/api/me")
async def update_me(data: dict, x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=400, detail="user_id required")
    await fs_write("profiles", data, doc_id=x_user_id)
    return {"status": "updated"}


@app.post("/api/last-active")
async def update_last_active(x_user_id: str = Header(None)):
    if x_user_id:
        await fs_write(
            "profiles",
            {"last_active": datetime.now(timezone.utc).isoformat()},
            doc_id=x_user_id,
        )
    return {"status": "ok"}


# Alerts
@app.post("/api/alerts/{alert_id}/dismiss")
async def dismiss_alert(alert_id: str, x_org_id: str = Header(None)):
    await fs_write(
        "dismissed_alerts",
        {
            "alert_id": alert_id,
            "org_id": x_org_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
        doc_id=alert_id,
    )
    return {"status": "dismissed", "id": alert_id}


@app.post("/api/alerts/{alert_id}/resolve")
async def resolve_alert(alert_id: str):
    return {"status": "resolved", "id": alert_id}


# Team
@app.post("/api/team/invite")
async def invite_team_member(data: dict, x_org_id: str = Header(None)):
    invite_id = f"inv_{int(datetime.now().timestamp())}"
    await fs_write(
        "team_invites",
        {
            "email": data.get("email"),
            "role": data.get("role", "member"),
            "org_id": x_org_id,
            "status": "pending",
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        doc_id=invite_id,
    )
    return {"status": "invited", "email": data.get("email")}


# Firewall
@app.get("/api/firewall/rules")
async def get_firewall_rules(x_org_id: str = Header(None)):
    if not x_org_id:
        return []
    rules = await fs_get_subcollection("org_settings", x_org_id, "firewall_rules")
    return rules


@app.put("/api/firewall/rules")
async def update_firewall_rule(rule: dict, x_org_id: str = Header(None)):
    if not x_org_id:
        raise HTTPException(status_code=400, detail="org_id required")
    rule_id = rule.get("tool_name", "").replace(" ", "_").lower()
    rule["updated_at"] = datetime.now(timezone.utc).isoformat()
    rule["org_id"] = x_org_id
    token = get_firestore_token()
    url = f"https://firestore.googleapis.com/v1/projects/{project_id()}/databases/(default)/documents/org_settings/{x_org_id}/firewall_rules/{rule_id}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        await client.patch(
            url,
            json={"fields": to_fs_fields(rule)},
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
    return {"status": "updated"}


@app.delete("/api/firewall/rules/{tool_name}")
async def delete_firewall_rule(tool_name: str, x_org_id: str = Header(None)):
    rule_id = tool_name.replace(" ", "_").lower()
    token = get_firestore_token()
    url = f"https://firestore.googleapis.com/v1/projects/{project_id()}/databases/(default)/documents/org_settings/{x_org_id}/firewall_rules/{rule_id}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        await client.delete(url, headers={"Authorization": f"Bearer {token}"})
    return {"status": "deleted"}


@app.get("/api/firewall/events")
async def get_firewall_events(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    blocked = [
        e
        for e in events
        if e.get("event_type") == "blocked"
        and (not x_org_id or e.get("org_id") == x_org_id)
    ]
    return blocked[:100]


@app.get("/api/firewall/stats")
async def get_firewall_stats(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]

    now = datetime.now(timezone.utc)
    today = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

    blocked = [e for e in events if e.get("event_type") == "blocked"]
    blocked_today = sum(1 for e in blocked if e.get("timestamp", "") >= today)

    rules_docs = (
        await fs_get_subcollection("org_settings", x_org_id or "", "firewall_rules")
        if x_org_id
        else []
    )
    total_rules = len(rules_docs)
    allowed = sum(1 for r in rules_docs if r.get("status") == "allowed")
    score = round((allowed / total_rules) * 100) if total_rules > 0 else 100

    return {
        "blockedToday": blocked_today,
        "blockEventsThisWeek": len(blocked),
        "policyViolations": len(blocked),
        "complianceScore": score,
    }


@app.post("/api/firewall/sync")
async def sync_firewall(x_org_id: str = Header(None)):
    return {"status": "synced"}


# Sensitivity / Data Risk
@app.get("/api/sensitivity/events")
async def get_sensitivity_events(
    flag: Optional[str] = None, x_org_id: str = Header(None)
):
    events = await fs_get_collection("detection_events")
    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]
    sensitive = [e for e in events if e.get("sensitivity_flag")]
    if flag:
        sensitive = [e for e in sensitive if e.get("sensitivity_flag") == flag]
    sensitive.sort(key=lambda e: e.get("timestamp", ""), reverse=True)
    return sensitive[:100]


@app.get("/api/sensitivity/risk-scores")
async def get_risk_scores(x_org_id: str = Header(None)):
    if not x_org_id:
        return []
    return await fs_get_subcollection("risk_scores", x_org_id, "employees")


@app.get("/api/sensitivity/stats")
async def get_sensitivity_stats(x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    if x_org_id:
        events = [e for e in events if e.get("org_id") == x_org_id]

    sensitive = [e for e in events if e.get("sensitivity_flag")]
    today = (
        datetime.now(timezone.utc)
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .isoformat()
    )

    high_today = sum(
        1
        for e in sensitive
        if e.get("timestamp", "") >= today and e.get("sensitivity_score", 0) >= 70
    )
    employees = set(e.get("user_id") for e in sensitive if e.get("user_id"))

    flag_counts = {}
    for e in sensitive:
        f = e.get("sensitivity_flag", "")
        flag_counts[f] = flag_counts.get(f, 0) + 1
    most_common = max(flag_counts, key=flag_counts.get) if flag_counts else "—"

    avg_score = (
        round(sum(e.get("sensitivity_score", 0) for e in sensitive) / len(sensitive))
        if sensitive
        else 0
    )

    return {
        "highRiskToday": high_today,
        "employeesWithRisk": len(employees),
        "mostCommonType": most_common,
        "orgRiskScore": avg_score,
    }


@app.patch("/api/sensitivity/events/{event_id}/review")
async def review_sensitivity_event(event_id: str):
    await fs_write("detection_events", {"reviewed": True}, doc_id=event_id)
    return {"status": "reviewed"}


@app.post("/api/sensitivity/rebuild-scores")
async def rebuild_scores():
    return {"status": "rebuilt"}


@app.get("/api/user-detection-count")
async def user_detection_count(email: str, x_org_id: str = Header(None)):
    events = await fs_get_collection("detection_events")
    count = sum(
        1 for e in events if e.get("user_id") == email or e.get("user_email") == email
    )
    return {"count": count}


# Run with: uvicorn backend.server:app --reload --port 8000
