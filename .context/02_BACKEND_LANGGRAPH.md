# 🧠 ScholarX — Backend & LangGraph Pipeline Reference

> **Deep-dive manual for the FastAPI backend, 10-node StateGraph, and Multi-Agent Network.**

---

## 1. Central State: `ScholarXState`

The entire pipeline operates on a centralized, type-safe dictionary defined in `backend/graph/state.py`:

```python
class ScholarXState(TypedDict):
    session_id: str
    student_profile: Optional[StudentProfile]
    search_strategy: Optional[Dict[str, Any]]
    raw_candidates: Annotated[List[Scholarship], add]  # Appended across parallel scouts
    deduped_candidates: List[Scholarship]
    eligibility_results: Dict[str, EligibilityResult]  # Keyed by scholarship_id
    cost_results: Dict[str, CostAnalysisResult]
    deadline_results: Dict[str, DeadlineAnalysisResult]
    skeptic_challenges: Dict[str, List[SkepticChallenge]]
    synthesized_cards: List[SynthesizedScholarshipCard]
    ranked_scholarships: List[RankedScholarship]
    roadmap: Optional[ApplicationRoadmap]
    errors: Annotated[List[str], add]
    current_node: str
    execution_time_ms: float
```

---

## 2. The 10 Pipeline Nodes

The graph is compiled linearly in `backend/graph/builder.py` using sequential edges for guaranteed execution stability:

| # | Node Name | Implementation | Functionality |
|:---|:---|:---|:---|
| **1** | `profile_analyzer` | `backend/agents/profile_agent.py` | Extracts structured `StudentProfile`, normalizes GPA, identifies missing documents |
| **2** | `discovery_commander`| `backend/agents/discovery_commander.py`| Formulates 5 regional queries, triggers scouts, deduplicates candidates via token-set Jaccard |
| **3** | `regional_scouts` | `backend/workflows/scouts/` | Runs 5 regional scouts (Europe, Asia, Americas, MENA, Oceania) with 6-stage search/scrape pipelines |
| **4** | `eligibility_analyzer`| `backend/workflows/eligibility.py` | 15-dimension deterministic audit: GPA, age, degree level, field, HEC HAT, MOI English waivers |
| **5** | `cost_analyzer` | `backend/workflows/cost_analyzer.py` | Calculates true out-of-pocket costs in PKR (pre-app, application, visa/travel, settlement) |
| **6** | `deadline_analyzer` | `backend/workflows/deadline.py` | Risk-tiered deadline runway with Pakistani administrative lead times (HEC, MOFA, IELTS) |
| **7** | `skeptic_agent` | `backend/agents/skeptic_agent.py` | Adversarial audit: return bonds, visa appointment backlogs, blocked accounts, supervisor gate |
| **8** | `synthesis_engine` | `backend/workflows/synthesis.py` | Reconciles signals, merges costs & challenges into unified `SynthesizedScholarshipCard` objects |
| **9** | `ranking_engine` | `backend/workflows/ranking.py` | Deterministic composite scoring formula (0-100) and candidate ordering |
| **10**| `advisor_agent` | `backend/agents/advisor_agent.py` | Generates 6-phase chronological execution journey + Pakistani Office Directory routing |

---

## 3. The 4 LLM Agents

### 1. ProfileAgent (`backend/agents/profile_agent.py`)
- Ingests student CV/Transcripts (PDF, DOCX, TXT via `document_parser.py`).
- Uses Groq (`qwen/qwen3.8-27b`) or Gemini (`gemini-flash-latest`) to extract Pydantic `StudentProfile`.
- Powers conversational counselor chat for refining missing fields.

### 2. DiscoveryCommander (`backend/agents/discovery_commander.py`)
- Evaluates student background, degree target, and financial constraints.
- Generates 5 distinct search queries tailored to regional bilateral opportunities.
- Dispatches scouts and deduplicates candidates (Jaccard similarity threshold > 0.7).

### 3. SkepticAgent (`backend/agents/skeptic_agent.py`)
- Employs an adversarial persona: "Admissions skeptic for Pakistani applicants".
- Analyzes top 6 high-ranking candidates to find hidden traps:
  - *Germany*: Blocked bank account (€11,904 = ~PKR 3.7M upfront cash).
  - *Fulbright*: 5-year mandatory return bond (HEC legal undertaking).
  - *Hungary*: Dual-gate bottleneck (HEC nomination != university admission).
  - *Visa*: Islamabad VFS Gerry's appointment delays (8-14 weeks).
