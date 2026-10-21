#!/usr/bin/env python3
"""
ScholarX System Doctor — Health Check Script
Validates the entire ScholarX development environment is correctly set up.

Usage:
    .venv/bin/python scripts/doctor.py
    # or
    make doctor
"""

import os
import sys
import json
import sqlite3
import importlib
import subprocess
from pathlib import Path

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Project root (parent of scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

passed = 0
failed = 0
warnings = 0


def check(name: str, condition: bool, detail: str = "", warn_only: bool = False):
    """Report a check result."""
    global passed, failed, warnings
    if condition:
        print(f"  {GREEN}✅ PASS{RESET}  {name}")
        passed += 1
    elif warn_only:
        print(f"  {YELLOW}⚠️  WARN{RESET}  {name}")
        if detail:
            print(f"           {YELLOW}{detail}{RESET}")
        warnings += 1
    else:
        print(f"  {RED}❌ FAIL{RESET}  {name}")
        if detail:
            print(f"           {RED}{detail}{RESET}")
        failed += 1


def check_python():
    """Check Python version and venv."""
    print(f"\n{BOLD}{CYAN}── Python Environment ──{RESET}")

    # Python version
    v = sys.version_info
    check(
        f"Python {v.major}.{v.minor}.{v.micro}",
        v.major == 3 and v.minor >= 11,
        f"Need Python 3.11+, got {v.major}.{v.minor}",
    )

    # Virtual environment
    venv_path = PROJECT_ROOT / ".venv"
    check("Virtual environment (.venv/)", venv_path.exists())

    # Check if running from venv
    in_venv = sys.prefix != sys.base_prefix
    check(
        "Running from virtual environment",
        in_venv,
        "Run with: .venv/bin/python scripts/doctor.py",
        warn_only=True,
    )


def check_packages():
    """Check required Python packages."""
    print(f"\n{BOLD}{CYAN}── Python Packages ──{RESET}")

    required = [
        ("fastapi", "FastAPI web framework"),
        ("uvicorn", "ASGI server"),
        ("pydantic", "Data validation"),
        ("aiosqlite", "Async SQLite"),
        ("langgraph", "Graph orchestration"),
        ("groq", "Groq LLM client"),
        ("httpx", "Async HTTP client"),
        ("pypdf", "PDF parser"),
        ("docx", "DOCX parser (python-docx)"),
        ("tavily", "Tavily search client"),
    ]

    for pkg, desc in required:
        try:
            importlib.import_module(pkg)
            check(f"{desc} ({pkg})", True)
        except ImportError:
            check(f"{desc} ({pkg})", False, f"Install: pip install {pkg}")


def check_env():
    """Check .env file and API keys."""
    print(f"\n{BOLD}{CYAN}── Environment & API Keys ──{RESET}")

    env_path = PROJECT_ROOT / ".env"
    check(".env file exists", env_path.exists())

    if env_path.exists():
        env_content = env_path.read_text()
        lines = [
            l.strip()
            for l in env_content.splitlines()
            if l.strip() and not l.strip().startswith("#")
        ]
        env_vars = {}
        for line in lines:
            if "=" in line:
                key, val = line.split("=", 1)
                env_vars[key.strip()] = val.strip()

        # Count real keys (not placeholders)
        groq_keys = sum(
            1
            for k, v in env_vars.items()
            if k.startswith("GROQ_API_KEY") and "your_" not in v
        )
        gemini_keys = sum(
            1
            for k, v in env_vars.items()
            if k.startswith("GEMINI_API_KEY") and "your_" not in v
        )
        tavily_keys = sum(
            1
            for k, v in env_vars.items()
            if k.startswith("TAVILY_API_KEY") and "your_" not in v
        )
        firecrawl_keys = sum(
            1
            for k, v in env_vars.items()
            if k.startswith("FIRECRAWL_API_KEY") and "your_" not in v
        )
        jina_keys = sum(
            1
            for k, v in env_vars.items()
            if k.startswith("JINA_API_KEY") and "your_" not in v
        )

        total = groq_keys + gemini_keys + tavily_keys + firecrawl_keys + jina_keys
        check(f"Groq API keys configured: {groq_keys}", groq_keys > 0)
        check(f"Gemini API keys configured: {gemini_keys}", gemini_keys > 0)
        check(
            f"Tavily API keys configured: {tavily_keys}",
            tavily_keys > 0,
            warn_only=True,
        )
        check(
            f"Firecrawl API keys configured: {firecrawl_keys}",
            firecrawl_keys > 0,
            warn_only=True,
        )
        check(
            f"Jina API key configured: {jina_keys}",
            jina_keys > 0,
            warn_only=True,
        )
        print(f"           Total API keys: {BOLD}{total}{RESET}")


def check_database():
    """Check SQLite database."""
    print(f"\n{BOLD}{CYAN}── Database ──{RESET}")

    db_path = PROJECT_ROOT / "data" / "scholarx_sessions.db"
    check("SQLite database exists", db_path.exists())

    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()

            # Check tables
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
            tables = [row[0] for row in cursor.fetchall()]
            expected_tables = [
                "students",
                "sessions",
                "scholarships_cache",
                "session_scholarships",
                "events_log",
                "search_queries_cache",
            ]
            for table in expected_tables:
                check(f"Table '{table}' exists", table in tables)

            # Count scholarships
            cursor.execute("SELECT COUNT(*) FROM scholarships_cache")
            count = cursor.fetchone()[0]
            check(
                f"Scholarships seeded: {count}",
                count >= 200,
                f"Expected ~205, got {count}",
                warn_only=count > 0,
            )

            # Count by region
            cursor.execute(
                "SELECT region, COUNT(*) FROM scholarships_cache GROUP BY region ORDER BY region"
            )
            regions = cursor.fetchall()
            for region, rcount in regions:
                print(f"           {region}: {rcount}")

            conn.close()
        except Exception as e:
            check("Database readable", False, str(e))


def check_data_files():
    """Check data files exist."""
    print(f"\n{BOLD}{CYAN}── Data Files ──{RESET}")

    data_files = [
        ("data/scholarships/europe.json", "Europe scholarships"),
        ("data/scholarships/asia.json", "Asia scholarships"),
        ("data/scholarships/americas.json", "Americas scholarships"),
        ("data/scholarships/mena.json", "MENA scholarships"),
        ("data/scholarships/oceania.json", "Oceania scholarships"),
        ("data/pakistan_costs.json", "Pakistan costs reference"),
        ("data/pakistan_education.json", "Pakistan education reference"),
    ]

    for path, desc in data_files:
        full_path = PROJECT_ROOT / path
        check(f"{desc}", full_path.exists())

    # Count profiles
    profiles_dir = PROJECT_ROOT / "data" / "profiles"
    if profiles_dir.exists():
        profile_count = len(list(profiles_dir.glob("*.json")))
        check(f"Student profiles: {profile_count}", profile_count >= 5)
    else:
        check("Student profiles directory", False)


def check_frontend():
    """Check frontend setup."""
    print(f"\n{BOLD}{CYAN}── Frontend ──{RESET}")

    frontend_dir = PROJECT_ROOT / "frontend"
    check("frontend/ directory exists", frontend_dir.exists())

    if frontend_dir.exists():
        check(
            "package.json exists",
            (frontend_dir / "package.json").exists(),
        )
        check(
            "node_modules installed",
            (frontend_dir / "node_modules").exists(),
            "Run: cd frontend && npm install",
        )
        next_config_exists = (
            (frontend_dir / "next.config.ts").exists()
            or (frontend_dir / "next.config.js").exists()
            or (frontend_dir / "next.config.mjs").exists()
        )
        check(
            "next.config exists (.ts / .js)",
            next_config_exists,
        )

        # Check video assets
        assets_dir = frontend_dir / "public" / "lets-scroll" / "assets"
        if assets_dir.exists():
            videos = list(assets_dir.glob("*.mp4"))
            stills = list(assets_dir.glob("*.png"))
            check(
                f"Scroll hero videos: {len(videos)}",
                len(videos) >= 4,
                "Expected 4 video legs (leg-01.mp4 to leg-04.mp4)",
            )
            check(
                f"Scroll hero stills: {len(stills)}",
                len(stills) >= 4,
                "Expected 4 poster stills",
            )


def check_project_metadata():
    """Check the project intelligence hub files."""
    print(f"\n{BOLD}{CYAN}── Project Intelligence Hub ──{RESET}")

    meta_files = [
        (".scholarx/project.yaml", "Project manifest"),
        (".scholarx/module_map.yaml", "Module dependency map"),
        (".scholarx/api_surface.yaml", "API surface documentation"),
        ("docs/ARCHITECTURE.md", "Architecture reference"),
        ("docs/STATUS.md", "Status tracker"),
        ("docs/DECISIONS.md", "Decision records"),
        ("docs/KNOWN_ISSUES.md", "Known issues tracker"),
    ]

    for path, desc in meta_files:
        full_path = PROJECT_ROOT / path
        check(f"{desc}", full_path.exists())


def check_ports():
    """Check if ports are available or in use."""
    print(f"\n{BOLD}{CYAN}── Ports ──{RESET}")

    import socket

    for port, service in [(8000, "Backend (FastAPI)"), (3000, "Frontend (Next.js)")]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("127.0.0.1", port))
        sock.close()
        if result == 0:
            check(f"Port {port} — {service} is RUNNING", True)
        else:
            check(
                f"Port {port} — {service} is available (not running)",
                True,
            )


def main():
    global passed, failed, warnings

    print(f"\n{BOLD}{'═' * 50}{RESET}")
    print(f"{BOLD}  ScholarX System Doctor{RESET}")
    print(f"{BOLD}{'═' * 50}{RESET}")

    check_python()
    check_packages()
    check_env()
    check_database()
    check_data_files()
    check_frontend()
    check_project_metadata()
    check_ports()

    # Summary
    total = passed + failed + warnings
    print(f"\n{BOLD}{'═' * 50}{RESET}")
    print(f"{BOLD}  Results: {total} checks{RESET}")
    print(f"  {GREEN}✅ Passed:   {passed}{RESET}")
    if warnings:
        print(f"  {YELLOW}⚠️  Warnings: {warnings}{RESET}")
    if failed:
        print(f"  {RED}❌ Failed:   {failed}{RESET}")
    print(f"{BOLD}{'═' * 50}{RESET}")

    if failed == 0:
        print(f"\n  {GREEN}{BOLD}🎓 ScholarX is healthy! Ready to go.{RESET}\n")
    else:
        print(
            f"\n  {RED}{BOLD}⚠️  {failed} issue(s) need attention.{RESET}\n"
        )

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
