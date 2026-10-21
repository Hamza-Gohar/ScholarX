import asyncio
import os
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from db.session_store import get_session_store
from schemas.events import AgentEventType, ScholarXEvent
from schemas.student import StudentProfile
from tools.document_parser import DocumentParserTool
from tools.document_extractor import DocumentExtractor
from utils.profile_validator import ProfileValidator
from agents.profile_agent import ProfileAgent
from agents.discovery_commander import DiscoveryCommander
from agents.skeptic_agent import SkepticAgent
from agents.advisor_agent import AdvisorAgent
from workflows.eligibility import EligibilityInvestigator
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.deadline import DeadlineAnalyzer
from workflows.synthesis import SynthesisWorkflow
from workflows.ranking import RankingEngine
from graph.builder import build_scholarx_graph


async def main():
    print("=" * 80)
    print("🚀 SCHOLARX REAL-WORLD LIVE SYSTEM DEMO: PHASES 0 TO 4")
    print("=" * 80)

    session_store = get_session_store()
    await session_store.init_db()

    # -------------------------------------------------------------
    # [PHASE 0] Knowledge Base & Pre-Seeded Datasets
    # -------------------------------------------------------------
    cached_scholarships = await session_store.get_all_cached_scholarships()
    print(f"\n[PHASE 0] Pre-Seeded Knowledge Base:")
    print(f"  ✓ Total Verified Scholarships in SQLite: {len(cached_scholarships)}")
    regions_count = {}
    for sc in cached_scholarships:
        regions_count[sc.region] = regions_count.get(sc.region, 0) + 1
    for reg, count in regions_count.items():
        print(f"    - {reg}: {count} scholarships")

    # -------------------------------------------------------------
    # [PHASE 1] Real Physical Pakistani Student Document Ingestion
    # -------------------------------------------------------------
    test_dir = Path("./data/test_documents")
    test_dir.mkdir(parents=True, exist_ok=True)
    resume_txt_path = test_dir / "Hamza_Tariq_CV.txt"
    with open(resume_txt_path, "w", encoding="utf-8") as f:
        f.write("""
        CURRICULUM VITAE
        Name: Hamza Tariq
        Email: hamza.tariq@gmail.com
        Contact: +92-300-1234567
        City: Lahore, Punjab, Pakistan
        Nationality: Pakistani (PK)

        ACADEMIC BACKGROUND:
        - Degree: Bachelor of Science in Computer Science (BS CS) - 16 Years
        - University: FAST National University of Computer and Emerging Sciences (FAST-NUCES), Lahore Campus
        - CGPA: 3.78 / 4.0 (Marks Equivalent: 85.5%)
        - Passing Year: 2026
        - Key Coursework: Distributed Systems, Machine Learning, Deep Learning, Cloud Computing, Algorithms

        INTERMEDIATE:
        - ICS (Physics, Mathematics, Computer Science) - Punjab Group of Colleges Lahore (BISE Lahore) - 88.0% Marks

        ENGLISH LANGUAGE PROFICIENCY:
        - IELTS Academic (Valid until 2027)
        - Overall Band Score: 7.5 (Listening: 8.0 | Reading: 7.5 | Writing: 7.0 | Speaking: 7.5)

        PREFERENCES & BUDGET:
        - Target Degree: Master's in Computer Science / Artificial Intelligence
        - Maximum Out-of-Pocket Budget: PKR 300,000
        - Target Regions: Europe, Asia, Americas
        """)

    print(f"\n[PHASE 1] Document Ingestion & Live Parsing:")
    parser = DocumentParserTool()
    parsed_doc = parser.parse_file(str(resume_txt_path))
    print(f"  ✓ File Ingested: {parsed_doc.filename}")
    print(f"  ✓ Document Type Classified: {parsed_doc.doc_type.value}")
    print(f"  ✓ Clean Character Count: {parsed_doc.char_count}")

    print(f"\n[PHASE 1] Live LLM Document Information Extraction:")
    extractor = DocumentExtractor()
    extracted_data = await extractor.extract_from_text(parsed_doc.clean_text, parsed_doc.doc_type.value)
    
    student_name = extracted_data.get('personal', {}).get('name', 'Hamza Tariq')
    print(f"  ✓ Extracted Candidate: {student_name} ({extracted_data.get('personal', {}).get('city', 'Lahore')})")
    print(f"  ✓ Extracted Degree: {extracted_data.get('academic', {}).get('current_level')} in {extracted_data.get('academic', {}).get('field_of_study')}")
    print(f"  ✓ Extracted GPA/Marks: {extracted_data.get('academic', {}).get('gpa_percentage')}%")
    print(f"  ✓ Extracted IELTS: Band {extracted_data.get('language', {}).get('ielts_overall')}")

    session_id = "sess-real-world-001"
    student = StudentProfile(
        student_id="std-real-world-001",
        session_id=session_id,
    )
    profile_agent = ProfileAgent()
    profile_agent._apply_extracted_updates(student, extracted_data)
    student.documents.cv.uploaded = True
    student.preferences.target_degree_level = "Master's"
    student.preferences.target_fields = ["Computer Science", "Artificial Intelligence"]
    student.preferences.max_out_of_pocket_pkr = 300000
    student = profile_agent.validator.validate_and_enrich(student)

    print(f"  ✓ Profile Completeness: {student.profile_completeness}%")
    print(f"  ✓ Converted US 4.0 GPA: {student.academic.gpa_4_scale}")
    print(f"  ✓ Converted UK Honours: {student.academic.uk_classification}")

    # -------------------------------------------------------------
    # [PHASE 2] Discovery Commander Mission
    # -------------------------------------------------------------
    print(f"\n[PHASE 2] Discovery Commander Multi-Regional Mission:")
    discovery_commander = DiscoveryCommander()
    events_captured = []

    def log_event(evt: ScholarXEvent):
        events_captured.append(evt)
        print(f"  📡 [EVENT STREAM] {evt.event_type.value:30s} | {evt.agent_display_name:22s} | {evt.payload.get('message', '') or evt.payload.get('scholarship_name', '') or str(evt.payload)}")

    candidates = await discovery_commander.execute_discovery_mission(student, event_callback=log_event)
    print(f"  ✓ Total Discovered Candidates: {len(candidates)} scholarships")

    # Pick top 4 representative candidates across regions for deep verification
    selected_pool = candidates[:4]

    # -------------------------------------------------------------
    # [PHASE 3] Deep Verification Workflows & Skeptic Agent
    # -------------------------------------------------------------
    print(f"\n[PHASE 3] Deep Verification & Adversarial Skeptic Arena:")
    eligibility_wf = EligibilityInvestigator()
    cost_wf = TrueCostAnalyzer()
    deadline_wf = DeadlineAnalyzer()
    skeptic_agent = SkepticAgent()
    synthesis_wf = SynthesisWorkflow()

    candidates_bundle = []
    synthesized_cards = []

    for sc in selected_pool:
        print(f"\n  🔬 Verifying: {sc.name} ({sc.host_country_name})")
        
        # 1. 15-Dimension Eligibility
        elig = eligibility_wf.evaluate(sc, student, event_callback=log_event)
        print(f"     • Eligibility: {'PASS' if elig.is_eligible else 'FAIL'} (Score: {elig.eligibility_score}/100)")
        if elig.pakistan_advantages:
            print(f"       + Pakistan Advantages: {', '.join(elig.pakistan_advantages)}")

        # 2. 4-Phase PKR True Cost
        cost = cost_wf.analyze(sc, student, event_callback=log_event)
        print(f"     • True PKR Out-of-Pocket: PKR {cost.total_out_of_pocket_pkr:,} ({'Within Budget' if cost.is_within_budget else 'Exceeds Budget'})")
        print(f"       + Funding Score: {cost.funding_score}/100")

        # 3. Deadline Intelligence
        dl = deadline_wf.analyze(sc, student, event_callback=log_event)
        print(f"     • Deadline Feasibility: {dl.days_remaining} days left ({dl.risk_level} Risk Tier)")

        # 4. Skeptic Adversarial Review
        evidence = await skeptic_agent.evaluate_skepticism(sc, student, event_callback=log_event)
        print(f"     • Skeptic Challenges Raised: {len(evidence.skeptic_challenges)}")
        for chk in evidence.skeptic_challenges[:2]:
            print(f"       ⚠️  [{chk.category}] {chk.title}: {chk.description[:90]}...")
        for db in evidence.debate_summary[:1]:
            print(f"       ⚔️  Clash Verdict: {db.topic} -> {db.verdict}")

        # 5. Synthesis
        synth = synthesis_wf.synthesize(sc, elig, cost, dl, evidence, student, event_callback=log_event)
        synthesized_cards.append(synth)
        candidates_bundle.append((sc, elig, cost, dl, evidence))

    # -------------------------------------------------------------
    # [PHASE 4] Weighted Ranking Engine & Final Advisor Roadmap
    # -------------------------------------------------------------
    print(f"\n[PHASE 4] Pakistan-Adjusted Weighted Composite Ranking:")
    ranking_engine = RankingEngine()
    ranked_results = ranking_engine.rank_opportunities(candidates_bundle, student, event_callback=log_event)

    print("\n  📊 Final Leaderboard (Composite Matching Scores):")
    print("  " + "-" * 75)
    for res in ranked_results:
        print(f"  Rank #{res.rank} | Score: {res.overall_match_score:5.1f}/100 | {res.scholarship_name}")
        print(f"          • Elig: {res.eligibility_score:.0f} | Funding: {res.true_funding_score:.0f} | Bilateral Bonus: {res.bilateral_bonus_score:.0f} | Deadlines: {res.deadline_score:.0f}")

    # Top Opportunity Roadmap Generation
    top_score = ranked_results[0]
    top_sc = next(sc for sc in selected_pool if sc.scholarship_id == top_score.scholarship_id)

    print(f"\n[PHASE 4] Final Advisor Agent Execution Roadmap:")
    print(f"  🎯 Generating Pakistan Action Plan for Top Match: {top_sc.name}")
    advisor_agent = AdvisorAgent()
    roadmap = await advisor_agent.generate_roadmap(top_sc, top_score, student, event_callback=log_event)

    print(f"\n  📋 Personalized Roadmap Summary:")
    print(f"     • Target Intake: {roadmap.target_intake}")
    print(f"     • Estimated Prep Time: {roadmap.total_preparation_days_estimated} days")
    print(f"     • Total Budget Needed: PKR {roadmap.total_budget_needed_pkr:,}")
    
    print("\n  🏛️  Designated Pakistani Government & Test Centers to Visit:")
    for office in roadmap.relevant_pakistani_offices:
        print(f"     📍 {office.office_name} ({office.city})")
        print(f"        - Address: {office.address}")
        print(f"        - Fee: PKR {office.fee_pkr:,} | Turnaround: ~{office.estimated_turnaround_days} days")
        if office.pro_tips:
            print(f"        - Pro Tip: {office.pro_tips[0]}")

    print("\n  🗓️  Milestone Action Plan:")
    for ms in roadmap.milestones:
        print(f"     📌 [{ms.phase.value}] {ms.title} ({ms.target_timeline_days}) - Est Cost: PKR {ms.total_phase_cost_pkr:,}")
        for act in ms.actions:
            office_str = f" [Office: {act.assigned_office}]" if act.assigned_office else ""
            print(f"        ✓ {act.description} (~{act.estimated_days}d, PKR {act.estimated_cost_pkr:,}){office_str}")

    print("\n  ⚡ Urgent Next Actions:")
    for act in roadmap.urgent_next_actions:
        print(f"     🔥 {act}")

    # -------------------------------------------------------------
    # Complete Master LangGraph 10-Node Pipeline Verification
    # -------------------------------------------------------------
    print(f"\n[PHASE 4] Master LangGraph StateGraph Live End-to-End Run:")
    graph = build_scholarx_graph()
    initial_state = {
        "session_id": "sess-graph-live-demo",
        "student_id": "std-real-world-001",
        "student_profile": student,
        "candidate_scholarships": selected_pool,
        "events_queue": [],
    }
    final_graph_state = await graph.ainvoke(initial_state)
    print(f"  ✓ LangGraph Pipeline Completed Successfully!")
    print(f"  ✓ Active Phase: {final_graph_state.get('active_phase')}")
    print(f"  ✓ Total Ranked in State: {len(final_graph_state.get('ranked_results', []))}")
    print(f"  ✓ Total Events Emitted in State: {len(final_graph_state.get('events_queue', []))}")

    print("\n" + "=" * 80)
    print(f"🎉 ALL PHASES (0, 1, 2, 3, 4) TESTED AND OPERATIONAL IN REAL-WORLD SCENARIO!")
    print(f"   Total Real-time SSE Events Emitted during execution: {len(events_captured)}")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
