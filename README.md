<div align="center">

# 🎓 ScholarX

### Autonomous Multi-Agent Scholarship Intelligence & Counseling System

[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2015-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-FF4F00?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![SQLite](https://img.shields.io/badge/Storage-SQLite%20WAL-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <b>A state-of-the-art dual-engine counseling platform engineered for Pakistani and international students to discover, evaluate, stress-test, and win fully-funded global scholarships.</b>
</p>

[Quickstart](#-quickstart-in-3-minutes) •
[Key Features](#-key-features) •
[Architecture](#-system-architecture) •
[Environment Setup](#-configuration--environment-variables) •
[Developer Commands](#-developer-cheat-sheet) •
[FAQ](#-frequently-asked-questions)

---

</div>

## 🌟 Overview

Winning a fully-funded international scholarship transforms lives, yet millions of qualified students—particularly from Pakistan and developing nations—are eliminated every year due to fragmented information, opaque eligibility requirements, hidden testing hurdles, and complex currency conversion math.

**ScholarX** solves this with an **autonomous multi-agent system** and **deterministic calculation engine**:
1. **Zero-Hallucination Logic**: Hard criteria (GPA minimums, age limits, testing deadlines, and Pakistani Rupee living expense benchmarks) are calculated deterministically in Python—never guessed by LLMs.
2. **Multi-Agent Intelligence**: 4 specialized AI agents collaborate across a 10-node LangGraph pipeline to match, audit, red-team, and roadmap your admissions journey.
3. **Command Theatre UI**: A futuristic Obsidian glassmorphism interface with an interactive D3-Geo world projection, real-time Server-Sent Events (SSE) telemetry, tactile audio, and instant PDF dossier generation.

---

## ✨ Key Features

### 🎯 1. Deterministic Matching & Pakistan Localization
* **Authentic Academic Standards**: First-class support for **BISE Matric/FSc**, **Cambridge O/A-Levels**, **IBCC equivalence** calculations, and **HEC recognized degrees** (Tiers 1-4).
* **True PKR Cost Modeling**: Computes realistic flight, visa, living, and insurance costs in Pakistani Rupees (PKR) alongside official scholarship stipends using localized cost data (`data/pakistan_costs.json`).
* **Provincial & Quota Awareness**: Accounts for regional and provincial quota considerations (Punjab, Sindh, KPK, Balochistan, AJK, GB).

### 🤖 2. The 4-Agent LangGraph Crew
* **🔍 Scout Agent**: Rapidly queries 310+ deep dossiers and live search APIs to surface high-probability programs tailored to the candidate's degree, target country, and financial need.
* **📋 Evaluator Agent**: Performs an unforgiving line-by-line audit of minimum eligibility criteria (GPA, IELTS/TOEFL/GRE requirements, research publications, and field restrictions).
* **🛡️ Skeptic Agent**: Plays adversarial devil's advocate to stress-test application weaknesses, visa risks, and hidden competitive hurdles before submission.
* **🗺️ Roadmap Architect**: Synthesizes findings into an actionable, chronologically ordered milestone strategy complete with deadline runway alerts.

### ⚡ 3. Command Theatre Frontend
* **Obsidian Dark Glassmorphism**: Clean, accessibility-compliant aesthetic (contrast ratio ≥ 7:1) built with Next.js 15, React 19, and Tailwind CSS.
* **Interactive D3-Geo World Stage**: Visualizes global scholarship destination clusters with real-time fly-to transitions and regional metrics.
* **Real-time SSE Stream**: Watch agents analyze, debate, and score dossiers live via structured Server-Sent Events.
* **One-Click Dossier PDF**: Instant generation of executive-grade scholarship analysis dossiers ready to print or share.

### 📚 4. Exhaustive 310+ Curated Dossiers
Pre-seeded database covering premier opportunities across 5 continents:
* **Americas (65)**: Fulbright Foreign Student Program, Knight-Hennessy, rotary fellowships, OAS.
* **Europe (101)**: Erasmus Mundus Joint Masters, DAAD (Germany), Chevening & Commonwealth (UK), Eiffel Excellence (France), Stipendium Hungaricum.
* **Asia (81)**: MEXT (Japan), Chinese Government Scholarship (CSC / Silk Road), Global Korea Scholarship (GKS), Singapore SINGA, Taiwan ICDF.
* **Middle East & North Africa (43)**: King Fahd University (KFUPM), KAUST Fellowship, Qatar University, Turkiye Burslari.
* **Oceania (20)**: Australia Awards, Melbourne Research Scholarships, New Zealand Manaaki.

---

## 🚀 Quickstart in 3 Minutes

Follow these 4 simple steps to run ScholarX locally.

### Prerequisites
* **Node.js**: v18.0.0 or later (v20+ recommended) — `node -v`
* **Python**: v3.11 or v3.12 — `python3 -v`
* **Git**: `git -v`

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/Hamza-Gohar/ScholarX.git
cd ScholarX
```

### Step 2: Install Dependencies

#### Frontend (Next.js):
```bash
cd frontend
npm install
cd ..
```

#### Backend (Python Virtual Environment):
```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Copy the template to `.env`:
```bash
cp .env.example .env
```
Open `.env` and add at least one **Gemini API Key** or **Groq API Key**:
```env
GEMINI_API_KEY_1=your_gemini_api_key_here
# or
GROQ_API_KEY_1=your_groq_api_key_here
```
*(Tip: ScholarX includes multi-key rotation! You can supply up to 13 Groq keys and 3 Gemini keys for automatic round-robin load distribution).*

### Step 4: Launch ScholarX
Run the entire stack (FastAPI backend + Next.js frontend) with a single command:
```bash
npm run dev
# or
make dev
```

That's it! 🎉
* **🌐 Web Application**: [http://localhost:3000](http://localhost:3000)
* **📑 Interactive API Docs (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **🏥 Backend Health Endpoint**: [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

## ⚙️ Configuration & Environment Variables

ScholarX manages rotating API key pools to ensure 100% uptime without hitting rate limits.

| Variable | Description | Default / Example | Required? |
| :--- | :--- | :--- | :---: |
| `GEMINI_API_KEY_1..3` | Google Gemini API keys for deep reasoning | `AIzaSy...` | Optional* |
| `GEMINI_PRIMARY_MODEL` | Primary Gemini model identifier | `gemini-2.5-flash` | No |
| `GROQ_API_KEY_1..13` | Groq high-speed inference API keys | `gsk_...` | Optional* |
| `GROQ_MODEL` | Default Groq model | `llama-3.3-70b-versatile` | No |
| `TAVILY_API_KEY_1..7` | Tavily search keys for live deadline scrapers | `tvly-...` | No (Cached) |
| `FIRECRAWL_API_KEY_1..6` | Firecrawl API keys for deep page crawling | `fc-...` | No (Cached) |
| `SESSION_DB_PATH` | Path to persistent SQLite database | `./data/scholarx_sessions.db`| No |

*\*At least one LLM key (either Gemini or Groq) is required for conversational counseling and deep analysis.*

---

## 🛠️ Developer Cheat Sheet

ScholarX comes with full `Makefile` and `npm` scripts:

| Task | Command | Description |
| :--- | :--- | :--- |
| **Start Full Stack** | `make dev` or `npm run dev` | Runs FastAPI (:8000) & Next.js (:3000) concurrently |
| **Backend Only** | `make backend` | Starts FastAPI with hot-reload |
| **Frontend Only** | `make frontend` | Starts Next.js frontend on port 3000 |
| **System Diagnostics** | `make doctor` or `npm run doctor` | Runs the 48-point environment and DB health check |
| **Run Fast Tests** | `make test-fast` | Runs schema validation and API key pool tests (<0.5s) |
| **Run Full Test Suite** | `make test` | Executes all backend pytest suites |
| **Seed Database** | `make seed` | Re-seeds 310 scholarships and benchmark student profiles |
| **System Primer** | `make primer` | Prints high-density architectural primer (~1,500 tokens) |

---

## 📁 Repository Tour

```text
SCHOLARX/
├── backend/
│   ├── agents/            # Scout, Evaluator, Skeptic, and Roadmap LLM agents
│   ├── api/               # FastAPI route definitions (sessions, scholarships, students)
│   ├── db/                # SQLite database models, aiosqlite handlers, and seed scripts
│   ├── events/            # Server-Sent Events (SSE) streaming engine
│   ├── graph/             # 10-node LangGraph StateGraph orchestration
│   ├── schemas/           # Pydantic v2 domain schemas & validation models
│   ├── tests/             # Pytest test suites (security, schema, workflows)
│   ├── tools/             # Search tools, scrapers, and document parsers
│   └── workflows/         # Deterministic scoring, checklist math & ranking algorithms
├── frontend/
│   ├── app/               # Next.js 15 App Router pages & API routes
│   ├── components/        # Obsidian glassmorphism UI components (Command Theatre, Stage)
│   ├── hooks/             # Custom React hooks (useSSE, useScholarships)
│   ├── lib/               # Utility functions, sound effects, and API client
│   └── store/             # Zustand v5 global state stores
├── data/
│   ├── scholarships/      # 310 JSON scholarship dossiers organized by continent
│   ├── pakistan_costs.json       # Localized PKR cost benchmarks (visas, flights, living)
│   └── pakistan_education.json   # BISE / IBCC / HEC conversion tables
├── docs/                  # Architecture Decision Records (ADRs) and design guides
├── exhibition_slides/     # Korean Minimalist interactive pitch deck & PDF builder
├── scripts/               # System doctor, context engine, and database curators
├── package.json           # Root package script runner
├── Makefile               # CLI shortcut targets
└── README.md              # Project documentation
```

---

## 🧠 System Architecture

```text
                      Candidate Profile / Resume
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │ Deterministic Intake  │ ◄── Validates GPA, Degree,
                     │  & Benchmark Engine   │     Field & Pakistan Equivalence
                     └──────────┬────────────┘
                                │
                                ▼
                   ┌───────────────────────────┐
                   │  10-Node LangGraph Graph  │
                   └─────────────┬─────────────┘
                                 │
         ┌───────────────────────┼──────────────────────┐
         ▼                       ▼                      ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Scout Agent   │    │ Evaluator Agent  │    │  Skeptic Agent  │
│ Surfaces top    │    │ Rigorous hard    │    │ Stress-tests    │
│ matches from    │───►│ eligibility and  │───►│ profile flaws,  │
│ 310+ dossiers   │    │ criteria audit   │    │ risks & hurdles │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
                                              ┌──────────────────┐
                                              │ Roadmap Agent    │
                                              │ Milestones &     │
                                              │ Action Checklist │
                                              └────────┬─────────┘
                                                        │
                                                        ▼
                                              ┌──────────────────┐
                                              │ Command Theatre  │
                                              │ Real-Time SSE    │
                                              │ UI & PDF Dossier │
                                              └──────────────────┘
```

---

## ❓ Frequently Asked Questions

<details>
<summary><b>1. Can I run ScholarX completely offline without API keys?</b></summary>
<br>
Yes! The deterministic matching engine, 310 seeded scholarships, database viewer, and Pakistan equivalence calculators run locally on SQLite without needing an active internet connection or LLM API keys. You only need API keys when invoking real-time conversational counseling or live agent debates.
</details>

<details>
<summary><b>2. Port 8000 or Port 3000 is already in use. How do I change them?</b></summary>
<br>
To change the backend port, run:
```bash
PYTHONPATH=backend .venv/bin/python -m uvicorn main:app --port 8080 --reload
```
To change the frontend port:
```bash
cd frontend && npm run dev -- -p 3001
```
</details>

<details>
<summary><b>3. How do I run the system health check?</b></summary>
<br>
ScholarX includes a built-in diagnostic tool that tests 48 environment invariants:
```bash
make doctor
# or
.venv/bin/python scripts/doctor.py
```
</details>

<details>
<summary><b>4. How do I build the Exhibition Slide Deck?</b></summary>
<br>
ScholarX includes an editorial Korean Minimalist presentation engine:
```bash
cd exhibition_slides
python3 build_deck.py
```
This builds an interactive HTML web deck, high-resolution PDF, and native PowerPoint presentation.
</details>

---

## 📄 License & Credits

Built with pride by **Hamza Gohar** & the ScholarX team for students worldwide.  
Released under the [MIT License](LICENSE).

<div align="center">
  <sub>ScholarX — Empowering the next generation of global scholars. 🎓🇵🇰</sub>
</div>
