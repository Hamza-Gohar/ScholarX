# 🌍 ScholarX — The Autonomous Scholarship Intelligence Network for Pakistani Students

> **An autonomous multi-agent system that discovers, verifies, ranks, and explains fully funded educational opportunities specifically for Pakistani students — in real time, with full transparency, running entirely on your local machine.**

---

## Table of Contents

- [1. Project Vision & Refinement](#1-project-vision--refinement)
- [2. System Architecture](#2-system-architecture)
- [3. Workflow-First Philosophy](#3-workflow-first-philosophy)
- [4. Agent & Workflow Definitions](#4-agent--workflow-definitions)
- [5. Session History & Research Persistence](#5-session-history--research-persistence)
- [6. Event System & Inter-Agent Communication](#6-event-system--inter-agent-communication)
- [7. Tech Stack](#7-tech-stack)
- [8. Frontend Visualization Architecture](#8-frontend-visualization-architecture)
- [9. Data Sources & APIs](#9-data-sources--apis)
- [10. Project Phases](#10-project-phases)
- [11. Tools & Services Required](#11-tools--services-required)
- [12. Preparation Checklist](#12-preparation-checklist)
- [13. Demo Flow — The Exhibition Experience](#13-demo-flow--the-exhibition-experience)
- [14. Scoring Model](#14-scoring-model)
- [15. Risk Mitigation & Resilience](#15-risk-mitigation--resilience)
- [16. Cost Estimation & Budget](#16-cost-estimation--budget)

---

## 1. Project Vision & Refinement

### 1.1 The Problem (Pakistan-Specific)

Every year, thousands of fully funded scholarships go unclaimed by Pakistani students because:
- Students don't know about bilateral government quotas (400+ Hungarian seats, 200+ Chinese CSC seats, Turkiye Burslari, etc.)
- Eligibility criteria are buried across HEC portal, foreign embassy websites, and university portals in different languages
- "Fully funded" rarely means zero out-of-pocket — hidden fees (IELTS/TOEFL registration PKR 75,600-76,240, visa fees, medical exams, HEC attestation, proof of funds) surprise applicants
- Pakistan-specific requirements (HEC HAT/USAT, IBCC equivalence, MOFA attestation) are not understood by generic scholarship engines
- There is no single system that discovers, verifies, matches, AND prepares a Pakistani student to apply

### 1.2 What ScholarX Does

ScholarX is not a search engine. It is an **autonomous intelligence network** optimized exclusively for **Pakistani students** — a team of specialized AI agents and deterministic workflows that:

| Capability | Traditional Tools | ScholarX |
|:---|:---|:---|
| **Discovery** | Manual Google searches | Regional scout agents scan 6 continents, Pakistan-aware |
| **Matching** | Generic filters | Deep eligibility analysis with Pakistan-specific criteria (HEC HAT, IBCC, MOFA) |
| **Verification** | Trust the first result | Multi-source cross-checking with skeptic challenge |
| **Cost Analysis** | "Fully funded" label | True out-of-pocket in PKR — visa, IELTS, attestation, flight, deposit |
| **Document Prep** | Manual checklist | AI document readiness with Pakistani document requirements (HEC attestation, IBCC, FRC) |
| **Timeline** | Static deadline lists | Dynamic risk-aware deadline intelligence with Pakistani prep timelines |
| **Transparency** | Black-box recommendations | Full evidence trail — every conclusion is traceable to sources |
| **Memory** | Start from scratch each time | Session history — learns from previous hunts, remembers research |

### 1.3 The Core Differentiator

> **ScholarX doesn't merely search. It investigates.**
> **ScholarX doesn't merely recommend. It verifies.**
> **ScholarX doesn't merely match a scholarship. It analyzes whether a Pakistani student can realistically apply.**
> **ScholarX doesn't merely give information. It creates an action plan calibrated to Pakistan's timelines and costs.**
> **ScholarX remembers. Every hunt makes the next one smarter.**

### 1.4 Deployment Model

ScholarX runs **entirely locally** on the developer's machine:
- Frontend: `localhost:3000` (Next.js dev server)
- Backend: `localhost:8000` (FastAPI / Uvicorn)
- Database: `localhost:5432` (PostgreSQL via Docker)
- Cache/Events: `localhost:6379` (Redis via Docker)
- Embeddings: `localhost:8100` (ChromaDB via Docker)

Only the following services are cloud-hosted:
- LLM APIs (Gemini, Groq)
- Search/Scraping APIs (Tavily, Firecrawl, Jina)

No deployment to Vercel, Railway, or any cloud hosting. This is a local-first exhibition project.

### 1.5 Exhibition Impact Statement

The judges will not see `User -> AI -> Answer`.

They will see:

```
Pakistani Student Profile -> Document Parsing (handling messy/incomplete docs) ->
Global Deployment -> Pakistan-Aware Intelligence Collection ->
Eligibility Filtering (HEC/IBCC/MOFA-aware) -> Productive Disagreement ->
Multi-Source Verification -> PKR Cost Deconstruction -> Deadline Risk Assessment ->
Weighted Synthesis -> Evidence-Backed Ranking -> Personalized Action Plan ->
Human Approval -> Session Saved for Future Reference
```

Every step is visible. Every agent is a living node. Every conclusion has an evidence trail.
And the next time the student returns, ScholarX **remembers everything**.

---

## 2. System Architecture

### 2.1 High-Level Architecture (Local Deployment)

```
                              +---------------------+
                              |     NEXT.JS UI       |
                              |   localhost:3000      |
                              +----------+-----------+
                                         | SSE Stream + REST
                                         v
                              +---------------------+
                              |   FASTAPI BACKEND    |
                              |   localhost:8000      |
                              +----------+-----------+
                                         |
                              +----------v----------+
                              |    LANGGRAPH         |
                              |  ORCHESTRATION       |
                              |     ENGINE           |
                              +----------+-----------+
                                         |
              +--------------------------+---------------------------+
              v                          v                           v
     +----------------+       +----------------+         +----------------+
     | AGENT/WORKFLOW |       |  TOOL LAYER    |         |  DATA LAYER    |
     |   CLUSTER      |       |  (Cloud APIs)  |         |  (Local)       |
     |                |       |                |         |                |
     | Profile Agent  |       | Tavily Search  |         | PostgreSQL     |
     | Scout Workflows|       | Firecrawl      |         | + pgvector     |
     | Eligibility WF |       | Jina Reader    |         | (localhost)    |
     | Document Agent |       | Crawl4AI       |         |                |
     | Cost Workflow  |       | PyMuPDF4LLM    |         | ChromaDB       |
     | Deadline WF    |       | pdfplumber     |         | (localhost)    |
     | Verification   |       | Docling        |         |                |
     | Skeptic Agent  |       | Gemini API     |         | Redis          |
     | Synthesis WF   |       | Groq API       |         | (localhost)    |
     | Ranker WF      |       |                |         |                |
     | Advisor Agent  |       |                |         | SQLite         |
     +----------------+       +----------------+         | (Session Store)|
                                                         +----------------+
```

### 2.2 Agent Network Topology

```
                         +---------------------+
                         |  ORCHESTRATOR        |
                         |  (Commander Agent)   |
                         +---------+-----------+
                                   |
                 +-----------------+------------------+
                 v                 v                   v
        +--------------+  +--------------+   +--------------+
        | PROFILE      |  | DISCOVERY    |   | DOCUMENT     |
        | ANALYST      |  | COMMANDER    |   | ANALYST      |
        | (Agent)      |  | (Agent)      |   | (Agent)      |
        +------+-------+  +------+-------+   +------+-------+
               |                 |                   |
               v          +------+------+------+     v
        Student Profile   v      v      v      v   Doc Readiness
                       EUROPE  ASIA  AMERICAS  MENA
                       SCOUT   SCOUT  SCOUT   SCOUT
                       (WF)    (WF)   (WF)    (WF)
                         |      |      |       |
                         +------+------+-------+
                                v
                      +-----------------+
                      | ELIGIBILITY     |
                      | INVESTIGATOR    |
                      | (Workflow)      |
                      +--------+--------+
                               v
                      +-----------------+
                      | TRUE COST       |
                      | ANALYZER (WF)   |
                      +--------+--------+
                               v
                      +-----------------+
                      | DEADLINE        |
                      | INTELLIGENCE    |
                      | (Workflow)      |
                      +--------+--------+
                               v
                      +-----------------+
                      | VERIFICATION    |
                      | AGENT           |
                      +--------+--------+
                               v
                      +-----------------+
                      | SKEPTIC AGENT   |
                      +--------+--------+
                               v
                      +-----------------+
                      | SYNTHESIS       |
                      | (Workflow)      |
                      +--------+--------+
                               v
                      +-----------------+
                      | RANKING ENGINE  |
                      | (Workflow)      |
                      +--------+--------+
                               v
                      +-----------------+
                      | FINAL ADVISOR   |
                      | (Agent)         |
                      +--------+--------+
                               v
                      +-----------------+
                      | HUMAN APPROVAL  |
                      +--------+--------+
                               v
                      +-----------------+
                      | SESSION SAVED   |
                      | (Persistence)   |
                      +-----------------+
```

### 2.3 Agent vs Workflow Decision Matrix

```
+---------------------------+----------+-----------+----------------------------------+
| Component                 | Type     | Why       | Notes                            |
+---------------------------+----------+-----------+----------------------------------+
| Orchestrator              | Agent    | Needs LLM | Dynamic routing, error recovery  |
| Profile Analyst           | Agent    | Needs LLM | Messy docs, user interaction     |
| Discovery Commander       | Agent    | Needs LLM | Dynamic query generation         |
| Regional Scouts           | Workflow | Determin. | search -> scrape -> extract      |
| Eligibility Investigator  | Workflow | Determin. | 15 criteria checks, no ambiguity |
| Document Analyst          | Agent    | Needs LLM | Quality assessment, gap analysis |
| True Cost Analyzer        | Workflow | Determin. | Lookup tables + arithmetic       |
| Deadline Intelligence     | Workflow | Determin. | Date math + risk formula         |
| Verification Agent        | Agent    | Needs LLM | Source evaluation, judgment      |
| Skeptic Agent             | Agent    | Needs LLM | Adversarial reasoning            |
| Synthesis                 | Workflow | Determin. | Aggregation + conflict rules     |
| Ranking Engine            | Workflow | Determin. | Weighted formula, no ambiguity   |
| Final Advisor             | Agent    | Needs LLM | Narrative generation, strategy   |
+---------------------------+----------+-----------+----------------------------------+
```

---

## 3. Workflow-First Philosophy

### 3.1 Core Principle

> **Workflow is always better than agent when the task is deterministic.**

Workflows provide:
- **Higher reliability** — no LLM hallucination in deterministic steps
- **Higher speed** — no LLM round-trip latency for arithmetic/lookups
- **Deterministic flow** — same input always produces same output
- **Lower cost** — no API tokens spent on things code can do

### 3.2 When to Use an Agent vs Workflow

| Use an **Agent** (LLM-powered) when: | Use a **Workflow** (deterministic code) when: |
|:---|:---|
| Task requires natural language understanding | Task is a fixed sequence of steps |
| Output format varies based on context | Output is always the same structure |
| Judgment, reasoning, or creativity is needed | Logic is pure arithmetic, lookup, or comparison |
| User interaction might be needed | No user interaction needed |
| Error recovery requires dynamic decisions | Errors are handled with simple retry/fallback |

### 3.3 In ScholarX

- **Agents (5):** Orchestrator, Profile Analyst, Document Analyst, Verification, Skeptic, Final Advisor
- **Workflows (7):** Regional Scouts, Eligibility Check, Cost Analysis, Deadline Calculation, Synthesis, Ranking, Discovery aggregation

The Discovery Commander is an agent because it dynamically generates search queries based on the student's profile. But each Regional Scout is a workflow because it follows a deterministic pipeline: `search -> scrape -> extract -> normalize -> return`.

---

## 4. Agent & Workflow Definitions

### Agent 1: Orchestrator (Commander Agent)

**Type:** Agent (LLM-powered)

**Role:** Central brain of ScholarX. Manages the entire pipeline, delegates tasks, handles errors, re-routes on failures, and maintains global state.

**Behavior:**
- Receives the student profile and initiates the mission
- Spawns and coordinates all downstream agents and workflows
- Monitors progress across all pipeline stages
- Handles agent failures with fallback strategies (including API key rotation)
- Emits high-level phase transition events for the UI
- Manages the global scholarship candidate pool state
- Loads relevant research from previous sessions when available
- Saves all findings to session history on mission completion

**LangGraph Implementation:**
- Acts as the root `StateGraph` that defines the entire execution DAG
- Uses conditional edges to route based on pipeline state
- Implements `interrupt()` for human-in-the-loop approval steps
- Maintains checkpointed state for resilience

**Tools:** None directly — orchestrates other agents via graph edges and handoffs.

**Inputs:** Student profile (structured JSON), user constraints, mission parameters, session_id.
**Outputs:** Mission status events, phase transitions, final aggregated results.

**Events Emitted:**
```
MISSION_INITIATED | PHASE_TRANSITION | AGENT_SPAWNED | AGENT_COMPLETED |
PIPELINE_ERROR | PIPELINE_RECOVERED | MISSION_COMPLETE | SESSION_SAVED |
PREVIOUS_SESSION_LOADED
```

---

### Agent 2: Student Profile Analyst

**Type:** Agent (LLM-powered)

**Role:** Ingests student documents and form inputs, extracts a comprehensive structured profile. Handles incomplete, messy, low-quality, and missing documents gracefully. Can ask the user to upload missing REQUIRED documents while treating others as optional.

**Behavior:**
1. Accepts form-based inputs (name, age, city, education level, field, marks, budget, preferences)
2. Accepts uploaded documents (PDFs) via drag-and-drop
3. Parses each document using tiered parsing strategy
4. Cross-validates extracted data against form inputs
5. **Handles incomplete/messy documents:**
   - If a PDF is corrupted or unreadable: flags it and asks user to re-upload or provide info manually
   - If a document is partially readable: extracts what it can, marks uncertain fields with confidence scores
   - If text is in Urdu or mixed Urdu/English: attempts extraction, flags for user verification
6. **Required vs Optional document logic:**
   - **REQUIRED (will ask user to upload if missing):**
     - Academic transcript / marksheet (at minimum, marks entered in form)
   - **OPTIONAL (will NOT block pipeline if missing):**
     - IELTS/TOEFL certificate (many Pakistani scholarships don't require it)
     - CV/Resume
     - Passport copy
     - Motivation letter draft
     - Recommendation letters
     - Financial documents
     - Any other certificates
   - If an optional document is missing, the system notes it and adjusts downstream analysis accordingly
7. Produces a canonical `StudentProfile` JSON schema
8. Stores the profile in the session database for future reference

**Pakistan-Specific Handling:**
- Understands Pakistani education system: Matric (SSC), Intermediate (HSSC/ICS/FSc/FA), Bachelor's (BS/BE/BBA), Master's (MS/MSc/MBA)
- Converts Pakistani percentage marks to GPA 4.0 scale and UK classification
- Understands Pakistani board/university names and grading systems
- Knows about HEC attestation, IBCC equivalence, MOFA apostille requirements
- Recognizes Pakistani CNIC format and passport patterns
- Understands HEC HAT/USAT requirements for bilateral scholarships

**Tools:**
| Tool | Purpose |
|:---|:---|
| `PyMuPDF4LLM` | Fast extraction from CVs and simple PDFs |
| `pdfplumber` | Table extraction from academic transcripts (course-by-course grades) |
| `Docling` | Complex multi-column institutional documents |
| `Gemini 3.7 Flash` | Structured extraction from messy/ambiguous documents |

**Document Handling Flow:**
```
Document Uploaded
       |
       v
  Is it readable?
   /         \
  YES         NO
   |           |
   v           v
 Parse it    Ask user to
   |         re-upload or
   v         enter manually
 Extract fields
   |
   v
 Confidence check
   /         \
 HIGH        LOW
  |           |
  v           v
Accept     Flag for user
           verification
```

**Output Schema (Pakistan-Optimized):**
```json
{
  "student_id": "uuid",
  "session_id": "uuid",
  "personal": {
    "name": "string",
    "nationality": "PK",
    "country_of_residence": "PK",
    "city": "Lahore",
    "province": "Punjab",
    "age": 19,
    "date_of_birth": "2007-03-15",
    "gender": "Male",
    "cnic": "35201-XXXXXXX-X",
    "passport_number": "XX-XXXXXXX",
    "passport_valid_until": "2032-01-01"
  },
  "academic": {
    "current_level": "Intermediate / ICS",
    "education_system": "Pakistani",
    "years_of_education": 12,
    "field_of_study": "Computer Science",
    "board_university": "Lahore Board of Intermediate Education",
    "gpa_percentage": 87.0,
    "gpa_4_scale": 3.7,
    "uk_classification": "First Class",
    "institution": "XYZ College, Lahore",
    "graduation_year": 2026,
    "subjects": ["Physics", "Math", "Computer Science", "English", "Urdu", "Islamiat/Pak Studies"],
    "relevant_courses": ["Programming Fundamentals", "Data Structures"],
    "gap_years": 0,
    "hec_attestation_done": false,
    "ibcc_equivalence_done": false
  },
  "language": {
    "english_proficiency_test": "IELTS",
    "ielts_overall": 7.0,
    "ielts_subbands": { "L": 7.5, "R": 7.0, "W": 6.5, "S": 7.0 },
    "toefl_score": null,
    "duolingo_score": null,
    "medium_of_instruction_english": true,
    "moi_certificate_available": false,
    "native_languages": ["Urdu", "Punjabi"],
    "has_english_test": true
  },
  "preferences": {
    "target_degree_level": "Bachelor's",
    "target_fields": ["Computer Science", "Artificial Intelligence", "Data Science"],
    "funding_requirement": "FULL",
    "budget_tier": "LOW",
    "max_out_of_pocket_pkr": 150000,
    "willing_to_relocate": true,
    "preferred_regions": [],
    "excluded_regions": [],
    "constraints": [
      "No large upfront bank deposit requirement",
      "Cannot show proof of funds > PKR 1,500,000"
    ]
  },
  "documents_uploaded": {
    "transcript": { "uploaded": true, "quality": "GOOD", "confidence": 0.95 },
    "cv": { "uploaded": false, "quality": null, "confidence": null },
    "passport": { "uploaded": false, "quality": null, "confidence": null },
    "ielts_certificate": { "uploaded": true, "quality": "GOOD", "confidence": 0.98 },
    "motivation_letter": { "uploaded": false, "quality": null, "confidence": null },
    "recommendation_letters": { "count": 0 },
    "financial_documents": { "uploaded": false },
    "police_clearance": { "uploaded": false },
    "medical_certificate": { "uploaded": false },
    "hec_attestation": { "uploaded": false },
    "ibcc_equivalence": { "uploaded": false }
  },
  "standardized_tests": {
    "hec_hat": null,
    "hec_usat": null,
    "gre": null,
    "sat": null,
    "gat_general": null,
    "gat_subject": null,
    "nts_nat": null
  },
  "experience": {
    "work_experience_years": 0,
    "research_publications": 0,
    "extracurriculars": ["Coding competitions", "Open source contributor"]
  },
  "profile_completeness": 72,
  "missing_required": [],
  "missing_optional": ["cv", "passport", "motivation_letter", "recommendation_letters"],
  "extraction_warnings": []
}
```

**Events Emitted:**
```
DOCUMENT_UPLOADED | DOCUMENT_PARSE_STARTED | DOCUMENT_PARSE_FAILED |
DOCUMENT_PARSED | EXTRACTION_FIELD_FOUND | EXTRACTION_LOW_CONFIDENCE |
DOCUMENT_MISSING_REQUIRED | DOCUMENT_MISSING_OPTIONAL |
USER_INPUT_REQUESTED | PROFILE_COMPLETE | PROFILE_VALIDATION_ERROR |
PROFILE_SAVED_TO_SESSION
```

---

### Agent 3: Discovery Commander + Regional Scout Workflows

**Commander Type:** Agent (LLM-powered)
**Scout Type:** Workflow (deterministic pipeline)

**Role:** The Commander generates Pakistan-optimized search strategies and deploys regional scout workflows that simultaneously search for scholarship opportunities. Scouts follow a deterministic pipeline: search -> scrape -> extract -> normalize -> return.

#### 3.1 Discovery Commander (Agent)
- Receives the student profile
- Generates region-specific search queries optimized for Pakistani students
- Example queries: "fully funded bachelor computer science scholarship Pakistan 2027", "Stipendium Hungaricum Pakistan HEC", "CSC scholarship Pakistani students requirements"
- Spawns regional scouts in parallel (LangGraph `Send()` API)
- Aggregates discovered opportunities into the candidate pool
- De-duplicates cross-region overlaps
- Checks session history for previously discovered scholarships and merges

#### 3.2 Regional Scout Workflows (Deterministic)

Each scout follows the EXACT same deterministic pipeline:

```
Step 1: Execute search queries (Tavily API)
    |
Step 2: Filter results for relevance (keyword matching + URL domain check)
    |
Step 3: Deep-scrape top results (Firecrawl / Jina Reader)
    |
Step 4: Extract structured scholarship data (Gemini 3.7 Flash with strict schema)
    |
Step 5: Normalize to canonical Scholarship schema
    |
Step 6: Return to Discovery Commander
```

**Regional Focus (Pakistan-Optimized):**

| Scout | Primary Focus | Key Sources for Pakistani Students |
|:---|:---|:---|
| EUROPE SCOUT | Stipendium Hungaricum, DAAD, Erasmus Mundus, Italian DSU, Eiffel, Swiss Excellence | DreamApply, DAAD Funding Guide, Campus France, HEC bilateral portal |
| ASIA SCOUT | CSC (China), MEXT (Japan), GKS/KGSP (South Korea), Brunei, ANSO | Campus China/CUCAS, JASSO, Study in Korea, HEC scholarships page |
| AMERICAS SCOUT | Fulbright (USEFP), direct US PhD RA/TA, Canadian scholarships, OAS | USEFP.org, Grants.gov, university funding pages |
| MENA SCOUT | Turkiye Burslari, KAUST, KFUPM, KAU, HBKU, IsDB | Turkey Scholarships portal, individual university pages |
| OCEANIA SCOUT | Australia Awards, New Zealand scholarships | Study in Australia, university portals |

**Search Tools (with failover):**
| Tool | Role | Failover Strategy |
|:---|:---|:---|
| `Tavily Search` | Primary web search | 5 API keys, rotate on failure |
| `Firecrawl` | Deep scraping of JS-heavy portals | 3 API keys, rotate on failure |
| `Jina Reader` | Fast URL-to-markdown | 1 API key, fallback to Firecrawl |
| `Crawl4AI` | Batch crawling of scholarship directories | Self-hosted, free |

**Discovered Scholarship Schema:**
```json
{
  "scholarship_id": "SCH-EU-0042",
  "name": "Stipendium Hungaricum",
  "host_country": "HU",
  "host_country_name": "Hungary",
  "host_institution": "Budapest University of Technology",
  "source_url": "https://stipendiumhungaricum.hu/...",
  "discovered_by": "europe_scout",
  "discovery_timestamp": "2026-09-01T13:42:07Z",
  "session_id": "uuid",
  "degree_levels": ["Bachelor's", "Master's", "PhD"],
  "eligible_fields": ["Computer Science", "Engineering", "Natural Sciences"],
  "pakistan_eligible": true,
  "pakistan_bilateral_quota": true,
  "pakistan_quota_seats": 400,
  "hec_managed": true,
  "funding_claims": {
    "tuition": "FULL",
    "accommodation": "PROVIDED_OR_ALLOWANCE",
    "monthly_stipend": "HUF 43,700-180,000",
    "health_insurance": "YES",
    "travel": "NOT_COVERED"
  },
  "language_requirements": {
    "english_test_required": true,
    "minimum_ielts": 5.5,
    "minimum_toefl": 72,
    "host_language_prep": true
  },
  "pakistan_specific_requirements": {
    "hec_hat_required": false,
    "hec_usat_required": true,
    "hec_attestation_required": true,
    "ibcc_equivalence_required": false,
    "noc_from_hec": false
  },
  "application_deadline": "2027-01-15",
  "application_opens": "2026-11-15",
  "age_limit": null,
  "gpa_minimum": null,
  "additional_requirements": ["HEC USAT for undergrad", "Two recommendation letters"],
  "raw_extracted_text": "...",
  "confidence": 0.85,
  "status": "DISCOVERED"
}
```

**Events Emitted:**
```
SCOUT_DEPLOYED | SEARCH_QUERY_EXECUTED | API_KEY_ROTATED |
SOURCE_FOUND | PAGE_SCRAPED | CANDIDATE_EXTRACTED |
SCOUT_COMPLETE | DISCOVERY_AGGREGATION_COMPLETE | DUPLICATE_DETECTED |
PREVIOUS_RESEARCH_LOADED
```

---

### Workflow 4: Eligibility Investigator

**Type:** Workflow (deterministic)

**Role:** Takes each discovered scholarship and performs a deterministic, personalized eligibility check against the student's profile across 15+ criteria dimensions. This is pure comparison logic — no LLM needed.

**Why Workflow?** Every eligibility check is a comparison operation:
- Is `student.nationality` in `scholarship.eligible_nationalities`? Yes/No.
- Is `student.age` <= `scholarship.age_limit`? Yes/No.
- Is `student.ielts_overall` >= `scholarship.minimum_ielts`? Yes/No.

No ambiguity. No judgment. Pure deterministic logic.

**Pakistan-Specific Dimensions:**

| # | Dimension | Check Logic |
|:--|:---|:---|
| 1 | Pakistan Eligible | scholarship.pakistan_eligible == true |
| 2 | Bilateral Quota | scholarship.pakistan_bilateral_quota (bonus if true) |
| 3 | Age | student.age <= scholarship.age_limit (at cutoff date) |
| 4 | Degree Level | student.target_degree in scholarship.degree_levels |
| 5 | Prior Education | student.years_of_education >= required |
| 6 | Field of Study | student.target_fields intersects scholarship.eligible_fields |
| 7 | GPA / Marks | student.gpa_percentage >= minimum (with scale conversion) |
| 8 | IELTS/TOEFL | If required: student has it AND score >= minimum |
| 9 | No English Test | If student has NO English test: does scholarship accept MOI certificate? |
| 10 | Host Language | If required: prep year provided? |
| 11 | HEC HAT/USAT | If required: student has score or can register in time |
| 12 | Application Deadline | deadline > today |
| 13 | Funding Match | scholarship funding >= student requirement |
| 14 | Budget Compatibility | estimated out-of-pocket <= student max budget |
| 15 | Special Constraints | user custom constraints satisfied |
| 16 | Proof of Funds | If required: amount <= student capacity |

**Output per Scholarship:**
```json
{
  "scholarship_id": "SCH-EU-0042",
  "eligibility_score": 92,
  "overall_status": "ELIGIBLE",
  "dimension_results": [
    { "dimension": "Pakistan Eligible", "status": "PASS", "detail": "Pakistan is in the eligible list" },
    { "dimension": "Bilateral Quota", "status": "BONUS", "detail": "400+ seats allocated for Pakistani students via HEC" },
    { "dimension": "Degree Level", "status": "PASS", "detail": "Bachelor's offered" },
    { "dimension": "Field", "status": "PASS", "detail": "CS is explicitly listed" },
    { "dimension": "GPA", "status": "PASS", "detail": "No minimum; 87% is competitive" },
    { "dimension": "English Test", "status": "PASS", "detail": "Min IELTS 5.5 — student has 7.0" },
    { "dimension": "HEC USAT", "status": "ACTION_REQUIRED", "detail": "HEC USAT required — student has not taken it yet" }
  ],
  "blocking_issues": [],
  "action_required": ["Register for HEC USAT immediately"],
  "pakistan_advantages": ["Dedicated bilateral quota of 400+ seats", "HEC manages the application process"]
}
```

**Events Emitted:**
```
ELIGIBILITY_CHECK_STARTED | DIMENSION_EVALUATED | ELIGIBILITY_WARNING |
ELIGIBILITY_PASS | ELIGIBILITY_FAIL | ELIGIBILITY_COMPLETE
```

---

### Agent 5: Document Analyst

**Type:** Agent (LLM-powered)

**Role:** Compares the student's uploaded documents against each scholarship's specific document requirements. Produces a document readiness score and gap analysis. Understands Pakistani-specific documentation requirements.

**Pakistan-Specific Document Requirements:**
- **HEC Attestation:** Required for most bilateral scholarships (CSC, Stipendium Hungaricum, Turkiye Burslari). Takes 3-4 weeks via HEC regional centers.
- **IBCC Equivalence:** Required for some scholarships. Converts Pakistani intermediate marks to international equivalent.
- **MOFA Apostille/Attestation:** Required for Italy, some European countries.
- **Family Registration Certificate (FRC):** Required for Turkey, Italy, some others.
- **CNIC/B-Form:** Pakistani national ID, sometimes needed.
- **Police Character Certificate:** From local SSP office. Takes 2-4 weeks.
- **Medical Exam:** Must be from approved panel clinic (varies by destination country).

**Output:**
```json
{
  "scholarship_id": "SCH-EU-0042",
  "readiness_score": 62,
  "documents_ready": 4,
  "documents_partial": 2,
  "documents_missing": 4,
  "total_required": 10,
  "critical_missing": ["Recommendation Letters", "HEC Attestation"],
  "estimated_preparation_days": 28,
  "estimated_preparation_cost_pkr": 25000,
  "action_plan": [
    {
      "priority": 1,
      "action": "Contact 2 academic references for recommendation letters",
      "estimated_days": 14,
      "estimated_cost_pkr": 0,
      "blocking": true
    },
    {
      "priority": 2,
      "action": "Submit transcript to HEC for attestation (nearest HEC regional center)",
      "estimated_days": 21,
      "estimated_cost_pkr": 3000,
      "blocking": true,
      "pakistan_specific": true
    }
  ]
}
```

**Events Emitted:**
```
DOCUMENT_REQUIREMENT_PARSED | DOCUMENT_MATCH_FOUND | DOCUMENT_MISSING |
DOCUMENT_QUALITY_WARNING | READINESS_SCORE_CALCULATED
```

---

### Workflow 6: True Cost Analyzer

**Type:** Workflow (deterministic)

**Role:** Deconstructs the real financial burden in PKR. Uses lookup tables for Pakistani-specific costs — no LLM needed.

**Why Workflow?** Costs are lookup values + arithmetic:
- IELTS fee = PKR 75,600-76,240 (computer-delivered)
- HEC e-Attestation = PKR 3,000 per doc (DAS 1-Link system)
- VFS/Gerry's appointment = PKR 15,000-45,000 (known by country)

**Pakistan-Specific Cost Database (hardcoded lookup):**

| Phase | Cost Item | Amount (PKR) | Notes |
|:---|:---|:---|:---|
| Pre-App | IELTS Academic exam | 75,600-76,240 | British Council Pakistan (Computer-Delivered) |
| Pre-App | TOEFL iBT | 65,000-78,000 | ETS Pakistan |
| Pre-App | HEC HAT test | 2,500 | HEC online registration |
| Pre-App | HEC USAT test | 2,500 | HEC online registration |
| Pre-App | HEC degree attestation | 3,000/doc | Digital e-Attestation Certificate |
| Pre-App | IBCC equivalence | 6,000/cert | Foreign equivalence (Urgent: 12,000) |
| Pre-App | MOFA attestation | 1,000/doc | Ministry of Foreign Affairs |
| Pre-App | Document translations | 5,000-20,000 | Notarized translations |
| App | Uni-Assist (Germany) | ~22,875 first + 9,150 each | EUR 75 + EUR 30 |
| App | University app fee | 0-45,000 | Varies; many waived for scholarships |
| App | DHL courier | 8,000-16,000/packet | For hard copy submissions |
| Visa | Schengen visa | ~27,450 | EUR 90 (Official consular fee) |
| Visa | UK visa | ~200,880 | GBP 558 (+ IHS GBP 776/year) |
| Visa | US visa (J-1/F-1) | ~51,800 | USD 185 |
| Visa | Turkish visa | 0 | Free for scholarship recipients |
| Visa | Hungarian visa | 0 | Free for SH recipients |
| Visa | VFS/Gerry's biometric | 15,000-45,000 | Appointment + biometrics |
| Visa | Medical exam (panel) | 15,000-40,000 | Approved clinic |
| Visa | Police clearance | 2,000-8,000 | SSP office |
| Travel | Flight (one-way) | 150,000-350,000 | Depends on destination |
| Settle | Dorm deposit | 0-350,000 | 1-3 months security |
| Settle | First month reserve | 60,000-180,000 | Before first stipend |
| Settle | Semester admin fee | 0-115,000 | Germany: EUR 150-400 |
| Settle | Residence permit | 30,000-75,000 | Country-dependent |

**Output:**
```json
{
  "scholarship_id": "SCH-EU-0042",
  "true_funding_score": 78,
  "total_out_of_pocket_pkr": 343000,
  "total_out_of_pocket_usd": 1225,
  "phase_breakdown": {
    "pre_application": { "total_pkr": 8000, "items": [] },
    "application": { "total_pkr": 0, "items": [] },
    "visa_travel": { "total_pkr": 235000, "items": [] },
    "settlement": { "total_pkr": 100000, "items": [] }
  },
  "budget_compatibility": "EXCEEDS_BUDGET",
  "student_max_budget_pkr": 150000,
  "shortfall_pkr": 193000,
  "risk_items": ["Flight not covered (~175,000 PKR)", "First month reserve needed (~60,000 PKR)"]
}
```

---

### Workflow 7: Deadline Intelligence

**Type:** Workflow (deterministic)

**Role:** Converts static deadlines into dynamic, risk-aware intelligence. Pure date math — no LLM needed.

**Pakistan-Specific Lead Times (hardcoded):**
- HEC attestation: 21-28 days
- IBCC equivalence: 14-21 days
- Police clearance: 14-28 days
- IELTS registration to test date: 14-21 days
- HEC HAT/USAT next available slot: check HEC schedule
- MOFA attestation: 3-7 days
- Recommendation letters (from Pakistani professors): 7-21 days
- Medical exam + results: 7-14 days

**Risk Calculation:**
```
Days Remaining = Deadline - Today
Preparation Time = Sum of all document preparation estimates (Pakistan timelines)
Buffer = 7 days
Slack = Days Remaining - Preparation Time - Buffer

Risk Level:
  Slack > 30 days   =  LOW
  Slack 15-30 days  =  MODERATE
  Slack 7-15 days   =  HIGH
  Slack 0-7 days    =  VERY HIGH
  Slack < 0 days    =  IMPOSSIBLE
```

---

### Agent 8: Verification Agent

**Type:** Agent (LLM-powered)

**Role:** Actively fights LLM hallucination by cross-checking every scholarship claim against official sources. Uses web search tools to find and verify official sources.

**Pakistan-Verification Priorities:**
- Is this scholarship listed on the HEC portal? (highest trust signal for bilateral scholarships)
- Is the embassy/consulate in Pakistan processing this scholarship? (check embassy websites)
- Has USEFP posted about this? (for US scholarships)
- Is the scholarship portal/DreamApply link active?

**Verification Labels:**
- VERIFIED — Official source confirmed (HEC portal, embassy, .gov/.edu domain)
- PARTIALLY VERIFIED — Source found but some claims unconfirmed
- SUSPICIOUS/OUTDATED — Source unavailable, conflicting info, or stale data
- HEC LISTED — Specifically listed on HEC Pakistan portal (highest confidence for bilateral)

**Tools:**
| Tool | Purpose | Failover |
|:---|:---|:---|
| `Tavily Search` | Find official sources | 5 keys, rotate |
| `Firecrawl` | Scrape official portals | 3 keys, rotate |
| `Jina Reader` | Quick page reads | 1 key, fallback to Firecrawl |
| `Crawl4AI` | Batch verification of multiple sources | Self-hosted, free |

---

### Agent 9: Skeptic Agent (Debate Arena)

**Type:** Agent (LLM-powered)

**Role:** The adversarial challenger. Specifically trained to find problems that affect Pakistani students.

**Pakistan-Specific Challenges the Skeptic Raises:**
- "Fully funded" but requires proof of funds > PKR 1.5M for visa?
- Country has high Pakistani visa rejection rate?
- Scholarship requires return-to-home-country obligation (affects career plans)?
- Stipend is in local currency that has been devaluing?
- Country has safety/political issues affecting Pakistani students?
- Hidden requirement for supervisor acceptance letter that Pakistani students struggle to get?
- Competition ratio is extremely high for Pakistani applicants specifically?
- No Pakistani alumni network at the university?

---

### Workflow 10: Synthesis

**Type:** Workflow (deterministic)

**Role:** Aggregates all agent outputs into a unified Scholarship DNA card. Pure data aggregation with conflict resolution rules — no LLM needed.

---

### Workflow 11: Ranking Engine

**Type:** Workflow (deterministic)

**Role:** Weighted composite scoring. Pure arithmetic.

**Pakistan-Adjusted Scoring Model:**

| Factor | Weight | Source | Rationale |
|:---|:---|:---|:---|
| Eligibility Match | 25% | Eligibility Workflow | Core fit |
| True Funding Score | 25% | Cost Workflow | PKR affordability is critical |
| Pakistan Bilateral Bonus | 10% | Discovery | HEC-managed quotas = higher acceptance |
| Academic & Field Fit | 10% | Profile + Eligibility | Program match |
| Document Readiness | 10% | Document Agent | Can they realistically apply? |
| Deadline Feasibility | 10% | Deadline Workflow | Pakistan prep timelines factored in |
| Verification Confidence | 5% | Verification Agent | Is this real? |
| Competition Estimate | 5% | Skeptic + Discovery | Realistic chances |

**Pakistan Bilateral Bonus:** Scholarships with dedicated Pakistan quotas via HEC (Stipendium Hungaricum, CSC, Turkiye Burslari) get a +10% bonus because acceptance rates are significantly higher through bilateral channels.

---

### Agent 12: Final Advisor (Application Planner)

**Type:** Agent (LLM-powered)

**Role:** Generates a personalized roadmap with Pakistan-specific timelines, HEC/IBCC/MOFA steps, and PKR cost estimates.

**Pakistan-Specific Output Includes:**
- Which HEC regional center to visit for attestation
- IBCC office locations and submission process
- MOFA attestation steps
- HEC HAT/USAT exam schedule and registration links
- IELTS test dates at British Council centers in student's city
- Approved medical exam clinics by destination country
- VFS/Gerry's appointment booking links for visa
- Embassy interview preparation tips
- Pakistani student community groups at destination universities

---

## 5. Session History & Research Persistence

### 5.1 Why Session History Matters

Every research session costs time and API calls. ScholarX should NEVER repeat work it has already done. When a student returns for another hunt (or a new student with similar profile arrives), the system should leverage previous research.

### 5.2 What Gets Saved

Every session saves the following to the local SQLite database:

```json
{
  "session_id": "uuid",
  "created_at": "2026-09-01T13:00:00Z",
  "student_profile": { "...full profile..." },
  "mission_parameters": { "constraints": [], "preferences": [] },
  "discovered_scholarships": [
    {
      "scholarship_id": "SCH-EU-0042",
      "name": "Stipendium Hungaricum",
      "discovery_data": { "...full record..." },
      "eligibility_result": { "...full result..." },
      "cost_analysis": { "...full breakdown..." },
      "deadline_analysis": { "...full analysis..." },
      "verification_result": { "...full evidence..." },
      "skeptic_challenges": { "...debate log..." },
      "final_score": 90,
      "final_rank": 1
    }
  ],
  "total_opportunities_scanned": 136,
  "total_verified": 21,
  "agent_timeline": [ "...all events..." ],
  "sources_visited": [ "...all URLs scraped..." ],
  "search_queries_used": [ "...all search queries..." ],
  "final_report": { "...full report..." },
  "roadmap": { "...full action plan..." }
}
```

### 5.3 How Previous Sessions Are Used

When a new session starts:

1. **Same Student Returns:** Load their profile, skip re-extraction. Show previous results. Only re-search for NEW or UPDATED scholarships.
2. **New Student, Similar Profile:** Cross-reference scholarship cache. If a scholarship was verified 7 days ago, skip re-verification. Use cached data.
3. **Scholarship Cache:** All discovered scholarships are cached with TTL:
   - Verification data: 7 days TTL (re-verify after 7 days)
   - Cost data: 30 days TTL (costs change slowly)
   - Deadline data: 1 day TTL (deadlines are time-critical)
   - Eligibility criteria: 30 days TTL (criteria rarely change mid-cycle)
4. **Search Query Cache:** Previously successful search queries are reused to seed new discoveries.

### 5.4 Student Session Dashboard

Students can see their previous sessions:

```
+--------------------------------------------------+
| MY SCHOLARX SESSIONS                              |
|                                                    |
| Session #3 — September 1, 2026                    |
|   Profile: CS Bachelor's, 87%, IELTS 7.0          |
|   Found: 21 verified opportunities                 |
|   Top Match: Stipendium Hungaricum (94%)           |
|   Status: COMPLETED                                |
|   [ VIEW RESULTS ]  [ NEW HUNT WITH SAME PROFILE ] |
|                                                    |
| Session #2 — August 15, 2026                      |
|   Profile: CS Bachelor's, 87%, No IELTS           |
|   Found: 14 verified opportunities                 |
|   Top Match: Turkiye Burslari (91%)                |
|   Status: COMPLETED                                |
|   [ VIEW RESULTS ]                                 |
|                                                    |
| Session #1 — August 1, 2026                       |
|   Profile: CS Bachelor's, 85%, No IELTS           |
|   Found: 12 verified opportunities                 |
|   Top Match: CSC China (88%)                       |
|   Status: COMPLETED                                |
|   [ VIEW RESULTS ]                                 |
+--------------------------------------------------+
```

### 5.5 Storage Architecture

```
SQLite Database: scholarx_sessions.db (local file)
  |
  +-- students table
  |     student_id, name, profile_json, created_at, updated_at
  |
  +-- sessions table
  |     session_id, student_id, mission_params, status, created_at
  |
  +-- scholarships_cache table
  |     scholarship_id, name, country, data_json, discovered_at,
  |     verified_at, verification_ttl, source_urls
  |
  +-- session_scholarships table (junction)
  |     session_id, scholarship_id, eligibility_json, cost_json,
  |     deadline_json, verification_json, skeptic_json, final_score, rank
  |
  +-- events_log table
  |     event_id, session_id, timestamp, event_type, agent_id, payload_json
  |
  +-- search_queries_cache table
        query_text, region, results_count, last_used, success_rate
```

---

## 6. Event System & Inter-Agent Communication

### 6.1 Event Architecture (Local)

```
Agent/Workflow --emit--> Event --publish--> Redis Pub/Sub (localhost:6379)
                                                  |
                                       +----------+----------+
                                       v          v          v
                                  SSE Stream   SQLite     Console
                                  (Frontend)   (History)   (Debug)
```

### 6.2 Event Schema

Every event follows a unified schema:
```json
{
  "event_id": "evt-uuid",
  "session_id": "session-uuid",
  "timestamp": "2026-09-01T13:42:07.123Z",
  "event_type": "TOOL_CALLED",
  "agent_id": "europe_scout",
  "agent_display_name": "Europe Scout",
  "component_type": "WORKFLOW",
  "phase": "DISCOVERY",
  "payload": {
    "tool_name": "tavily_search",
    "api_key_index": 2,
    "query": "fully funded bachelor CS scholarship Pakistani students Europe 2027",
    "result_count": 12
  },
  "related_scholarship_id": null,
  "severity": "INFO"
}
```

### 6.3 Complete Event Catalog

Same as v1 but with additional events:
```
SESSION_CREATED | SESSION_LOADED | SESSION_SAVED |
PREVIOUS_RESEARCH_LOADED | CACHE_HIT | CACHE_MISS |
API_KEY_ROTATED | API_KEY_EXHAUSTED | FALLBACK_TOOL_USED |
USER_INPUT_REQUESTED | USER_INPUT_RECEIVED |
DOCUMENT_REUPLOAD_REQUESTED
```

---

## 7. Tech Stack

### 7.1 Stack Overview (Local-First)

```
FRONTEND (localhost:3000)              BACKEND (localhost:8000)
-------------------------              -------------------------
Next.js 15 (App Router)               Python 3.12+
React 19                              FastAPI
TypeScript                             LangGraph
TailwindCSS v4                         LangChain
Framer Motion                          Pydantic v2
@xyflow/react (Agent Graph)            Uvicorn (ASGI)
react-simple-maps (World Map)
react-force-graph-3d (3D)             LLM LAYER (Cloud APIs)
@microsoft/fetch-event-source          -------------------------
                                       Gemini 3.7 Flash (primary)
LOCAL DATA (Docker)                    Gemini 3.0 Flash (fallback)
--------------------------             Groq gpt-oss-120b (summaries)
PostgreSQL + pgvector (5432)
Redis (6379)                           SEARCH/SCRAPE (Cloud APIs)
ChromaDB (8100)                        -------------------------
SQLite (file-based sessions)           Tavily (5 keys)
                                       Firecrawl (3 keys)
DOCUMENT PARSING (Local)               Jina Reader (1 key)
--------------------------             Crawl4AI (self-hosted)
PyMuPDF4LLM (CVs)
pdfplumber (Transcripts)
Docling (Complex PDFs)
```

### 7.2 LLM Strategy with Multi-Key Failover

**Principle:** Multiple API keys per service. If one fails (rate limit, quota exhausted, network error), automatically rotate to the next key.

**Gemini (High-intelligence tasks):**
- Primary model: `gemini-3.7-flash` — used for profile extraction, document analysis, verification reasoning, skeptic challenges, advisor generation
- Fallback model: `gemini-3.0-flash` — used if 3.7 is unavailable
- 3 API keys with automatic rotation

**Groq (Small/fast tasks):**
- Model: `gpt-oss-120b`
- Used for: summarization, simple text formatting, event description generation
- 4 API keys with automatic rotation

**Key Rotation Implementation:**
```python
# Pseudocode for key rotation (actual keys in .env)
class APIKeyRotator:
    def __init__(self, keys: list[str]):
        self.keys = keys
        self.current_index = 0
        self.failed_keys = set()

    def get_key(self) -> str:
        while self.current_index < len(self.keys):
            key = self.keys[self.current_index]
            if key not in self.failed_keys:
                return key
            self.current_index += 1
        raise AllKeysExhaustedError()

    def mark_failed(self, key: str):
        self.failed_keys.add(key)
        self.current_index += 1
        emit_event("API_KEY_ROTATED", {"provider": "...", "new_index": self.current_index})
```

### 7.3 Search Tool Failover Strategy

```
Primary: Tavily Search (5 keys)
   |-- Key 1 fails -> Key 2 -> Key 3 -> Key 4 -> Key 5
   |-- All Tavily keys exhausted?
       |
       v
Fallback 1: Firecrawl (3 keys) — direct URL scraping of known portals
   |-- Key 1 fails -> Key 2 -> Key 3
   |-- All Firecrawl keys exhausted?
       |
       v
Fallback 2: Jina Reader (direct URL reads)
   |-- For known URLs only (pre-seeded database)
   |-- If Jina fails:
       |
       v
Fallback 3: Crawl4AI (self-hosted, no API key needed)
   |-- Local headless browser crawling
   |-- If target site blocks:
       |
       v
Fallback 4: Pre-seeded local database only
   |-- Use cached/pre-researched scholarship data
   |-- Mark results as "FROM_CACHE" in UI
```

### 7.4 Environment Variables (.env file)

All API keys MUST be stored in `.env` file. NEVER in code or documentation.

```
# .env.example (template — actual keys are secret)

# === Gemini API Keys (rotate on failure) ===
GEMINI_API_KEY_1=your_key_here
GEMINI_API_KEY_2=your_key_here
GEMINI_API_KEY_3=your_key_here
GEMINI_PRIMARY_MODEL=gemini-3.7-flash
GEMINI_FALLBACK_MODEL=gemini-3.0-flash

# === Groq API Keys (rotate on failure) ===
GROQ_API_KEY_1=your_key_here
GROQ_API_KEY_2=your_key_here
GROQ_API_KEY_3=your_key_here
GROQ_API_KEY_4=your_key_here
GROQ_MODEL=gpt-oss-120b

# === Tavily Search API Keys (rotate on failure) ===
TAVILY_API_KEY_1=your_key_here
TAVILY_API_KEY_2=your_key_here
TAVILY_API_KEY_3=your_key_here
TAVILY_API_KEY_4=your_key_here
TAVILY_API_KEY_5=your_key_here

# === Firecrawl API Keys (rotate on failure) ===
FIRECRAWL_API_KEY_1=your_key_here
FIRECRAWL_API_KEY_2=your_key_here
FIRECRAWL_API_KEY_3=your_key_here

# === Jina Reader API Key ===
JINA_API_KEY=your_key_here

# === Local Database ===
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=scholarx
POSTGRES_USER=scholarx
POSTGRES_PASSWORD=scholarx_local

REDIS_HOST=localhost
REDIS_PORT=6379

CHROMADB_HOST=localhost
CHROMADB_PORT=8100

SESSION_DB_PATH=./data/scholarx_sessions.db
```

---

## 8. Frontend Visualization Architecture

### 8.1 Screen Layout

Same as v1 but with additions:
- **Session Selector** in top-left: dropdown to view previous sessions
- **Pakistan Flag/Context** in header: "Optimized for Pakistani Students"
- **PKR Cost Display**: All costs shown in PKR with USD equivalent

### 8.2 Key Visual Components

Same as v1 (Brain Map, World Map, Opportunity Cards, DNA View, Evidence Graph, Debate Arena, Agent Timeline, Phase Progress, Mission Control) with these Pakistan-specific additions:

#### Pakistan-Optimized Opportunity Card:
```
+=============================================+
| [flag] STIPENDIUM HUNGARICUM                 |
| Budapest University of Technology            |
|                                              |
| MATCH                     94%                |
| FUNDING                   FULL               |
| APPLICATION READINESS    82%                 |
| DEADLINE                 136 DAYS            |
|                                              |
| Eligible                                     |
| Pakistan bilateral quota (400+ seats)        |
| HEC managed application                     |
| Recommendation required                      |
|                                              |
| ESTIMATED OUT-OF-POCKET                      |
| PKR 343,000 (~USD 1,225)                    |
|                                              |
| HEC USAT Required                            |
|                                              |
| [ INVESTIGATE ] [ APPLICATION PLAN ]         |
+=============================================+
```

#### Session History Sidebar:
```
+------------------------------------------+
| PREVIOUS SESSIONS                         |
|                                           |
| Sep 1 — CS Bachelor, 87%                 |
|   21 verified, Top: Hungary 94%          |
|   [ LOAD ]                               |
|                                           |
| Aug 15 — CS Bachelor, No IELTS           |
|   14 verified, Top: Turkey 91%           |
|   [ LOAD ]                               |
+------------------------------------------+
```

---

## 9. Data Sources & APIs

### 9.1 Pakistan-Priority Scholarship Databases

| Priority | Database/Portal | URL | Pakistan Relevance |
|:---|:---|:---|:---|
| 1 | HEC Scholarship Portal | scholarship.hec.gov.pk | Central hub for all bilateral quotas |
| 2 | Turkiye Burslari | turkiyeburslari.gov.tr | Most popular among Pakistani students |
| 3 | Stipendium Hungaricum (DreamApply) | apply.stipendiumhungaricum.hu | 400+ seats for Pakistan |
| 4 | Campus China / CUCAS | campuschina.org | CSC Type A (via HEC) and Type B (direct) |
| 5 | USEFP (Fulbright Pakistan) | usefp.org | Largest Fulbright program globally |
| 6 | Study in Korea (GKS) | studyinkorea.go.kr | Embassy + University tracks |
| 7 | JASSO / MEXT | jasso.go.jp | Embassy track via Japanese Embassy Islamabad |
| 8 | DAAD Funding Guide | funding-guide.de | EPOS, PPGG, Helmut-Schmidt |
| 9 | Erasmus Mundus Catalogue | eacea.ec.europa.eu | Joint master's across EU |
| 10 | KAUST | kaust.edu.sa | Direct merit-based, no HEC quota |
| 11 | ScholarshipPortal (Studyportals) | scholarshipportal.com | Global aggregator |
| 12 | Scholars4dev | scholars4dev.com | Curated for developing countries |

### 9.2 Pre-Seeded Knowledge Base

ScholarX will have a **pre-seeded database** of ~200-300 scholarships specifically relevant to Pakistani students, with verified data including:
- All HEC bilateral scholarships (China, Turkey, Hungary, Korea, Japan, Germany, Italy, etc.)
- All USEFP programs (Fulbright, Global UGRAD, Humphrey)
- Major university-specific scholarships accepting Pakistani students
- All Erasmus Mundus programs open to Pakistan
- Gulf scholarships (KAUST, KFUPM, HBKU)

This ensures fast, reliable demo performance. Live search agents discover additional/updated opportunities on top of this base.

**Pre-seeded data includes:**
- Verified eligibility criteria
- Accurate deadline windows
- Pakistan-specific requirements (HEC HAT/USAT, attestation, etc.)
- True cost estimates in PKR
- Application portal URLs
- Success stories / acceptance rates for Pakistani applicants (where available)

---

## 10. Project Phases

### Phase 0: Foundation & Research (Week 1-2)

| Task | Deliverable |
|:---|:---|
| Set up monorepo structure (/frontend, /backend, /shared) | Project skeleton |
| Set up Docker Compose (PostgreSQL, Redis, ChromaDB — all local) | docker-compose.yml |
| Create .env with all API keys (Gemini x3, Groq x4, Tavily x5, Firecrawl x3, Jina x1) | .env file |
| Define all Pydantic schemas (Pakistan-optimized) | schemas/ directory |
| Build API key rotation utility | utils/api_keys.py |
| Research and document 50 Pakistan-priority scholarships | Seed database JSON |
| Set up SQLite session database | Session schema |
| Create the LangGraph state schema | graph/ directory |

### Phase 1: Profile Agent + Document Parsing (Week 3-4)

| Task | Deliverable |
|:---|:---|
| Build the profile input form (Pakistan-optimized fields) | Student intake UI |
| Implement file upload with drag-and-drop | Document upload component |
| Integrate PyMuPDF4LLM + pdfplumber + Docling | Document parsing pipeline |
| Build incomplete document handling (ask user to re-upload/provide manually) | Error handling flow |
| Build Profile Analyst agent with Gemini 3.7 Flash structured output | agents/profile_agent.py |
| Implement Pakistani education system GPA conversion | utils/gpa_converter.py |
| Build session creation and profile persistence | Session management |

### Phase 2: Discovery Pipeline (Week 5-7)

| Task | Deliverable |
|:---|:---|
| Implement Tavily search with 5-key rotation | tools/tavily_search.py |
| Implement Firecrawl with 3-key rotation | tools/firecrawl_scrape.py |
| Implement Jina Reader | tools/jina_reader.py |
| Implement Crawl4AI batch crawler | tools/crawl4ai_batch.py |
| Build Discovery Commander agent | agents/discovery_commander.py |
| Build 5 Regional Scout WORKFLOWS (deterministic pipelines) | workflows/scouts/ |
| Implement LangGraph Send() fan-out for parallel scouts | Fan-out pipeline |
| Build scholarship extraction prompt (Gemini 3.7 Flash) | Extraction prompts |
| Seed database with 200+ pre-researched scholarships | Seed data |
| Implement session-aware scholarship caching | Cache layer |

### Phase 3: Analysis Workflows + Agents (Week 8-10)

| Task | Deliverable |
|:---|:---|
| Build Eligibility Investigator WORKFLOW (15 Pakistan-aware dimensions) | workflows/eligibility.py |
| Build True Cost Analyzer WORKFLOW (PKR lookup tables) | workflows/cost_analyzer.py |
| Build Deadline Intelligence WORKFLOW (Pakistan lead times) | workflows/deadline.py |
| Build Document Analyst AGENT (LLM-powered quality assessment) | agents/document_agent.py |
| Build Pakistan-specific cost lookup database | data/pakistan_costs.json |
| Test analysis pipeline with Pakistani student profiles | Integration tests |

### Phase 4: Verification + Skeptic + Debate (Week 11-13)

| Task | Deliverable |
|:---|:---|
| Build Verification Agent (multi-source, HEC-priority) | agents/verification_agent.py |
| Build Skeptic Agent (Pakistan-specific challenges) | agents/skeptic_agent.py |
| Build Synthesis WORKFLOW (aggregation + conflict rules) | workflows/synthesis.py |
| Build Ranking Engine WORKFLOW (Pakistan-adjusted weights) | workflows/ranking.py |
| Build Final Advisor Agent (Pakistan roadmap with HEC/IBCC steps) | agents/advisor_agent.py |
| Wire all components into complete LangGraph DAG | Full pipeline |

### Phase 5: Event System + Streaming (Week 14-15)

| Task | Deliverable |
|:---|:---|
| Implement Redis Pub/Sub event bus (localhost) | events/bus.py |
| Add event emission to all agents and workflows | Event integration |
| Build FastAPI SSE streaming endpoint | /api/stream/{session_id} |
| Implement event persistence to SQLite session DB | Event store |
| Build frontend SSE consumer | SSE client hook |
| Test real-time event flow end-to-end locally | Local streaming test |

### Phase 6: Frontend Visualization (Week 16-20)

| Task | Deliverable |
|:---|:---|
| Week 16: Agent Brain Map (React Flow, custom nodes, animated edges) | Brain Map component |
| Week 17: Global Discovery Map (world map, animated arcs, Pakistan origin) | World Map component |
| Week 18: Scholarship Cards (PKR costs), DNA View, Evidence Graph | Results components |
| Week 19: Mission Control, Agent Timeline, Phase Progress, Debate Arena | Dashboard components |
| Week 19: Session History sidebar and session loading | Session UI |
| Week 20: Cinematic transitions, launch animation, dark theme, judge controls | Visual polish |
| Week 20: "Add Constraint" / "Change Field" interactive controls | HITL controls |

### Phase 7: Integration, Testing & Exhibition Prep (Week 21-24)

| Task | Deliverable |
|:---|:---|
| Full end-to-end integration testing (locally) | Test suite |
| Performance optimization (caching, parallel execution) | Optimized pipeline |
| Pre-cache 5 complete demo profiles with results | Offline fallback |
| Demo script creation and rehearsal | Demo playbook |
| Error handling and graceful degradation | Resilience layer |
| Final visual polish | Production-ready UI |
| Exhibition materials (poster, talking points) | Exhibition kit |
| Dress rehearsal with mock judges | Rehearsal |

---

## 11. Tools & Services Required

### 11.1 Cloud API Services (Keys in .env)

| Service | Purpose | Keys | Cost |
|:---|:---|:---|:---|
| Gemini API (3.7 Flash + 3.0 Flash) | Primary LLM | 3 keys, rotate | Free tier / low cost |
| Groq (gpt-oss-120b) | Summarization, small tasks | 4 keys, rotate | Free tier |
| Tavily | Web search | 5 keys, rotate | Free: 1000/month per key |
| Firecrawl | Deep web scraping | 3 keys, rotate | Free: 500/month per key |
| Jina Reader | URL-to-markdown | 1 key | Free tier |
| Crawl4AI | Batch crawling | N/A | Free (self-hosted) |

### 11.2 Local Infrastructure (Docker)

| Service | Port | Purpose |
|:---|:---|:---|
| PostgreSQL + pgvector | 5432 | Scholarship records, embeddings |
| Redis | 6379 | Event Pub/Sub, page cache |
| ChromaDB | 8100 | Vector search for semantic matching |
| SQLite | File | Session history, student profiles |

### 11.3 Python Dependencies

```
# Core
fastapi>=0.115.0
uvicorn>=0.30.0
pydantic>=2.0
python-dotenv>=1.0

# Agent Framework
langgraph>=0.3.0
langchain>=0.3.0
langchain-google-genai>=2.0

# Groq
groq>=0.11.0

# Document Parsing
pymupdf4llm>=0.0.10
pdfplumber>=0.11.0
docling>=2.0

# Web Search & Scraping
tavily-python>=0.5.0
firecrawl-py>=1.0
crawl4ai>=0.4.0

# Database
asyncpg>=0.30.0
sqlalchemy>=2.0
redis>=5.0
chromadb>=0.5.0
pgvector>=0.3.0
aiosqlite>=0.20.0

# Utilities
httpx>=0.27.0
tenacity>=9.0
structlog>=24.0
```

### 11.4 Node.js Dependencies

```json
{
  "dependencies": {
    "next": "^15.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "@xyflow/react": "^12.0.0",
    "react-simple-maps": "^3.0.0",
    "react-force-graph-3d": "^1.25.0",
    "framer-motion": "^12.0.0",
    "recharts": "^2.12.0",
    "@microsoft/fetch-event-source": "^2.0.1",
    "zustand": "^5.0.0",
    "tailwindcss": "^4.0.0",
    "lucide-react": "latest",
    "clsx": "^2.1.0",
    "date-fns": "^4.0.0",
    "topojson-client": "^3.1.0",
    "d3-geo": "^3.1.0"
  }
}
```

---

## 12. Preparation Checklist

### 12.1 Before You Start Coding

- [ ] Create .env file with all API keys (Gemini x3, Groq x4, Tavily x5, Firecrawl x3, Jina x1)
- [ ] Install Python 3.12+, Node.js 20+, Docker Desktop
- [ ] Set up Docker Compose for PostgreSQL, Redis, ChromaDB
- [ ] Test all API keys (verify each one works)
- [ ] Study 20-30 Pakistan-relevant scholarship pages manually
- [ ] Prepare 3-5 Pakistani student test profiles
- [ ] Collect sample Pakistani documents (marksheet, transcript, CNIC, passport)
- [ ] Build the Pakistan-specific cost lookup table (visa fees, attestation costs, etc.)

### 12.2 Demo Profiles (All Pakistani)

| Profile | Details | Tests |
|:---|:---|:---|
| Pakistani ICS Student | 87%, CS, IELTS 7.0, bachelor's, full funding, low budget | Primary demo |
| Pakistani FSc Student | 78%, Engineering, no IELTS, bachelor's, full funding | Tests "no English test" path |
| Pakistani BS Graduate | 3.5 GPA, CS, IELTS 7.5, master's, full funding | Tests postgraduate path |
| Pakistani BBA Graduate | 3.2 GPA, Business, no GRE, MBA, partial funding | Tests non-STEM path |
| Pakistani Working Professional | BE + 3yr experience, IELTS 6.5, PhD, DAAD | Tests experienced applicant |

### 12.3 Exhibition Day Preparation

- [ ] Laptop with 16GB+ RAM, Docker running
- [ ] All services started locally (docker-compose up)
- [ ] External monitor (24"+ or TV) for visual impact
- [ ] Mobile hotspot as backup internet
- [ ] Pre-cached results for all 5 demo profiles
- [ ] Pre-recorded demo video as last-resort backup
- [ ] Poster with architecture diagram
- [ ] Verify all API keys are working day-of

---

## 13. Demo Flow — The Exhibition Experience

Same as v1 but with Pakistan-specific elements:
- Landing page says "Optimized for Pakistani Students"
- Form has Pakistan-specific fields (board, city, HEC HAT/USAT scores)
- Costs displayed in PKR
- HEC bilateral scholarships highlighted with special badge
- Session history shows on return visits

---

## 14. Scoring Model

### 14.1 Pakistan-Adjusted Composite Score

```
Score = (0.25 x Eligibility) + (0.25 x Funding) + (0.10 x BilateralBonus) +
        (0.10 x AcademicFit) + (0.10 x DocReadiness) + (0.10 x DeadlineFeasibility) +
        (0.05 x Verification) + (0.05 x CompetitionFactor)
```

### 14.2 Pakistan Bilateral Bonus

```
If scholarship has dedicated Pakistan quota via HEC:
  BilateralBonus = 100 (maximum)
  Rationale: Acceptance rate is 5-10x higher through bilateral channels

If scholarship accepts Pakistani students but no dedicated quota:
  BilateralBonus = 50

If scholarship has unclear Pakistan eligibility:
  BilateralBonus = 0
```

### 14.3 True Funding Score (PKR-based)

```
TrueFundingScore = 100 - (total_uncovered_cost_pkr / student_max_budget_pkr * 100)
Clamped to [0, 100]
```

---

## 15. Risk Mitigation & Resilience

### 15.1 API Key Exhaustion Protection

| Scenario | Response |
|:---|:---|
| Tavily key 1 rate limited | Rotate to key 2 (up to key 5) |
| All 5 Tavily keys exhausted | Fall back to Firecrawl, then Jina, then Crawl4AI, then cache |
| Gemini key 1 fails | Rotate to key 2, then key 3 |
| All Gemini keys fail | Fall back to Groq for what it can handle |
| Groq key fails | Rotate through 4 keys |
| Firecrawl exhausted | Fall back to Jina Reader for static pages |
| All search tools fail | Use pre-seeded database only, mark as CACHED |

### 15.2 Exhibition-Day Safeguards

- Pre-cached Mode: 5 complete demo runs cached in SQLite — works fully offline
- Graceful Degradation: If live search fails, system uses cached data with "Using cached intelligence" indicator
- Timeout Protection: Each agent/workflow has a 30-second timeout
- Mobile Hotspot: Backup internet
- Screen Recording: Pre-recorded video as last-resort

---

## 16. Cost Estimation & Budget

### 16.1 Development Costs

| Item | Cost | Notes |
|:---|:---|:---|
| Gemini API | Free tier | Sufficient for development |
| Groq API | Free tier | Generous free limits |
| Tavily (5 keys) | Free tier | 5000 searches/month total |
| Firecrawl (3 keys) | Free tier | 1500 credits/month total |
| Jina Reader | Free tier | Generous |
| PostgreSQL + Redis + ChromaDB | Free (Docker) | Local |
| Total | 0 USD / 0 PKR | Everything on free tiers |

### 16.2 Exhibition Day Costs

| Item | Cost | Notes |
|:---|:---|:---|
| API usage during live demo | ~PKR 500-1500 | Gemini Flash is cheap |
| Poster printing | ~PKR 3000-5000 | Optional |
| Total | ~PKR 5000-7000 | Minimal |

---

## Appendix A: Project Directory Structure

```
SCHOLARX/
|-- Agents.md                          # This document
|-- docker-compose.yml                 # Local dev infrastructure
|-- .env                               # API keys (NEVER commit to git)
|-- .env.example                       # Template without actual keys
|-- .gitignore                         # Must include .env
|
|-- backend/
|   |-- pyproject.toml
|   |-- main.py                        # FastAPI app entry
|   |-- config.py                      # Settings + key rotation
|   |
|   |-- api/routes/
|   |   |-- discover.py                # POST /api/discover
|   |   |-- stream.py                  # GET /api/stream/{session_id}
|   |   |-- resume.py                  # POST /api/sessions/{id}/resume
|   |   |-- profile.py                 # Profile management
|   |   |-- sessions.py                # Session history CRUD
|   |   +-- scholarships.py            # Scholarship queries
|   |
|   |-- agents/                        # LLM-powered agents
|   |   |-- orchestrator.py
|   |   |-- profile_agent.py           # Handles messy docs, asks for re-upload
|   |   |-- discovery_commander.py
|   |   |-- document_agent.py
|   |   |-- verification_agent.py
|   |   |-- skeptic_agent.py
|   |   +-- advisor_agent.py
|   |
|   |-- workflows/                     # Deterministic workflows
|   |   |-- scouts/
|   |   |   |-- base_scout.py          # Shared scout pipeline
|   |   |   |-- europe_scout.py
|   |   |   |-- asia_scout.py
|   |   |   |-- americas_scout.py
|   |   |   |-- mena_scout.py
|   |   |   +-- oceania_scout.py
|   |   |-- eligibility.py             # 15-dimension deterministic check
|   |   |-- cost_analyzer.py           # PKR lookup tables + arithmetic
|   |   |-- deadline.py                # Date math + Pakistan lead times
|   |   |-- synthesis.py               # Data aggregation + conflict rules
|   |   +-- ranking.py                 # Weighted formula
|   |
|   |-- graph/
|   |   |-- state.py                   # Global state schema
|   |   |-- nodes.py                   # Graph node functions
|   |   |-- edges.py                   # Conditional edge logic
|   |   +-- builder.py                 # StateGraph construction
|   |
|   |-- tools/
|   |   |-- tavily_search.py           # 5-key rotation
|   |   |-- firecrawl_scrape.py        # 3-key rotation
|   |   |-- jina_reader.py             # 1 key + Firecrawl fallback
|   |   |-- crawl4ai_batch.py          # Batch crawler (self-hosted)
|   |   |-- pdf_parser.py              # PyMuPDF + pdfplumber + Docling
|   |   +-- scholarship_db.py          # DB query tool
|   |
|   |-- schemas/                       # Pydantic models
|   |   |-- student.py                 # Pakistan-optimized profile
|   |   |-- scholarship.py             # With pakistan_specific_requirements
|   |   |-- evidence.py
|   |   |-- events.py
|   |   |-- scoring.py
|   |   |-- session.py                 # Session history schemas
|   |   +-- roadmap.py
|   |
|   |-- events/
|   |   |-- bus.py                     # Redis Pub/Sub (localhost)
|   |   |-- emitter.py
|   |   +-- stream.py                  # SSE streaming
|   |
|   |-- db/
|   |   |-- postgres_models.py         # SQLAlchemy models
|   |   |-- session_store.py           # SQLite session CRUD
|   |   |-- seed.py                    # Seed data loader
|   |   +-- cache.py                   # Redis + TTL cache logic
|   |
|   |-- utils/
|   |   |-- api_keys.py                # Multi-key rotation utility
|   |   |-- gpa_converter.py           # Pakistani percentage/GPA conversion
|   |   |-- pakistan_costs.py           # PKR cost lookup tables
|   |   |-- country_data.py
|   |   +-- date_utils.py
|   |
|   +-- tests/
|       |-- test_agents/
|       |-- test_workflows/
|       |-- test_tools/
|       |-- test_key_rotation/
|       +-- fixtures/
|           +-- sample_pakistani_profiles/
|
|-- frontend/
|   |-- package.json
|   |-- next.config.js
|   |-- tailwind.config.js
|   |
|   |-- app/
|   |   |-- layout.tsx
|   |   |-- page.tsx                   # Landing page
|   |   |-- hunt/page.tsx              # Main dashboard
|   |   +-- sessions/page.tsx          # Session history page
|   |
|   |-- components/
|   |   |-- brain-map/                 # Agent Brain Map
|   |   |-- world-map/                 # Global Discovery Map
|   |   |-- scholarship/               # Cards, DNA, Evidence, Debate
|   |   |-- mission-control/           # Mission Control, Timeline, Stats
|   |   |-- profile/                   # Student intake (Pakistan fields)
|   |   |-- sessions/                  # Session history sidebar
|   |   |-- controls/                  # Judge interaction controls
|   |   +-- ui/                        # Shared components
|   |
|   |-- hooks/
|   |   |-- useSSEStream.ts
|   |   |-- useAgentState.ts
|   |   |-- useMissionStore.ts
|   |   +-- useSessionHistory.ts       # Session management hook
|   |
|   +-- lib/
|       |-- api.ts
|       |-- events.ts
|       +-- constants.ts
|
|-- data/
|   |-- scholarships/                  # Pre-seeded scholarship JSON
|   |   |-- europe.json                # Stipendium Hungaricum, DAAD, etc.
|   |   |-- asia.json                  # CSC, MEXT, GKS, etc.
|   |   |-- americas.json              # Fulbright, US PhDs, etc.
|   |   |-- mena.json                  # Turkiye Burslari, KAUST, etc.
|   |   +-- oceania.json               # Australia Awards, etc.
|   |-- pakistan_costs.json             # PKR cost lookup tables
|   |-- pakistan_education.json         # Board names, grading systems
|   |-- profiles/                      # Sample Pakistani profiles
|   |   |-- ics_student.json
|   |   |-- fsc_student.json
|   |   |-- bs_graduate.json
|   |   |-- bba_graduate.json
|   |   +-- working_professional.json
|   |-- countries.json
|   +-- scholarx_sessions.db           # SQLite session database
+
```

---

## Appendix B: Key Talking Points for Judges

### What Makes ScholarX Different?

1. **"Built specifically for Pakistani students — understands HEC, IBCC, MOFA, and the real cost in PKR."**
2. **"Our agents don't blindly trust the first result. They investigate and challenge each other."**
3. **"We show the cost of 'free' — IELTS fees, HEC attestation, visa charges — all in PKR."**
4. **"Some steps are agents (need intelligence), others are workflows (need reliability). We use the right tool for each job."**
5. **"The system remembers. Every hunt makes the next one faster and smarter."**
6. **"Multiple API keys with automatic failover — if one key fails, the system keeps running."**
7. **"Every conclusion is traceable. Click any score to see the evidence trail."**

### Technical Depth Points

- **Workflow-First:** Deterministic workflows for eligibility, cost, deadline, ranking (no hallucination)
- **Agent Where Needed:** LLM agents only for tasks requiring judgment (profile parsing, verification, skeptic)
- **Multi-Key Failover:** 5 Tavily + 3 Firecrawl + 3 Gemini + 4 Groq keys with automatic rotation
- **Session Persistence:** SQLite-based history with TTL-aware caching
- **Pakistan Optimization:** HEC bilateral bonus in scoring, PKR cost tables, IBCC/MOFA awareness
- **Event-Driven UI:** Real SSE events from agents/workflows drive truthful animations

---

## Appendix C: Exhibition Taglines

> *"12 AI agents. 6 continents. 1 mission: A Pakistani student's future."*
> *"We don't search. We investigate."*
> *"The first AI system that tells you the real cost of 'free' — in PKR."*
> *"Watch AI agents disagree — and reach a better answer."*
> *"Built for Pakistan. Powered by intelligence."*

---

*Document Version: 2.0*
*Created: September 1, 2026*
*Updated: September 1, 2026*
*Project: ScholarX — The Autonomous Scholarship Intelligence Network for Pakistani Students*
