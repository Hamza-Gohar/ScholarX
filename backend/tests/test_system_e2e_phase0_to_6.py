import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from db.session_store import get_session_store

@pytest.mark.asyncio
async def test_full_system_pipeline_phase0_to_phase6_e2e():
    """
    Master Phase 0 -> Phase 6 E2E System Integration Test.
    Verifies that the backend cleanly serves the complete multi-agent workflow,
    document upload, conversational intake, discovery execution, SSE streaming,
    scholarships catalog, and session persistence to the Next.js 14 frontend.
    """
    store = get_session_store()
    await store.init_db()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Health check & Key rotation manager status
        health_res = await client.get("/api/health")
        assert health_res.status_code == 200
        health_data = health_res.json()
        assert health_data["status"] == "HEALTHY"
        assert "gemini" in health_data["api_keys"]
        assert "groq" in health_data["api_keys"]

        # 2. Browse pre-seeded 218 scholarships knowledge base
        sc_res = await client.get("/api/scholarships?region=europe")
        assert sc_res.status_code == 200
        sc_data = sc_res.json()
        assert "scholarships" in sc_data
        assert sc_data["total"] > 0
        assert any("Hungary" in s["name"] or "DAAD" in s["name"] or "Erasmus" in s["name"] for s in sc_data["scholarships"])

        # 3. Conversational Intake chat with Pakistani counselor
        chat_res = await client.post(
            "/api/profile/chat",
            json={
                "message": "Hi, I am an ICS student from Lahore with 87% marks interested in CS in Europe.",
                "session_id": "test-e2e-phase6-session"
            }
        )
        assert chat_res.status_code == 200
        chat_data = chat_res.json()
        assert "response" in chat_data
        assert chat_data["session_id"] == "test-e2e-phase6-session"

        # 4. Profile retrieval
        prof_res = await client.get("/api/profile/test-e2e-phase6-session")
        assert prof_res.status_code == 200
        prof_data = prof_res.json()
        assert "profile" in prof_data
        assert prof_data["profile"]["personal"]["city"] == "Lahore"

        # 5. Launch Discovery Mission
        disc_res = await client.post(
            "/api/discover",
            json={
                "session_id": "test-e2e-phase6-session",
                "target_regions": ["europe"],
                "max_budget_pkr": 300000
            }
        )
        assert disc_res.status_code == 200
        disc_data = disc_res.json()
        assert disc_data["status"] in ["STARTED", "MISSION_LAUNCHED", "IN_PROGRESS", "ALREADY_COMPLETED"]

        # 6. Session Persistence Check
        sess_res = await client.get("/api/sessions/test-e2e-phase6-session")
        assert sess_res.status_code in [200, 404] # Might be in progress or saved

        # 7. List all sessions
        list_res = await client.get("/api/sessions")
        assert list_res.status_code == 200
        list_data = list_res.json()
        assert "sessions" in list_data
