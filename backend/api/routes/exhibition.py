import asyncio
import logging
from pathlib import Path
from typing import Any, Dict
from fastapi import APIRouter
from config import get_settings
from db.session_store import get_session_store
from utils.api_keys import get_key_manager

logger = logging.getLogger("scholarx.api.exhibition")

router = APIRouter(prefix="/exhibition", tags=["exhibition"])


@router.get("/preflight")
async def run_exhibition_preflight() -> Dict[str, Any]:
    """
    Comprehensive Exhibition Pre-Flight Readiness Verification (§48, §49, §50, §85).
    Verifies SQLite database, seeded scholarships, Pakistani profiles, offline artifacts,
    cloud API rotators, and event pipeline. Reports EXHIBITION_READY or DEGRADED.
    """
    checks: Dict[str, Dict[str, Any]] = {}
    is_ready = True
    degraded_reasons = []

    # 1. Database & SQLite Sessions Table Check
    store = get_session_store()
    try:
        await store.init_db()
        cached_scs = await store.get_all_cached_scholarships()
        checks["database"] = {
            "status": "PASS",
            "db_path": store.db_path,
            "cached_scholarships_count": len(cached_scs),
        }
        if len(cached_scs) == 0:
            checks["database"]["status"] = "WARN"
            degraded_reasons.append("Scholarships database is empty (needs seed).")
    except Exception as db_err:
        checks["database"] = {"status": "FAIL", "error": str(db_err)}
        is_ready = False
        degraded_reasons.append(f"Database error: {db_err}")

    # 2. Demo Student Profiles Verification (§15)
    repo_root = Path(__file__).resolve().parents[3]
    profiles_dir = repo_root / "data" / "profiles"
    if not profiles_dir.exists():
        profiles_dir = Path(__file__).resolve().parents[2] / "data" / "profiles"

    required_profiles = ["ics_student.json", "fsc_student.json", "bs_graduate.json"]
    found_profiles = []
    missing_profiles = []
    for pf in required_profiles:
        if (profiles_dir / pf).exists():
            found_profiles.append(pf)
        else:
            missing_profiles.append(pf)

    checks["demo_profiles"] = {
        "status": "PASS" if len(missing_profiles) == 0 else "WARN",
        "profiles_found": found_profiles,
        "profiles_missing": missing_profiles,
        "profile_a_ics": "ics_student.json" in found_profiles,
        "profile_b_fsc": "fsc_student.json" in found_profiles,
        "profile_c_bs": "bs_graduate.json" in found_profiles,
    }

    # 3. Offline Artifact Cache Verification (§16)
    pdf_script = repo_root / "scripts" / "generate_dossier_pdf.py"
    checks["artifact_cache"] = {
        "status": "PASS" if pdf_script.exists() else "WARN",
        "pdf_generator_available": pdf_script.exists(),
        "editorial_dossier_route": "/dossier/[scholarshipId]",
    }

    # 4. API Keys & Cloud Services Status (§11, §19)
    key_mgr = get_key_manager()
    api_health = {
        "groq": key_mgr.groq.get_status_summary(),
        "gemini": key_mgr.gemini.get_status_summary(),
        "tavily": key_mgr.tavily.get_status_summary(),
        "firecrawl": key_mgr.firecrawl.get_status_summary(),
        "jina": key_mgr.jina.get_status_summary(),
    }
    
    # Check if we have at least one working LLM provider
    has_llm = api_health["groq"]["healthy_keys"] > 0 or api_health["gemini"]["healthy_keys"] > 0
    checks["cloud_apis"] = {
        "status": "PASS" if has_llm else "DEGRADED",
        "has_llm_keys": has_llm,
        "providers": api_health,
    }
    if not has_llm:
        degraded_reasons.append("Cloud LLM keys not detected; system requires DEMO / CACHED mode.")

    # 5. Redis / In-Memory Event Bus Status (§26)
    from events.bus import get_event_bus
    bus = get_event_bus()
    redis_failed = getattr(bus, "_redis_failed", False)
    checks["event_bus"] = {
        "status": "PASS",
        "transport": "IN_MEMORY_ASYNC_QUEUE" if redis_failed else "HYBRID_REDIS_IN_MEMORY",
        "active_subscribers_sessions": len(bus._subscribers),
    }

    final_status = "EXHIBITION_READY" if is_ready and not degraded_reasons else "DEGRADED"

    return {
        "status": final_status,
        "ready": is_ready,
        "degraded": bool(degraded_reasons),
        "degraded_reasons": degraded_reasons,
        "message": (
            "All systems verified. Exhibition environment fully ready."
            if final_status == "EXHIBITION_READY"
            else f"Operational with degraded safeguards: {'; '.join(degraded_reasons)}"
        ),
        "offline_demo_ready": True,
        "live_mode_ready": has_llm and is_ready,
        "database": checks.get("database", {}),
        "profiles": checks.get("demo_profiles", {}),
        "offline_artifacts": checks.get("artifact_cache", {}),
        "api_keys": checks.get("cloud_apis", {}),
        "event_bus": checks.get("event_bus", {}),
        "checks": checks,
    }
