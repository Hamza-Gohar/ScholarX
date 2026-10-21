# ScholarX — Known Issues & Technical Debt

> Tracked bugs, gaps, and improvement opportunities.

**Last Updated**: 2026-10-03
**Status**: 🟢 Verified & Exhibition Safe

---

## Active Known Issues

### ISS-001: Legacy Explorer Flat vs Nested Schema
- **Severity**: 🟢 Low (Diagnostic/Legacy Component Only)
- **Location**: `frontend/src/components/scholarships/ScholarshipDNAExplorer.tsx`
- **Problem**: Legacy exploratory component expects flat fields whereas backend models return nested Pydantic objects.
- **Impact**: Command Theatre is unaffected (theatre uses canonical normalized event payloads).
- **Resolution Path**: Add schema adapter if legacy explorer is revived for standalone view.

### ISS-002: Intake Profile Extraction Mapping
- **Severity**: 🟢 Low
- **Location**: `frontend/src/components/intake/IntakeDropzone.tsx`
- **Problem**: Document extractions populate nested profile attributes.
- **Impact**: Pre-demo intake card fallback defaults provide full coverage for exhibition testing.

### ISS-003: Skeptic Review Evaluates Top 6 Candidates
- **Severity**: 🟢 Low
- **Location**: `backend/graph/nodes.py`
- **Problem**: `skeptic_node` limits in-depth adversarial audit to top 6 candidates to conserve LLM token budget.
- **Impact**: High-priority candidates receive full multi-angle adversarial challenge; lower-ranked candidates carry baseline heuristics.
- **Status**: Intended optimization for exhibition runtime efficiency.

### ISS-004: Docker Services Provisioned but Unused
- **Severity**: 🟢 Low
- **Location**: `docker-compose.yml`, `backend/config.py`
- **Context**: Docker defines optional external PostgreSQL, Redis, and ChromaDB containers.
- **Status**: Intentional architecture decision (ADR-001) for local-first zero-config exhibition reliability using SQLite WAL and in-memory session buses.

---

## Resolved Issues

### ✅ ISS-005: Real-Time SSE Stream Integration
- **Resolved In**: Phase 8 & Phase 9
- **Resolution**: Implemented `pipeline_broadcaster.py`, session-isolated event queues, Redis Pub/Sub, FastAPI SSE `/stream/{session_id}` route, and client-side `presentationQueue` with dynamic burst coalescing.

### ✅ ISS-006: Modern Google GenAI SDK Migration
- **Resolved In**: Phase 8
- **Resolution**: Fully migrated `backend/agents/skeptic_agent.py` to `from google import genai` and `genai.Client(api_key=key)`, removing deprecated `google.generativeai` calls.

### ✅ ISS-007: Exhibition Resilience & Safeguard Fallback
- **Resolved In**: Phase 9
- **Resolution**: Implemented `DemoEventPlayer` providing 100% deterministic 12-stage exhibition replay across 3 Pakistani profiles with search failover and partial fleet isolation.

### ✅ ISS-008: Dual Footer Redundancy & Clutter Removal
- **Resolved In**: Phase 10
- **Resolution**: Consolidated all exhibition controls, live SSE streaming telemetry, playback scrubbing, and artifact modal triggers into unified, collapsible `JudgeControlBar.tsx`.
