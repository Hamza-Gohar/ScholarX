# 🏛️ ScholarX — System Architecture Reference

> **The Autonomous Scholarship Intelligence Network for Pakistani Students**  
> *Authoritative architectural specification for AI agents and human engineers.*

---

## 1. Dual Execution Topology (LIVE vs DEMO)

ScholarX is architected with a dual-execution engine that operates in two primary modes:

```
+───────────────────────────────────────────────────────────────────────────────────────────+
│                                  SCHOLARX OPERATIONAL MODES                               │
+─────────────────────────────────────────────┬─────────────────────────────────────────────+
│                LIVE STREAM MODE             │               DEMO REPLAY MODE              │
├─────────────────────────────────────────────┼─────────────────────────────────────────────┤
│ • Full 10-Node LangGraph execution          │ • 100% deterministic 12-stage event replay  │
│ • Live multi-provider API calls (30 keys)   │ • Zero cloud/network dependency             │
│ • Real-time SSE streaming via EventBus      │ • 3 Pakistani demo student profiles         │
│ • Dynamic discovery + SQLite hydration      │ • Stage scrubbing (0-12) & presenter hotkeys│
│ • Full candidate pool extraction & ranking  │ • Partial fleet fault failover simulation   │
+─────────────────────────────────────────────┴─────────────────────────────────────────────+
```

---

## 2. End-to-End System Topology

