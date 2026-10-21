import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from main import app
from workflows.scouts.base_scout import BaseScout
from agents.discovery_commander import DiscoveryCommander
from schemas.events import AgentEventType
from schemas.student import StudentProfile


client = TestClient(app)


def test_exhibition_preflight_endpoint():
    """Verify exhibition pre-flight check endpoint reports readiness and health."""
    response = client.get("/api/exhibition/preflight")
    assert response.status_code == 200
    data = response.json()

    assert data["ready"] is True
    assert "degraded" in data
    assert "database" in data
    assert "profiles" in data
    assert "offline_artifacts" in data
    assert "api_keys" in data
    assert "event_bus" in data

    # Verify 3 Pakistani demonstration profiles
    assert data["profiles"]["profile_a_ics"] is True
    assert data["profiles"]["profile_b_fsc"] is True
    assert data["profiles"]["profile_c_bs"] is True

    # Verify database seeded
    assert data["database"]["status"] == "PASS"
    assert data["database"]["cached_scholarships_count"] >= 4

    # Verify offline artifacts
    assert data["offline_artifacts"]["status"] == "PASS"


@pytest.mark.asyncio
async def test_base_scout_search_failover():
    """Verify BaseScout falls back to local verified cache when primary search returns empty."""
    scout = BaseScout(region="Europe")
    emitted_events = []

    def callback(evt):
        emitted_events.append(evt)

    profile = StudentProfile(
        student_id="std-test-resilience",
        session_id="sess-resilience-01",
        personal={"name": "Hamza Tariq", "nationality": "PK", "city": "Lahore"},
        academic={"current_level": "Intermediate / ICS / FSc / FA", "field_of_study": "Computer Science", "gpa_percentage": 87.0},
        language={"english_proficiency_test": "IELTS", "ielts_overall": 7.0, "has_english_test": True},
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    )

    # Mock search_tool.search returning empty list to trigger failover
    scout.search_tool.search = AsyncMock(return_value=[])

    discovered, events = await scout.run_scout_pipeline(
        student=profile,
        queries=["HEC Stipendium Hungaricum quota 2025/2026"],
        event_callback=callback,
    )

    # Verify failover events were emitted
    event_types = [e.event_type for e in emitted_events]
    assert AgentEventType.PRIMARY_SEARCH_UNAVAILABLE in event_types
    assert AgentEventType.FALLBACK_SEARCH_ACTIVE in event_types
    assert AgentEventType.RESEARCH_RESUMED in event_types

    # Discovered candidates should be populated from verified cache
    assert len(discovered) > 0


@pytest.mark.asyncio
async def test_discovery_commander_scout_fault_isolation():
    """Verify DiscoveryCommander isolates a single scout crash and emits PARTIAL_DISCOVERY."""
    commander = DiscoveryCommander()
    emitted_events = []

    def callback(evt):
        emitted_events.append(evt)

    profile = StudentProfile(
        student_id="std-test-resilience",
        session_id="sess-resilience-02",
        personal={"name": "Hamza Tariq", "nationality": "PK", "city": "Lahore"},
        academic={"current_level": "Intermediate / ICS / FSc / FA", "field_of_study": "Computer Science", "gpa_percentage": 87.0},
        language={"english_proficiency_test": "IELTS", "ielts_overall": 7.0, "has_english_test": True},
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    )

    # Cause Oceania regional scout to fail with a runtime exception
    commander.scouts["Oceania"].run = AsyncMock(side_effect=RuntimeError("Oceania satellite uplink lost"))

    # Execute discovery mission
    candidates = await commander.execute_discovery_mission(profile, event_callback=callback)

    # Verify mission does not crash and collects from other scouts
    assert len(candidates) > 0

    event_types = [e.event_type for e in emitted_events]
    assert AgentEventType.SCOUT_FAILED in event_types
    assert AgentEventType.PARTIAL_DISCOVERY in event_types

