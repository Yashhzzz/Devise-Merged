/**
 * Devise Iris - Local Demo Backend
 * Serves all mock data as REST API endpoints on port 3001
 */

const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// ─── HELPERS ────────────────────────────────────────────────────────────────
const now = new Date();
const ago = (minutes) => new Date(now.getTime() - minutes * 60000).toISOString();

// ─── DEMO DATA ───────────────────────────────────────────────────────────────
const devices = [
  { device_id: "03479922-d748-5ca6-aaf9-31f1f7e93c28", hostname: "DESKTOP-YASH", os: "Windows 11", status: "online" },
  { device_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890", hostname: "LAPTOP-SARAH", os: "Windows 10", status: "online" },
  { device_id: "f9e8d7c6-b5a4-3210-fedc-ba0987654321", hostname: "MACBOOK-MIKE", os: "macOS 14.2", status: "online" },
  { device_id: "11223344-5566-7788-99aa-bbccddeeff00", hostname: "DESKTOP-EMILY", os: "Windows 11", status: "offline" },
  { device_id: "deadbeef-cafe-babe-face-123456789abc", hostname: "MACBOOK-ALEX", os: "macOS 15.0", status: "online" },
];

const users = [
  { id: "yashm", email: "yash.m@company.com", dept: "Engineering" },
  { id: "sarahk", email: "sarah.k@company.com", dept: "Product" },
  { id: "mikej", email: "mike.j@company.com", dept: "Design" },
  { id: "emilyw", email: "emily.w@company.com", dept: "Marketing" },
  { id: "alexr", email: "alex.r@company.com", dept: "Engineering" },
];

let evtCount = 0;
const eid = () => `evt-${String(++evtCount).padStart(4, "0")}-${Math.random().toString(36).slice(2, 10)}`;

const detectionEvents = [
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "OpenAI ChatGPT", domain: "chat.openai.com", category: "chat", vendor: "OpenAI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(2), connection_frequency: 3, is_blocked: false, sensitivity_score: 20 },
  { event_id: eid(), org_id: "demo", user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1].device_id, tool_name: "Claude", domain: "claude.ai", category: "chat", vendor: "Anthropic", risk_level: "medium", source: "desktop", process_name: "firefox.exe", process_path: "C:\\Program Files\\Mozilla Firefox\\firefox.exe", is_approved: true, timestamp: ago(5), is_blocked: false, sensitivity_score: 15 },
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "OpenAI API", domain: "api.openai.com", category: "api", vendor: "OpenAI", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(8), connection_frequency: 15, high_frequency: true, bytes_read: 2048000, bytes_write: 512000, is_blocked: false, sensitivity_score: 85, sensitivity_flag: "SOURCE_CODE" },
  { event_id: eid(), org_id: "demo", user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2].device_id, tool_name: "Midjourney", domain: "midjourney.com", category: "image", vendor: "Midjourney", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(12), is_blocked: false, sensitivity_score: 30 },
  { event_id: eid(), org_id: "demo", user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4].device_id, tool_name: "GitHub Copilot", domain: "copilot.github.com", category: "coding", vendor: "Microsoft", risk_level: "low", source: "desktop", process_name: "Code.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", is_approved: true, timestamp: ago(15), is_blocked: false, sensitivity_score: 10 },
  { event_id: eid(), org_id: "demo", user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3].device_id, tool_name: "Jasper", domain: "jasper.ai", category: "productivity", vendor: "Jasper", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(18), is_blocked: false, sensitivity_score: 45, sensitivity_flag: "FINANCIAL_KEYWORDS" },
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "Anthropic API", domain: "api.anthropic.com", category: "api", vendor: "Anthropic", risk_level: "high", source: "desktop", process_name: "node.exe", process_path: "C:\\Program Files\\nodejs\\node.exe", is_approved: false, timestamp: ago(22), connection_frequency: 8, is_blocked: false, sensitivity_score: 90, sensitivity_flag: "LARGE_PASTE" },
  { event_id: eid(), org_id: "demo", user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1].device_id, tool_name: "Perplexity", domain: "perplexity.ai", category: "search", vendor: "Perplexity", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(30), is_blocked: false, sensitivity_score: 25 },
  { event_id: eid(), org_id: "demo", user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2].device_id, tool_name: "DALL-E", domain: "labs.openai.com", category: "image", vendor: "OpenAI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(35), is_blocked: false, sensitivity_score: 20 },
  { event_id: eid(), org_id: "demo", user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4].device_id, tool_name: "Cursor", domain: "cursor.sh", category: "coding", vendor: "Anysphere", risk_level: "medium", source: "desktop", process_name: "Cursor.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Cursor\\Cursor.exe", is_approved: false, timestamp: ago(40), is_blocked: false, sensitivity_score: 55, sensitivity_flag: "SOURCE_CODE" },
  { event_id: eid(), org_id: "demo", user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3].device_id, tool_name: "Grammarly", domain: "grammarly.com", category: "productivity", vendor: "Grammarly", risk_level: "low", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(45), is_blocked: false, sensitivity_score: 5 },
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "Google Gemini", domain: "gemini.google.com", category: "chat", vendor: "Google", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: true, timestamp: ago(55), is_blocked: false, sensitivity_score: 18 },
  { event_id: eid(), org_id: "demo", user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1].device_id, tool_name: "Notion AI", domain: "notion.so", category: "productivity", vendor: "Notion", risk_level: "low", source: "desktop", process_name: "Notion.exe", process_path: "C:\\Users\\sarahk\\AppData\\Local\\Programs\\Notion\\Notion.exe", is_approved: true, timestamp: ago(60), is_blocked: false, sensitivity_score: 12 },
  { event_id: eid(), org_id: "demo", user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4].device_id, tool_name: "DeepSeek", domain: "deepseek.com", category: "chat", vendor: "DeepSeek", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(70), is_blocked: false, sensitivity_score: 35 },
  { event_id: eid(), org_id: "demo", user_id: "mikej", user_email: "mike.j@company.com", department: "Design", device_id: devices[2].device_id, tool_name: "Leonardo AI", domain: "leonardo.ai", category: "image", vendor: "Leonardo AI", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(80), is_blocked: false, sensitivity_score: 28 },
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "Replicate", domain: "replicate.com", category: "api", vendor: "Replicate", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(90), connection_frequency: 12, high_frequency: true, is_blocked: false, sensitivity_score: 75, sensitivity_flag: "CREDENTIALS_PATTERN" },
  { event_id: eid(), org_id: "demo", user_id: "emilyw", user_email: "emily.w@company.com", department: "Marketing", device_id: devices[3].device_id, tool_name: "ElevenLabs", domain: "elevenlabs.io", category: "audio", vendor: "ElevenLabs", risk_level: "medium", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(100), is_blocked: false, sensitivity_score: 40 },
  { event_id: eid(), org_id: "demo", user_id: "alexr", user_email: "alex.r@company.com", department: "Engineering", device_id: devices[4].device_id, tool_name: "Tabnine", domain: "tabnine.com", category: "coding", vendor: "Tabnine", risk_level: "medium", source: "desktop", process_name: "Code.exe", process_path: "C:\\Users\\alexr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", is_approved: false, timestamp: ago(120), is_blocked: false, sensitivity_score: 50, sensitivity_flag: "SOURCE_CODE" },
  { event_id: eid(), org_id: "demo", user_id: "sarahk", user_email: "sarah.k@company.com", department: "Product", device_id: devices[1].device_id, tool_name: "Runway", domain: "runwayml.com", category: "video", vendor: "Runway", risk_level: "high", source: "desktop", process_name: "chrome.exe", process_path: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", is_approved: false, timestamp: ago(140), is_blocked: false, sensitivity_score: 70, sensitivity_flag: "FILE_UPLOAD" },
  { event_id: eid(), org_id: "demo", user_id: "yashm", user_email: "yash.m@company.com", department: "Engineering", device_id: devices[0].device_id, tool_name: "Groq", domain: "groq.com", category: "api", vendor: "Groq", risk_level: "high", source: "desktop", process_name: "python.exe", process_path: "C:\\Python311\\python.exe", is_approved: false, timestamp: ago(160), is_blocked: false, sensitivity_score: 80, sensitivity_flag: "CREDENTIALS_PATTERN" },
];

