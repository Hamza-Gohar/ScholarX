# 🚀 ScholarX — Agent 60-Second Quickstart Primer

> **The Autonomous Scholarship Intelligence Network for Pakistani Students**  
> *Targeted reading time: 2 minutes (<1,800 tokens). Start here whenever entering with a fresh context window.*

---

## 1. What is ScholarX?

ScholarX is a production-grade, local-first autonomous intelligence platform purpose-built to discover, verify, calculate true out-of-pocket costs (in PKR), rank, and roadmap international scholarships specifically for **Pakistani students**.

### Core Problem Solved
Pakistani students miss out on hundreds of fully funded international scholarships (e.g. 400+ Hungarian bilateral seats, Chinese CSC, Turkiye Burslari, DAAD, Erasmus Mundus) due to hidden out-of-pocket costs (IELTS PKR 75k+, visa fees, HEC attestation, German blocked accounts €11,904), bureaucratic bottlenecks (HEC HAT/USAT, IBCC 12-year equivalence, MOFA stamps), and scattered criteria. ScholarX automates the entire discovery, friction auditing, and application roadmap pipeline.

---

## 2. Current System Posture (October 2026)

- **Overall Status**: ✅ **100% Complete & Exhibition Verified** (Phase 10 delivery complete).
- **Scholarships Database**: **510 Deep Dossier scholarships** across 5 continental regions (Europe 161, Asia 131, Americas 105, MENA 73, Oceania 40) with 11-dimension research dossiers. Standalone viewer in `scholarships_database_viewer.html` and `scholarships_database.db` (512 records).
- **Backend**: FastAPI (Python 3.12, port 8000) compiling a **10-node LangGraph StateGraph pipeline**, offline typo-resilient field matching, and async SSE real-time event streaming.
- **Frontend**: Next.js 15.1.0 (port 3000, App router) featuring the **Command Theatre** (1920×1080 spatial stage, D3-geo map, curved Bezier flight packets, obsidian glass aesthetic, collapsible `JudgeControlBar`), plus hybrid serverless SQLite (`node:sqlite` via `sqliteClient.ts`).
- **Database**: Single-file local SQLite with WAL mode (`data/scholarx_sessions.db`). Zero external Docker dependencies required (ADR-001). Portable to Vercel/serverless via `databaseBundle.ts`.
- **API Key Pool**: 30 keys (13 Groq, 3 Gemini, 7 Tavily, 6 Firecrawl, 1 Jina) with automatic per-request round-robin rotation, 60s cooldown, and health tracking.
- **Test Suite**: 135+ test cases across 44 test modules in `backend/tests/` (including offline typo & fuzzy matching).

---

## 3. The 7 Non-Negotiable Invariants

When working on ScholarX, **NEVER** violate these architectural rules:

1. **Workflow-First Philosophy (ADR-003)**:
   - Arithmetic, scoring, date math, eligibility comparisons, and ranking MUST run via deterministic Python code workflows.
   - LLMs are reserved ONLY for document extraction, counselor conversation, adversarial skeptic challenges, and narrative roadmaps.
   - **Zero LLM hallucination in numeric scores or rankings.**
2. **Pakistan-Localized Reality**:
   - All expenses must be converted to **PKR**.
   - Pakistani education boards (BISE, Cambridge O/A Levels, IBCC equivalence, HEC recognized universities) and tests (HEC HAT, USAT, NTS GAT) are first-class concepts.
3. **Local-First & Offline Resilient (ADR-001, ADR-013, ADR-014)**:
   - SQLite WAL is the sole production database. Do NOT require Docker, PostgreSQL, or Redis containers for standard local execution.
   - System must function 100% offline with fuzzy field matching resilient to spelling mistakes and typos without requiring external LLM calls.
4. **Key Management Protocol (ADR-005, ADR-006)**:
   - Never hardcode or call API providers directly without `backend.utils.api_keys.get_key_manager()`. All external LLM, search, and scrape calls must rotate per-request.
5. **Modern SDK Usage (ISS-006)**:
   - For Gemini calls, use `from google import genai` and `genai.Client(api_key=key)` (NOT the deprecated `google.generativeai`).
