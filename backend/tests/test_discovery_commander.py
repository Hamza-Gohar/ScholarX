import pytest
from unittest.mock import AsyncMock, patch
from agents.discovery_commander import DiscoveryCommander
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import Scholarship, ScholarshipStatus
from schemas.student import StudentProfile


@pytest.fixture
def ics_student():
    return StudentProfile(
        student_id="std-ics-pk",
        session_id="sess-cmd-01",
        personal={"name": "Hamza Tariq", "nationality": "PK", "city": "Lahore"},
        academic={"current_level": "Intermediate / ICS / FSc / FA", "field_of_study": "Computer Science", "gpa_percentage": 87.0},
        language={"english_proficiency_test": "IELTS", "ielts_overall": 7.0, "has_english_test": True},
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science", "AI"]},
    )


@pytest.fixture
def fsc_no_ielts_student():
    return StudentProfile(
        student_id="std-fsc-no-ielts",
        session_id="sess-cmd-02",
        personal={"name": "Zainab Ali", "nationality": "PK", "city": "Rawalpindi"},
        academic={"current_level": "Intermediate / ICS / FSc / FA", "field_of_study": "Pre-Engineering", "gpa_percentage": 78.0},
        language={"english_proficiency_test": "None / Not Available", "has_english_test": False},
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Engineering", "Robotics"]},
    )


@pytest.fixture
def bs_graduate_student():
    return StudentProfile(
        student_id="std-bs-pk",
        session_id="sess-cmd-03",
        personal={"name": "Bilal Ahmed", "nationality": "PK", "city": "Islamabad"},
        academic={"current_level": "Bachelor's / BS / BE / BBA", "field_of_study": "Software Engineering", "gpa_percentage": 85.0},
        language={"english_proficiency_test": "IELTS", "ielts_overall": 7.5, "has_english_test": True},
        preferences={"target_degree_level": "Master's", "target_fields": ["Software Engineering", "Cloud Computing"]},
    )


def test_query_generation_strategy_all_regions(ics_student, fsc_no_ielts_student, bs_graduate_student):
    """Verifies that query generation adapts correctly to IELTS status, degree levels, and regions."""
    commander = DiscoveryCommander()

    regions = ["Europe", "Asia", "Americas", "MENA", "Oceania"]

    for reg in regions:
        # Student with IELTS
        q_with_ielts = commander.generate_scout_queries(ics_student, region=reg)
        assert len(q_with_ielts) >= 1
        assert any("Pakistan" in q or "Pakistani" in q for q in q_with_ielts)

        # Student without IELTS (should generate non-IELTS / MOI / Embassy queries for Europe/Asia)
        q_no_ielts = commander.generate_scout_queries(fsc_no_ielts_student, region=reg)
        assert len(q_no_ielts) >= 1
        assert any("Pakistan" in q or "Pakistani" in q for q in q_no_ielts)

        # Master's Graduate (Fulbright / KAUST / Vanier)
        q_grad = commander.generate_scout_queries(bs_graduate_student, region=reg)
        assert len(q_grad) >= 1
        if reg == "Americas":
            assert any("Fulbright" in q for q in q_grad)
        if reg == "MENA":
            assert any("KAUST" in q or "KFUPM" in q for q in q_grad)


def test_scholarship_deduplication():
    """Tests deduplication based on core tokens, noise word removal, and URL matching."""
    commander = DiscoveryCommander()

    sc1 = Scholarship(
        scholarship_id="SCH-1",
        name="Stipendium Hungaricum",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu/apply",
        status=ScholarshipStatus.DISCOVERED,
    )
    sc2 = Scholarship(
        scholarship_id="SCH-2",
        name="stipendium hungaricum scholarship programme",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        status=ScholarshipStatus.DISCOVERED,
    )
    sc3 = Scholarship(
        scholarship_id="SCH-3",
        name="Turkiye Burslari",
        host_country="TR",
        host_country_name="Turkey",
        region="MENA",
        source_url="https://turkiyeburslari.gov.tr",
        status=ScholarshipStatus.DISCOVERED,
    )
    sc4 = Scholarship(
        scholarship_id="SCH-4",
        name="Different Scholarship Name",
        host_country="TR",
        host_country_name="Turkey",
        region="MENA",
        source_url="https://turkiyeburslari.gov.tr/",
        status=ScholarshipStatus.DISCOVERED,
    )

    # sc1 and sc2 should deduplicate (same token set)
    # sc3 and sc4 should deduplicate (same URL)
    deduped = commander.deduplicate_scholarships([sc1, sc2, sc3, sc4])
    assert len(deduped) == 2


@pytest.mark.asyncio
async def test_execute_discovery_mission_with_resilience(ics_student):
    """Tests commander parallel orchestration, event emissions, and resilience when one scout fails."""
    commander = DiscoveryCommander()
    events = []

    def on_event(e: ScholarXEvent):
        events.append(e)

    mock_discovered_eu = [
        Scholarship(
            scholarship_id="SCH-EU-LIVE-1",
            name="DAAD Fellowship Live",
            host_country="DE",
            host_country_name="Germany",
            region="Europe",
            source_url="https://daad.de/live",
            status=ScholarshipStatus.DISCOVERED,
        )
    ]

    # Europe scout succeeds
    commander.scouts["Europe"].run = AsyncMock(return_value=(mock_discovered_eu, []))
    # Asia scout raises unexpected error (should not crash entire mission)
    commander.scouts["Asia"].run = AsyncMock(side_effect=RuntimeError("Asia Scout Connection Timeout"))
    # Americas, MENA, Oceania succeed
    commander.scouts["Americas"].run = AsyncMock(return_value=([], []))
    commander.scouts["MENA"].run = AsyncMock(return_value=([], []))
    commander.scouts["Oceania"].run = AsyncMock(return_value=([], []))

    with patch.object(commander.session_store, "get_all_cached_scholarships", new_callable=AsyncMock) as mock_cache:
        mock_cache.return_value = []
        with patch.object(commander.session_store, "bulk_upsert_scholarships_cache", new_callable=AsyncMock) as mock_upsert:
            results = await commander.execute_discovery_mission(ics_student, event_callback=on_event)

            assert len(results) >= 1
            assert any(r.scholarship_id == "SCH-EU-LIVE-1" for r in results)
            assert mock_upsert.call_count >= 1

            event_types = [e.event_type for e in events]
            assert AgentEventType.SCOUT_DEPLOYED in event_types
            assert AgentEventType.DISCOVERY_AGGREGATION_COMPLETE in event_types