```
+───────────────────────────────────────────────────────────────────────────────────────────+
│                            PRESENTATION LAYER: NEXT.JS 15.1.0                             │
│                                                                                           │
│  / (Intake & Briefing)       /mission/[sessionId] (Command Theatre)   /dossier/[id]       │
│  - 3 Pakistani presets       - 1920×1080 Spatial Map Floor            - 10-sec Web Dossier│
│  - Document dropzone         - Central Commander Console (6 states)   - Print PDF Engine  │
│  - Fast launch bar           - 5 Regional Scout Beacons (Europe..)    - Catalog view      │
│                              - Quadratic Bezier Data Packet Canvas                        │
│                              - Specialist Investigation Bay & Nodes                       │
│                              - Deterministic 8-Factor Ranking Matrix                      │
│                              - Collapsible JudgeControlBar [J] & Presenter Hotkeys        │
+──────────────────────────────────────────────┬────────────────────────────────────────────+
                                               │ SSE Stream (/api/stream/{sessionId})
                                               │ REST API (/api/discover, /api/profile..)
                                               ▼
+───────────────────────────────────────────────────────────────────────────────────────────+
│                               FASTAPI BACKEND SERVICE (PORT 8000)                         │
│                                                                                           │
│  Endpoints:                                                                               │
│    • POST /api/discover         -> Triggers async 10-node LangGraph pipeline              │
│    • GET  /api/stream/{session} -> Real-time Server-Sent Events (SSE) via EventBus        │
│    • POST /api/profile/upload   -> Student document intake & validation                   │
│    • POST /api/profile/chat     -> Conversational counselor interaction                   │
│    • GET  /api/scholarships     -> 310 Deep Dossier catalog retrieval & queries           │
│    • GET  /api/sessions         -> SQLite session history & replay hydration              │
│    • GET  /api/health           -> System health & 30-key provider pool monitor           │
│    • GET  /api/exhibition/preflight -> 12-stage test rehearsal & preflight check           │
│                                                                                           │
│  Core Infrastructure:                                                                     │
│    • EventBus: Session-isolated async queues with 500-event circular replay buffer        │
│    • KeyManager: 30-key round-robin rotator with 60s cooldown & health metrics            │
+──────────────────────────────────────────────┬────────────────────────────────────────────+
                                               │
                                               ▼
+───────────────────────────────────────────────────────────────────────────────────────────+
│                         LANGGRAPH 10-NODE STATEGRAPH PIPELINE                             │
│                                                                                           │
│  START                                                                                    │
│    │                                                                                      │
│    ▼                                                                                      │
│  [1. ProfileAnalyzer]      -> Parses documents, builds StudentProfile & GPA conversion    │
│    │                                                                                      │
│    ▼                                                                                      │
│  [2. DiscoveryCommander]   -> Generates search strategy, deploys 5 regional scouts        │
│    │                                                                                      │
│    ▼                                                                                      │
│  [3. 5 Regional Scouts]    -> Europe, Asia, Americas, MENA, Oceania search/scrape         │
│    │                                                                                      │
│    ▼                                                                                      │
│  [4. EligibilityAnalyzer]  -> 15-dimension deterministic eligibility comparison           │
│    │                                                                                      │
│    ▼                                                                                      │
│  [5. TrueCostAnalyzer]     -> 4-phase out-of-pocket PKR calculation (visa, flights..)     │
│    │                                                                                      │
│    ▼                                                                                      │
│  [6. DeadlineAnalyzer]     -> Risk-tiered deadline runway & Pakistani prep bottlenecks    │
│    │                                                                                      │
│    ▼                                                                                      │
│  [7. SkepticAgent]         -> Adversarial Pakistani friction audit (return bonds, etc.)   │
│    │                                                                                      │
│    ▼                                                                                      │
│  [8. SynthesisEngine]      -> Reconciles signals into verified DNA cards                  │
│    │                                                                                      │
│    ▼                                                                                      │
│  [9. RankingEngine]        -> 8-factor composite arithmetic scoring formula (0-100)       │
│    │                                                                                      │
│    ▼                                                                                      │
│  [10. AdvisorAgent]        -> 6-phase journey roadmap + Pakistani Office Directory        │
│    │                                                                                      │
│   END                                                                                     │
+───────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 3. Workflow-First Philosophy (The Architectural Split)

ScholarX strictly enforces a division between **Deterministic Code Workflows** and **Stochastic LLM Agents**:

| Pipeline Stage | Implementation | Rationale | Zero Hallucination Guarantee |
|:---|:---|:---|:---:|
| **Profile Parsing** | LLM Agent + Heuristics | Complex unstructured CV/Transcript text extraction | ❌ (Constrained by Pydantic) |
| **Search Strategy** | LLM Agent | Dynamic query generation based on student profile | ❌ (LLM Creativity) |
| **Regional Scouts** | Deterministic Workflow | Strict 6-stage search→scrape→extract pipeline | ✅ 100% Deterministic |
| **Eligibility Audit** | Deterministic Workflow | 15-dimension exact comparison (GPA, age, degree) | ✅ 100% Deterministic |
| **True Cost (PKR)** | Deterministic Workflow | Table lookups & arithmetic math from benchmarks | ✅ 100% Deterministic |
| **Deadline Runway** | Deterministic Workflow | Calendar date calculations & bottleneck buffers | ✅ 100% Deterministic |
| **Skeptic Challenge** | LLM Agent + Rules | Adversarial reasoning & bureaucratic edge cases | ❌ (LLM Reasoning) |
| **Signal Synthesis** | Deterministic Workflow | Data merging, reconciliation, card packaging | ✅ 100% Deterministic |
| **Ranking Engine** | Deterministic Workflow | Exact weighted arithmetic formula | ✅ 100% Deterministic |
| **Advisor Roadmap** | LLM Agent + Directory | Narrative milestone generation & office routing | ❌ (LLM Guidance) |

---

## 4. Key Subsystem Boundaries

1. **State Persistence**: SQLite (`data/scholarx_sessions.db`) using WAL mode. The database manages students, sessions, scholarship caches, session results, and event logs.
2. **Key Rotation Pool**: `backend/utils/api_keys.py` manages 30 keys across 5 services. Rotation occurs on every single HTTP/API request.
3. **Event Streaming**: `backend/events/bus.py` provides pub/sub with async queues per session. The frontend hooks into this via native SSE (`/api/stream/{sessionId}`) with client-side burst coalescing.
4. **Spatial Stage**: The Next.js frontend uses D3-geo projection onto an SVG canvas of 1920×1080 virtual resolution, mapping scouts geographically and drawing quadratic Bezier curves for inter-agent communication packets.
