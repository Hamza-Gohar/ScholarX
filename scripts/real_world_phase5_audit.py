import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from httpx import ASGITransport, AsyncClient
from db.session_store import get_session_store
from events.bus import get_event_bus
from main import app
from schemas.events import AgentEventType, ScholarXEvent
from utils.api_keys import get_key_manager


async def run_audit():
    print("=" * 90)
    print("🚀 SCHOLARX REAL-WORLD LIVE SYSTEM DEMO & FULL AUDIT (PHASES 0 TO 5)")
    print("=" * 90)

    audit_metrics: Dict[str, Any] = {
        "timings": {},
        "api_keys": {},
        "events": {},
        "database": {},
        "results_summary": {},
    }

    start_total_time = time.perf_counter()

    # -------------------------------------------------------------
    # Step 0: Database & KeyManager Pre-Flight Audit
    # -------------------------------------------------------------
    t0 = time.perf_counter()
    store = get_session_store()
    await store.init_db()
    key_mgr = get_key_manager()
    cached_scholarships = await store.get_all_cached_scholarships()
    t_db_init = time.perf_counter() - t0
    audit_metrics["timings"]["db_initialization_sec"] = round(t_db_init, 4)

    print("\n[STEP 0] System Pre-Flight & Knowledge Base Audit:")
    print(f"  ✓ Database Initialization: {t_db_init * 1000:.2f} ms")
    print(f"  ✓ Pre-Seeded Verified Scholarships in Cache: {len(cached_scholarships)}")
    print(f"  ✓ API Key Manager Status:")
    print(f"      • Groq Keys Pool: {key_mgr.groq.total_keys} keys active")
    print(f"      • Tavily Keys Pool: {key_mgr.tavily.total_keys} keys active")
    print(f"      • Gemini Keys Pool: {key_mgr.gemini.total_keys} keys active")
    print(f"      • Firecrawl Keys Pool: {key_mgr.firecrawl.total_keys} keys active")
    print(f"      • Jina Keys Pool: {key_mgr.jina.total_keys} keys active")

    session_id = f"audit-sess-{int(time.time())}"
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test", timeout=180.0) as client:
        # -------------------------------------------------------------
        # Step 1: Real Pakistani Document Ingestion via FastAPI Multipart
        # -------------------------------------------------------------
        print("\n[STEP 1] Real Physical Pakistani Student Document Ingestion (/api/profile/upload):")
        cv_content = b"""
        CURRICULUM VITAE
        Name: Muhammad Hamza Farooq
        Email: hamza.farooq.dev@gmail.com
        Contact: +92-301-8765432
        City: Lahore, Punjab, Pakistan
        Nationality: Pakistani (PK)

        ACADEMIC PROFILE:
        - Current Degree: Bachelor of Science in Computer Science (16-Year BS CS)
        - Institution: National University of Computer and Emerging Sciences (FAST-NUCES), Lahore
        - CGPA: 3.78 / 4.0 (Marks Equivalent: 85.5%)
        - Graduation Year: 2026
        - Core Courses: Distributed Systems, Advanced Algorithms, Machine Learning, Deep Learning, Cloud Computing

        HIGHER SECONDARY SCHOOL CERTIFICATE (HSSC / F.Sc Pre-Engineering):
        - Board of Intermediate and Secondary Education (BISE) Lahore
        - Marks: 92.1% (Grade A-1)

        ENGLISH LANGUAGE PROFICIENCY:
        - IELTS Academic
        - Overall Band: 7.5 (Listening: 8.5, Reading: 8.0, Writing: 7.0, Speaking: 7.5)

        STANDARDIZED TEST:
        - HEC HAT Score: 84 / 100
        - GRE General: 318 (Quant: 165, Verbal: 153, AWA: 4.0)

        PREFERENCES & FINANCIAL CAPACITY:
        - Target Degree Level: Master's (MS/MSc)
        - Target Specialization: Computer Science / Machine Learning / Artificial Intelligence
        - Preferred Regions: Europe, Asia, Americas
        - Maximum Out-of-Pocket Family Budget: PKR 350,000
        """

        t_upload_start = time.perf_counter()
        files = {"file": ("Muhammad_Hamza_CV.txt", cv_content, "text/plain")}
        data = {"session_id": session_id}

        upload_res = await client.post("/api/profile/upload", data=data, files=files)
        t_upload_duration = time.perf_counter() - t_upload_start
        audit_metrics["timings"]["document_upload_and_extraction_sec"] = round(t_upload_duration, 4)

        if upload_res.status_code != 200:
            print(f"  ❌ Upload failed: {upload_res.text}")
            return

        upload_json = upload_res.json()
        student_profile_dict = upload_json.get("profile", {})
        print(f"  ✓ Ingestion Completed in {t_upload_duration:.2f} s")
        print(f"  ✓ Extracted Student: {student_profile_dict.get('personal', {}).get('name')}")
        print(f"  ✓ Extracted University: {student_profile_dict.get('academic', {}).get('board_university')}")
        print(f"  ✓ Academic Level: {student_profile_dict.get('academic', {}).get('current_level')}")
        print(f"  ✓ Synced GPA / Marks: {student_profile_dict.get('academic', {}).get('gpa_percentage')}%")
        print(f"  ✓ Profile Completeness Score: {upload_json.get('completeness_score')}%")

        # -------------------------------------------------------------
        # Step 2: Live Multi-Turn Intake Counselor Chat (/api/profile/chat)
        # -------------------------------------------------------------
        print("\n[STEP 2] Conversational Profile Refinement (/api/profile/chat):")
        chat_payload = {
            "session_id": session_id,
            "message": "Assalam-o-Alaikum, I graduated from FAST Lahore in BS Computer Science with 3.78 CGPA and 7.5 IELTS. I want to apply for fully funded Master's programs like Erasmus Mundus, DAAD, CSC China, or Turkiye Burslari. My family budget is PKR 350,000. Please guide me through eligibility and hidden costs.",
        }
        t_chat_start = time.perf_counter()
        chat_res = await client.post(
            "/api/profile/chat",
            json=chat_payload,
        )
        t_chat_duration = time.perf_counter() - t_chat_start
        audit_metrics["timings"]["counselor_chat_sec"] = round(t_chat_duration, 4)

        chat_json = chat_res.json()
        print(f"  ✓ Counselor Chat Latency: {t_chat_duration:.2f} s")
        print(f"  ✓ Counselor Response: {chat_json.get('response', '')[:120]}...")

        # -------------------------------------------------------------
        # Step 3: SSE Real-Time Event Subscription & Event Capture
        # -------------------------------------------------------------
        print("\n[STEP 3] SSE Real-time Event Stream Initialized (/api/stream):")
        bus = get_event_bus()
        subscription = bus.subscribe(session_id, replay_history=True)
        captured_events: List[ScholarXEvent] = []

        async def event_collector():
            try:
                async for event in subscription:
                    captured_events.append(event)
                    print(f"  📡 [LIVE SSE] {event.event_type.value:28s} | {event.agent_display_name:22s} | {str(event.payload.get('message') or event.payload.get('scholarship_name') or event.payload)[:70]}")
                    if event.event_type == AgentEventType.MISSION_COMPLETE:
                        break
            except (asyncio.CancelledError, StopAsyncIteration):
                pass

        collector_task = asyncio.create_task(event_collector())

        # -------------------------------------------------------------
        # Step 4: Autonomous 10-Node Discovery, Verification, Skeptic & Roadmap
        # -------------------------------------------------------------
        print("\n[STEP 4] Launching Autonomous Multi-Agent Mission (/api/discover):")
        t_disc_start = time.perf_counter()
        disc_res = await client.post("/api/discover", json={"session_id": session_id})
        assert disc_res.status_code == 200
        print(f"  ✓ Discovery Mission Initiated for session: {session_id}")

        # Poll status until complete
        max_wait = 120
        poll_start = time.perf_counter()
        mission_status = "RUNNING"
        while time.perf_counter() - poll_start < max_wait:
            await asyncio.sleep(3.0)
            status_res = await client.get(f"/api/discover/{session_id}/status")
            if status_res.status_code == 200:
                sdata = status_res.json()
                mission_status = sdata.get("status")
                if mission_status in ("COMPLETE", "ERROR"):
                    break

        t_disc_total = time.perf_counter() - t_disc_start
        audit_metrics["timings"]["full_10_node_pipeline_sec"] = round(t_disc_total, 4)
        collector_task.cancel()
        subscription.close()

        print(f"\n  ✓ Mission Status: {mission_status} in {t_disc_total:.2f} s")

        # -------------------------------------------------------------
        # Step 5: Session Detail & Final Results Verification
        # -------------------------------------------------------------
        print("\n[STEP 5] Research Session & Results Retrieval (/api/sessions/{session_id}):")
        session_res = await client.get(f"/api/sessions/{session_id}")
        session_json = session_res.json()
        student_obj = await store.get_student_profile(session_id)
        
        detail = await store.get_session_detail(session_id)
        if detail and detail.discovered_scholarships:
            print(f"  ✓ Total Verified Scholarships in Session: {len(detail.discovered_scholarships)}")
            print("\n  🏆 Top Matched Scholarships for Candidate:")
            for sc in detail.discovered_scholarships[:3]:
                print(f"     • {sc.name} ({sc.host_country_name})")
                print(f"       - Funding: {sc.funding.funding_type.value} (Stipend: {sc.funding.monthly_stipend or 'Covered'})")
                print(f"       - Bilateral Quota: {'Yes' if sc.pakistan_requirements.pakistan_bilateral_quota else 'No'}")
        
        # Load roadmap if present in session parameters
        params = detail.mission_parameters if detail else {}
        if "roadmap" in params:
            roadmap_data = params["roadmap"]
            print(f"\n  🏛️  Personalized Action Plan for Pakistani Applicant:")
            print(f"     • Estimated Prep Time: {roadmap_data.get('total_preparation_days_estimated')} days")
            print(f"     • Total Budget Needed: PKR {roadmap_data.get('total_budget_needed_pkr', 0):,}")
            print(f"     • Designated Offices: {len(roadmap_data.get('relevant_pakistani_offices', []))} local offices mapped")
            for office in roadmap_data.get("relevant_pakistani_offices", [])[:2]:
                print(f"       📍 {office.get('office_name')} ({office.get('city')}) - Fee: PKR {office.get('fee_pkr', 0):,}")
            print("     • Urgent Actions:")
            for act in roadmap_data.get("urgent_next_actions", [])[:2]:
                print(f"       ⚡ {act}")

        # -------------------------------------------------------------
        # Step 6: Full System & API Key Performance Audit
        # -------------------------------------------------------------
        total_time = time.perf_counter() - start_total_time
        audit_metrics["timings"]["total_audit_runtime_sec"] = round(total_time, 4)
        audit_metrics["events"]["total_events_streamed"] = len(captured_events)
        audit_metrics["events"]["event_types"] = list(set(e.event_type.value for e in captured_events))

        # API Keys summary
        health_res = await client.get("/api/health")
        health_data = health_res.json()
        audit_metrics["api_keys"] = health_data.get("api_keys", {})

        print("\n" + "=" * 90)
        print("📊 SCHOLARX FULL PERFORMANCE, API & SPEED AUDIT REPORT")
        print("=" * 90)

        print("\n⏱️  1. LATENCY & SPEED AUDIT:")
        print(f"  • Database Connection & Init:          {audit_metrics['timings']['db_initialization_sec'] * 1000:8.2f} ms")
        print(f"  • Document Upload & LLM Extraction:    {audit_metrics['timings']['document_upload_and_extraction_sec']:8.2f} s")
        print(f"  • Intake Counselor Chat Response:      {audit_metrics['timings']['counselor_chat_sec']:8.2f} s")
        print(f"  • 10-Node Master Pipeline Execution:   {audit_metrics['timings']['full_10_node_pipeline_sec']:8.2f} s")
        print(f"  • Total End-to-End Audit Run Time:     {audit_metrics['timings']['total_audit_runtime_sec']:8.2f} s")

        print("\n🔑 2. API KEYS POOL & HEALTH AUDIT:")
        for service, stats in audit_metrics["api_keys"].items():
            print(f"  • {service.upper():10s} | Total Keys: {stats.get('total_keys', 0)} | Healthy: {stats.get('healthy_keys', 0)} | Rate-Limited: {stats.get('rate_limited_keys', 0)} | Total Calls: {stats.get('total_requests', 0)} | Errors: {stats.get('error_count', 0)}")

        print("\n📡 3. REAL-TIME EVENT STREAMING AUDIT:")
        print(f"  • Total SSE Events Emitted & Received:  {len(captured_events)}")
        throughput = len(captured_events) / max(audit_metrics['timings']['full_10_node_pipeline_sec'], 0.1)
        print(f"  • Streaming Event Throughput:           {throughput:5.2f} events/second")
        print(f"  • Distinct Event Types Emitted:         {len(audit_metrics['events']['event_types'])}")

        print("\n💾 4. PERSISTENCE & SQLITE CACHE AUDIT:")
        all_cached = await store.get_all_cached_scholarships()
        all_sessions = await store.list_sessions()
        print(f"  • Verified Scholarships in SQLite:     {len(all_cached)}")
        print(f"  • Active Sessions in Store:            {len(all_sessions)}")

        # Save audit report to disk
        report_path = Path("./data/audit_report_phase5.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(audit_metrics, f, indent=2)
        print(f"\n  ✓ Complete JSON Audit Report exported to: {report_path.resolve()}")
        print("=" * 90)


if __name__ == "__main__":
    asyncio.run(run_audit())