6. **Exhibition Visual Standards (ADR-009, ADR-012)**:
   - Obsidian dark glassmorphism theme with semantic accents (`emerald` success, `cyan` discovery, `gold` costs/bilateral, `amber` deadlines, `rose` skeptic, `purple` ranking).
   - Strict 6-scale typography: `DISPLAY` (24-32px), `LARGE` (18-20px), `MEDIUM` (14-15px), `BODY` (13-14px), `LABEL` (11-12px mono), `MICRO` (10px mono floor). **Sub-10px text is strictly prohibited.**
7. **Hybrid Serverless & Node:SQLite Portability**:
   - Frontend components can resolve and filter scholarships directly using Node 22 built-in `node:sqlite` (`frontend/lib/db/sqliteClient.ts`) or fall back to JSON/API. Single source of truth is always preserved.

---

## 4. Golden Commands

| Action | Command | Purpose |
|:---|:---|:---|
| **System Primer** | `python scripts/context.py primer` | Concentrated context dump for agent prompt injection |
| **System Status** | `python scripts/context.py status` | Live check of DB, API keys, ports, and tests |
| **System Doctor** | `python scripts/doctor.py` | Full 48-check environment verification |
| **Start Full Stack** | `npm run dev` or `make dev` | Starts FastAPI (8000) and Next.js (3000) concurrently |
| **Start Backend** | `make backend` | Starts FastAPI with auto-reload on port 8000 |
| **Start Frontend** | `make frontend` | Starts Next.js development server on port 3000 |
| **Run Fast Tests** | `.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py` | Fast 0.2s unit test verification |
| **Run All Tests** | `make test` | Full backend test suite |
| **Validate Context** | `python scripts/context.py validate` | Self-healing audit of docs vs actual codebase |

---

## 5. File Structure Quick-Map

```
SCHOLARX/
├── backend/
│   ├── agents/         → 4 LLM agents: profile_agent, discovery_commander, skeptic_agent, advisor_agent
│   ├── workflows/      → 7 Deterministic workflows: scouts/ (5 regions), eligibility, cost, deadline, ranking, synthesis
│   ├── graph/          → 10-node LangGraph DAG: builder.py, nodes.py, state.py, edges.py
│   ├── tools/          → External integrations: tavily_search, firecrawl_scrape, jina_reader, extractor, document_parser
│   ├── schemas/        → Pydantic models: student, scholarship, scoring, evidence, roadmap, events, session
│   ├── api/routes/     → FastAPI endpoints: discover, stream, profile, scholarships, sessions, exhibition
│   ├── db/             → SQLite session store (aiosqlite + WAL), seed scripts, cache
│   └── utils/          → KeyManager (30 keys), GPA converter, Pakistan costs, date utils
├── frontend/
│   ├── app/            → Next.js 15 App router: page.tsx, mission/[sessionId], dossier/[scholarshipId], catalog/
│   ├── components/     → Command Theatre: theatre/, mission/, intake/, overlays/, ranking/, map/, dossier/
│   └── lib/            → Zustand store.ts, api.ts, simulation-engine.ts, seed-data.ts, sessionStore.ts
├── data/
│   ├── scholarships/   → 310 Deep Dossier JSON seed files across 5 global regions
│   ├── profiles/       → 6 Verified Pakistani demo student profiles
│   ├── pakistan_costs.json → Pakistani PKR benchmarks (visa, flights, attestation, medical)
│   └── pakistan_education.json → BISE grading scales, IBCC Cambridge formulas, degree tiers
├── .context/           → Hierarchical deep-dive context manuals (01 through 08)
└── scripts/            → Diagnostic, context, curation, and slide generation automation
```

---

## 6. How to Work on ScholarX (The 5-Step Agent Loop)

1. **Orient**: Check `.context/CURRENT_TASK.md` to see what is currently in flight. Run `python scripts/context.py status`.
2. **Reference**: Read the relevant subsystem manual in `.context/` (`02_BACKEND_LANGGRAPH.md`, `03_FRONTEND_THEATRE.md`, etc.).
3. **Execute**: Make surgical changes while preserving existing comments, schemas, and invariants.
4. **Verify**: Run fast tests (`.venv/bin/pytest backend/tests/test_schemas.py`) and `python scripts/context.py validate`.
5. **Handover**: Record notes with `python scripts/context.py record "<summary of changes>"` so the next agent has full continuity.
