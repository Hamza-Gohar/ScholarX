from unittest.mock import patch
import pytest
from httpx import ASGITransport, AsyncClient
from db.session_store import get_session_store
from main import app
from schemas.student import AcademicRecord, EducationLevel, PersonalInfo, Preferences, StudentProfile
from utils.security import create_signed_session_token


@pytest.mark.asyncio
async def test_api_discover_launches_mission():
    store = get_session_store()
    await store.init_db()
    session_id = "sess-api-disc-01"

    # Pre-seed student profile
    student = StudentProfile(
        student_id="std-disc-01",
        session_id=session_id,
        personal=PersonalInfo(name="Khadija", city="Karachi", age=22),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            gpa_percentage=86.0,
            gpa_4_scale=3.75,
        ),
        preferences=Preferences(target_degree_level="Master's", max_out_of_pocket_pkr=250000),
    )
    await store.save_student_profile(student)

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Mock background pipeline for unit test speed
        async def mock_background(sess, prof):
            from api.routes.discover import _ACTIVE_MISSIONS
            _ACTIVE_MISSIONS[sess] = {"status": "COMPLETE", "phase": "MISSION_COMPLETE"}

        with patch("api.routes.discover._run_discovery_pipeline_background", side_effect=mock_background):
            # Trigger discovery
            res = await client.post("/api/discover", json={"session_id": session_id})
            assert res.status_code == 200
            data = res.json()
            assert data["session_id"] == session_id
            assert data["status"] in ("STARTED", "RUNNING", "COMPLETE")

            # Check status endpoint
            status_res = await client.get(
                f"/api/discover/{session_id}/status",
                headers={"X-Session-Token": create_signed_session_token(session_id)},
            )
            assert status_res.status_code == 200
            status_data = status_res.json()
            assert "active_phase" in status_data
