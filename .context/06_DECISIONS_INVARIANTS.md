# ⚖️ ScholarX — Architectural Decisions & Invariants

> **Consolidated Architectural Decision Records (ADRs 001-012) and Non-Negotiable System Invariants.**

---

## 1. Architectural Decision Records (ADRs)

### ADR-001: SQLite over PostgreSQL & Docker
- **Status**: Accepted
- **Decision**: Use single-file local SQLite (`aiosqlite`, WAL mode) as the sole production database. Do NOT require external Docker containers (PostgreSQL, Redis, ChromaDB).
- **Rationale**: ScholarX is a local-first exhibition and demo platform. It must run instantly on any machine with zero container configuration or port conflict risk.

### ADR-002: Groq Primary, Gemini Fallback
- **Status**: Accepted
- **Decision**: Use Groq (`qwen/qwen3.8-27b`) as primary LLM and Google Gemini (`gemini-flash-latest`) as fallback.
- **Rationale**: Groq provides ultra-low latency inference across 13 keys; Gemini handles deeper narrative reasoning across 3 keys.

### ADR-003: Workflow-First Philosophy
- **Status**: Accepted
- **Decision**: 7 of 12 pipeline stages are deterministic Python workflows, not LLM agents.
- **The Rule**: If a task can be specified as conditional logic, table lookups, or arithmetic math (eligibility, costs, deadlines, ranking), it MUST be code. Reserve LLMs only for messy text extraction, conversational counselor, and adversarial reasoning.
- **Impact**: Zero numeric hallucination in scoring and ranking.

### ADR-004: Server-Sent Events (SSE) over WebSocket
- **Status**: Accepted
- **Decision**: Real-time event streaming is delivered via native browser `EventSource` over HTTP `/api/stream/{session_id}`.
- **Rationale**: Data flow is strictly unidirectional (server telemetry → client theatre). SSE auto-reconnects and works seamlessly through Next.js proxy rewrites.

### ADR-005: 30-Key Round-Robin Rotation
- **Status**: Accepted
- **Decision**: Distribute 30 API keys across 5 providers (13 Groq, 3 Gemini, 7 Tavily, 6 Firecrawl, 1 Jina) with automatic per-request rotation and 60-second cooldown on 429 errors.
- **Rationale**: Prevents rate-limit halts during intensive multi-scout parallel discovery.

### ADR-006: Per-Request Routing (Not Per-Session)
- **Status**: Accepted
- **Decision**: Keys rotate on every individual request rather than binding a session to a single key.
- **Rationale**: Prevents key saturation from long-running sessions.

### ADR-007: Spatial Stage & Command Theatre Architecture
- **Status**: Accepted
- **Decision**: Render multi-agent intelligence on an interactive 1920×1080 virtual coordinate floor with D3-geo continental beacons and Bezier communication arcs.

### ADR-008: Zero-Auth Local Sessions
- **Status**: Accepted
- **Decision**: No passwords, OAuth, or multi-tenant database partitions. Sessions are identified by client-generated UUIDs stored in `localStorage`.

### ADR-009: Unified `JudgeControlBar` Surface
- **Status**: Accepted
- **Decision**: Elevate `JudgeControlBar` as the sole, unified exhibition control dock at the bottom of the viewport, deprecating redundant footer controls.
- **Features**: Stage scrubbing (0-12), Play/Pause (<kbd>Space</kbd>), Reset (<kbd>R</kbd>), Mode Toggle (<kbd>D</kbd>), Collapse (<kbd>J</kbd>).

### ADR-010: Executive Brand Header
- **Status**: Accepted
- **Decision**: Remove early-phase developer mode buttons (`PHASE 3`, `PHASE 4`..) from the brand header. Retain a clean `LIVE STREAM` vs `DEMO REPLAY` toggle.

### ADR-011: Spatial Stage Priority & Clutter Removal
- **Status**: Accepted
- **Decision**: Remove static debug token bars from the presentation floor, returning 100% of vertical canvas to the world map and packet dynamics.

### ADR-012: 6-Scale Semantic Typography & Strict 10px Floor
- **Status**: Accepted
- **Decision**: Standardize all theatre typography on 6 scales: `DISPLAY` (24-32px), `LARGE` (18-20px), `MEDIUM` (14-15px), `BODY` (13-14px), `LABEL` (11-12px mono), `MICRO` (10px mono floor). Sub-10px text is strictly prohibited to guarantee 3-meter presentation legibility.

### ADR-013: Hybrid Serverless SQLite & Node 22 Built-in Engine
- **Status**: Accepted
- **Decision**: Provide direct SQLite querying from Next.js server components and API routes using Node 22 built-in `node:sqlite` (`frontend/lib/db/sqliteClient.ts` and `databaseBundle.ts`), with read-only multi-candidate path resolution and `/tmp` copy for serverless writes.
- **Rationale**: Eliminates backend proxy round-trip latency for instant scholarship queries while retaining complete offline portability for Vercel lambdas and static environments.

### ADR-014: Typo-Resilient Offline Academic Field Matching
- **Status**: Accepted
- **Decision**: Implement deterministic fuzzy matching and faculty taxonomies in `backend/workflows/field_matching.py` that handle student spelling mistakes (e.g., `compter scince`, `machne lerning`) offline without requiring external Groq/LLM calls.
- **Rationale**: Students commonly misspell academic specializations. The system must never reject eligible students due to typographical errors even when running fully offline.

---

## 2. Inviolable Invariants for AI Agents

1. **Never Calculate Costs or Rankings via LLM Prompting**:
   - Always call `backend.workflows.cost_analyzer` and `backend.workflows.ranking`.
2. **Never Add Docker Requirements for Default Setup**:
   - Zero-config local SQLite must always work out of the box.
3. **Never Hardcode API Keys or Call Providers Directly**:
   - Always request keys from `get_key_manager()`.
4. **Never Downgrade Gemini SDK**:
   - Use `from google import genai` (ISS-006). Never import `google.generativeai`.
5. **Never Introduce Sub-10px Typography on Frontend Surfaces**:
   - Preserve the 10px minimum mono floor for presentation legibility.
6. **Always Convert Financial Metrics to Pakistani Rupees (PKR)**:
   - Provide local currency context alongside PKR, but PKR is the primary benchmark.
7. **Ensure 100% Offline Resilience for Querying & Field Matching**:
   - Misspelled queries and academic fields must resolve via `field_matching.py` without requiring online LLM availability.
