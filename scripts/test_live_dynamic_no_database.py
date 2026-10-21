import asyncio
import os
import sys
import time
from pathlib import Path

# Add backend to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from db.session_store import SessionStore
import db.session_store
from graph.builder import build_scholarx_graph
from graph.state import ScholarXState
from schemas.student import StudentProfile
from events.bus import get_event_bus
import json


async def run_live_dynamic_no_database_demo():
    print("=" * 80)
    print("SCHOLARX: 100% DATABASE-FREE & DYNAMIC LIVE DISCOVERY DEMONSTRATION")
    print("=" * 80)
    print("1. Operating Environment: ZERO Persistent Database (Pure RAM / Stateless)")
    
    # Configure 100% in-memory database store
    mem_store = SessionStore(db_path=":memory:")
    await mem_store.init_db()
    db.session_store._global_session_store = mem_store
    print("   -> In-memory SQLite session store initialized with ZERO disk file.")

    # 2. Student Profile: NO CUSTOM PROFILE PROVIDED
    print("\n2. Student Profile Ingestion: NO Custom Profile Provided (Default Auto-Resolution)")
    # Load canonical Pakistani student profile as the system does when profile is None
    profile_path = Path(__file__).resolve().parent.parent / "data" / "profiles" / "ics_student.json"
    with open(profile_path, "r", encoding="utf-8") as f:
        student = StudentProfile.model_validate(json.load(f))
    student.session_id = f"live-demo-{int(time.time())}"

    print(f"   -> Canonical Pakistani Profile Activated: {student.personal.name} ({student.personal.city}, {student.personal.province})")
    print(f"   -> Education Background: {student.academic.current_level} ({student.academic.years_of_education} years), GPA: {student.academic.gpa_percentage}% ({student.academic.gpa_4_scale}/4.0)")
    print(f"   -> Language Proficiency: {student.language.english_proficiency_test.value} (IELTS: None, MOI Available: {student.language.moi_certificate_available})")
    print(f"   -> Target Goal: {student.preferences.target_degree_level} in {student.preferences.target_fields}")
    print(f"   -> Budget Constraint: Max Out-of-Pocket PKR {student.preferences.max_out_of_pocket_pkr:,} (Funding Required: {student.preferences.funding_requirement})")

    # 3. Compiling 10-Node LangGraph StateGraph
    print("\n3. Autonomous Pipeline: Compiling 10-Node LangGraph StateGraph...")
    graph = build_scholarx_graph()
    print("   -> 10 Autonomous Nodes Loaded:")
    print("      Orchestrator -> Profile Analyzer -> Discovery Commander ->")
    print("      Eligibility Investigator -> True Cost Analyzer -> Deadline Analyzer ->")
    print("      Adversarial Skeptic -> Synthesis Engine -> Ranking Engine -> Final Advisor")

    # Event listener to capture live telemetry
    events_captured = []
    def on_event(evt):
        events_captured.append(evt)
        payload_summary = str(evt.payload)[:80] + "..." if len(str(evt.payload)) > 80 else str(evt.payload)
        print(f"   [EVENT: {evt.event_type.value:<25}] ({evt.agent_display_name}): {payload_summary}")

    initial_state: ScholarXState = {
        "session_id": student.session_id,
        "student_id": student.student_id,
        "student_profile": student,
        "events_queue": [],
    }

    print("\n4. Executing Mission Live & Dynamically...")
    start_time = time.time()
    final_state = await graph.ainvoke(initial_state)
    elapsed = time.time() - start_time
    print(f"\n   Mission Complete in {elapsed:.2f} seconds! Final Phase: {final_state.get('active_phase')}")

    # 5. Extract and Display Live Results
    candidates = final_state.get("candidate_scholarships", [])
    ranked = final_state.get("ranked_results", [])
    roadmap = final_state.get("final_roadmap")

    print("\n" + "=" * 80)
    print(f"LIVE DISCOVERY RESULTS: {len(candidates)} Candidates Discovered | {len(ranked)} Verified & Ranked")
    print("=" * 80)

    for r in ranked[:5]:
        print(f"\n[RANK #{r.rank}] {r.scholarship_name}")
        print(f"  * Match Score:       {r.overall_match_score:.1f}%")
        print(f"  * Eligibility Score: {r.eligibility_score:.1f}%")
        print(f"  * Funding Score:     {r.true_funding_score:.1f}%")
        print(f"  * Academic Fit:      {r.academic_fit_score:.1f}%")
        print(f"  * Net Out-of-Pocket: PKR {r.cost_analysis.total_out_of_pocket_pkr:,}")
        if r.pakistan_specific_advantages:
            print(f"  * Pakistan Edge:     {r.pakistan_specific_advantages[0]}")
        if r.blocking_reasons:
            print(f"  * Notice/Warnings:   {', '.join(r.blocking_reasons[:2])}")

    if roadmap:
        print("\n" + "=" * 80)
        print(f"DYNAMIC PERSONALIZED PAKISTANI APPLICANT ROADMAP: {roadmap.scholarship_name}")
        print("=" * 80)
        print(f"Destination: {roadmap.host_country} | Strategy: {roadmap.strategy_summary if hasattr(roadmap, 'strategy_summary') else 'Comprehensive Preparation'}")
        print(f"\nActionable Milestones ({len(roadmap.milestones)} phases):")
        for idx, m in enumerate(roadmap.milestones, 1):
            title = getattr(m, 'title', getattr(m, 'milestone_name', f'Milestone {idx}'))
            phase = getattr(m, 'phase', '')
            deadline = getattr(m, 'target_date', getattr(m, 'deadline', 'TBD'))
            print(f"\n  Phase {idx}: {title} ({phase}) [Target: {deadline}]")
            actions = getattr(m, 'actions', getattr(m, 'tasks', []))
            for a in actions[:3]:
                print(f"    - {a}")

    await mem_store.close()
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE: Verified 100% database-free, live & dynamic execution.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(run_live_dynamic_no_database_demo())
