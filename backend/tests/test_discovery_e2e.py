import pytest
from unittest.mock import AsyncMock, patch
from agents.discovery_commander import DiscoveryCommander
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import Scholarship, ScholarshipStatus
from schemas.student import StudentProfile


@pytest.mark.asyncio
async def test_discovery_mission_end_to_end():
    commander = DiscoveryCommander()

    student = StudentProfile(
        student_id="std-e2e-pk",
        session_id="sess-e2e-disc",
        personal={"name": "Hamza Tariq", "nationality": "PK", "city": "Lahore"},
        academic={
            "current_level": "Intermediate / ICS / FSc / FA",
            "field_of_study": "Computer Science",
            "gpa_percentage": 87.0,
            "intermediate_board": "BISE Lahore",
        },
        language={
            "english_proficiency_test": "IELTS",
            "ielts_overall": 7.0,
            "has_english_test": True,
        },
        preferences={
            "target_degree_level": "Bachelor's",
            "target_fields": ["Computer Science", "Artificial Intelligence"],
            "budget_max_pkr": 500000,
        },
    )

    events = []
    def on_event(evt: ScholarXEvent):
        events.append(evt)

    # Mock the scout live run methods to return discovered scholarships without network latency
    mock_scout_return = (
        [
            Scholarship(
                scholarship_id="SCH-EU-DISC-01",
                name="Stipendium Hungaricum (Live Discovered)",
                host_country="HU",
                host_country_name="Hungary",
                region="Europe",
                source_url="https://stipendiumhungaricum.hu",
                status=ScholarshipStatus.DISCOVERED,
            )
        ],
        [
            ScholarXEvent(
                session_id="sess-e2e-disc",
                event_type=AgentEventType.SCOUT_COMPLETE,
                agent_id="europe_scout",
            )
        ],
    )

    for scout in commander.scouts.values():
        scout.run = AsyncMock(return_value=mock_scout_return)

    # Run discovery mission
    candidates = await commander.execute_discovery_mission(student=student, event_callback=on_event)

    assert len(candidates) >= 10
    assert any(sc.host_country == "HU" for sc in candidates)  # Stipendium Hungaricum
    assert any(sc.host_country == "TR" for sc in candidates)  # Turkiye Burslari
    assert len(events) >= 2
    assert any(e.event_type == AgentEventType.DISCOVERY_AGGREGATION_COMPLETE for e in events)
