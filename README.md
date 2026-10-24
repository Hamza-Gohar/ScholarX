# ScholarX

Autonomous multi-agent scholarship intelligence and admissions counseling system.

ScholarX pairs deterministic validation logic with a multi-agent backend to evaluate applicants against 510 curated scholarship programs worldwide across 5 continental regions. It is built specifically with Pakistani academic credentials (BISE Matric/FSc, Cambridge O/A-Levels, IBCC equivalence, and HEC-recognized university tiers) and realistic Pakistani Rupee (PKR) living expense modeling.

---

## Table of Contents

- [Core Design](#core-design)
- [System Architecture](#system-architecture)
- [AI Agent & Context System](#ai-agent--context-system)
- [Quickstart](#quickstart)
- [Configuration and Environment Variables](#configuration-and-environment-variables)
- [Developer Commands](#developer-commands)
- [Repository Structure](#repository-structure)
- [Database and Offline Execution](#database-and-offline-execution)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Core Design

ScholarX avoids common LLM pitfalls by separating math and rules from language generation:

1. **Deterministic logic for rules and finances**: Hard eligibility checks (minimum GPA, degree requirements, language score cutoffs, and testing deadlines) and cost calculations (stipends vs. local PKR visa, flight, and living expenses) run as pure Python code in `backend/workflows/`. LLMs are never asked to calculate numbers or make up policy rules.
2. **LLMs for qualitative analysis**: Agent calls in `backend/agents/` handle qualitative tasks: parsing resumes and student background, summarizing selection criteria, red-teaming profile weaknesses, and drafting personalized preparation roadmaps.
3. **Pakistan localization**: Includes Pakistani credential conversions (such as Cambridge grades to IBCC percentage equivalents) and localized cost projections in Pakistani Rupees using `data/pakistan_costs.json` and `data/pakistan_education.json`.
4. **Command Theatre frontend**: A Next.js 15 interface built with Tailwind CSS and Zustand, featuring an interactive D3-Geo world projection map, live Server-Sent Events (SSE) telemetry, and PDF dossier generation.
5. **Offline & typo resilience**: Deterministic fuzzy taxonomy matching in `backend/workflows/field_matching.py` resolves student academic fields even with misspellings (e.g. `compter scince` ➔ `Computer Science`) completely offline.
6. **Serverless portability**: Next.js 15 features built-in Node 22 `node:sqlite` client support (`frontend/lib/db/sqliteClient.ts`), enabling zero-proxy queries locally and on serverless platforms.

---

## System Architecture

ScholarX executes admissions intelligence through a structured pipeline supervised by an Orchestrator Agent. The architecture separates qualitative reasoning (**Agents**, powered by LLMs) from deterministic calculations (**Workflows**, executed in Python):

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                              ORCHESTRATOR AGENT                              │
│                                                                              │
│                         ┌────────────────────────────┐                       │
│                         │      PROFILE ANALYSER      │ ──► AGENT             │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │    DISCOVERY COMMANDER     │ ──► AGENT             │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│         ┌──────────────────────────────────────────────────────────┐         │
│         │                         WORKFLOW                         │         │
│         │ ┌─────────┐  ┌──────┐  ┌────────┐  ┌──────┐  ┌─────────┐ │         │
│         │ │ AMERICA │  │ ASIA │  │ EUROPE │  │ MENA │  │AUSTRALIA│ │         │
│         │ └─────────┘  └──────┘  └────────┘  └──────┘  └─────────┘ │         │
│         └─────────────────────────────┬────────────────────────────┘         │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │  ELIGIBILITY INVESTIGATOR  │ ──► WORKFLOW          │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │     TRUE COST ANALYZER     │ ──► WORKFLOW          │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │      DEADLINE CHECKER      │ ──► WORKFLOW          │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │       SKEPTIC AGENT        │ ──► AGENT             │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │      SYNTHESIS ENGINE      │ ──► WORKFLOW          │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │       RANKING ENGINE       │ ──► WORKFLOW          │
│                         └─────────────┬──────────────┘                       │
│                                       ▼                                      │
│                         ┌────────────────────────────┐                       │
│                         │       ADVISER AGENT        │ ──► AGENT             │
│                         └────────────────────────────┘                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Pipeline Components

| Stage | Classification | Responsibility |
| :--- | :--- | :--- |
| **Orchestrator Agent** | Agent (Director) | Oversees the full pipeline, coordinates state transitions, and manages SSE telemetry streams. |
| **Profile Analyser** | Agent | Extracts candidate academic credentials, normalizes Pakistani grading systems (BISE/FBISE), Cambridge A-Levels, and English requirements. |
| **Discovery Commander** | Agent | Translates normalized candidate goals into targeted regional queries across scholarship databases and search scrapers. |
| **Regional Scouts** | Workflow | Five parallel pipelines scanning 510+ deep dossiers across Europe (161), Asia (131), Americas (105), MENA (73), and Oceania (40). |
| **Eligibility Investigator** | Workflow | Applies deterministic 15-dimension audits to verify hard requirements: HEC degree recognition, 16-year equivalence, GPA cutoffs, and age caps. |
| **True Cost Analyzer** | Workflow | Calculates 4-phase expenses in Pakistani Rupees (PKR): initial test fees, visa and embassy costs, airfare, and settling-in allowances versus official stipends. |
| **Deadline Checker** | Workflow | Calculates application runways, dual-gate deadlines (HEC nomination vs university deadline), and visa appointment lead times. |
| **Skeptic Agent** | Agent | Red-teams candidate applications to identify risk factors, return-to-home bonds, hidden bench fees, and competition bottlenecks. |
| **Synthesis Engine** | Workflow | Merges deterministic eligibility and cost data with qualitative risk alerts into a structured evaluation payload. |
| **Ranking Engine** | Workflow | Calculates an 8-factor composite match index (0-100) based on eligibility match, PKR financial burden, acceptance likelihood, and deadline feasibility. |
| **Adviser Agent** | Agent | Formulates an actionable roadmap, personalized milestone calendar, document preparation guide, and contingency options. |

---

## AI Agent & Context System

ScholarX features a built-in **Universal Multi-Agent Context System** allowing any AI agent (Claude Code, Antigravity, Cursor, Devin, OpenAI Operator, Copilot) to drop in with a fresh context window and begin working in under 60 seconds without token bloat or hallucination:

- **60-Second Primer**: [`.context/00_QUICKSTART.md`](.context/00_QUICKSTART.md) (<1,800 tokens).
- **Universal Standards**: [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md), [`CONTEXT.md`](CONTEXT.md), [`.cursorrules`](.cursorrules), and [`.gemini/rules/`](.gemini/rules/).
- **Dynamic Context CLI** (`scripts/context.py`):
  ```bash
  python scripts/context.py primer      # Concentrated ~1,500 token system overview
  python scripts/context.py status      # Real-time database counts, API keys, ports, and active task
  python scripts/context.py validate    # Self-healing validation of context vs code contracts (31 checks)
  python scripts/context.py inspect db  # Targeted subsystem manual (backend, frontend, db, api)
  ```
- **Hierarchical Documentation**: Modular context manuals in [`.context/`](.context/) covering architecture, LangGraph nodes, frontend Command Theatre, SQLite schemas, REST/SSE APIs, decisions (ADRs 001-014), developer playbooks, and active task scratchpad (`CURRENT_TASK.md`).

---

## Quickstart

Follow these steps to run ScholarX locally.

### Prerequisites

- **Node.js**: v18.0.0 or later (v20+ recommended)
- **Python**: v3.11 or v3.12
- **Git**

### 1. Clone the repository

```bash
git clone https://github.com/Hamza-Gohar/ScholarX.git
cd ScholarX
```

### 2. Install dependencies

Install frontend dependencies:

```bash
cd frontend
npm install
cd ..
```

Create a Python virtual environment and install backend packages:

```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the sample environment file:

```bash
cp .env.example .env
```

Open `.env` and add at least one API key for Gemini or Groq:

```env
GEMINI_API_KEY_1=your_gemini_key_here
# or
GROQ_API_KEY_1=your_groq_key_here
```

ScholarX supports round-robin key rotation across up to 13 Groq keys and 3 Gemini keys to prevent rate limit bottlenecks.

### 4. Start the application

Run both the FastAPI backend and Next.js frontend with one command:

```bash
npm run dev
# or
make dev
```

The application runs on:

- **Frontend interface**: http://localhost:3000
- **Interactive API documentation (Swagger)**: http://localhost:8000/docs
- **Health check endpoint**: http://localhost:8000/api/health

---

## Configuration and Environment Variables

| Variable | Description | Example | Required |
| :--- | :--- | :--- | :---: |
| `GEMINI_API_KEY_1..3` | Google Gemini keys for deep analysis | `AIzaSy...` | Optional* |
| `GEMINI_PRIMARY_MODEL` | Primary Gemini model identifier | `gemini-2.5-flash` | No |
| `GROQ_API_KEY_1..13` | Groq keys for low-latency reasoning | `gsk_...` | Optional* |
| `GROQ_MODEL` | Default Groq model | `llama-3.3-70b-versatile` | No |
| `TAVILY_API_KEY_1..7` | Tavily keys for live web search | `tvly-...` | No (Cached) |
| `FIRECRAWL_API_KEY_1..6` | Firecrawl keys for deep URL scraping | `fc-...` | No (Cached) |
| `SESSION_DB_PATH` | Path to the local SQLite database | `./data/scholarx_sessions.db` | No |

\*At least one working LLM API key (Gemini or Groq) is required to run live multi-agent counseling.

---

## Developer Commands

The project root provides shortcuts via `Makefile` and `npm`:

| Command | Action |
| :--- | :--- |
| `make dev` or `npm run dev` | Starts FastAPI (port 8000) and Next.js (port 3000) concurrently |
| `make backend` | Starts the FastAPI backend with hot-reload enabled |
| `make frontend` | Starts the Next.js development server |
| `make doctor` or `npm run doctor` | Runs the 48-point environment and database diagnostic suite |
| `make test-fast` | Runs unit tests for schemas, API keys, and offline typo matching (<1.0s) |
| `make test` | Runs the full pytest test suite (44 test modules) |
| `make seed` | Seeds SQLite with 510 scholarships and benchmark student profiles |
| `make primer` or `npm run context:primer` | Prints high-density architectural overview (~1,500 tokens) |
| `make context` or `npm run context:status` | Prints real-time database, API key, port, and test status |
| `make validate` or `npm run context:validate` | Validates context manuals against code contracts (31 checks) |

---

## Repository Structure

```text
SCHOLARX/
├── backend/
│   ├── agents/            # Scout, Evaluator, Skeptic, and Roadmap agent implementations
│   ├── api/               # FastAPI route definitions (sessions, scholarships, students)
│   ├── db/                # SQLite database models, connection handlers, and seed logic
│   ├── events/            # Server-Sent Events (SSE) streaming engine
│   ├── graph/             # 10-node LangGraph StateGraph orchestration
│   ├── schemas/           # Pydantic v2 schemas and validation contracts
│   ├── tests/             # Pytest test suites (44 modules: security, schemas, offline typo)
│   ├── tools/             # Search clients, scrapers, and document parsers
│   └── workflows/         # Deterministic scoring, field matching, and ranking algorithms
├── frontend/
│   ├── app/               # Next.js 15 App Router pages and API routes
│   ├── components/        # UI components (Command Theatre, Stage, D3 projection, JudgeControlBar)
│   ├── hooks/             # React hooks (useSSE, useScholarships, useDevicePerformance)
│   ├── lib/               # Utility functions, sound effects, db/sqliteClient, cost/deadline engines
│   └── store/             # Zustand v5 state stores
├── data/
│   ├── scholarships/      # 510 scholarship JSON dossiers grouped by region (Europe, Asia, Americas, MENA, Oceania)
│   ├── profiles/          # 6 Pakistani benchmark student profiles
│   ├── pakistan_costs.json       # Pakistan cost benchmarks (visas, flights, living)
│   └── pakistan_education.json   # BISE / IBCC / HEC conversion tables
├── .context/              # Hierarchical multi-agent context hub (00_QUICKSTART to 08_ACTIVE_STATE)
├── docs/                  # Architecture Decision Records (ADRs 001-014) and reference notes
├── exhibition_slides/     # Presentation deck and PDF builder
├── scripts/               # Diagnostics (doctor.py), context engine (context.py), database curators
├── scholarships_database.db      # Standalone SQLite database (512 scholarships)
├── scholarships_database.csv     # Tabular CSV export
├── scholarships_database_viewer.html # Zero-dependency offline interactive browser viewer
├── AGENTS.md              # Universal AI Agent standard entry point
├── CLAUDE.md              # Claude Code / Anthropic operational guide
├── CONTEXT.md             # Human and AI Agent root context index
├── .cursorrules           # Cursor IDE instructions and invariants
├── Makefile               # Task runner shortcuts
├── package.json           # Node scripts and runner configuration
├── requirements.txt       # Root Python dependency specification
└── README.md              # Project documentation
```

---

## Database and Offline Execution

ScholarX uses a local, single-file SQLite database with Write-Ahead Logging (WAL) enabled (`data/scholarx_sessions.db`).

The deterministic matching engine, Pakistan equivalence conversions, offline scholarship catalog (510 dossiers, 512 in standalone database), and database viewer work without third-party services or network calls. External network calls occur only when requesting live web scraping or when invoking LLM agents for conversational counseling.

To test the system offline:

```bash
# 1. Run offline typo-resilient field matching tests
.venv/bin/pytest backend/tests/test_offline_typo_retrieval.py -v

# 2. Check live offline database counts
python scripts/context.py status

# 3. Launch the zero-dependency offline database viewer in your browser
xdg-open scholarships_database_viewer.html
```

---

## Troubleshooting

### Port 8000 or 3000 is already in use

If port 8000 is busy, start FastAPI on another port:

```bash
PYTHONPATH=backend .venv/bin/python -m uvicorn main:app --port 8080 --reload
```

If port 3000 is busy, tell Next.js to use port 3001:

```bash
cd frontend && npm run dev -- -p 3001
```

### Running the environment doctor

Run `doctor.py` to identify missing packages, missing files, or port conflicts:

```bash
.venv/bin/python scripts/doctor.py
```

### Running the context validator

Run `context.py validate` to verify that all documentation and code paths are in sync:

```bash
.venv/bin/python scripts/context.py validate
```

### Python packages not detected

Make sure you run scripts using the virtual environment interpreter (`.venv/bin/python`) rather than your global system Python.

---

## License

Released under the [MIT License](LICENSE).
