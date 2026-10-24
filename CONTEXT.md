# 🌐 ScholarX — Context & Architecture Hub

> **The Central Knowledge Repository for AI Agents and Human Engineers.**  
> *Everything you need to understand, develop, and extend ScholarX with fresh context.*

---

## ⚡ 60-Second Agent Bootstrap

If you are an AI agent landing here with a fresh context window:

1. **Read the Primer**: [`.context/00_QUICKSTART.md`](.context/00_QUICKSTART.md) (Under 2 minutes, <1,800 tokens).
2. **Check Live Telemetry**: Run `python scripts/context.py status`.
3. **Check Active Task**: Inspect [`.context/CURRENT_TASK.md`](.context/CURRENT_TASK.md).

```bash
# Generate prompt-ready concentrated context:
python scripts/context.py primer

# Inspect live database, API keys, and test health:
python scripts/context.py status

# Verify documentation and codebase synchronization:
python scripts/context.py validate
```

---

## 📊 Live System Scale (October 2026)
- **Opportunities**: **510 Deep Dossier scholarships** researched across Europe (161), Asia (131), Americas (105), MENA (73), and Oceania (40).
- **Standalone Explorer**: `scholarships_database_viewer.html` & `scholarships_database.db` (512 opportunities).
- **Backend Architecture**: FastAPI (port 8000), 10-node LangGraph StateGraph, offline typo-resilient field matching (`field_matching.py`).
- **Frontend Architecture**: Next.js 15.1.0 (port 3000), Command Theatre (1920×1080 stage floor), Node 22 built-in `node:sqlite` serverless client.
- **Verification Posture**: ✅ **Phase 10 Locked & Exhibition Verified** (44 test modules in `backend/tests/`).

---

## 📚 Hierarchical Context System (`.context/`)

All architecture, subsystem documentation, design decisions, and playbooks are maintained in `.context/`:

```
.context/
├── 00_QUICKSTART.md           → 60-second orientation, golden commands, core invariants
├── 01_ARCHITECTURE.md         → System topology, dual execution modes (LIVE vs DEMO), dataflow
├── 02_BACKEND_LANGGRAPH.md    → 10-node StateGraph, 4 LLM agents, 7 deterministic workflows, 30 keys
├── 03_FRONTEND_THEATRE.md     → Next.js 15, Command Theatre, 1920x1080 stage floor, Zustand store
├── 04_DATA_SCHEMAS_DB.md      → SQLite WAL tables, 510 Deep Dossiers, Pakistan cost benchmarks
├── 05_API_SSE_EVENTS.md       → Complete REST endpoints & 34+ real-time SSE event catalog
├── 06_DECISIONS_INVARIANTS.md → Consolidated ADRs (001-014) & 7 inviolable system invariants
├── 07_DEVELOPER_PLAYBOOK.md   → Actionable recipes for common dev tasks & debugging
├── 08_ACTIVE_STATE.md         → Living status, verified features, active technical debt
├── CURRENT_TASK.md            → Active agent scratchpad for in-flight work and handovers
└── MEMORY.md                  → Permanent agent memory bank (historical session records)
```

---

## 🛠️ Multi-Agent Auto-Loaders

Depending on your agent framework or IDE, entry points are available:
- **Universal Multi-Agent Standard**: [`AGENTS.md`](AGENTS.md)
- **Anthropic / Claude Code**: [`CLAUDE.md`](CLAUDE.md)
- **Cursor IDE**: [`.cursorrules`](.cursorrules) & [`.cursor/rules/`](.cursor/rules/)
- **Antigravity / Gemini CLI**: [`.gemini/rules/scholarx-context.md`](.gemini/rules/scholarx-context.md)

---

## 🏛️ Foundational Archival Documents
- Comprehensive Architecture Reference: [`README.md`](README.md)
- Historical initial blueprint: [`docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md`](docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md)
- Complete technical architecture: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Delivery status history: [`docs/STATUS.md`](docs/STATUS.md)
- Architectural decision records: [`docs/DECISIONS.md`](docs/DECISIONS.md)
- Known issues register: [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md)
