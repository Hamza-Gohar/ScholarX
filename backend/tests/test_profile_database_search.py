import pytest
from httpx import AsyncClient, ASGITransport
from db.session_store import get_session_store
from main import app
from schemas.student import (
    StudentProfile,
    PersonalInfo,
    AcademicRecord,
    LanguageProficiency,
    Preferences,
    EducationLevel,
    EnglishTestType,
)


@pytest.mark.asyncio
async def test_search_scholarships_for_undergraduate_profile():
    store = get_session_store()
    await store.init_db()

    profile = StudentProfile(
        student_id="std-test-undergrad",
        personal=PersonalInfo(name="Hamza Gohar", city="Lahore"),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            field_of_study="Computer Science",
            gpa_percentage=92.0,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.0,
            has_english_test=True,
        ),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            target_fields=["Computer Science"],
            preferred_regions=["Europe", "Asia"],
            max_out_of_pocket_pkr=150000,
        ),
    )

    results = await store.search_scholarships_for_profile(student=profile, limit=10)
    assert len(results) > 0, "Expected database search to return scholarships for undergraduate profile"
    
    # Verify all returned scholarships are Pakistan eligible and match Bachelor's level
    for sc in results:
        assert sc.pakistan_requirements.pakistan_eligible is True
        degrees = [d.lower() for d in (sc.eligibility.degree_levels if sc.eligibility else [])]
        assert any(k in " ".join(degrees) for k in ["bachelor", "undergrad", "bs", "diploma"]), (
            f"Scholarship {sc.name} degree levels {degrees} mismatch for Bachelor's target"
        )


@pytest.mark.asyncio
async def test_search_scholarships_for_postgraduate_profile():
    store = get_session_store()
    await store.init_db()

    profile = StudentProfile(
        student_id="std-test-postgrad",
        personal=PersonalInfo(name="Muhammad Usman", city="Islamabad"),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            field_of_study="Artificial Intelligence",
            gpa_percentage=88.0,
            gpa_4_scale=3.82,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
        ),
        preferences=Preferences(
            target_degree_level="Master's",
            target_fields=["Artificial Intelligence", "Data Science"],
            preferred_regions=["Europe", "Americas", "MENA"],
            max_out_of_pocket_pkr=350000,
        ),
    )

    results = await store.search_scholarships_for_profile(student=profile, limit=10)
    assert len(results) > 0, "Expected database search to return scholarships for Master's profile"
    
    for sc in results:
        assert sc.pakistan_requirements.pakistan_eligible is True
        degrees = [d.lower() for d in (sc.eligibility.degree_levels if sc.eligibility else [])]
        assert any(k in " ".join(degrees) for k in ["master", "ms", "msc", "mphil", "phd", "graduate", "postgrad"]), (
            f"Scholarship {sc.name} degree levels {degrees} mismatch for Master's target"
        )


@pytest.mark.asyncio
async def test_api_scholarships_match_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        profile_dict = {
            "student_id": "std-test-api",
            "personal": {"name": "Aisha Siddiqui", "city": "Karachi"},
            "academic": {
                "current_level": "Intermediate / ICS / FSc / FA",
                "field_of_study": "Computer Science",
                "gpa_percentage": 87.2,
            },
            "language": {
                "english_proficiency_test": "IELTS",
                "ielts_overall": 8.0,
                "has_english_test": True,
            },
            "preferences": {
                "target_degree_level": "Bachelor's",
                "target_fields": ["Computer Science"],
                "preferred_regions": ["Europe", "Asia", "Americas"],
            },
        }

        resp = await client.post("/api/scholarships/match", json=profile_dict)
        assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}: {resp.text}"
        data = resp.json()
        assert "scholarships" in data
        assert data["total"] > 0
        assert len(data["scholarships"]) > 0
