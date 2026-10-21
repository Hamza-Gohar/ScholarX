import os
import tempfile
import pytest
from db.session_store import SessionStore
from schemas.scholarship import Scholarship, ScholarshipStatus
from schemas.student import StudentProfile


@pytest.mark.asyncio
async def test_session_store_crud():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        store = SessionStore(db_path=tmp_path)
        await store.init_db()

        # Save student
        profile = StudentProfile(student_id="std-temp-1", session_id="sess-temp-1")
        await store.save_student_profile(profile)

        # Create session
        session_id = await store.create_session("sess-temp-1", "std-temp-1", {"pref": "Europe"})
        assert session_id == "sess-temp-1"

        # List sessions
        sessions = await store.list_sessions()
        assert len(sessions) == 1
        assert sessions[0].session_id == "sess-temp-1"

        # Save scholarship in cache
        sc = Scholarship(
            scholarship_id="TEST-TEMP-01",
            name="Test Scholarship",
            host_country="DE",
            host_country_name="Germany",
            region="Europe",
            source_url="https://daad.de",
            status=ScholarshipStatus.VERIFIED,
        )
        await store.upsert_scholarship_cache(sc)

        cached_list = await store.get_all_cached_scholarships()
        assert len(cached_list) == 1
        assert cached_list[0].scholarship_id == "TEST-TEMP-01"

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