const heartbeats = [
  { org_id: "demo", device_id: devices[0].device_id, hostname: devices[0].hostname, agent_version: "1.0.0", queue_depth: 0, last_detection_time: ago(2), os_version: "Windows 11", restart_detected: false, timestamp: ago(1), status: "online" },
  { org_id: "demo", device_id: devices[1].device_id, hostname: devices[1].hostname, agent_version: "1.0.0", queue_depth: 2, last_detection_time: ago(5), os_version: "Windows 10", restart_detected: false, timestamp: ago(3), status: "online" },
  { org_id: "demo", device_id: devices[2].device_id, hostname: devices[2].hostname, agent_version: "0.9.8", queue_depth: 0, last_detection_time: ago(12), os_version: "macOS 14.2", restart_detected: false, timestamp: ago(4), status: "online" },
  { org_id: "demo", device_id: devices[3].device_id, hostname: devices[3].hostname, agent_version: "1.0.0", queue_depth: 5, last_detection_time: ago(18), os_version: "Windows 11", restart_detected: true, timestamp: ago(200), status: "offline" },
  { org_id: "demo", device_id: devices[4].device_id, hostname: devices[4].hostname, agent_version: "1.0.1", queue_depth: 0, last_detection_time: ago(15), os_version: "macOS 15.0", restart_detected: false, timestamp: ago(2), status: "online" },
];

