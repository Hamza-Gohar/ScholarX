---
trigger: always
---

# ScholarX Project Context

You are working on **ScholarX**, an autonomous multi-agent AI scholarship discovery and intelligence platform built exclusively for Pakistani students.

## Quick Reference
- **Backend**: FastAPI (port 8000) + LangGraph 10-node StateGraph DAG, Python 3.12, offline typo-resilient field matching
- **Frontend**: Next.js 15.1.0 (port 3000), React 19, TypeScript, Tailwind CSS, Zustand v5, Node:sqlite serverless support
- **Database**: SQLite via aiosqlite (`data/scholarx_sessions.db`), WAL mode (zero Docker requirement)
- **Standalone DB**: `scholarships_database.db` (512 opportunities) + `scholarships_database_viewer.html`
- **LLM**: Groq (`qwen/qwen3.8-27b` primary, 13 keys) + Google Gemini (`gemini-flash-latest` fallback, 3 keys)
- **API Keys**: 30 keys total across 5 providers (Groq 13, Gemini 3, Tavily 7, Firecrawl 6, Jina 1) with per-request round-robin rotation
- **Tests**: 135+ tests collected in 44 modules in `backend/tests/`, run with `.venv/bin/pytest backend/tests/ -v`
- **Scholarships**: 510 Deep Dossiers verified across 5 regions (Europe 161, Asia 131, Americas 105, MENA 73, Oceania 40)
- **Status**: Phase 10 Locked & Verified (Command Theatre, JudgeControlBar, Live SSE, 12-Stage Replay, Node:sqlite, Offline Typo Matching)

## Architecture — 10-Node LangGraph DAG
4 LLM Agents + 7 Deterministic Workflows:
1. **ProfileAgent** → Document parsing, profile extraction, conversational counselor
2. **DiscoveryCommander** → Search strategy, parallel 5-scout deployment, dedup
3. **5 Regional Scouts** → Deterministic search→scrape→extract pipelines (Europe, Asia, Americas, MENA, Oceania)
4. **EligibilityInvestigator** → 15-dimension deterministic matching (GPA, age, degree, HEC HAT/USAT, MOI) + `field_matching.py` typo resilience
5. **TrueCostAnalyzer** → 4-phase PKR out-of-pocket calculation
6. **DeadlineIntelligence** → Risk-tiered deadline runway with Pakistani administrative lead times
7. **SkepticAgent** → Adversarial Pakistani friction analysis (return bonds, blocked accounts, backlogs)
8. **SynthesisWorkflow** → Reconcile all data into DNA cards
9. **RankingEngine** → 8-factor weighted composite arithmetic scoring (0-100)
10. **AdvisorAgent** → Personalized roadmap with Pakistani office directory

## Key Invariants
- **Workflow > Agent (ADR-003)**: Deterministic workflows for all arithmetic, scoring, and rules. Zero LLM numeric hallucination.
- **Pakistan-Specific**: All costs in PKR, education system is BISE/HEC/IBCC, bilateral quotas tracked.
- **Offline Resilience (ADR-014)**: Field matching and scholarship search must resolve typos offline without requiring online LLMs.
- **Key Manager (ADR-005)**: Never hardcode keys; use `backend.utils.api_keys.get_key_manager()`.
- **Modern Gemini SDK (ISS-006)**: Use `from google import genai` and `genai.Client()`. Never import `google.generativeai`.
- **Typography Floor (ADR-012)**: 6-scale typography with 10px monospace minimum floor. Sub-10px text is prohibited.

## File Structure Quick Map
```
backend/agents/       → 4 LLM-powered agents
backend/workflows/    → 7 deterministic workflows (including scouts/ and field_matching.py)
backend/tools/        → Document parser, extractor, Tavily, Firecrawl, Jina Reader
backend/schemas/      → Pydantic v2 models (student, scholarship, scoring, events, roadmap)
backend/api/routes/   → 5 FastAPI route modules
backend/db/           → Session store (aiosqlite WAL), seed scripts, cache
backend/utils/        → GPA converter, Pakistan costs, API key rotator, date utils
backend/graph/        → LangGraph builder, nodes, edges, state
frontend/app/         → Next.js 15 App router (page.tsx, mission/[sessionId], dossier/[id], catalog)
frontend/components/  → Command Theatre, StageFloor, PacketCanvas, JudgeControlBar
frontend/lib/         → Zustand store.ts, api.ts, simulation-engine.ts, seed-data.ts, db/sqliteClient.ts
data/scholarships/    → 510 scholarships across 5 regions (JSON)
data/profiles/        → 6 Pakistani demo student profiles
.context/             → Full hierarchical context manuals (00_QUICKSTART to 08_ACTIVE_STATE)
```

## Instant Context Commands
- High-density primer: `python scripts/context.py primer`
- Live telemetry: `python scripts/context.py status`
- System doctor: `python scripts/doctor.py`
- Validate context: `python scripts/context.py validate`
