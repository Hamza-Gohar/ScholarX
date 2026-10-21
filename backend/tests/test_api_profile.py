import pytest
from httpx import ASGITransport, AsyncClient
from db.session_store import get_session_store
from main import app
from schemas.student import EducationLevel, PersonalInfo, StudentProfile


@pytest.mark.asyncio
async def test_api_profile_upload_and_get():
    store = get_session_store()
    await store.init_db()
    session_id = "sess-api-prof-01"

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Upload mock document
        file_content = b"""
        Name: Ayesha Khan
        City: Islamabad, Pakistan
        Degree: Bachelor of Science in Software Engineering (16 Years)
        GPA: 3.8 / 4.0 (88% marks)
        IELTS: 7.5
        Target Degree: Master's
        """
        files = {"file": ("cv.txt", file_content, "text/plain")}
        data = {"session_id": session_id}

        upload_res = await client.post("/api/profile/upload", data=data, files=files)
        assert upload_res.status_code == 200
        res_json = upload_res.json()
        assert res_json["session_id"] == session_id
        assert "profile" in res_json
        assert res_json["profile"]["academic"]["gpa_percentage"] > 0

        # 2. Get profile
        get_res = await client.get(f"/api/profile/{session_id}")
        assert get_res.status_code == 200
        profile_data = get_res.json()["profile"]
        assert profile_data["session_id"] == session_id


@pytest.mark.asyncio
async def test_api_profile_chat():
    store = get_session_store()
    await store.init_db()
    session_id = "sess-api-prof-chat"

    # Pre-seed student
    student = StudentProfile(
        student_id="std-chat-01",
        session_id=session_id,
        personal=PersonalInfo(name="Bilal", city="Lahore"),
    )
    await store.save_student_profile(student)

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "session_id": session_id,
            "message": "I want to apply for fully funded Master's in Germany in AI.",
        }
        res = await client.post("/api/profile/chat", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert "reply" in data
        assert len(data["reply"]) > 0
        assert "profile" in data
