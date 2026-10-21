# ============================================================
# ScholarX — Development Makefile
# One-command operations for common tasks.
# ============================================================

.PHONY: dev backend frontend test test-fast health seed doctor status issues context primer validate all

# Start both FastAPI backend and Next.js frontend concurrently
dev:
	node scripts/dev.mjs

# Start the FastAPI backend server (port 8000)
backend:
	PYTHONPATH=backend .venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Start the Next.js frontend (port 3000)
frontend:
	cd frontend && npm run dev

# Run the complete test suite
test:
	.venv/bin/python -m pytest backend/tests/ -v

# Run fast unit tests (<0.5s)
test-fast:
	.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py -v

# Check backend health and API key pool status
health:
	@curl -sf http://localhost:8000/api/health | python3 -m json.tool 2>/dev/null || echo "❌ Backend not running on port 8000"

# Seed the database with 310 scholarships + profiles
seed:
	.venv/bin/python -c "from backend.db.seed import load_and_seed_scholarships, load_and_seed_profiles; import asyncio; asyncio.run(load_and_seed_scholarships()); asyncio.run(load_and_seed_profiles())"

# Run the system doctor health check
doctor:
	.venv/bin/python scripts/doctor.py

# Context Engine Commands
context:
	.venv/bin/python scripts/context.py status

primer:
	.venv/bin/python scripts/context.py primer

validate:
	.venv/bin/python scripts/context.py validate

# Run the live audit benchmark
audit:
	.venv/bin/python scripts/real_world_phase5_audit.py

# Show current project status
status:
	@echo ""
	@echo "═══════════════════════════════════════════════"
	@echo "  ScholarX — Project Status"
	@echo "═══════════════════════════════════════════════"
	@echo ""
	@cat docs/STATUS.md
	@echo ""

# Show known issues
issues:
	@cat docs/KNOWN_ISSUES.md

# Start all application services (backend + frontend)
all: dev