- Uses modern Google GenAI SDK (`from google import genai`) with Groq fallback.

### 4. AdvisorAgent (`backend/agents/advisor_agent.py`)
- Synthesizes the final recommendations into a 6-phase actionable roadmap:
  1. *Phase 1*: Document Attestation & Equivalences (IBCC, HEC, MOFA)
  2. *Phase 2*: Standardized Testing & Language (IELTS, HEC HAT)
  3. *Phase 3*: Admissions & Portal Submissions
  4. *Phase 4*: Dual-Gate Interviews & Nominations
  5. *Phase 5*: Visa Application & Financial Proof
  6. *Phase 6*: Pre-Departure & Settlement
- Embeds verified Pakistani Office Directory entries (HEC H-9 Islamabad, IBCC G-10/4, Gerry's Visa Centre).

---

## 4. The 7 Deterministic Workflows

1. **Regional Scouts (`backend/workflows/scouts/`)**:
   - `BaseScout`: 6-stage lifecycle: `DEPLOY` → `SEARCH` → `SCRAPE` → `EXTRACT` → `FILTER` → `COMPLETE`.
   - Scout implementations for `EuropeScout`, `AsiaScout`, `AmericasScout`, `MenaScout`, `OceaniaScout`.
   - Tool chain: Tavily search → Jina Reader markdown extraction → Firecrawl deep scraper fallback.
2. **EligibilityInvestigator (`backend/workflows/eligibility.py`)**:
   - 15 criteria checked: degree level, minimum GPA, age limit, citizenship, field of study, IELTS/TOEFL waiver status, HEC HAT/USAT requirement, work experience, etc.
3. **TrueCostAnalyzer (`backend/workflows/cost_analyzer.py`)**:
   - 4-phase expense waterfall based on `data/pakistan_costs.json`:
     - Phase 1: Pre-Application (IELTS PKR 75.6k, HEC attestation PKR 10k, IBCC PKR 7.5k, Passport PKR 5.5k)
     - Phase 2: Application (Portal fees + 10% FBR advance tax Section 236Y)
     - Phase 3: Visa & Travel (Embassy fee, biometric, flight ticket PKR 180k-350k)
     - Phase 4: Initial Settlement (1st month deposit & food PKR 150k-300k)
4. **DeadlineIntelligence (`backend/workflows/deadline.py`)**:
   - Calculates exact calendar runway and subtracts Pakistani administrative lead times (HEC attestation 21-28 days, passport renewal 14 days, visa appointment 60 days).
5. **SynthesisWorkflow (`backend/workflows/synthesis.py`)**:
   - Compiles multidimensional audit results into complete DNA cards.
6. **RankingEngine (`backend/workflows/ranking.py`)**:
   - Deterministic 8-factor composite arithmetic formula (see §5).

---

## 5. Deterministic Ranking Formula

ScholarX uses **100% transparent arithmetic scoring** with zero LLM variance:

$$\text{Score} = (0.25 \times E) + (0.25 \times F) + (0.10 \times B) + (0.10 \times A) + (0.10 \times D) + (0.10 \times T) + (0.05 \times V) + (0.05 \times C)$$

Where:
- $E$ = **Eligibility Match** (0-100, hard requirement fulfillment)
- $F$ = **Funding Coverage** (0-100, full tuition + stipend + housing = 100)
- $B$ = **Bilateral Quota Advantage** (0-100, HEC/Government quota seats)
- $A$ = **Academic Acceptance Probability** (0-100, GPA & profile strength)
- $D$ = **Deadline Runway** (0-100, sufficient preparation slack)
- $T$ = **True Cost Feasibility** (0-100, PKR out-of-pocket alignment with student budget)
- $V$ = **Verification Confidence** (0-100, verified official sources)
- $C$ = **Pakistani Candidate Acceptance History** (0-100, known track record)

---

## 6. KeyManager & Rotation Infrastructure

Defined in `backend/utils/api_keys.py`:
- Manages **30 total API keys**:
  - Groq (13 keys) — primary LLM
  - Google Gemini (3 keys) — fallback LLM & complex reasoning
  - Tavily (7 keys) — academic search
  - Firecrawl (6 keys) — deep JavaScript scraping
  - Jina Reader (1 key) — URL-to-markdown reader
- **Per-request rotation**: Every individual query switches to the next available key in the round-robin cycle.
- **Fault Tolerance**: If a key receives a 429 (rate limit) or 503, it enters a 60-second cooldown period, and the request instantly retries on the next key without halting the pipeline.
