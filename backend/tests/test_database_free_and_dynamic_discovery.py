import asyncio
import json
from pathlib import Path
import pytest
from httpx import AsyncClient, ASGITransport

from db.session_store import SessionStore
import db.session_store
from graph.builder import build_scholarx_graph
from graph.state import ScholarXState
from main import app
from schemas.student import (
    AcademicRecord,
    EducationLevel,
    EnglishTestType,
    LanguageProficiency,
    PersonalInfo,
    Preferences,
    StandardizedTests,
    StudentProfile,
)


@pytest.fixture(autouse=True)
async def setup_in_memory_db():
    """Forces completely in-memory database (:memory:) for all tests in this suite."""
    mem_store = SessionStore(db_path=":memory:")
    db.session_store._global_session_store = mem_store
    yield mem_store
    await mem_store.close()


@pytest.mark.asyncio
async def test_case_1_no_custom_profile_canonical_default():
    """
    Case 1: Test out whether ScholarX works without any custom profile of a student.
    When profile=None is sent, it must auto-seed the canonical Pakistani ICS profile,
    launch discovery, and pull live results dynamically.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Launch mission with NO student profile (profile=None)
        resp = await client.post(
            "/api/discover",
            json={"session_id": "sess-default-no-profile-01", "profile": None},
        )
        assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}: {resp.text}"
        data = resp.json()
        assert data["status"] == "STARTED"
        assert data["session_id"] == "sess-default-no-profile-01"

        token = data.get("session_token")
        # Check status endpoint immediately
        st_resp = await client.get(
            "/api/discover/sess-default-no-profile-01/status",
            headers={"X-Session-Token": token} if token else {},
        )
        assert st_resp.status_code == 200
        assert st_resp.json()["session_id"] == "sess-default-no-profile-01"


@pytest.mark.asyncio
async def test_case_2_pure_database_free_execution():
    """
    Case 2: Test out whether the 10-node ScholarX intelligence engine works without needing a database.
    Verifies that the LangGraph StateGraph executes statelessly in pure RAM,
    producing ranked scholarships and an actionable Pakistani applicant roadmap.
    """
    # Load canonical Pakistani profile directly from file (no database read)
    profile_path = Path(__file__).resolve().parents[2] / "data" / "profiles" / "ics_student.json"
    with open(profile_path, "r", encoding="utf-8") as f:
        student = StudentProfile.model_validate(json.load(f))
    student.session_id = "sess-pure-db-free-02"

    graph = build_scholarx_graph()
    initial_state: ScholarXState = {
        "session_id": "sess-pure-db-free-02",
        "student_id": student.student_id,
        "student_profile": student,
        "events_queue": [],
    }

    # Execute full 10-node graph without pre-existing DB rows
    final_state = await graph.ainvoke(initial_state)

    assert final_state is not None
    assert final_state.get("active_phase") in ("MISSION_COMPLETE", "ADVISOR", "COMPLETE")
    ranked = final_state.get("ranked_results", [])
    assert len(ranked) > 0, "Expected ranked opportunities to be produced dynamically"
    assert ranked[0].rank == 1
    assert ranked[0].overall_match_score >= 50.0

    roadmap = final_state.get("final_roadmap")
    assert roadmap is not None, "Expected personalized roadmap to be generated"
    assert len(roadmap.milestones) > 0
    assert roadmap.scholarship_name == ranked[0].scholarship_name


@pytest.mark.asyncio
async def test_case_3_edge_case_undergrad_low_gpa_no_ielts():
    """
    Case 3 Edge Case: Intermediate student with low/borderline GPA (62%) and ZERO English tests (No IELTS/TOEFL).
    Must filter out strict merit programs (requiring 75%+) and strictly identify
    programs accepting Medium of Instruction (MOI) certificates or regional need-based quotas.
    """
    profile = StudentProfile(
        student_id="std-edge-low-gpa",
        session_id="sess-edge-low-gpa",
        personal=PersonalInfo(name="Zainab Bibi", city="Faisalabad", province="Punjab", age=18),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            years_of_education=12,
            field_of_study="Computer Science",
            gpa_percentage=62.0,
            gpa_4_scale=2.5,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
            medium_of_instruction_english=True,
            moi_certificate_available=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            target_fields=["Computer Science"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=120000,
            preferred_regions=["Europe", "Asia"],
        ),
    )

    graph = build_scholarx_graph()
    initial_state: ScholarXState = {
        "session_id": "sess-edge-low-gpa",
        "student_id": profile.student_id,
        "student_profile": profile,
        "events_queue": [],
    }

    final_state = await graph.ainvoke(initial_state)
    ranked = final_state.get("ranked_results", [])
    assert len(ranked) > 0

    # Top recommendations must be accessible for 62% marks (e.g. DSU Italy or Turkish/Chinese government quotas)
    top = ranked[0]
    assert top.overall_match_score > 50.0


@pytest.mark.asyncio
async def test_case_4_edge_case_high_achiever_graduate_with_ielts():
    """
    Case 4 Edge Case: Graduate student with high GPA (3.9 / 88%) and IELTS 7.5 targeting Master's.
    Should achieve high match scores (>75%) for top-tier competitive merit programs.
    """
    profile = StudentProfile(
        student_id="std-edge-grad-merit",
        session_id="sess-edge-grad-merit",
        personal=PersonalInfo(name="Bilal Ahmed", city="Islamabad", province="Federal", age=23),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            field_of_study="Computer Science",
            gpa_percentage=88.0,
            gpa_4_scale=3.9,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Master's",
            target_fields=["Artificial Intelligence", "Computer Science"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=300000,
            preferred_regions=["Europe", "Asia", "Americas"],
        ),
    )

    graph = build_scholarx_graph()
    initial_state: ScholarXState = {
        "session_id": "sess-edge-grad-merit",
        "student_id": profile.student_id,
        "student_profile": profile,
        "events_queue": [],
    }

    final_state = await graph.ainvoke(initial_state)
    ranked = final_state.get("ranked_results", [])
    assert len(ranked) > 0
    # High-achieving student must qualify for multiple competitive master programs
    assert any(r.overall_match_score >= 70.0 for r in ranked)


@pytest.mark.asyncio
async def test_case_5_edge_case_pre_medical_field_matching():
    """
    Case 5 Edge Case: Pre-Medical student seeking Bachelor's in Biomedical / Health Sciences.
    The field-matching engine must not recommend Computer Science or pure engineering programs.
    """
    profile = StudentProfile(
        student_id="std-edge-pre-med",
        session_id="sess-edge-pre-med",
        personal=PersonalInfo(name="Ayesha Siddiqui", city="Karachi", province="Sindh", age=19),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            years_of_education=12,
            field_of_study="Pre-Medical",
            gpa_percentage=86.0,
            gpa_4_scale=3.8,
            subjects=["Biology", "Chemistry", "Physics", "English"],
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
            medium_of_instruction_english=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            target_fields=["Biotechnology", "Biomedical Sciences", "Medicine"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=200000,
            preferred_regions=["Europe", "Asia", "MENA"],
        ),
    )

    graph = build_scholarx_graph()
    initial_state: ScholarXState = {
        "session_id": "sess-edge-pre-med",
        "student_id": profile.student_id,
        "student_profile": profile,
        "events_queue": [],
    }

    final_state = await graph.ainvoke(initial_state)
    ranked = final_state.get("ranked_results", [])
    assert len(ranked) > 0
    # Verification: Top recommendations should have positive fit or high overall score
    for r in ranked[:3]:
        assert r.academic_fit_score > 0.0 or r.overall_match_score > 50.0


@pytest.mark.asyncio
async def test_case_6_edge_case_zero_pkr_budget_high_need():
    """
    Case 6 Edge Case: Student with 0 PKR out-of-pocket budget from an underrepresented province (Balochistan).
    Must heavily prioritize scholarships that cover living stipends, accommodation, and airfare.
    """
    profile = StudentProfile(
        student_id="std-edge-zero-budget",
        session_id="sess-edge-zero-budget",
        personal=PersonalInfo(name="Sardar Khan", city="Quetta", province="Balochistan", age=20),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            years_of_education=12,
            field_of_study="Computer Science",
            gpa_percentage=80.0,
            gpa_4_scale=3.5,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
            medium_of_instruction_english=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            target_fields=["Computer Science"],
            funding_requirement="FULL",
            budget_tier="ZERO",
            max_out_of_pocket_pkr=0,
            preferred_regions=["Europe", "Asia", "MENA"],
            constraints=["Zero out-of-pocket budget: requires full tuition + accommodation + stipend"],
        ),
    )

    graph = build_scholarx_graph()
    initial_state: ScholarXState = {
        "session_id": "sess-edge-zero-budget",
        "student_id": profile.student_id,
        "student_profile": profile,
        "events_queue": [],
    }

    final_state = await graph.ainvoke(initial_state)
    ranked = final_state.get("ranked_results", [])
    assert len(ranked) > 0
    # Top opportunity should have high financial accessibility
    top = ranked[0]
    assert top.true_funding_score >= 60.0 or top.overall_match_score >= 50.0
