# 🎭 ScholarX — Frontend Command Theatre Reference

> **Deep-dive manual for Next.js 15, Zustand state, SSE streaming, and Spatial Stage visualization.**

---

## 1. Presentation Architecture Overview

ScholarX's frontend is built with **Next.js 15.1.0** (App Router), **React 19**, **Tailwind CSS**, and **Zustand v5**. It is designed as an immersive, broadcast-quality **Command Theatre** that visualizes multi-agent coordination in real time.

```
frontend/
├── app/
│   ├── page.tsx                    → MissionInitScreen (Intake, 3 presets, mission launch)
│   ├── layout.tsx                  → Root obsidian layout, metadata, fonts
│   ├── globals.css                 → Semantic design tokens, glassmorphism utilities
│   ├── mission/[sessionId]/page.tsx → Fullscreen Command Theatre spatial canvas
│   ├── dossier/[id]/page.tsx       → 10-section Canonical Web Dossier & Print PDF
│   └── catalog/page.tsx            → 310 Deep Dossier scholarship catalog view
├── components/
│   ├── theatre/                    → Core theatre: StageFloor, PacketCanvas, Beacons, JudgeControlBar
│   ├── command/                    → ScholarXCommander central console (6 states)
│   ├── mission/                    → MissionControl, LiveDirector, Stage scrubber
│   ├── intake/                     → IntakeDropzone, ProfileCard, CounselorChat
│   ├── dossier/                    → CanonicalDossierModal, PrintDossierTemplate
│   ├── ranking/                    → DeterministicMatrixView, CompositeScoreCard
│   ├── overlays/                   → SpecialistInvestigationBay, SkepticAuditModal
│   └── ui/                         → Reusable UI buttons, modals, badges
└── lib/
    ├── store.ts                    → Central Zustand state store
    ├── presentation-queue.ts       → SSE burst coalescing & presentation pacing
    ├── simulation-engine.ts        → 12-stage deterministic replay engine (Demo mode)
    ├── api.ts                      → Type-safe API client with Next.js rewrites
    ├── types.ts                    → TypeScript schemas matching backend Pydantic models
    └── sound-fx.ts                 → Tactile audio synthesis for packet delivery
```

---

## 2. Command Theatre Spatial Coordinate System

The theatre renders a fixed **1920×1080 virtual coordinate stage** that scales responsively across any viewport:

```
(0, 0) ──────────────────────────────────────────────────────── (1920, 0)
│                                                                       │
│  [Europe Scout]         [Asia Scout]               [Americas Scout]   │
│  (x: 480, y: 240)       (x: 1280, y: 260)          (x: 220, y: 380)   │
│                                                                       │
│                        [CENTRAL COMMANDER]                            │
│                         (x: 960, y: 520)                              │
│                                                                       │
│  [MENA Scout]                                      [Oceania Scout]    │
│  (x: 820, y: 440)                                  (x: 1540, y: 680)  │
│                                                                       │
│             [SPECIALIST INVESTIGATION & RANKING STAGE]                │
│                         (y: 720 - 980)                                │
│                                                                       │
│  =================== JUDGE CONTROL BAR [J] ==========================  │
(0, 1080) ──────────────────────────────────────────────────── (1920, 1080)
```

### Communication Packet Flight
Inter-agent messages travel along **quadratic Bezier curves** rendered at 60 FPS:
- **Control Point Math**: $P_{\text{control}} = ((x_1 + x_2)/2,\; \min(y_1, y_2) - \text{arcHeight})$
- **Envelopes**: Packets carry semantic payloads (Command, Ack, Query, Report, Evidence, Challenge).

---

## 3. Central Commander Console (6 States)

The central authority beacon transitions through 6 distinct visual states:

1. `IDLE` (Amber/Cyan standby): Waiting for student profile or mission dispatch.
2. `THINKING` (Pulsing violet): Formulating regional search strategy and query generation.
3. `DIRECTING` (Radiant gold): Dispatching regional scout fleet across continental coordinates.
4. `RECEIVING` (Emerald docking): Ingesting candidate dossiers and evidence packets.
5. `SYNTHESIZING` (Cyan matrix): Multi-factor eligibility, cost, and deadline reconciliation.
6. `COMPLETE` (Obsidian gold): Mission resolved, ranking locked, advisor roadmap generated.

---

## 4. Zustand State Store (`frontend/lib/store.ts`)

The single source of truth for the frontend UI:
- **Execution Mode**: `LIVE` (real-time SSE stream from port 8000) vs `DEMO` (deterministic 12-stage replay).
- **Active Session**: `sessionId`, `studentProfile`, `currentStage` (0-12).
- **Candidate Pool**: Raw and deduped scholarships list.
- **Investigation State**: Active specialist nodes, evidence cards, skeptic challenge logs.
- **Ranked Dossiers**: Top candidates with 8-dimension composite score breakdowns.
- **Telemetry Log**: Circular buffer of recent events with color coding and timestamps.

---

## 5. Unified `JudgeControlBar` & Presenter Hotkeys (ADR-009)

The bottom control surface is consolidated into a single collapsible bar (<kbd>J</kbd>):

| Key | Action | Function |
|:---:|:---|:---|
| <kbd>Space</kbd> | Play / Pause | Starts or pauses stage playback in DEMO mode |
| <kbd>R</kbd> | Reset | Restores theatre to initial standby state |
| <kbd>D</kbd> | Toggle Mode | Switches between LIVE STREAM and DEMO REPLAY |
| <kbd>J</kbd> | Collapse Bar | Toggles minimalist capsule vs full control dock |
| <kbd>0</kbd>–<kbd>9</kbd> | Stage Scrub | Jumps directly to stage 0 through 9 |
| <kbd>?</kbd> | Help | Toggles hotkey reference overlay |

---

## 6. Visual Theme & 6-Scale Semantic Typography (ADR-012)

- **Obsidian Palette**: Surface `bg-[#0a0f1a]`, glass borders `border-cyan-500/20`, cards `bg-slate-900/80 backdrop-blur-md`.
- **Semantic Colors**:
  - `Gold (#f59e0b)`: Central Commander directives, bilateral government quotas.
  - `Cyan (#06b6d4)`: Scout discovery queries, live SSE event streams.
  - `Emerald (#10b981)`: Verified eligibility, fully funded status.
  - `Amber (#f59e0b)`: Deadlines, warning runways, administrative lead times.
  - `Rose (#f43f5e)`: Skeptic agent adversarial challenges, hidden costs.
  - `Purple (#a855f7)`: Composite ranking engine scores.
- **Strict Typography Floor**: Minimum 10px monospace (`text-[10px] font-mono`) for sub-telemetry. Never use sub-10px fonts.
