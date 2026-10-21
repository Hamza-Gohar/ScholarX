import pytest
from graph.builder import build_scholarx_graph
from graph.state import ScholarXState
from schemas.scholarship import FundingDetails, FundingType, PakistanSpecificRequirements, Scholarship
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


@pytest.mark.asyncio
async def test_langgraph_full_pipeline_execution():
    """Tests the compiled LangGraph StateGraph end-to-end through all 10 nodes."""
    graph = build_scholarx_graph()

    student = StudentProfile(
        student_id="std-graph-01",
        session_id="sess-graph-01",
        personal=PersonalInfo(name="Sara", city="Islamabad", age=21),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            field_of_study="Computer Science",
            gpa_percentage=85.0,
            gpa_4_scale=3.7,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.0,
            has_english_test=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(target_degree_level="Master's", max_out_of_pocket_pkr=250000),
    )

    initial_state: ScholarXState = {
        "session_id": "sess-graph-01",
        "student_id": "std-graph-01",
        "student_profile": student,
        "candidate_scholarships": [
            Scholarship(
                scholarship_id="SCH-GRAPH-01",
                name="Stipendium Hungaricum",
                host_country="HU",
                host_country_name="Hungary",
                region="Europe",
                source_url="https://stipendiumhungaricum.hu",
                funding=FundingDetails(funding_type=FundingType.FULL),
                pakistan_requirements=PakistanSpecificRequirements(
                    pakistan_eligible=True,
                    pakistan_bilateral_quota=True,
                    pakistan_quota_seats=400,
                ),
            )
        ],
        "events_queue": [],
    }

    final_state = await graph.ainvoke(initial_state)

    assert final_state is not None
    assert final_state["active_phase"] in ("COMPLETE", "MISSION_COMPLETE", "ADVISOR")
    assert len(final_state["ranked_results"]) >= 1
    assert final_state["ranked_results"][0].rank == 1
    assert final_state["final_roadmap"] is not None
    assert len(final_state["events_queue"]) >= 5
