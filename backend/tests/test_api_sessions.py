import pytest
from httpx import ASGITransport, AsyncClient
from db.session_store import get_session_store
from main import app
from schemas.student import PersonalInfo, StudentProfile
from utils.security import create_signed_session_token


@pytest.mark.asyncio
async def test_api_sessions_crud():
    store = get_session_store()
    await store.init_db()

    session_id = "sess-api-crud-01"
    student = StudentProfile(
        student_id="std-crud-01",
        session_id=session_id,
        personal=PersonalInfo(name="Farhan", city="Multan"),
    )
    await store.save_student_profile(student)
    await store.create_session(session_id, "std-crud-01", {"target_degree": "Master's"})

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        headers = {"X-Session-Token": create_signed_session_token(session_id)}
        # 1. List sessions
        list_res = await client.get("/api/sessions", headers=headers)
        assert list_res.status_code == 200
        sessions = list_res.json()["sessions"]
        assert any(s["session_id"] == session_id for s in sessions)

        # 2. Get session detail
        detail_res = await client.get(f"/api/sessions/{session_id}", headers=headers)
        assert detail_res.status_code == 200
        detail = detail_res.json()
        assert detail["session"]["session_id"] == session_id

        # 3. Delete session
        del_res = await client.delete(f"/api/sessions/{session_id}", headers=headers)
        assert del_res.status_code == 200
        assert del_res.json()["status"] == "DELETED"
