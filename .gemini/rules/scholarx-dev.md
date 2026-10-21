---
trigger: always
---

# ScholarX Development Rules

## Before Making Changes
1. Check live status: `python scripts/context.py status`
2. Check active scratchpad: `.context/CURRENT_TASK.md`
3. Read relevant subsystem manual in `.context/` (`02_BACKEND_LANGGRAPH.md`, `03_FRONTEND_THEATRE.md`, etc.)
4. Review `.context/06_DECISIONS_INVARIANTS.md` for architectural boundaries

## When Writing Backend Code
1. **Workflow-First (ADR-003)**: Prefer deterministic workflows over LLM agents for rule-based/arithmetic tasks. Zero numeric hallucination.
2. **API Keys**: Never hardcode. Always use `backend.utils.api_keys.get_key_manager()` — 30 keys rotate per-request.
3. **Events**: Emit SSE events via `backend/events/bus.py` with typed `ScholarXEvent` models.
4. **Database**: Use `db.session_store.get_session_store()` — async SQLite with WAL mode (`data/scholarx_sessions.db`).
5. **Schemas**: Use Pydantic v2 models from `backend/schemas/` — never raw dicts.
6. **LLM Calls**: Groq primary with Gemini fallback. Always use `from google import genai` (never `google.generativeai`).
7. **Test-First**: Write unit tests in `backend/tests/test_*.py`.

## When Writing Frontend Code
1. **Architecture**: Next.js 15.1.0 (App Router), React 19, Tailwind CSS, Zustand v5.
2. **Offline Fallbacks**: Every component must handle backend offline states gracefully.
3. **Typography (ADR-012)**: 6-scale semantic typography. Minimum font size is 10px monospace (`text-[10px] font-mono`). Sub-10px fonts are strictly prohibited.
4. **Controls (ADR-009)**: `JudgeControlBar.tsx` is the sole bottom exhibition control surface.
5. **Styling**: Obsidian dark glassmorphism theme (`bg-[#0a0f1a]`, glass borders `border-cyan-500/20`).
6. **SSE**: Use native browser `EventSource` with burst coalescing in `presentation-queue.ts`.

## After Making Changes
1. Run fast unit tests: `.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py -v`
2. Run context validation: `python scripts/context.py validate`
3. Run system doctor: `python scripts/doctor.py`
4. Update `.context/CURRENT_TASK.md` and record changes with `python scripts/context.py record "<summary>"`
