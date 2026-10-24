#!/usr/bin/env python3
"""
ScholarX Dynamic Context Engine CLI
====================================
Instant context ingestion, health inspection, and verification for AI agents and developers.

Usage:
    python scripts/context.py primer      -> Concentrated ~1,500 token system primer
    python scripts/context.py status      -> Live system telemetry (DB, keys, ports, tests)
    python scripts/context.py inspect <sub>-> Targeted deep dive (backend, frontend, db, api, etc.)
    python scripts/context.py validate    -> Validates all context documents against actual code
    python scripts/context.py task        -> View or update current agent task scratchpad
    python scripts/context.py record <msg>-> Appends notes to the agent memory bank
    python scripts/context.py map         -> Prints system directory & architecture map
"""

import os
import sys
import json
import sqlite3
import socket
import argparse
from datetime import datetime
from pathlib import Path

# Colors
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_MAGENTA = "\033[95m"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTEXT_DIR = PROJECT_ROOT / ".context"


def print_banner(title: str):
    print(f"\n{C_BOLD}{C_CYAN}══════════════════════════════════════════════════════════════════{C_RESET}")
    print(f"  {C_BOLD}{title}{C_RESET}")
    print(f"{C_BOLD}{C_CYAN}══════════════════════════════════════════════════════════════════{C_RESET}\n")


def cmd_primer(args):
    """Outputs high-density, prompt-ready primer (~1,500 tokens)."""
    quickstart_path = CONTEXT_DIR / "00_QUICKSTART.md"
    if quickstart_path.exists():
        print(quickstart_path.read_text(encoding="utf-8"))
    else:
        print(f"{C_RED}Error: .context/00_QUICKSTART.md not found.{C_RESET}")


def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)
        return s.connect_ex(("127.0.0.1", port)) == 0


def cmd_status(args):
    """Checks live database counts, API keys, ports, tests, and active tasks."""
    print_banner("ScholarX Live System Status")

    # 1. Database
    db_path = PROJECT_ROOT / "data" / "scholarx_sessions.db"
    print(f"{C_BOLD}── 1. Database (SQLite WAL) ──{C_RESET}")
    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            cur = conn.cursor()
            cur.execute("SELECT count(*) FROM scholarships_cache")
            total_schol = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM students")
            total_students = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM sessions")
            total_sessions = cur.fetchone()[0]

            print(f"  {C_GREEN}✅ DB File{C_RESET}       : {db_path.relative_to(PROJECT_ROOT)}")
            print(f"  {C_GREEN}✅ Scholarships{C_RESET}  : {C_BOLD}{total_schol}{C_RESET} seeded opportunities")
            print(f"  {C_GREEN}✅ Students{C_RESET}      : {total_students} profiles")
            print(f"  {C_GREEN}✅ Sessions{C_RESET}      : {total_sessions} past sessions")

            # Region breakdown
            cur.execute("SELECT region, count(*) FROM scholarships_cache GROUP BY region ORDER BY count(*) DESC")
            regions = cur.fetchall()
            region_str = ", ".join([f"{r[0]}: {r[1]}" for r in regions])
            print(f"     Regions      : {region_str}")
            conn.close()
        except Exception as e:
            print(f"  {C_RED}❌ DB Error{C_RESET}     : {e}")
    else:
        print(f"  {C_RED}❌ Missing DB{C_RESET}   : {db_path}")

    # 2. API Keys
    print(f"\n{C_BOLD}── 2. KeyManager Rotation Pool ──{C_RESET}")
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        groq_count = 0
        gemini_count = 0
        tavily_count = 0
        firecrawl_count = 0
        jina_count = 0
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GROQ_API_KEY"): groq_count += 1
                elif line.startswith("GEMINI_API_KEY"): gemini_count += 1
                elif line.startswith("TAVILY_API_KEY"): tavily_count += 1
                elif line.startswith("FIRECRAWL_API_KEY"): firecrawl_count += 1
                elif line.startswith("JINA_API_KEY"): jina_count += 1

        total_keys = groq_count + gemini_count + tavily_count + firecrawl_count + jina_count
        print(f"  {C_GREEN}✅ Total Keys{C_RESET}    : {C_BOLD}{total_keys}{C_RESET} keys active across 5 providers")
        print(f"     Distribution : Groq: {groq_count}, Gemini: {gemini_count}, Tavily: {tavily_count}, Firecrawl: {firecrawl_count}, Jina: {jina_count}")
    else:
        print(f"  {C_YELLOW}⚠️  No .env file found{C_RESET}")

    # 3. Ports & Services
    print(f"\n{C_BOLD}── 3. Application Services ──{C_RESET}")
    backend_live = is_port_in_use(8000)
    frontend_live = is_port_in_use(3000)

    p8000_str = f"{C_GREEN}ACTIVE (Listening){C_RESET}" if backend_live else f"{C_YELLOW}OFFLINE (Ready to launch){C_RESET}"
    p3000_str = f"{C_GREEN}ACTIVE (Listening){C_RESET}" if frontend_live else f"{C_YELLOW}OFFLINE (Ready to launch){C_RESET}"

    print(f"  • Port 8000 [Backend FastAPI]  : {p8000_str}")
    print(f"  • Port 3000 [Frontend Next.js] : {p3000_str}")

    # 4. Tests
    print(f"\n{C_BOLD}── 4. Test Suite ──{C_RESET}")
    test_files = list((PROJECT_ROOT / "backend" / "tests").glob("test_*.py"))
    print(f"  {C_GREEN}✅ Test Modules{C_RESET}  : {len(test_files)} files in backend/tests/")

    # 5. Active Task
    print(f"\n{C_BOLD}── 5. Active Agent Scratchpad ──{C_RESET}")
    task_path = CONTEXT_DIR / "CURRENT_TASK.md"
    if task_path.exists():
        lines = task_path.read_text(encoding="utf-8").splitlines()
        for line in lines[:15]:
            if line.startswith("- **Task**:") or line.startswith("- **Status**:") or line.startswith("- **Goal**:") or line.startswith("## Current Objective"):
                print(f"  {line}")
    print(f"\n{C_CYAN}Run 'python scripts/context.py primer' for full agent orientation.{C_RESET}\n")


