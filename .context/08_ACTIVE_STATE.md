# 📊 ScholarX — Active State & Health Tracker

> **Living system state, verified capabilities, active technical debt, and sprint posture.**

---

## 1. System Posture (October 2026)

- **Overall Delivery**: ✅ **Phase 10 Locked & Exhibition Verified**
- **Scholarship Intelligence**: **510/510 Opportunities Researched with 11-Dimension Dossiers** (512 in standalone database)
  - Europe: 161
  - Asia: 131
  - Americas: 105
  - MENA: 73
  - Oceania: 40
- **Pakistani Demo Profiles**: 6 Verified Presets (`data/profiles/`)
- **Backend Infrastructure**:
  - FastAPI 0.115+ on port 8000
  - 10-node LangGraph StateGraph pipeline (`backend/graph/builder.py`)
  - aiosqlite SQLite WAL mode (`data/scholarx_sessions.db`)
  - Deterministic typo-resilient field matching (`backend/workflows/field_matching.py`)
  - 30-key round-robin rotation pool across Groq, Gemini, Tavily, Firecrawl, Jina
- **Frontend Infrastructure**:
  - Next.js 15.1.0 on port 3000
  - 1920×1080 Command Theatre Spatial Stage Floor
  - Unified `JudgeControlBar` (ADR-009)
  - Dual Execution Mode (`LIVE STREAM` vs `DEMO REPLAY`)
  - Serverless & local Node 22 built-in SQLite engine (`frontend/lib/db/sqliteClient.ts`)
  - Client-side cost engine (`pakistanCostEngine.ts`) & deadline runway (`deadlineEngine.ts`)
- **Test Verification**: 135+ tests collected and passing across 44 modules in `backend/tests/`.

---

## 2. Active Technical Debt & Tracked Gaps

### ISS-001: Legacy Explorer Flat vs Nested Schema
- **Severity**: 🟢 Low (Diagnostic/Legacy Component Only)
- **Location**: `frontend/components/scholarships/ScholarshipDNAExplorer.tsx`
- **Context**: Legacy standalone table expects flat scholarship attributes, while backend models return nested objects. Command Theatre is unaffected as it uses canonical normalized event payloads.

### ISS-002: Intake Profile Extraction Mapping
- **Severity**: 🟢 Low
- **Location**: `frontend/components/intake/IntakeDropzone.tsx`
- **Context**: Automatic document extraction maps to nested profile attributes. Fallback defaults in `data/profiles/` provide 100% coverage during exhibition demonstrations.

### ISS-003: Skeptic Review Top 6 Optimization
- **Severity**: 🟢 Low (Intended Runtime Optimization)
- **Location**: `backend/graph/nodes.py`
- **Context**: `skeptic_node` limits deep LLM adversarial friction auditing to the top 6 highest-scoring candidates to conserve token budget and optimize latency. Lower-ranked candidates carry baseline heuristic friction flags.

### ISS-004: Docker Services Unused
- **Severity**: 🟢 Low (Architectural Standard - ADR-001)
- **Location**: `docker-compose.yml`, `backend/config.py`
- **Context**: Docker defines optional external PostgreSQL, Redis, and ChromaDB containers. Unused by default in favor of zero-dependency SQLite WAL.

---

## 3. Recently Resolved Milestones

- **✅ ISS-009: 510 Scholarship Expansion**: Expanded catalog from 310 to 510 fully researched deep dossiers across all 5 global regions.
- **✅ ISS-010: Typo-Resilient Offline Field Matching**: Built deterministic fuzzy taxonomy engine in `backend/workflows/field_matching.py` with zero online dependencies (`test_offline_typo_retrieval.py`).
- **✅ ISS-011: Node 22 Built-in SQLite Portability**: Implemented `frontend/lib/db/sqliteClient.ts` and `databaseBundle.ts` supporting Vercel serverless `/tmp` mutation and read-only local dev.
- **✅ ISS-012: Standalone Interactive Database Viewer**: Created zero-server HTML5 viewer `scholarships_database_viewer.html` and portable SQLite `scholarships_database.db`.
- **✅ ISS-005: Real-Time SSE Stream Integration**: Session-isolated event queues, dynamic burst coalescing on client.
- **✅ ISS-006: Modern Google GenAI SDK Migration**: Migrated `backend/agents/skeptic_agent.py` to `from google import genai` and `genai.Client()`.
- **✅ ISS-007: Exhibition Resilience & 12-Stage Replay**: Implemented `simulation-engine.ts` deterministic replay across 3 Pakistani student profiles.
- **✅ ISS-008: Dual Footer Redundancy Consolidated**: Consolidated all playback controls, stage scrubbing, and telemetry into `JudgeControlBar.tsx`.
