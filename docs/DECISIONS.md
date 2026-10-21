# ScholarX — Architectural Decision Records

> Documents the reasoning behind key technical decisions. Consult before proposing architectural changes.

---

## ADR-001: SQLite over PostgreSQL

**Date**: 2026-08
**Status**: Accepted

**Context**: The original blueprint (`Agents.md` §1.4) specifies PostgreSQL + pgvector, Redis, and ChromaDB running in Docker containers.

**Decision**: Use SQLite (aiosqlite, WAL mode) as the sole database. No Docker containers.

**Reasoning**:
- ScholarX is a **local-first exhibition project** — runs entirely on the developer's machine for judges
- SQLite is zero-config, single-file, sufficient for demo scale (205 scholarships, <100 sessions)
- Docker adds complexity for exhibition setup (judges shouldn't need to run `docker-compose up`)
- WAL mode provides concurrent read/write for the async FastAPI server

**Trade-offs**:
- No vector search (ChromaDB was planned for semantic scholarship matching)
- No pub/sub (Redis was planned for distributed event bus)
- Event bus is in-memory only (session-isolated asyncio.Queue)
- No persistence across server restarts for active events

**Revisit when**: Moving to production deployment or multi-user scenarios.

---

## ADR-002: Groq Primary, Gemini Fallback

**Date**: 2026-08
**Status**: Accepted

**Decision**: Use Groq (qwen/qwen3.8-27b) as the primary LLM, Gemini (gemini-3.7-flash) as fallback.

**Reasoning**:
- Groq has faster inference on free tier and we have 13 API keys for high-throughput round-robin
- Gemini is reliable but has lower free-tier RPM limits (3 keys)
- Both produce structured JSON output compatible with our Pydantic schemas
- Failover is automatic — if Groq rate-limits, Gemini picks up seamlessly

---

## ADR-003: Workflow-First Architecture

**Date**: 2026-08
**Status**: Accepted

**Decision**: 7 of 12 pipeline stages are deterministic workflows, not LLM agents.

**Reasoning**:
- Eligibility checking, cost calculation, deadline math, ranking — these are pure comparison/arithmetic
- Using LLM for deterministic tasks adds: latency, API cost, hallucination risk, non-reproducibility
- Workflows give: higher reliability, faster execution, zero token cost, identical results every run

**The rule**: If a task can be fully specified as if/else logic, arithmetic, or table lookups, it's a workflow. If it needs language understanding, judgment, or creativity, it's an agent.

---

## ADR-004: SSE over WebSocket

**Date**: 2026-09
**Status**: Accepted

**Decision**: Use Server-Sent Events (native EventSource) instead of WebSocket for real-time streaming.

**Reasoning**:
- Data flow is unidirectional: server → client only (telemetry events)
- SSE auto-reconnects on network interruption
- Works transparently through HTTP proxies (Next.js rewrites)
- Simpler implementation — no handshake, no ping/pong
- Native browser API (`EventSource`) — no libraries needed

---

## ADR-005: 27-Key Round-Robin Rotation

**Date**: 2026-08
**Status**: Accepted

**Decision**: Distribute 27 API keys across 5 providers with per-request automatic rotation.

**Reasoning**:
- Free-tier API keys have aggressive rate limits (Groq: 30 req/min per key)
- A single discovery mission makes 50+ LLM calls and 20+ search queries
- Round-robin across 13 Groq keys = effective 390 req/min capacity
- Automatic cooldown + recovery prevents cascading failures
- No single key exhaustion can halt the pipeline

---

## ADR-006: Per-Request Routing (Not Per-Session)

**Date**: 2026-08
**Status**: Accepted

**Decision**: Rotate API keys on every individual request, not per session or per agent.

**Reasoning**:
- Per-session routing would concentrate all requests from a long-running mission on one key
- Per-request ensures maximum distribution and fastest recovery
- Trade-off: Slightly more complex key state tracking, but `APIKeyRotator` handles it cleanly

---

## ADR-007: Single-Page Scroll Architecture (Frontend)

**Date**: 2026-09
**Status**: Accepted

**Decision**: Build the frontend as a single-page with anchor-linked scroll sections instead of multi-page routing.

**Reasoning**:
- Exhibition demo flows linearly: cinematic intro → upload docs → launch mission → explore results → roadmap
- Judges should see the entire system in one continuous scroll experience
- Eliminates page transition latency and navigation complexity
- Cinematic scroll-scrub hero requires continuous scroll context

---

## ADR-008: No Authentication / Multi-Tenancy

**Date**: 2026-08
**Status**: Accepted

**Decision**: No user authentication, no multi-tenancy. Single-user local system.

**Reasoning**:
- Exhibition project — only one user at a time (the demonstrator or judges)
- Sessions are identified by client-generated IDs in localStorage
- Adding auth would add complexity with zero value for the use case

**Revisit when**: Building a production SaaS version.

---

## ADR-009: Unified Exhibition Judge Mode Control Surface

**Date**: 2026-10-03
**Status**: Accepted

**Context**: In Phase 8, `Phase8LiveDirector` was introduced for real-time SSE stream controls. In Phase 9, `JudgeControlBar` was introduced for deterministic exhibition playback, stage scrubbing (0-12), student profiles, and resilience failover demonstrations. Having both rendered created a dual-footer layout that consumed vertical stage space and duplicated playback actions.

**Decision**: Elevate `JudgeControlBar` to be the sole, unified exhibition controller across both `LIVE` and `DEMO` execution modes, and deprecate redundant footer components from the live viewport.

**Reasoning**:
- Single source of exhibition authority: one cohesive control bar at the bottom with high-contrast obsidian glass styling.
- Context-aware UI: In DEMO mode, presents stage scrubber (0-12), start/pause/restart, student profile selector, and resilience scenarios. In LIVE mode, presents SSE connection state, Launch Live Hunt / live computation streaming indicator, and event count.
- In both modes: Authoritative Reset, Web Dossier trigger, Print PDF trigger, and Presenter Keyboard Shortcuts (<kbd>Space</kbd>, <kbd>R</kbd>, <kbd>D</kbd>, <kbd>J</kbd>, <kbd>0-9</kbd>, <kbd>?</kbd>).
- Unobtrusive: Supports collapsing into a minimal status capsule (<kbd>J</kbd>), maximizing theatre immersion.

---

## ADR-010: Executive Brand Header & Deprecation of Developer Phase Buttons

**Date**: 2026-10-03
**Status**: Accepted

**Context**: Early testing phases (Phase 3 through Phase 7) added 5 developer mode buttons (`PHASE 3`, `PHASE 4`, `PHASE 5`, `PHASE 6`, `PHASE 7`) directly into the `ScholarXIdentity` header.

**Decision**: Remove developer phase pills from the primary brand header in production. Retain a clean, high-contrast toggle between `LIVE STREAM` and `DEMO REPLAY`.

**Reasoning**:
- The 10-Second Test & 3-Meter Test: When an evaluator views the application, it must read as an authoritative, finished autonomous intelligence theatre, not an internal test harness.
- Diagnostic stage scrubbing is already accessible via the unified `JudgeControlBar` (stages 0 through 12 encompass all lifecycle phases).

---

## ADR-011: Spatial Stage Priority & Removal of Visual Token Debug Bars

**Date**: 2026-10-03
**Status**: Accepted

**Context**: A static `DesignTokensBar` was pinned to the floor displaying "SEMANTIC TOKENS: ... STAGE COORDINATE SYSTEM // 1920x1080 TARGET".

**Decision**: Remove `DesignTokensBar` from production layout to restore ~40px of vertical spatial canvas to the global map and communication packet arcs.

**Reasoning**:
- Tokens are properly communicated by the visual components themselves through consistent semantic styling.
- Pinned token bars introduce visual clutter and reduce stage immersion.

---

## ADR-012: 6-Scale Semantic Typography & Restrained Exhibition Visual Palette

**Date**: 2026-10-03
**Status**: Accepted

**Context**: Components used ad-hoc font sizes as low as 8px-9px, which became unreadable when viewed from presentation distance (3-meter test).

**Decision**: Standardize all theatre typography on 6 semantic scales:
1. `DISPLAY`: 24-32px (Brand title, modal headers)
2. `LARGE`: 18-20px (Node titles, scholarship names)
3. `MEDIUM`: 14-15px (Section headers, primary directives)
4. `BODY`: 13-14px (Narrative text, descriptions, criteria)
5. `LABEL`: 11-12px mono (Status indicators, badges, factor labels)
6. `MICRO`: 10px mono (Sub-telemetry, node IDs, weights — strict floor)

Sub-10px text is prohibited across all exhibition surfaces.

