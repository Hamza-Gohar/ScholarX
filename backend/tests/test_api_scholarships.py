import pytest
from httpx import ASGITransport, AsyncClient
from db.seed import load_and_seed_scholarships
from db.session_store import get_session_store
from main import app


@pytest.mark.asyncio
async def test_api_scholarships_list_and_filter():
    store = get_session_store()
    await store.init_db()
    await load_and_seed_scholarships()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. List all scholarships
        res = await client.get("/api/scholarships")
        assert res.status_code == 200
        data = res.json()
        assert "scholarships" in data
        assert len(data["scholarships"]) >= 50
        assert "total" in data

        # 2. Filter by region
        res_eu = await client.get("/api/scholarships?region=Europe")
        assert res_eu.status_code == 200
        eu_data = res_eu.json()
        assert all(s["region"] == "Europe" for s in eu_data["scholarships"])

        # 3. Get single scholarship
        first_id = data["scholarships"][0]["scholarship_id"]
        res_single = await client.get(f"/api/scholarships/{first_id}")
        assert res_single.status_code == 200
        assert res_single.json()["scholarship"]["scholarship_id"] == first_id

        # 4. Test Master Catalog PDF Download
        res_master = await client.get("/api/scholarships/download/master-pdf")
        assert res_master.status_code == 200
        assert "application/pdf" in res_master.headers["content-type"]
        assert len(res_master.content) > 500000

        # 5. Test Single Scholarship Dossier PDF Download
        res_single_pdf = await client.get(f"/api/scholarships/{first_id}/pdf?download=true")
        assert res_single_pdf.status_code == 200
        assert "application/pdf" in res_single_pdf.headers["content-type"]
        assert len(res_single_pdf.content) > 10000
