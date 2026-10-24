# 🤖 ScholarX — Universal AI Agent Handbook

> **Universal entry point for all autonomous AI agents (Devin, Claude Code, Antigravity, Cursor, Codex, GPT-4).**  
> *Notice: The historical September 2 specification is archived at [docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md](docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md).*

---

## 1. Welcome to ScholarX

ScholarX is a production-grade, local-first autonomous intelligence platform designed to discover, verify, calculate out-of-pocket costs (in PKR), rank, and roadmap international scholarships exclusively for **Pakistani students**.

### Key System Metrics
- **Intelligence Scale**: **510 Deep Dossier scholarships** researched across Europe (161), Asia (131), Americas (105), MENA (73), and Oceania (40). Standalone database in `scholarships_database.db` (512 records).
- **Architecture**: 10-node LangGraph StateGraph backend (FastAPI, Python 3.12) + Command Theatre frontend (Next.js 15.1.0, React 19) + Node 22 built-in `node:sqlite` serverless client.
- **Storage**: Local SQLite with WAL mode (`data/scholarx_sessions.db`). Zero external Docker requirement (ADR-001). Portable to Vercel/serverless (`databaseBundle.ts`).
- **API Rotator**: 30 keys (13 Groq, 3 Gemini, 7 Tavily, 6 Firecrawl, 1 Jina) rotating per-request (ADR-005, ADR-006).
- **Delivery Posture**: ✅ **Phase 10 Locked & Exhibition Verified** (44 test modules, 135+ tests passing).

---

## 2. Inviolable Invariants (DO NOT VIOLATE)

1. **Workflow-First Philosophy (ADR-003)**:
   - Arithmetic, scoring formulas, calendar math, eligibility rules, and rankings MUST run via deterministic Python code workflows.
   - LLMs are strictly reserved for unstructured text parsing, conversational counseling, adversarial skeptic audits, and narrative roadmaps.
   - **Zero LLM hallucination in numeric calculations or rankings.**
2. **Pakistan-Specific Localization**:
   - All costs must be computed in **PKR**.
   - Pakistani education boards (BISE, Cambridge O/A-Levels, IBCC 12-year equivalence, HEC recognized degrees) and tests (HEC HAT, USAT, NTS GAT) are first-class primitives.
3. **Local-First & Offline Resilient (ADR-001, ADR-013, ADR-014)**:
   - SQLite WAL is the sole production database. Do not add required Docker services.
   - Querying and field matching must work 100% offline, handling typos and misspellings deterministically via `field_matching.py`.
4. **Key Management Protocol (ADR-005, ADR-006)**:
   - Never call LLM or search APIs directly. Always use `backend.utils.api_keys.get_key_manager()`.
5. **Modern SDK Usage (ISS-006)**:
   - For Gemini calls, always use `from google import genai` and `genai.Client(api_key=key)`. Never use `google.generativeai`.
6. **Presentation Standards (ADR-009, ADR-012)**:
   - Obsidian dark glassmorphism theme with 6-scale semantic typography. Minimum 10px mono floor (`text-[10px] font-mono`). Sub-10px text is strictly prohibited.

---

## 3. Quick-Start Commands

```bash
# Check live status (DB, keys, ports, tests)
python scripts/context.py status

# Dump concentrated 1,500 token system primer
python scripts/context.py primer

# Run system doctor (48 environment checks)
python scripts/doctor.py

# Run full development stack (FastAPI 8000 + Next.js 3000)
npm run dev
# or
make dev

# Run fast unit tests (0.2s)
.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py

# Validate context & documentation synchronization
python scripts/context.py validate
```

---

## 4. Hierarchical Context Directory (`.context/`)

Whenever you need deep context on a subsystem, consult the specialized manual:

| Manual | File Path | Focus Area |
|:---|:---|:---|
| **00. Quickstart** | [`.context/00_QUICKSTART.md`](.context/00_QUICKSTART.md) | 60-second orientation (<1,800 tokens) |
| **01. Architecture** | [`.context/01_ARCHITECTURE.md`](.context/01_ARCHITECTURE.md) | System topology, dual execution modes, end-to-end dataflow |
| **02. Backend Graph** | [`.context/02_BACKEND_LANGGRAPH.md`](.context/02_BACKEND_LANGGRAPH.md) | 10-node DAG, 4 agents, 7 workflows, 5 regional scouts |
| **03. Frontend Theatre**| [`.context/03_FRONTEND_THEATRE.md`](.context/03_FRONTEND_THEATRE.md) | Next.js 15, Command Theatre, Zustand store, SSE client |
| **04. Data & Schemas** | [`.context/04_DATA_SCHEMAS_DB.md`](.context/04_DATA_SCHEMAS_DB.md) | SQLite schema, 510 Deep Dossiers, Pakistan cost benchmarks |
| **05. API & Events** | [`.context/05_API_SSE_EVENTS.md`](.context/05_API_SSE_EVENTS.md) | FastAPI routes & 34+ distinct real-time SSE event types |
| **06. Decisions & Rules**| [`.context/06_DECISIONS_INVARIANTS.md`](.context/06_DECISIONS_INVARIANTS.md) | Consolidated ADRs (001-014) & non-negotiable rules |
| **07. Dev Playbook** | [`.context/07_DEVELOPER_PLAYBOOK.md`](.context/07_DEVELOPER_PLAYBOOK.md) | Step-by-step recipes: add agent, add test, add route |
| **08. Active State** | [`.context/08_ACTIVE_STATE.md`](.context/08_ACTIVE_STATE.md) | Living status, verified features, active technical debt |
| **Current Task** | [`.context/CURRENT_TASK.md`](.context/CURRENT_TASK.md) | Active scratchpad for in-flight work and handovers |
| **Memory Bank** | [`.context/MEMORY.md`](.context/MEMORY.md) | Permanent chronological log of session achievements |

---

## 5. Agent Protocol for Incoming Tasks

1. **Check Active Task**: Read `.context/CURRENT_TASK.md` to understand what was done and what remains.
2. **Inspect Subsystem**: Use `python scripts/context.py inspect <topic>` (e.g. `backend`, `frontend`, `db`) for targeted context.
3. **Execute Incrementally**: Make clean changes respecting invariants and preserving existing docstrings and comments.
4. **Verify**: Run fast tests (`.venv/bin/pytest backend/tests/test_schemas.py`) and context validator (`python scripts/context.py validate`).
5. **Record Handover**: Run `python scripts/context.py record "<description of completed work>"` and update `.context/CURRENT_TASK.md`.
