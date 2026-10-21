# ScholarX — System Architecture Reference

> **The Autonomous Scholarship Intelligence Network for Pakistani Students**  
> Living technical reference and authoritative system architecture. For the foundational specification, see [Agents.md](../Agents.md). For current operational and delivery status, see [STATUS.md](STATUS.md).

---

## 1. System Mission & Core Posture

ScholarX is an autonomous multi-agent intelligence platform purpose-built to discover, verify, calculate true costs for, rank, and roadmap international scholarships specifically for Pakistani students.

Unlike generic search engines or LLM wrappers, ScholarX operates on five non-negotiable architectural tenets:
1. **Pakistan-Localized Intelligence**: Encodes Pakistan-specific institutional realities (HEC bilateral quotas, HEC HAT/USAT tests, IBCC 12-year equivalence, MOFA attestation, FBR Section 236Y advance tax on card transactions, and VFS Gerry's appointment backlogs).
2. **Workflow-First Philosophy**: Uses deterministic algorithmic workflows for math, dates, criteria checks, and ranking; LLM agents are restricted to unstructured text parsing, conversational intake, adversarial reasoning, and narrative strategy. Zero LLM hallucination in numeric calculations or ranking order.
3. **Dual Execution Engine (LIVE vs DEMO)**: Operates seamlessly in two distinct execution modes:
   - **LIVE MODE**: Real-time FastAPI SSE stream executing a 10-node LangGraph pipeline, live candidate extraction from multi-provider search APIs, and live SQLite session hydration.
   - **DEMO REPLAY MODE**: Deterministic, zero-cloud-dependency 12-stage exhibition replay engine with 3 Pakistani student presets and presenter keyboard shortcuts.
4. **Adversarial Friction Auditing**: Deploys a dedicated Skeptic Agent to identify upfront airfare gaps, living stipend vs. cost-of-living deficits, visa appointment backlogs, and return-to-home bonds.
5. **Canonical Dossier & Multi-Surface Delivery**: Synthesizes verified intelligence into a unified 10-section Canonical Dossier accessible as an In-Theatre Web Dossier and a publication-grade Print PDF.

---

## 2. High-Level System Topology

```
+--------------------------------------------------------------------------------------------------+
|                                    PRESENTATION LAYER (Next.js 15.1.0)                           |
|                                                                                                  |
|   / (Intake & Briefing)       /mission/[sessionId] (Command Theatre)    /dossier/[scholarshipId]  |
|   - MissionInitScreen         - 1920x1080 Spatial Canvas Floor           - WebDossierView (10-sec) |
|   - 3 Pakistani Presets       - Central Commander Console (6 States)     - Publication Print PDF   |
|   - Recent Missions Drawer    - 5 Regional Scout Beacons (Europe/Asia..) - Catalog Print (/catalog)|
|   - Quick Exhibition Launch   - Quadratic Bezier Data Packet Canvas                                |
|                               - Specialist Investigation Bay & Conduits                            |
|                               - Deterministic Ranking Matrix Stage                                 |
|                               - Collapsible JudgeControlBar [J] & Presenter Hotkeys [Space, D, R]   |
+--------------------------------------------------+-----------------------------------------------+
                                                   | SSE Event Stream (/api/stream?session_id=...)
                                                   | REST API Calls (Proxy Rewrites via next.config)
                                                   v
+--------------------------------------------------------------------------------------------------+
|                                  FASTAPI BACKEND SERVICE (Port 8000)                             |
|                                                                                                  |
|   API Routes:                                                                                    |
|     • /api/discover      -> Triggers 10-Node LangGraph Discovery & Execution Pipeline            |
|     • /api/stream        -> Server-Sent Events (SSE) Stream via EventBus Async Queue             |
|     • /api/profile       -> Student Profile Intake, Validation, and Pakistani Normalization      |
|     • /api/scholarships  -> 310 Deep Dossier Catalog Retrieval, Regional Queries, Detail Lookup  |
|     • /api/sessions      -> SQLite Session History, State Hydration, and Replay Persistence      |
|     • /api/health        -> Health Status & Live Multi-Provider Key Pool Monitor                 |
|     • /api/exhibition    -> Preflight Diagnostics & Rehearsal Verification Suite                 |
|                                                                                                  |
|   Core Infrastructure:                                                                           |
|     • EventBus: Async pub/sub with session-isolated queues & 500-event circular replay buffer     |
|     • KeyManager: Multi-key round-robin rotator (30 keys) with 60s cooldown & failure telemetry   |
+--------------------------------------------------+-----------------------------------------------+
                                                   |
                                                   v
+--------------------------------------------------------------------------------------------------+
|                                LANGGRAPH MULTI-AGENT STATEGRAPH PIPELINE                         |
|                                                                                                  |
|   START -> Orchestrator -> ProfileAnalyzer -> DiscoveryCommander -> EligibilityAnalyzer          |
|                                                                            │                     |
|            AdvisorAgent <- RankingEngine <- SynthesisEngine <- SkepticAgent <- DeadlineAnalyzer   |
|                 │                                                            │                   |
|                END                                                     CostAnalyzer              |
+-----------------------+----------------------------------+-----------------------+---------------+
                        |                                  |                       |
                        v                                  v                       v
+-------------------------------+  +-------------------------------+  +----------------------------+
|   SPECIALIZED AGENTS (LLM)    |  | DETERMINISTIC WORKFLOWS (Code)|  |   DATA LAYER (Local-First) |
|                               |  |                               |  |                            |
| • Orchestrator                |  | • 5 Regional Scouts           |  | • SQLite (WAL Mode)        |
| • Profile Analyst             |  | • Eligibility Investigator    |  |   data/scholarx_sessions.db|
| • Discovery Commander         |  | • True Cost Analyzer (PKR)    |  |   - 6 Normalized Tables    |
| • Skeptic Agent (Adversarial) |  | • Deadline Intelligence       |  |   - Async Batch Queue      |
| • Advisor Agent (Roadmap)     |  | • Synthesis Engine            |  | • 310 Seeded Deep Dossiers |
|                               |  | • Ranking Engine (8 Factors)  |  | • Memory Fallback Mode     |
+-------------------------------+  +-------------------------------+  +----------------------------+
                        |                                  |
                        +-----------------+----------------+
                                          |
                                          v
+--------------------------------------------------------------------------------------------------+
|                                    EXTERNAL CLOUD API POOL                                       |
|                                                                                                  |
|   • Groq API (13 Keys)           -> Model: qwen/qwen3.8-27b (Fast extraction, parsing, debates) |
|   • Google Gemini API (3 Keys)   -> Model: gemini-flash-latest (Complex synthesis & roadmaps)     |
|   • Tavily Search API (7 Keys)   -> Targeted academic & government domain discovery              |
|   • Firecrawl API (6 Keys)       -> Deep JS-rendered portal scraping & markdown conversion        |
|   • Jina Reader API (1 Key)      -> Fast direct-URL markdown reader & fallback extractor          |
+--------------------------------------------------------------------------------------------------+
```

---

## 3. The 10-Node LangGraph StateGraph Pipeline

The core intelligence pipeline is implemented as a compiled LangGraph `StateGraph` in `backend/graph/builder.py`, operating on a centralized `ScholarXState`.

```
START 
  │
  ▼
[ 1. Orchestrator Node ] ───────> Validates session continuity; broadcasts MISSION_INITIATED event.
  │
  ▼
[ 2. Profile Analyzer Node ] ───> Normalizes Pakistani academic marks, Cambridge GCE A-Levels, IELTS/MOI.
  │
  ▼
[ 3. Discovery Commander Node ] ─> Deploys 5 Regional Scouts; queries Tavily/Firecrawl; falls back to cache.
  │
  ▼
[ 4. Eligibility Analyzer Node ] > Executes deterministic 15-dimension Pakistani criteria audit.
  │
  ▼
[ 5. Cost Analyzer Node ] ──────> Computes 4-phase out-of-pocket expenses in PKR (FBR 236Y tax, flights).
  │
  ▼
[ 6. Deadline Analyzer Node ] ──> Evaluates runway, application slack days, and HEC dual-gate lead times.
  │
  ▼
[ 7. Skeptic Agent Node ] ──────> Adversarial cross-examination (Fulbright bond, visa queues, Sperrkonto).
  │
  ▼
[ 8. Synthesis Engine Node ] ───> Aggregates multi-source evidence into unified candidate intelligence cards.
  │
  ▼
[ 9. Ranking Engine Node ] ─────> Calculates deterministic 8-factor composite scores (zero LLM drift).
  │
  ▼
[ 10. Advisor Agent Node ] ─────> Synthesizes personalized 6-phase Pakistani application roadmap & offices.
  │
  ▼
 END
```

### 3.1 Agent vs. Workflow Decision Matrix

| Pipeline Component | Classification | Engine | Rationale |
|:---|:---|:---|:---|
| **Orchestrator** | **Agent** | LLM / State Machine | Evaluates high-level mission constraints, dynamically recovers from phase errors, and issues commander directives. |
| **Profile Analyst** | **Agent** | LLM / Heuristics | Ingests unstructured student inputs (transcripts, certificates, informal notes) and converts them into normalized schemas. |
| **Discovery Commander** | **Agent** | LLM / Templates | Formulates dynamic, contextual search queries tailored to the student's field, degree level, and target destination. |
| **5 Regional Scouts** | **Workflow** | Deterministic Code | Pure pipeline: `Deploy -> Search -> Filter -> Scrape -> Extract -> Complete`. Zero reasoning needed. |
| **Eligibility Investigator** | **Workflow** | Deterministic Code | Evaluates 15 hard/soft dimensions against strict boolean and numerical thresholds without hallucination. |
| **True Cost Analyzer** | **Workflow** | Deterministic Code | Multi-currency conversions, FBR Section 236Y advance tax math, and Pakistani local price lookup tables. |
| **Deadline Intelligence** | **Workflow** | Deterministic Code | Strict date arithmetic: `Slack = (Deadline - Today) - (Required Document Prep Days)`. |
| **Skeptic Agent** | **Agent** | Adversarial LLM + Rules | Challenges claims, spots hidden traps, and conducts structured debate clashes with a rule-based fallback. |
| **Synthesis Engine** | **Workflow** | Deterministic Code | Merges evidence trails, resolves conflicting criteria, and deduplicates candidate data cards. |
| **Ranking Engine** | **Workflow** | Deterministic Math | Exact 8-factor weighted arithmetic formula. No LLM discretion permitted in numeric scoring or rank assignment. |
| **Final Advisor** | **Agent** | LLM + Template Injection | Crafts narrative strategy, chronologically sequences milestones, and assigns physical Pakistani offices. |

### 3.2 State Schema (`ScholarXState`)

Defined in `backend/graph/state.py` using Python `TypedDict` with functional reducers:

```python
class ScholarXState(TypedDict, total=False):
    session_id: str
    student_id: str
    active_phase: str
    student_profile: Optional[StudentProfile]
    raw_documents: List[Dict[str, Any]]
    mission_constraints: List[str]
    candidate_scholarships: Annotated[List[Scholarship], merge_lists]
    eligibility_results: Annotated[Dict[str, Any], merge_dicts]
    cost_results: Annotated[Dict[str, CostAnalysisResult], merge_dicts]
    deadline_results: Annotated[Dict[str, DeadlineAnalysisResult], merge_dicts]
    evidence_trails: Annotated[Dict[str, EvidenceTrail], merge_dicts]
    skeptic_challenges: Annotated[Dict[str, List[SkepticChallenge]], merge_dicts]
    ranked_results: List[CompositeScoreResult]
    final_roadmap: Optional[ApplicationRoadmap]
    events_queue: Annotated[List[ScholarXEvent], merge_lists]
    errors: Annotated[List[str], merge_lists]
    human_approval_required: bool
    human_approved: bool
```

---

## 4. Pakistan-Localized Specialist Intelligence Engine

The core value of ScholarX lies in its domain-specific knowledge models for Pakistani applicants.

### 4.1 15-Dimension Eligibility Investigator

Located in `backend/workflows/eligibility.py`, this module evaluates candidate opportunities against 15 discrete dimensions:

1. **Pakistan Nationality (Hard Gate)**: Verifies applicant citizenship against eligible country lists or bilateral agreements.
2. **Pakistan Bilateral Quota (Bonus)**: Awards bonus points for reserved government quotas (e.g., 400 Stipendium Hungaricum bilateral seats, Chinese CSC Type-A).
3. **Degree Level Match (Hard Gate)**: Ensures match between student's intended level (Bachelor's, Master's, PhD, Postdoc) and program offerings.
4. **Field of Study Match**: Checks academic discipline overlap using fuzzy and exact keyword matching (`is_field_match`).
5. **Prior Education Years**: Evaluates required vs completed years of education (e.g., 12-year Intermediate vs 16-year BS). Recognizes Cambridge GCE A-Levels (13 years benchmark) for direct European university matriculation.
6. **Academic Merit & GPA (Hard Gate)**: Evaluates student's percentage or 4.0-scale CGPA against competitive cutoffs using bidirectional conversion (`gpa_4_to_percentage`).
7. **Age Limits (Hard Gate)**: Validates undergraduate (typically $\le 25$) and postgraduate (typically $\le 35$) age ceilings.
8. **English Language Proficiency & MOI Waiver**: Adjudicates standardized tests (IELTS/TOEFL) vs English Medium of Instruction (MOI) certificate acceptability.
9. **HEC Standardized Tests**: Checks HEC USAT (Undergraduate) or HEC HAT (Postgraduate) registration and score records.
10. **HEC Degree Attestation**: Checks if higher education degrees are e-attested via HEC DAS portal.
11. **IBCC Equivalence Requirement**: Audits whether intermediate/matric certificates or O/A-Levels have IBCC equivalence.
12. **MOFA Attestation Readiness**: Flags requirements for Ministry of Foreign Affairs apostille/attestation stamps.
13. **Funding Tier Alignment**: Validates whether the scholarship is FULL, TUITION_ONLY, or PARTIAL against student's financial profile.
14. **Provincial / Regional Quotas**: Identifies seats reserved for Balochistan, FATA/Merged Districts, AJK, or rural Sindh.
15. **Special Category Eligibility**: Checks for female-specific awards, disability concessions, or public sector university affiliations.

### 4.2 4-Phase True Cost Waterfall (PKR)

Located in `backend/utils/pakistan_costs.py`, this engine computes out-of-pocket expenses across four distinct chronological phases:

$$\text{Total Out-of-Pocket (PKR)} = \text{Phase 1} + \text{Phase 2} + \text{Phase 3} + \text{Phase 4}$$

- **Phase 1: Pre-Application Costs**
  - IELTS Academic Exam Fee (British Council / AEO Pakistan): ~PKR 76,000
  - HEC USAT / HAT Registration Fee: PKR 2,500
  - IBCC Equivalence Certificate: PKR 3,500 – 10,000 (Urgent/Normal)
  - HEC Degree Attestation Fee: PKR 5,000 (per original degree)
  - MOFA Apostille / Attestation Stamp: PKR 1,500
  - Machine Readable Passport Renewal (10-year, 36-page): PKR 4,500 – 9,000
- **Phase 2: Application Stage Costs**
  - University application fees converted via dynamic exchange benchmarks (USD, EUR, GBP, HUF, TRY, CNY).
  - **FBR Section 236Y Advance Tax**: Applies 5% withholding for active tax filers or 10% for non-filers on international card transactions.
  - **Bank Card FX Markup**: Adds 3.5% foreign transaction fee charged by Pakistani commercial banks.
- **Phase 3: Post-Acceptance & Visa Stage Costs**
  - Foreign embassy visa processing fees (e.g., Schengen Type D visa fee).
  - VFS Gerry's biometric handling and courier drop-box fees.
  - IOM TB Screening & Medical Examination (Islamabad, Lahore, Karachi): ~PKR 25,000.
  - Police Character Clearance Certificate: PKR 500 – 1,000.
  - Upfront One-Way Airfare from Pakistan (KHI/LHE/ISB) if not prepaid by sponsor.
- **Phase 4: Initial Settlement Buffer**
  - Security deposit for student dormitory or private accommodation.
  - First-month living expense buffer required before the first government scholarship stipend installment is credited.

### 4.3 Deadline Runway & Slack Intelligence

Located in `backend/workflows/deadline.py` and `backend/utils/date_utils.py`:

$$\text{Slack Days} = \text{Days Until Deadline} - \text{Total Preparation Days Required}$$

Where preparation lead times are calibrated to Pakistani institutional realities:
- HEC Dual-Gate Bilateral Nomination Processing: 21 – 28 days
- IBCC Equivalence Verification: 10 – 17 days
- BISE Board Verification Envelope: 7 – 10 days
- IELTS Preparation & Result Delivery: 14 – 21 days
- MOFA Attestation: 3 – 5 days

**Risk Tiers**:
- `GREEN` ($\text{Slack} \ge 21\text{ days}$): Feasible with standard pacing.
- `AMBER` ($7\text{ days} \le \text{Slack} < 21\text{ days}$): Tight runway; requires urgent fee tracks and parallel attestations.
- `RED` ($0\text{ days} \le \text{Slack} < 7\text{ days}$): High risk of deadline breach.
- `IMPOSSIBLE` ($\text{Slack} < 0\text{ days}$): Preparation time exceeds available calendar days.

### 4.4 Skeptic Agent (Adversarial Audit)

Located in `backend/agents/skeptic_agent.py`:
- Cross-examines scholarship promises against hidden Pakistani friction points:
  - **Return Obligations**: Spots mandatory 2-year physical return bonds (Fulbright J-1 212(e) clause, Australia Awards DFAT bond) restricting post-study work abroad.
  - **Embassy Visa Queues**: Highlights 6–12 month German student visa appointment backlogs at Islamabad and Karachi consulates.
  - **Sperrkonto / Living Deficits**: Calculates gaps between basic monthly stipends and actual rents in major cities (London, Munich, Paris, Tokyo).
  - **HEC Bottlenecks**: Flags dual-portal synchronization risks where failing to submit on HEC's portal voids nomination even if accepted by foreign university.
- **Resilience Fallback**: Includes a complete deterministic rule engine that generates ground-truth evidence trails if external LLM APIs are unreachable.

---

## 5. Deterministic 8-Factor Composite Ranking Engine

Located in `backend/workflows/ranking.py`, the Ranking Engine calculates match scores with mathematical transparency. Zero LLM hallucination is permitted in numerical scoring or rank assignment.

### 5.1 Mathematical Formulation

$$\text{Match Score} = \min\left(100.0, \, \max\left(0.0, \, \sum_{i=1}^{8} (W_i \times S_i) + \text{Bonus}\right)\right)$$

| Factor ($i$) | Weight ($W_i$) | Component | Description |
|:---|:---:|:---|:---|
| $S_1$ | **0.25** | **Eligibility Match** | Score from 15-dimension eligibility check (0–100). |
| $S_2$ | **0.25** | **True Funding Score** | Evaluates tuition, stipend adequacy, airfare, and out-of-pocket PKR requirements. |
| $S_3$ | **0.10** | **Pakistan Bilateral Quota** | 100 for reserved HEC quota seats; 50 for general PK eligibility; 0 otherwise. |
| $S_4$ | **0.10** | **Academic & Field Fit** | Average of normalized student GPA and subject field overlap score. Includes Cambridge rigor adjustment (+6.0). |
| $S_5$ | **0.10** | **Document Readiness** | Baseline 65–80 based on HEC/IBCC attestations, +15 for valid English test. |
| $S_6$ | **0.10** | **Deadline Feasibility** | Normalized score based on calendar slack days and urgency risk tier. |
| $S_7$ | **0.05** | **Verification Confidence** | Evidence verification score (0.0–1.0) derived from source corroboration. |
| $S_8$ | **0.05** | **Competition Factor** | Inverted selectivity: LOW (95), MODERATE (80), HIGH (65), EXTREME (50). |
| $\text{Bonus}$ | **+5.0** | **Cambridge Direct-Entry** | Awarded to A-Levels candidates targeting competitive destinations (UK, DE, NL, US, CA) where 12-year FSc faces Studienkolleg barriers. |

### 5.2 Degree-Calibrated Output Limits

To prevent overwhelming the student, `get_degree_scholarship_limit` caps the final qualified list:
- Bachelor's / Undergraduate: Top 8 ranked opportunities
- Master's / Postgraduate: Top 10 ranked opportunities
- PhD / Doctoral: Top 12 ranked opportunities
- Postdoctoral: Top 15 ranked opportunities

---

## 6. Canonical Dossier & Multi-Surface Delivery

The platform synthesizes verified intelligence into a single **Canonical Dossier** data model consumed across three frontend surfaces:

```
                          Canonical Dossier (10 Verified Sections)
                                             │
             ┌───────────────────────────────┼───────────────────────────────┐
             ▼                               ▼                               ▼
    In-Theatre Modal               Standalone Web Route              Publication Print PDF
    (CommandTheatreClient)         (/dossier/[scholarshipId])        (@media print / A4 Format)
    - In-context slide-over        - Fullscreen editorial view       - Clean pagination & breaks
    - Tabbed deep inspection       - Deep section anchor jump        - High-contrast typography
    - Real-time SSE updates        - Shareable URL routing           - Formal Pakistani headers
```

### 6.1 The 10 Canonical Dossier Sections

1. **Executive Summary & Opportunity Identity**: Official title, host institution, country, flag, region, bilateral quota status, and composite match badge.
2. **Comprehensive Eligibility Audit**: 15-dimension status breakdown (Pass / Action Required / Fail) with specific Pakistani rationale.
3. **4-Phase Out-of-Pocket Cost Waterfall**: Itemized expenses in PKR, covered vs uncovered breakdown, and card withholding tax.
4. **Dynamic Deadline Runway**: Calendar countdown, slack analysis, and document preparation lead-time warnings.
5. **Multi-Source Evidence Trail**: Exact source URLs, official portal links, scraping timestamps, and verification confidence score.
6. **Skeptic Cross-Examination**: Clashes, hidden bond obligations, visa wait-time warnings, and counter-mitigations.
7. **Academic Requirements & Equivalence**: Minimum GPA, IBCC equivalence benchmarks, and Cambridge GCE direct-entry recognition.
8. **Document Preparation Checklist**: Attestation status across BISE, IBCC, HEC, and MOFA portals.
9. **6-Phase Pakistani Application Roadmap**: Chronological step-by-step milestones with exact deadline target dates.
10. **Verified Pakistani Office Directory**: Physical addresses, fee tables, turnaround times, and pro-tips for HEC, IBCC, MOFA, and VFS Gerry's centers across Pakistan.

---

## 7. Database & Persistence Layer

All session data, student profiles, cached scholarship intelligence, and SSE events are persisted in a local SQLite database configured with high-concurrency settings.

- **File Location**: `data/scholarx_sessions.db`
- **Driver**: `aiosqlite`
- **Concurrency & WAL Mode**:
  - `PRAGMA journal_mode=WAL;` (Write-Ahead Logging allows concurrent reads while writing)
  - `PRAGMA synchronous=NORMAL;` (Ensures performance without sacrificing durability)
  - `PRAGMA busy_timeout=60000;` (60-second timeout avoids database locks under burst traffic)
- **Asynchronous Batch Flusher**: Event logs are queued in an in-memory `asyncio.Queue` and committed to `events_log` in batches of 100 under an async write lock.
- **In-Memory Fallback**: If disk write permissions fail, the system transitions to `file:scholarx_mem_db?mode=memory&cache=shared`.

### 7.1 Database Schema (6 Normalized Tables)

```sql
-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    profile_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- 2. Sessions Table
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL,
    mission_params_json TEXT NOT NULL,
    status TEXT NOT NULL,
    total_scanned INTEGER DEFAULT 0,
    total_verified INTEGER DEFAULT 0,
    top_scholarship TEXT,
    top_score REAL,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);

-- 3. Scholarships Cache Table (310 Seeded + Discovered Opportunities)
CREATE TABLE IF NOT EXISTS scholarships_cache (
    scholarship_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT NOT NULL,
    data_json TEXT NOT NULL,
    discovered_at TEXT NOT NULL,
    verified_at TEXT,
    ttl_seconds INTEGER DEFAULT 604800,
    source_urls_json TEXT
);

-- 4. Session Scholarships Junction Table
CREATE TABLE IF NOT EXISTS session_scholarships (
    session_id TEXT NOT NULL,
    scholarship_id TEXT NOT NULL,
    eligibility_json TEXT,
    cost_json TEXT,
    deadline_json TEXT,
    verification_json TEXT,
    skeptic_json TEXT,
    final_score REAL,
    rank INTEGER,
    PRIMARY KEY(session_id, scholarship_id),
    FOREIGN KEY(session_id) REFERENCES sessions(session_id),
    FOREIGN KEY(scholarship_id) REFERENCES scholarships_cache(scholarship_id)
);

-- 5. Events Log Table
CREATE TABLE IF NOT EXISTS events_log (
    event_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    event_type TEXT NOT NULL,
    agent_id TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    severity TEXT DEFAULT 'INFO',
    FOREIGN KEY(session_id) REFERENCES sessions(session_id)
);

-- 6. Search Queries Cache Table
CREATE TABLE IF NOT EXISTS search_queries_cache (
    query_text TEXT PRIMARY KEY,
    region TEXT NOT NULL,
    results_count INTEGER DEFAULT 0,
    last_used TEXT NOT NULL,
    success_rate REAL DEFAULT 1.0
);
```

---

## 8. Event System & Real-Time Streaming Subsystem

ScholarX communicates all pipeline actions through an asynchronous Server-Sent Events (SSE) bus.

### 8.1 Backend Event Pipeline

- **EventBus (`backend/events/bus.py`)**:
  - In-memory async pub/sub with session-isolated `asyncio.Queue` subscribers.
  - Maintains a **500-event circular replay buffer** per session so late-connecting clients immediately receive historical pipeline state.
- **34 Distinct Event Types (`schemas/events.py`)**:
  - Orchestration: `MISSION_INITIATED`, `MISSION_COMPLETE`, `PIPELINE_ERROR`
  - Profile: `PROFILE_INGESTED`, `PROFILE_VALIDATED`, `PROFILE_COMPLETE`
  - Discovery: `SCOUT_DEPLOYED`, `SEARCH_QUERY_EXECUTED`, `PRIMARY_SEARCH_UNAVAILABLE`, `FALLBACK_SEARCH_ACTIVE`, `OPPORTUNITY_DISCOVERED`
  - Eligibility: `ELIGIBILITY_CHECK_STARTED`, `ELIGIBILITY_DIMENSION_EVALUATED`, `ELIGIBILITY_PASSED`, `ELIGIBILITY_FAILED`
  - Cost: `COST_ANALYSIS_STARTED`, `COST_BREAKDOWN_CALCULATED`, `BUDGET_EXCEEDED`
  - Deadline: `DEADLINE_EVALUATED`, `DEADLINE_RISK_HIGH`, `DEADLINE_RISK_LOW`, `DEADLINE_COMPLETE`
  - Verification: `EVIDENCE_COLLECTED`, `SKEPTIC_CHALLENGE_RAISED`, `VERIFICATION_COMPLETE`
  - Ranking & Roadmap: `RANKING_CALCULATED`, `CANDIDATE_EMERGED`, `ROADMAP_GENERATED`
- **SSE Stream Protocol**:
  ```http
  GET /api/stream?session_id=session-123 HTTP/1.1
  Accept: text/event-stream

  event: SCOUT_DEPLOYED
  data: {"region": "Europe", "active_queries_count": 3}

  event: OPPORTUNITY_DISCOVERED
  data: {"scholarship_id": "hungary-stipendium", "name": "Stipendium Hungaricum"}
  ```

### 8.2 Frontend Presentation Queue & Coalescing

In `frontend/lib/presentation/presentationQueue.ts`, incoming SSE events are not dumped directly into React state, which would cause frame drops. Instead:
- Events pass through `eventNormalizer.ts` to map backend schemas to theatre UI models.
- The `masterPresentationQueue` buffers bursts, coalescing rapid events during high-velocity scout sweeps.
- Pacing controls allow users or judges to adjust playback speed ($1\times, 2\times, 5\times, 10\times$).

---

## 9. API Key Rotation & Multi-Provider Resilience

To prevent API rate limits or quota failures during live operations, ScholarX employs a 30-key round-robin rotation pool managed by `backend/utils/api_keys.py`.

### 9.1 Key Allocation Matrix

| Provider | Key Count | Active Model / Scope | Failover Strategy |
|:---|:---:|:---|:---|
| **Google Gemini** | 3 Keys | `gemini-flash-latest` | Per-request round-robin; automatic cooldown on 429/503. |
| **Groq Cloud** | 13 Keys | `qwen/qwen3.8-27b` | Round-robin with individual key health tracking and cooldown. |
| **Tavily Search** | 7 Keys | Academic & scholarship web search | Round-robin; falls back to `VERIFIED_REGISTRY_CACHE` on quota exhaustion. |
| **Firecrawl** | 6 Keys | Deep JS web scraping & markdown | Round-robin; falls back to Jina Reader or pre-seeded deep dossiers. |
| **Jina Reader** | 1 Key | URL to clean markdown reader | Fallback scraping engine for direct official university portals. |
| **Total Pool** | **30 Keys** | — | **Zero single points of failure across all cloud dependencies.** |

### 9.2 Key Health State Machine

Each key is tracked via a `KeyHealth` object:
- **Success**: Increments `total_successes`, resets `failure_count` to 0, marks `is_healthy = True`.
- **Failure**: Records `last_failure_time`, sets `is_healthy = False`, and initiates a 60-second cooldown window.
- **Recovery Check**: After 60 seconds, the key automatically re-enters the active rotation pool for validation.
- **Telemetry**: Key strings are masked in logs (e.g., `AIzaSy...4x9B`) and monitored via `GET /api/health`.

---

## 10. Frontend Spatial Theatre Architecture

The frontend is built on **Next.js 15.1.0** (App Router) and **Tailwind CSS**, rendering an obsidian dark glassmorphism Command Theatre certified for high-impact presentations and 3-meter legibility.

### 10.1 Spatial Coordinate System

The theatre floor is structured on a virtual 1920×1080 coordinate plane:
- **Central Intelligence Director** (`X: 960, Y: 460`): Root Orchestrator console with 6 distinct states (`IDLE`, `THINKING`, `DIRECTING`, `RECEIVING`, `SYNTHESIZING`, `COMPLETE`).
- **5 Continental Scout Beacons**:
  - Europe: `X: 420, Y: 320`
  - Asia: `X: 1380, Y: 360`
  - Americas: `X: 240, Y: 560`
  - MENA: `X: 860, Y: 420`
  - Oceania: `X: 1540, Y: 720`
- **Quadratic Bezier Packet Canvas**: Animates real-time curved data packets between scouts and the Commander across 6 semantic packet types:
  - `COMMAND` (Gold): Directives issued from Commander to scouts.
  - `ACK` (Cyan): Confirmation signals from regional beacons.
  - `QUERY` (Cyan-Violet): Live search queries dispatched to external APIs.
  - `REPORT` (Emerald): Candidate discovery batches returning to central authority.
  - `EVIDENCE` (Purple): Corroborated source citations and portal verifications.
  - `CHALLENGE` (Rose): Adversarial friction points flagged by the Skeptic Agent.

### 10.2 Unified Control Surface (`JudgeControlBar`)

A consolidated control bar (<kbd>J</kbd>) gives evaluators and presenters instant control:
- <kbd>Space</kbd>: Play / Pause execution or demo replay.
- <kbd>R</kbd>: Reset and restart pipeline from Stage 0.
- <kbd>D</kbd>: Toggle between **LIVE STREAM** and **DEMO REPLAY** modes.
- <kbd>J</kbd>: Expand / Collapse the Judge Control Bar.
- <kbd>1 – 9</kbd>: Direct jump to Stages 1 through 9.
- <kbd>0</kbd>: Authoritative reset to standby posture.
- <kbd>?</kbd>: Open presenter shortcut reference sheet.

---

## 11. System Verification & Operating Runbook

### 11.1 Backend Test Suite

Run the full pytest suite (100% passing across 35 test modules):
```bash
PYTHONPATH=backend:.venv/lib/python3.12/site-packages python3 -m pytest backend/tests
```

### 11.2 Exhibition Rehearsal Certification Script

Executes a 10-cycle automated exhibition stress test, testing burst event flows, key rotation, and packet coalescing:
```bash
PYTHONPATH=backend:.venv/lib/python3.12/site-packages python3 scripts/verify_phase9_rehearsal.py
```

### 11.3 Production Frontend Compilation

Verify that the Next.js production build compiles cleanly without type or lint errors:
```bash
cd frontend && npm run build
```

### 11.4 Launching the Platform

```bash
# Terminal 1: FastAPI Backend (Port 8000)
PYTHONPATH=backend:.venv/lib/python3.12/site-packages uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Next.js Frontend (Port 3000)
cd frontend && npm run dev
```

Navigate to `http://localhost:3000` to launch the ScholarX Command Theatre.
