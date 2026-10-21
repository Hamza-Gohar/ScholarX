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

## 📚 Hierarchical Context System (`.context/`)

All architecture, subsystem documentation, design decisions, and playbooks are maintained in `.context/`:

```
.context/
├── 00_QUICKSTART.md           → 60-second orientation, golden commands, core invariants
├── 01_ARCHITECTURE.md         → System topology, dual execution modes (LIVE vs DEMO), dataflow
├── 02_BACKEND_LANGGRAPH.md    → 10-node StateGraph, 4 LLM agents, 7 deterministic workflows, 30 keys
├── 03_FRONTEND_THEATRE.md     → Next.js 15, Command Theatre, 1920x1080 stage floor, Zustand store
├── 04_DATA_SCHEMAS_DB.md      → SQLite WAL tables, 310 Deep Dossiers, Pakistan cost benchmarks
├── 05_API_SSE_EVENTS.md       → Complete REST endpoints & 34+ real-time SSE event catalog
├── 06_DECISIONS_INVARIANTS.md → Consolidated ADRs (001-012) & 6 inviolable system invariants
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
- Historical initial blueprint: [`docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md`](docs/archive/ORIGINAL_BLUEPRINT_SEPT2026.md)
- Complete technical architecture: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Delivery status history: [`docs/STATUS.md`](docs/STATUS.md)
- Architectural decision records: [`docs/DECISIONS.md`](docs/DECISIONS.md)
- Known issues register: [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md)