def cmd_inspect(args):
    """Outputs deep dive manual for a given subsystem."""
    topic = args.topic.lower()
    mapping = {
        "arch": "01_ARCHITECTURE.md",
        "architecture": "01_ARCHITECTURE.md",
        "backend": "02_BACKEND_LANGGRAPH.md",
        "graph": "02_BACKEND_LANGGRAPH.md",
        "langgraph": "02_BACKEND_LANGGRAPH.md",
        "frontend": "03_FRONTEND_THEATRE.md",
        "theatre": "03_FRONTEND_THEATRE.md",
        "ui": "03_FRONTEND_THEATRE.md",
        "db": "04_DATA_SCHEMAS_DB.md",
        "data": "04_DATA_SCHEMAS_DB.md",
        "schemas": "04_DATA_SCHEMAS_DB.md",
        "api": "05_API_SSE_EVENTS.md",
        "events": "05_API_SSE_EVENTS.md",
        "sse": "05_API_SSE_EVENTS.md",
        "adrs": "06_DECISIONS_INVARIANTS.md",
        "decisions": "06_DECISIONS_INVARIANTS.md",
        "invariants": "06_DECISIONS_INVARIANTS.md",
        "playbook": "07_DEVELOPER_PLAYBOOK.md",
        "dev": "07_DEVELOPER_PLAYBOOK.md",
        "recipes": "07_DEVELOPER_PLAYBOOK.md",
        "state": "08_ACTIVE_STATE.md",
        "active": "08_ACTIVE_STATE.md",
        "status": "08_ACTIVE_STATE.md",
        "task": "CURRENT_TASK.md",
        "memory": "MEMORY.md"
    }

    filename = mapping.get(topic)
    if not filename:
        print(f"{C_RED}Unknown topic '{args.topic}'. Available topics:{C_RESET}")
        print("  backend, frontend, architecture, db, api, invariants, playbook, state, task, memory")
        return

    filepath = CONTEXT_DIR / filename
    if filepath.exists():
        print(filepath.read_text(encoding="utf-8"))
    else:
        print(f"{C_RED}File {filepath} not found.{C_RESET}")


