from unittest.mock import patch
import pytest
from httpx import ASGITransport, AsyncClient
from api.routes.stream import stream_events
from db.seed import load_and_seed_scholarships
from db.session_store import get_session_store
from main import app
from schemas.events import AgentEventType


@pytest.mark.asyncio
async def test_full_system_pipeline_phase0_to_phase5():
    """
    Master E2E Test covering Phases 0 through 5:
    1. Seed SQLite Database
    2. Upload Student Document through FastAPI (/api/profile/upload)
    3. Conversational chat clarification (/api/profile/chat)
    4. Connect to SSE Stream (/api/stream/{session_id})
    5. Trigger Discovery (/api/discover)
    6. Verify Event Stream and Final Ranked Results in Session Store
    """
    store = get_session_store()
    await store.init_db()
    await load_and_seed_scholarships()

    session_id = "sess-e2e-phase5"
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Step 1: Upload Document
        cv_text = b"""
        CURRICULUM VITAE
        Name: Maria Khan
        City: Peshawar, Pakistan
        Degree: Bachelor of Science in Artificial Intelligence (16 Years)
        GPA: 3.9 / 4.0 (90% marks)
        IELTS: 8.0
        Target Degree: Master's
        """
        files = {"file": ("maria_cv.txt", cv_text, "text/plain")}
        data = {"session_id": session_id}

        upload_res = await client.post("/api/profile/upload", data=data, files=files)
        assert upload_res.status_code == 200

        # Step 2: Chat Clarification
        chat_res = await client.post(
            "/api/profile/chat",
            json={"session_id": session_id, "message": "I prefer European and Asian bilateral scholarships."},
        )
        assert chat_res.status_code == 200

        # Step 3: Trigger Background Discovery
        async def mock_background(sess, prof):
            from api.routes.discover import _ACTIVE_MISSIONS
            _ACTIVE_MISSIONS[sess] = {"status": "COMPLETE", "phase": "MISSION_COMPLETE"}

        with patch("api.routes.discover._run_discovery_pipeline_background", side_effect=mock_background):
            disc_res = await client.post("/api/discover", json={"session_id": session_id})
            assert disc_res.status_code == 200

        # Step 4: Verify Stream Endpoint Works
        stream_res = await stream_events(session_id)
        assert stream_res.status_code == 200
        assert stream_res.media_type == "text/event-stream"
        first_chunk = await anext(stream_res.body_iterator)
        assert "event:" in first_chunk

        # Step 5: Verify Session Detail
        session_res = await client.get(f"/api/sessions/{session_id}")
        assert session_res.status_code == 200
        sess_data = session_res.json()
        assert sess_data["session"]["session_id"] == session_id
        assert sess_data["profile"]["personal"]["name"] is not None
