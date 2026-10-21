# 📡 ScholarX — API Routes & SSE Event Streaming Reference

> **Complete catalog of FastAPI REST endpoints, request/response models, and the 34+ real-time SSE event types.**

---

## 1. REST API Endpoints Overview

All endpoints are served from FastAPI on port 8000 and proxied via Next.js rewrites:

### Discovery & LangGraph Pipeline
- **`POST /api/discover`**
  - **Purpose**: Spawns an asynchronous 10-node LangGraph mission in a background task.
  - **Request Body**:
    ```json
    {
      "student_profile": { ... },
      "target_regions": ["Europe", "Asia", "Americas", "MENA", "Oceania"],
      "session_id": "optional-custom-session-uuid"
    }
    ```
  - **Response**: `202 Accepted`
    ```json
    {
      "session_id": "d748f21e-...",
      "status": "DISPATCHED",
      "message": "LangGraph multi-agent mission launched"
    }
    ```

### Real-Time Streaming
- **`GET /api/stream/{session_id}`**
  - **Protocol**: Server-Sent Events (SSE) via `text/event-stream`.
  - **Behavior**: Subscribes to the `EventBus` async queue for that session. Automatically replays up to 500 buffered events if the client reconnects.

### Profile Intake & Conversational Counselor
- **`POST /api/profile/upload`**
  - **Content-Type**: `multipart/form-data` (PDF, DOCX, TXT file).
  - **Response**: Extracted `StudentProfile` with completeness percentage and identified gaps.
- **`POST /api/profile/chat`**
  - **Purpose**: Conversational Q&A to clarify student GPA, budget, or preferences.
  - **Request Body**: `{"session_id": "...", "message": "My budget is PKR 500,000"}`
  - **Response**: `{"reply": "...", "updated_profile": { ... }}`

### Scholarships Database
- **`GET /api/scholarships`**
  - **Query Params**: `q` (search string), `region` (Europe/Asia..), `degree_level`, `funding_type`, `limit` (default 20), `offset` (default 0).
  - **Response**: Array of 310 Deep Dossier scholarship summaries.
- **`GET /api/scholarships/{scholarship_id}`**
  - **Response**: Complete 11-dimension Canonical Dossier object.

### Sessions & Replay Hydration
- **`GET /api/sessions`** — Lists past sessions with student names, dates, and top match.
- **`GET /api/sessions/{session_id}`** — Returns full state, ranked scholarships, and event history.
- **`DELETE /api/sessions/{session_id}`** — Deletes session and associated ranked records.

### System Health & Exhibition Preflight
- **`GET /api/health`**
  - **Response**: System status, SQLite connectivity, and live pool metrics for all 30 API keys.
- **`GET /api/exhibition/preflight`**
  - **Response**: Validates all 12 stages, 3 Pakistani demo profiles, and offline fallback caches.

---

## 2. Server-Sent Events (SSE) Streaming Protocol

Events emitted via `/api/stream/{session_id}` follow standard SSE framing:

```
event: message
data: {
  "event_type": "SCOUT_DEPLOYED",
  "source": "EuropeScout",
  "severity": "INFO",
  "title": "Europe Scout Dispatched",
  "message": "Scanning 101 European bilateral and university quotas",
  "payload": {
    "region": "Europe",
    "scout_id": "scout_eu",
    "coordinates": {"x": 480, "y": 240}
  },
  "timestamp": "2026-10-20T21:00:00.000Z"
}

```

---

## 3. The 34+ Distinct `AgentEventType` Catalog

Categorized by pipeline lifecycle:

### Phase 1: Intake & Discovery
- `PROFILE_PARSED` (Intake complete, completeness score generated)
- `STRATEGY_GENERATED` (Commander formulates regional queries)
- `SCOUT_DEPLOYED` (Scout beacon illuminates and launches on map)
- `QUERY_EXECUTED` (Tavily search query sent)
- `PAGE_SCRAPED` (Firecrawl or Jina Reader reads URL markdown)
- `CANDIDATE_FOUND` (Scout extracts a potential opportunity)
- `CANDIDATE_DEDUPED` (Token-set Jaccard removes duplicates)
- `SCOUT_COMPLETED` (Regional scout finishes search pipeline)

### Phase 2: Specialist Investigation
- `ELIGIBILITY_EVALUATED` (15-dimension checklist processed)
- `COST_CALCULATED` (4-phase PKR expense waterfall computed)
- `DEADLINE_ANALYZED` (Runway computed against Pakistani lead times)
- `SKEPTIC_CHALLENGE` (Adversarial challenge issued by Skeptic Agent)
- `SKEPTIC_REBUTTAL` (Evidence-based rebuttal produced)
- `EVIDENCE_VERIFIED` (Official portal citation confirmed)

### Phase 3: Synthesis & Ranking
- `SYNTHESIS_STARTED` (Aggregating multi-specialist signals)
- `CARD_SYNTHESIZED` (Unified DNA card compiled)
- `SCORE_COMPUTED` (8-factor composite arithmetic applied)
- `RANKING_LOCKED` (Final candidate hierarchy locked)
- `ROADMAP_GENERATED` (6-phase Pakistani application journey created)

### Phase 4: Stage & Lifecycle Infrastructure
- `MISSION_STARTED` (Pipeline starts)
- `MISSION_COMPLETED` (Pipeline finishes successfully)
- `STAGE_TRANSITION` (Scrubber jumps to next stage 0-12)
- `KEY_ROTATED` (KeyManager switches API key)
- `KEY_COOLDOWN` (API key hit 429 and enters 60s sleep)
- `FAILOVER_TRIGGERED` (Search provider failover from Tavily to Firecrawl)
- `ERROR_RECORDED` (Error logged in circular buffer)

---

## 4. Semantic Event Color Coding on the Spatial Canvas

| Envelope Color | Event Category | Meaning |
|:---|:---|:---|
| **Gold (`#f59e0b`)** | `COMMAND` | Central Orchestrator orders, bilateral HEC seats |
| **Cyan (`#06b6d4`)** | `QUERY / FLOW` | Scout search queries, SSE network pulses |
| **Emerald (`#10b981`)**| `VERIFIED` | 100% eligibility match, full funding verified |
| **Amber (`#f59e0b`)** | `DEADLINE` | Approaching deadlines, administrative lead warnings |
| **Rose (`#f43f5e`)** | `CHALLENGE` | Skeptic adversarial friction, blocked accounts, return bonds |
| **Purple (`#a855f7`)**| `RANKING` | 8-factor composite arithmetic scores |
