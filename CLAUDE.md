# CLAUDE.md — ScholarX Guidelines for Claude Code

> **Operational manual for Claude Code & Anthropic AI agents working on ScholarX.**

---

## Commands & Workflows

### Environment & Diagnostics
```bash
# High-density system primer (~1,500 tokens)
python scripts/context.py primer

# Real-time telemetry (DB counts, keys, ports, active task)
python scripts/context.py status

# Full system doctor (48 environment checks)
python scripts/doctor.py

# Self-healing context verification
python scripts/context.py validate
```

### Development Servers
```bash
# Start full stack concurrently (FastAPI port 8000 + Next.js port 3000)
npm run dev
# or
make dev

# Start backend only (FastAPI with reload)
make backend

# Start frontend only (Next.js 15)
make frontend
```

### Testing
```bash
# Fast unit tests (schemas + API keys, ~0.2s)
.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py

# Security remediation test suite
.venv/bin/pytest backend/tests/test_security_audit_remediation.py

# Full test suite
make test
```

---

## Architecture & Code Style Guidelines

### 1. Workflow-First Philosophy (ADR-003)
- **Deterministic Workflows for Math & Logic**: All arithmetic, ranking formulas, eligibility checklists, and deadline runways MUST be written as deterministic Python code in `backend/workflows/`.
- **LLM Agents for Semantics**: Reserve LLM calls (`backend/agents/`) exclusively for unstructured document extraction, conversational counseling, adversarial skeptic challenges, and personalized roadmaps.
- **Zero Hallucination**: Never calculate numbers, costs, or rankings via LLM prompts.

### 2. Localization & Pakistan Benchmarks
- All costs must be calculated and displayed in **Pakistani Rupees (PKR)** using `data/pakistan_costs.json`.
- Pakistan-specific educational credentials (BISE Matric/FSc, Cambridge O/A-Levels, IBCC equivalence, HEC recognized degrees) and testing standards (HEC HAT, USAT) are first-class concepts.

### 3. API Key Management (ADR-005, ADR-006)
- Never call external LLM or search APIs directly.
- Always retrieve rotating keys via `backend.utils.api_keys.get_key_manager()`. All 30 keys rotate on a per-request basis with 60s cooldowns on HTTP 429s.

### 4. Database & Storage (ADR-001)
- The system uses local single-file SQLite (`aiosqlite`) with Write-Ahead Logging (`data/scholarx_sessions.db`).
- Do not add Docker or external PostgreSQL/Redis dependencies for standard local execution.

### 5. Frontend Conventions (ADR-009, ADR-012)
- **Stack**: Next.js 15.1.0 (App Router), React 19, Tailwind CSS, Zustand v5.
- **Theme**: Obsidian dark glassmorphism.
- **Typography Floor**: 6-scale semantic typography. Minimum font size is 10px monospace (`text-[10px] font-mono`). Sub-10px text is strictly prohibited.
- **Controls**: `JudgeControlBar.tsx` is the sole bottom exhibition control surface.

---

## Context Manuals (`.context/`)

Whenever you need specialized context, inspect these files:
- [`.context/00_QUICKSTART.md`](.context/00_QUICKSTART.md) — 60-Second Primer (<1,800 tokens)
- [`.context/01_ARCHITECTURE.md`](.context/01_ARCHITECTURE.md) — System Topology & Dual Execution Modes
- [`.context/02_BACKEND_LANGGRAPH.md`](.context/02_BACKEND_LANGGRAPH.md) — 10-Node LangGraph StateGraph & 4 Agents
- [`.context/03_FRONTEND_THEATRE.md`](.context/03_FRONTEND_THEATRE.md) — Command Theatre, D3-Geo Stage, Zustand Store
- [`.context/04_DATA_SCHEMAS_DB.md`](.context/04_DATA_SCHEMAS_DB.md) — SQLite Tables, 310 Deep Dossiers, Pakistan Benchmarks
- [`.context/05_API_SSE_EVENTS.md`](.context/05_API_SSE_EVENTS.md) — REST Endpoints & 34+ SSE Event Types Catalog
- [`.context/06_DECISIONS_INVARIANTS.md`](.context/06_DECISIONS_INVARIANTS.md) — Consolidated ADRs (001-012) & Invariants
- [`.context/07_DEVELOPER_PLAYBOOK.md`](.context/07_DEVELOPER_PLAYBOOK.md) — Common Developer Recipes & Troubleshooting
- [`.context/08_ACTIVE_STATE.md`](.context/08_ACTIVE_STATE.md) — Verified Features, Current Posture, Technical Debt
- [`.context/CURRENT_TASK.md`](.context/CURRENT_TASK.md) — Active Agent Task Scratchpad
- [`.context/MEMORY.md`](.context/MEMORY.md) — Permanent Session Memory Bank