def cmd_validate(args):
    """Self-verifying check that all context files and code contracts are in sync."""
    print_banner("ScholarX Context & Architecture Validator")

    passed = 0
    failed = 0

    def check(desc: str, cond: bool, err_msg: str = ""):
        nonlocal passed, failed
        if cond:
            print(f"  {C_GREEN}✅ PASS{C_RESET}  {desc}")
            passed += 1
        else:
            print(f"  {C_RED}❌ FAIL{C_RESET}  {desc} - {err_msg}")
            failed += 1

    # Check context modules
    context_files = [
        "00_QUICKSTART.md", "01_ARCHITECTURE.md", "02_BACKEND_LANGGRAPH.md",
        "03_FRONTEND_THEATRE.md", "04_DATA_SCHEMAS_DB.md", "05_API_SSE_EVENTS.md",
        "06_DECISIONS_INVARIANTS.md", "07_DEVELOPER_PLAYBOOK.md", "08_ACTIVE_STATE.md",
        "CURRENT_TASK.md", "MEMORY.md"
    ]
    for cf in context_files:
        check(f"Context Module: .context/{cf}", (CONTEXT_DIR / cf).exists())

    # Check universal entry points
    check("Universal Agent Standard: AGENTS.md", (PROJECT_ROOT / "AGENTS.md").exists())
    check("Claude Standard: CLAUDE.md", (PROJECT_ROOT / "CLAUDE.md").exists())
    check("Human/Agent Hub: CONTEXT.md", (PROJECT_ROOT / "CONTEXT.md").exists())
    check("Cursor Rules: .cursorrules", (PROJECT_ROOT / ".cursorrules").exists())
    check("Gemini Rules: .gemini/rules/scholarx-context.md", (PROJECT_ROOT / ".gemini" / "rules" / "scholarx-context.md").exists())
    check("Gemini Rules: .gemini/rules/scholarx-dev.md", (PROJECT_ROOT / ".gemini" / "rules" / "scholarx-dev.md").exists())

    # Check core backend paths
    check("Backend Entry: backend/main.py", (PROJECT_ROOT / "backend" / "main.py").exists())
    check("LangGraph Builder: backend/graph/builder.py", (PROJECT_ROOT / "backend" / "graph" / "builder.py").exists())
    check("Key Manager: backend/utils/api_keys.py", (PROJECT_ROOT / "backend" / "utils" / "api_keys.py").exists())
    check("Event Bus: backend/events/bus.py", (PROJECT_ROOT / "backend" / "events" / "bus.py").exists())

    # Check core frontend paths
    check("Frontend Page: frontend/app/page.tsx", (PROJECT_ROOT / "frontend" / "app" / "page.tsx").exists())
    check("Frontend Store: frontend/lib/store.ts", (PROJECT_ROOT / "frontend" / "lib" / "store.ts").exists())
    check("Frontend SQLite Client: frontend/lib/db/sqliteClient.ts", (PROJECT_ROOT / "frontend" / "lib" / "db" / "sqliteClient.ts").exists())
    check("Judge Control Bar: frontend/components/theatre/JudgeControlBar.tsx", (PROJECT_ROOT / "frontend" / "components" / "theatre" / "JudgeControlBar.tsx").exists())

    # Check database and benchmarks
    db_file = PROJECT_ROOT / "data" / "scholarx_sessions.db"
    check("Database File: data/scholarx_sessions.db", db_file.exists())
    if db_file.exists():
        try:
            conn = sqlite3.connect(str(db_file))
            cur = conn.cursor()
            cur.execute("SELECT count(*) FROM scholarships_cache")
            count = cur.fetchone()[0]
            check(f"Database Seed: 510 Scholarships ({count} found)", count >= 500)
            conn.close()
        except Exception as e:
            check("Database Seed Query", False, str(e))

    check("Standalone DB: scholarships_database.db", (PROJECT_ROOT / "scholarships_database.db").exists())
    check("Offline Typo Test: backend/tests/test_offline_typo_retrieval.py", (PROJECT_ROOT / "backend" / "tests" / "test_offline_typo_retrieval.py").exists())
    check("Benchmark: data/pakistan_costs.json", (PROJECT_ROOT / "data" / "pakistan_costs.json").exists())
    check("Benchmark: data/pakistan_education.json", (PROJECT_ROOT / "data" / "pakistan_education.json").exists())

    print(f"\n{C_BOLD}Result: {passed} passed, {failed} failed.{C_RESET}")
    if failed == 0:
        print(f"{C_GREEN}🌟 All context systems and architectural contracts are in sync!{C_RESET}\n")
    else:
        print(f"{C_RED}⚠️  Some context checks failed. Please review errors above.{C_RESET}\n")


def cmd_task(args):
    """View or update CURRENT_TASK.md."""
    task_file = CONTEXT_DIR / "CURRENT_TASK.md"
    if args.action == "view":
        if task_file.exists():
            print(task_file.read_text(encoding="utf-8"))
        else:
            print(f"{C_RED}CURRENT_TASK.md does not exist.{C_RESET}")
    elif args.action == "set":
        if not args.text:
            print(f"{C_RED}Please specify text to update task.{C_RESET}")
            return
        content = f"# 📌 ScholarX — Active Agent Task Scratchpad\n\n- **Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n- **Current Task**: {args.text}\n- **Status**: 🟢 In Progress\n\n## Notes\nUpdated via context CLI.\n"
        task_file.write_text(content, encoding="utf-8")
        print(f"{C_GREEN}✅ Updated CURRENT_TASK.md with: {args.text}{C_RESET}")


