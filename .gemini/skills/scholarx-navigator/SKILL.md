---
name: scholarx-navigator
description: Navigate, understand, and work with the ScholarX multi-agent scholarship platform codebase. Use when working on ScholarX.
---

# ScholarX Navigator Skill

## When to Use
Activate when working on the ScholarX project — the autonomous scholarship intelligence platform for Pakistani students at `/mnt/windows/AntiGravity/SCHOLARX`.

## Quick Start for New AI Sessions
1. Read `.scholarx/project.yaml` for the complete project manifest
2. Read `docs/STATUS.md` for what's currently working and what's broken
3. Read `.scholarx/module_map.yaml` to find relevant modules for your task
4. Read `.scholarx/api_surface.yaml` for API contracts and response shapes
5. Read `docs/KNOWN_ISSUES.md` to see tracked bugs before starting work

## Key Commands
```bash
# Start the backend server
.venv/bin/uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# Start the frontend dev server
cd frontend && npm run dev

# Run all 87 tests
.venv/bin/pytest backend/tests/ -v

# Check backend health
curl -s http://localhost:8000/api/health | python3 -m json.tool

# Run system doctor (validates everything is set up)
.venv/bin/python scripts/doctor.py

# Run live audit benchmark
.venv/bin/python scripts/real_world_phase5_audit.py
```

## Architecture at a Glance

ScholarX uses a **10-node LangGraph StateGraph** that processes student profiles through discovery, verification, and ranking. The philosophy is **Workflow-First** — deterministic workflows for rule-based tasks, LLM agents only where reasoning is needed.

### The 10-Node Pipeline
1. **Orchestrator** → Initialize mission, emit startup events
2. **ProfileAgent** (LLM) → Parse docs, build student profile, conversational counselor
3. **DiscoveryCommander** (LLM) → Generate queries, deploy 5 scouts in parallel
4. **EligibilityInvestigator** (Workflow) → 15-dimension deterministic matching
5. **TrueCostAnalyzer** (Workflow) → 4-phase PKR out-of-pocket expenses
6. **DeadlineIntelligence** (Workflow) → Pakistan prep time + risk tiering
7. **SkepticAgent** (LLM) → Adversarial friction analysis (return bonds, visa risks)
8. **SynthesisWorkflow** (Workflow) → Merge everything into DNA cards
9. **RankingEngine** (Workflow) → Weighted composite scoring (0-100)
10. **AdvisorAgent** (LLM) → Personalized roadmap with Pakistani offices

### Data Flow
```
Frontend (port 3000) → Next.js Proxy → FastAPI (port 8000) → LangGraph DAG → Agents/Workflows → Cloud APIs
     ↑                                        |                                                |
     └──────────── SSE Stream ─────────────┤                                                |
                                               └──────────── SQLite DB ──────────────────┘
```

## Pakistan-Specific Domain Knowledge

### Education System
- **SSC (Matric)**: 10 years, 26 BISE examination boards
- **HSSC (Intermediate)**: 12 years, streams: ICS, FSc Pre-Eng, FSc Pre-Med
- **BS/BE/BBA**: 16 years (standard Pakistani bachelor's)
- **MS/MPhil/MBA**: 18 years

### Key Pakistani Requirements Tracked
- **HEC HAT**: Higher Education Commission Aptitude Test (postgrad bilateral scholarships)
- **HEC USAT**: University Scholastic Aptitude Test (undergrad bilateral scholarships)
- **HEC e-Attestation**: Degree verification via DAS 1-Link portal (PKR 3,000/doc)
- **IBCC Equivalence**: Inter Board Committee of Chairmen certificate (PKR 6,000)
- **MOFA Apostille**: Ministry of Foreign Affairs attestation (PKR 1,000/doc)
- **MOI Certificate**: Medium of Instruction English certificate (alternative to IELTS)

### GPA Conversion
- 80-100% → 4.0 GPA → UK First Class
- 70-79% → 3.7 GPA → UK First Class
- 60-69% → 3.0 GPA → UK Upper Second (2:1)
- 50-59% → 2.5 GPA → UK Lower Second (2:2)
- 40-49% → 2.0 GPA → UK Third Class

## Common Tasks

### Adding a New Scholarship
1. Add to appropriate `data/scholarships/<region>.json`
2. Follow the `Scholarship` Pydantic schema in `backend/schemas/scholarship.py`
3. Run `make seed` or restart backend to load into SQLite
4. Update the scholarship count in `docs/STATUS.md`

### Adding a New API Endpoint
1. Create route in `backend/api/routes/`
2. Register router in `backend/main.py`
3. Write tests in `backend/tests/test_api_*.py`
4. Document in `.scholarx/api_surface.yaml`
5. Update `.scholarx/module_map.yaml`

### Debugging the Pipeline
1. Check EventBus output via SSE: `curl -N http://localhost:8000/api/stream/<session_id>`
2. Check session state: `GET /api/sessions/<session_id>`
3. Check API key health: `GET /api/health`
4. Review node functions in `backend/graph/nodes.py`