const subscriptions = [
  { id: "sub_001", org_id: "demo", tool_name: "GitHub Copilot", vendor: "Microsoft", seats: 10, seats_used: 8, cost_monthly: 190, currency: "USD", status: "active", renewal_date: new Date(now.getTime() + 30 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(180 * 24 * 60) },
  { id: "sub_002", org_id: "demo", tool_name: "OpenAI ChatGPT Teams", vendor: "OpenAI", seats: 15, seats_used: 12, cost_monthly: 375, currency: "USD", status: "active", renewal_date: new Date(now.getTime() + 15 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(90 * 24 * 60) },
  { id: "sub_003", org_id: "demo", tool_name: "Notion AI", vendor: "Notion", seats: 20, seats_used: 7, cost_monthly: 200, currency: "USD", status: "zombie", renewal_date: new Date(now.getTime() + 60 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(365 * 24 * 60) },
  { id: "sub_004", org_id: "demo", tool_name: "Jasper", vendor: "Jasper", seats: 5, seats_used: 2, cost_monthly: 250, currency: "USD", status: "zombie", renewal_date: new Date(now.getTime() + 5 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(200 * 24 * 60) },
  { id: "sub_005", org_id: "demo", tool_name: "Midjourney", vendor: "Midjourney", seats: 8, seats_used: 8, cost_monthly: 240, currency: "USD", status: "active", renewal_date: new Date(now.getTime() + 20 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(120 * 24 * 60) },
  { id: "sub_006", org_id: "demo", tool_name: "Grammarly Business", vendor: "Grammarly", seats: 25, seats_used: 18, cost_monthly: 375, currency: "USD", status: "active", renewal_date: new Date(now.getTime() + 45 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(240 * 24 * 60) },
  { id: "sub_007", org_id: "demo", tool_name: "Runway Pro", vendor: "Runway", seats: 3, seats_used: 1, cost_monthly: 96, currency: "USD", status: "zombie", renewal_date: new Date(now.getTime() + 10 * 24 * 60 * 60000).toISOString().split("T")[0], created_at: ago(300 * 24 * 60) },
];

const teamMembers = [
  { id: "uid_yashm", org_id: "demo", full_name: "Yash M", email: "yash.m@company.com", department: "Engineering", role: "admin", avatar_url: null, created_at: ago(365 * 24 * 60), last_active: ago(5) },
  { id: "uid_sarahk", org_id: "demo", full_name: "Sarah K", email: "sarah.k@company.com", department: "Product", role: "member", avatar_url: null, created_at: ago(300 * 24 * 60), last_active: ago(30) },
  { id: "uid_mikej", org_id: "demo", full_name: "Mike J", email: "mike.j@company.com", department: "Design", role: "member", avatar_url: null, created_at: ago(250 * 24 * 60), last_active: ago(45) },
  { id: "uid_emilyw", org_id: "demo", full_name: "Emily W", email: "emily.w@company.com", department: "Marketing", role: "member", avatar_url: null, created_at: ago(200 * 24 * 60), last_active: ago(60) },
  { id: "uid_alexr", org_id: "demo", full_name: "Alex R", email: "alex.r@company.com", department: "Engineering", role: "member", avatar_url: null, created_at: ago(180 * 24 * 60), last_active: ago(20) },
];

const teamInvites = [
  { id: "inv_001", org_id: "demo", email: "jess.t@company.com", role: "member", status: "pending", created_at: ago(2 * 24 * 60), expires_at: new Date(now.getTime() + 5 * 24 * 60 * 60000).toISOString() },
];

let orgSettings = {
  id: "demo",
  org_id: "demo",
  monthly_budget: 2000,
  alert_threshold: 80,
  auto_block: false,
  allowed_categories: ["AI Assistant", "Development", "coding"],
  blocked_domains: [],
  notification_email: true,
  notification_slack: false,
  slack_webhook_url: null,
};

const firewallRules = [
  { id: "openai_chatgpt", tool_name: "OpenAI ChatGPT", domain: "chat.openai.com", status: "allowed", updated_at: ago(24 * 60), updated_by: "yash.m@company.com", block_count: 0 },
  { id: "claude", tool_name: "Claude", domain: "claude.ai", status: "allowed", updated_at: ago(24 * 60), updated_by: "yash.m@company.com", block_count: 0 },
  { id: "openai_api", tool_name: "OpenAI API", domain: "api.openai.com", status: "blocked", updated_at: ago(12 * 60), updated_by: "yash.m@company.com", block_count: 12 },
  { id: "midjourney", tool_name: "Midjourney", domain: "midjourney.com", status: "allowed", updated_at: ago(48 * 60), updated_by: "yash.m@company.com", block_count: 0 },
  { id: "github_copilot", tool_name: "GitHub Copilot", domain: "copilot.github.com", status: "allowed", updated_at: ago(72 * 60), updated_by: "yash.m@company.com", block_count: 0 },
  { id: "replicate", tool_name: "Replicate", domain: "replicate.com", status: "blocked", updated_at: ago(6 * 60), updated_by: "yash.m@company.com", block_count: 5 },
  { id: "runway", tool_name: "Runway", domain: "runwayml.com", status: "blocked", updated_at: ago(3 * 60), updated_by: "yash.m@company.com", block_count: 3 },
];

const tamperAlerts = [
  { id: "ta_001", org_id: "demo", device_id: devices[3].device_id, expected_hash: "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6", actual_hash: "e5f6a7b8c9d0e1f2a3b4c5d6a1b2c3d4", timestamp: ago(45) },
  { id: "ta_002", org_id: "demo", device_id: devices[1].device_id, expected_hash: "1234567890abcdef1234567890abcdef", actual_hash: "fedcba0987654321fedcba0987654321", timestamp: ago(200) },
];

const agentGaps = [
  { id: "gap_001", org_id: "demo", device_id: devices[3].device_id, gap_seconds: 3600, last_seen: ago(120), suspicious: true, timestamp: ago(60) },
  { id: "gap_002", org_id: "demo", device_id: devices[1].device_id, gap_seconds: 900, last_seen: ago(50), suspicious: false, timestamp: ago(35) },
];

const employeeRiskScores = [
  { id: "yashm", user_email: "yash.m@company.com", risk_score: 82, high_risk_events: 4, medium_risk_events: 3, last_incident: ago(8), top_sensitivity_type: "SOURCE_CODE", updated_at: ago(5) },
  { id: "alexr", user_email: "alex.r@company.com", risk_score: 60, high_risk_events: 1, medium_risk_events: 4, last_incident: ago(40), top_sensitivity_type: "SOURCE_CODE", updated_at: ago(30) },
  { id: "emilyw", user_email: "emily.w@company.com", risk_score: 47, high_risk_events: 0, medium_risk_events: 3, last_incident: ago(18), top_sensitivity_type: "FINANCIAL_KEYWORDS", updated_at: ago(18) },
  { id: "sarahk", user_email: "sarah.k@company.com", risk_score: 35, high_risk_events: 1, medium_risk_events: 1, last_incident: ago(30), top_sensitivity_type: "FILE_UPLOAD", updated_at: ago(30) },
  { id: "mikej", user_email: "mike.j@company.com", risk_score: 28, high_risk_events: 0, medium_risk_events: 2, last_incident: ago(12), top_sensitivity_type: "FILE_UPLOAD", updated_at: ago(12) },
];

// In-memory dismissed alerts
let dismissedAlerts = new Set();

// ─── UTILITY FUNCTIONS ────────────────────────────────────────────────────────
function buildStats() {
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();
  const sixMinsAgo = new Date(now.getTime() - 6 * 60000).toISOString();

  const toolsSet = new Set();
  let highRiskCount = 0, unapprovedCount = 0, highRiskUnapproved = 0, todayDetections = 0;
  detectionEvents.forEach((e) => {
    toolsSet.add(e.tool_name);
    if (e.risk_level === "high") highRiskCount++;
    if (!e.is_approved) unapprovedCount++;
    if (e.risk_level === "high" && !e.is_approved) highRiskUnapproved++;
    if (e.timestamp >= todayStart) todayDetections++;
  });

  const onlineDevices = heartbeats.filter((h) => h.timestamp >= sixMinsAgo).length;

  return {
    totalDetections: todayDetections,
    uniqueTools: toolsSet.size,
    highRiskCount,
    unapprovedCount,
    onlineDevices,
    totalDevices: heartbeats.length,
    activeAlerts: tamperAlerts.length + agentGaps.filter((g) => g.suspicious).length + highRiskUnapproved,
  };
}

function buildAlerts() {
  const alerts = [];
  detectionEvents.filter((e) => e.risk_level === "high" && !e.is_approved).forEach((e) => {
    alerts.push({ id: `hr-${e.event_id}`, type: "high_risk", title: `High-risk unapproved tool: ${e.tool_name}`, description: `${e.user_email} accessed ${e.domain} via ${e.process_name}`, timestamp: e.timestamp, severity: "high" });
  });
  tamperAlerts.forEach((ta) => {
    alerts.push({ id: `ta-${ta.device_id}-${ta.timestamp}`, type: "tamper", title: "Agent binary tampered", description: `Device ${ta.device_id.slice(0, 8)}… — hash mismatch detected`, timestamp: ta.timestamp, severity: "high" });
  });
  agentGaps.filter((g) => g.suspicious).forEach((g) => {
    alerts.push({ id: `gap-${g.device_id}-${g.timestamp}`, type: "agent_gap", title: "Suspicious agent gap detected", description: `Device ${g.device_id.slice(0, 8)}… was offline for ${Math.round(g.gap_seconds / 60)} minutes`, timestamp: g.timestamp, severity: "medium" });
  });
  return alerts.filter((a) => !dismissedAlerts.has(a.id)).sort((a, b) => b.timestamp.localeCompare(a.timestamp));
}

function buildAnalytics() {
  const toolCounts = {}, catCounts = {}, procCounts = {}, timeCounts = {};
  detectionEvents.forEach((e) => {
    toolCounts[e.tool_name] = (toolCounts[e.tool_name] || 0) + 1;
    catCounts[e.category] = (catCounts[e.category] || 0) + 1;
    procCounts[e.process_name] = (procCounts[e.process_name] || 0) + 1;
    const hour = e.timestamp.substring(11, 13) + ":00";
    timeCounts[hour] = (timeCounts[hour] || 0) + 1;
  });
  return {
    byTool: Object.entries(toolCounts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count).slice(0, 8),
    byCategory: Object.entries(catCounts).map(([name, value]) => ({ name, value })).sort((a, b) => b.value - a.value),
    overTime: Object.entries(timeCounts).map(([time, count]) => ({ time, count })).sort((a, b) => a.time.localeCompare(b.time)),
    topProcesses: Object.entries(procCounts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count).slice(0, 10),
  };
}

// ─── ROUTES ──────────────────────────────────────────────────────────────────

// Health check
app.get("/api/health", (_, res) => res.json({ status: "ok", version: "1.0.0" }));

// Profile / Me (demo user)
app.get("/api/me", (_, res) => {
  res.json({
    id: "uid_yashm",
    org_id: "demo",
    full_name: "Yash M",
    email: "yash.m@company.com",
    department: "Engineering",
    role: "admin",
    avatar_url: null,
    org_name: "Demo Organization",
    org_slug: "demo-org",
    created_at: ago(365 * 24 * 60),
    last_active: ago(5),
    dark_mode: false,
    notification_prefs: { high_risk_alerts: true, daily_summary: true, block_notifications: true },
  });
});
app.put("/api/me", (req, res) => res.json({ status: "updated" }));

// Detection Events
app.get("/api/events", (req, res) => {
  let events = [...detectionEvents];
  if (req.query.category && req.query.category !== "all") events = events.filter((e) => e.category === req.query.category);
  if (req.query.risk_level && req.query.risk_level !== "all") events = events.filter((e) => e.risk_level === req.query.risk_level);
  const limit = parseInt(req.query.limit) || 200;
  events = events.slice(0, limit);
  res.json({ total: events.length, events });
});

// Heartbeats
app.get("/api/heartbeats", (_, res) => res.json(heartbeats));

// Stats
app.get("/api/stats", (_, res) => res.json(buildStats()));

// Alerts
app.get("/api/alerts", (_, res) => res.json(buildAlerts()));
app.post("/api/alerts/:id/dismiss", (req, res) => { dismissedAlerts.add(req.params.id); res.json({ status: "dismissed", id: req.params.id }); });
app.post("/api/alerts/:id/resolve", (req, res) => { dismissedAlerts.add(req.params.id); res.json({ status: "resolved", id: req.params.id }); });

// Analytics
app.get("/api/analytics", (_, res) => res.json(buildAnalytics()));

// Subscriptions
app.get("/api/subscriptions", (_, res) => res.json(subscriptions));
app.put("/api/subscriptions/:id", (req, res) => res.json({ status: "updated", id: req.params.id }));

// Spend Overview
app.get("/api/spend", (_, res) => {
  const activeSubs = subscriptions.filter((s) => s.status === "active");
  const zombies = subscriptions.filter((s) => s.status === "zombie");
  const totalMonthlySpend = activeSubs.reduce((acc, s) => acc + s.cost_monthly, 0);
  const zombieCost = zombies.reduce((acc, s) => acc + s.cost_monthly, 0);
  res.json({
    totalMonthlySpend,
    monthlyBudget: orgSettings.monthly_budget,
    budgetRemaining: orgSettings.monthly_budget - totalMonthlySpend,
    zombieLicenses: zombies.length,
    zombieCost,
  });
});

// Team
app.get("/api/team", (_, res) => res.json({ members: teamMembers, invites: teamInvites }));
app.post("/api/team/invite", (req, res) => {
  const { email, role = "member" } = req.body;
  const invite = { id: `inv_${Date.now()}`, org_id: "demo", email, role, status: "pending", created_at: new Date().toISOString(), expires_at: new Date(now.getTime() + 7 * 24 * 60 * 60000).toISOString() };
  teamInvites.push(invite);
  res.json({ status: "invited", email });
});

// User detection count
app.get("/api/user-detection-count", (req, res) => {
  const email = req.query.email;
  const count = detectionEvents.filter((e) => e.user_email === email || e.user_id === email).length;
  res.json({ count });
});

// Settings
app.get("/api/settings", (_, res) => res.json(orgSettings));
app.put("/api/settings", (req, res) => { orgSettings = { ...orgSettings, ...req.body }; res.json({ status: "updated" }); });

// Firewall Rules
app.get("/api/firewall/rules", (_, res) => res.json(firewallRules));
app.put("/api/firewall/rules", (req, res) => {
  const rule = req.body;
  const ruleId = rule.tool_name.replace(/\s+/g, "_").toLowerCase();
  const existing = firewallRules.find((r) => r.id === ruleId);
  if (existing) { Object.assign(existing, { ...rule, id: ruleId, updated_at: new Date().toISOString(), updated_by: "yash.m@company.com" }); }
  else { firewallRules.push({ id: ruleId, ...rule, updated_at: new Date().toISOString(), updated_by: "yash.m@company.com", block_count: 0 }); }
  res.json({ status: "updated" });
});
app.delete("/api/firewall/rules/:tool", (req, res) => {
  const ruleId = req.params.tool.replace(/\s+/g, "_").toLowerCase();
  const idx = firewallRules.findIndex((r) => r.id === ruleId);
  if (idx !== -1) firewallRules.splice(idx, 1);
  res.json({ status: "deleted" });
});
app.get("/api/firewall/events", (_, res) => res.json([]));
app.get("/api/firewall/stats", (_, res) => {
  const blocked = firewallRules.filter((r) => r.status === "blocked");
  const allowed = firewallRules.filter((r) => r.status === "allowed");
  const complianceScore = firewallRules.length > 0 ? Math.round((allowed.length / firewallRules.length) * 100) : 100;
  res.json({ blockedToday: 17, blockEventsThisWeek: 89, policyViolations: blocked.reduce((a, r) => a + r.block_count, 0), complianceScore });
});
app.post("/api/firewall/sync", (_, res) => res.json({ status: "synced" }));

// Sensitivity / Data Risk
app.get("/api/sensitivity/events", (req, res) => {
  let events = detectionEvents.filter((e) => e.sensitivity_flag);
  if (req.query.flag) events = events.filter((e) => e.sensitivity_flag === req.query.flag);
  res.json(events.map((e) => ({ ...e, id: e.event_id, reviewed: false })));
});
app.patch("/api/sensitivity/events/:id/review", (req, res) => res.json({ status: "reviewed", id: req.params.id }));
app.get("/api/sensitivity/risk-scores", (_, res) => res.json(employeeRiskScores));
app.get("/api/sensitivity/stats", (_, res) => {
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();
  const sensitive = detectionEvents.filter((e) => e.sensitivity_flag);
  const highRiskToday = sensitive.filter((e) => e.timestamp >= todayStart && (e.sensitivity_score || 0) >= 70).length;
  const employeeSet = new Set(sensitive.map((e) => e.user_id).filter(Boolean));
  const flagCounts = {};
  sensitive.forEach((e) => { flagCounts[e.sensitivity_flag] = (flagCounts[e.sensitivity_flag] || 0) + 1; });
  const mostCommonType = Object.entries(flagCounts).sort((a, b) => b[1] - a[1])[0]?.[0] || "—";
  const avgScore = sensitive.length > 0 ? Math.round(sensitive.reduce((s, e) => s + (e.sensitivity_score || 0), 0) / sensitive.length) : 0;
  res.json({ highRiskToday, employeesWithRisk: employeeSet.size, mostCommonType, orgRiskScore: avgScore });
});
app.post("/api/sensitivity/rebuild-scores", (_, res) => res.json({ status: "rebuilt" }));
app.post("/api/last-active", (_, res) => res.json({ status: "updated" }));

// Tamper Alerts
app.get("/api/tamper-alerts", (_, res) => res.json(tamperAlerts));

// Subscribe to events (polling alternative, just return latest)
app.get("/api/live-events", (_, res) => {
  const latest = [...detectionEvents].sort((a, b) => b.timestamp.localeCompare(a.timestamp)).slice(0, 5);
  res.json(latest);
});

// ─── START ───────────────────────────────────────────────────────────────────
const PORT = 3001;
app.listen(PORT, () => {
  console.log(`\n✅ Devise Backend running at http://localhost:${PORT}`);
  console.log(`   All endpoints available at http://localhost:${PORT}/api/...\n`);
});