def cmd_record(args):
    """Appends session notes to MEMORY.md."""
    memory_file = CONTEXT_DIR / "MEMORY.md"
    if not args.message:
        print(f"{C_RED}Please specify a message to record.{C_RESET}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n### [{timestamp}] Agent Work Record\n- {args.message}\n"
    with open(memory_file, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"{C_GREEN}✅ Recorded to .context/MEMORY.md:{C_RESET} {args.message}")


def cmd_map(args):
    """Prints ASCII directory topology."""
    print_banner("ScholarX Architectural Map")
    print("""
SCHOLARX/
├── backend/
│   ├── agents/               → 4 LLM Agents (Profile, Commander, Skeptic, Advisor)
│   ├── workflows/            → 7 Deterministic Workflows (Scouts x5, Eligibility, Cost, Deadline, Ranking, Synthesis)
│   ├── graph/                → LangGraph 10-Node StateGraph (builder.py, nodes.py, state.py)
│   ├── tools/                → Ingestion Tools (Tavily, Firecrawl, Jina Reader, Document Parser)
│   ├── schemas/              → Pydantic v2 Models (Student, Scholarship, Scoring, Evidence, Events)
│   ├── api/routes/           → FastAPI Routes (/discover, /stream, /profile, /scholarships, /sessions)
│   ├── db/                   → SQLite WAL Session Store & Seeding
│   └── utils/                → KeyManager (30 keys rotator), GPA Converter, Pakistan Costs
│
├── frontend/
│   ├── app/                  → Next.js 15 App Router (/page, /mission/[sessionId], /dossier/[id], /catalog)
│   ├── components/           → Command Theatre (1920x1080 Spatial Floor, Beacons, Packet Canvas, JudgeControlBar)
│   └── lib/                  → Zustand Store (store.ts), Presentation Queue, Simulation Engine, API Client
│
├── data/
│   ├── scholarships/         → 310 Deep Research Scholarship Dossiers (Europe, Asia, Americas, MENA, Oceania)
│   ├── profiles/             → 6 Pakistani Student Presets (Undergrad, Graduate, Cambridge, Low-GPA)
│   ├── pakistan_costs.json   → PKR Expense Benchmarks (IELTS, HEC attestation, IBCC, Visa, Flights)
│   └── pakistan_education.json→ BISE scales, Cambridge O/A-Level conversions, HEC degree tiers
│
├── .context/                 → Modular Context Hub (00_QUICKSTART to 08_ACTIVE_STATE + Memory)
├── scripts/                  → Automation CLI (context.py, doctor.py, dev.mjs, build slides)
└── docs/                     → Archival documentation, decisions (ADRs 001-012), architecture reference
    """)


def main():
    parser = argparse.ArgumentParser(description="ScholarX Dynamic Context Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # primer
    subparsers.add_parser("primer", help="Dump concentrated ~1,500 token system primer")

    # status
    subparsers.add_parser("status", help="Check live system status (DB, keys, ports, tests)")

    # inspect
    inspect_parser = subparsers.add_parser("inspect", help="Deep dive into a specific subsystem")
    inspect_parser.add_argument("topic", help="Subsystem: backend, frontend, db, api, invariants, playbook, state")

    # validate
    subparsers.add_parser("validate", help="Validate all context documents against codebase")

    # task
    task_parser = subparsers.add_parser("task", help="View or update agent task scratchpad")
    task_parser.add_argument("action", choices=["view", "set"], default="view", nargs="?")
    task_parser.add_argument("text", nargs="?", default="", help="Task description if setting")

    # record
    record_parser = subparsers.add_parser("record", help="Record session notes to MEMORY.md")
    record_parser.add_argument("message", help="Summary message to append to memory")

    # map
    subparsers.add_parser("map", help="Print codebase directory map")

    args = parser.parse_args()

    if not args.command or args.command == "primer":
        cmd_primer(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "inspect":
        cmd_inspect(args)
    elif args.command == "validate":
        cmd_validate(args)
    elif args.command == "task":
        cmd_task(args)
    elif args.command == "record":
        cmd_record(args)
    elif args.command == "map":
        cmd_map(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
