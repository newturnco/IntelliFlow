import pytest
from app.models import Lead

@pytest.mark.asyncio
async def test_create_lead(client):
    payload = {"name": "Test Lead", "email": "test@acme.com", "source": "web"}
    response = await client.post("/leads", json=payload, headers={"X-Tenant-ID": "demo-tenant-uuid"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Lead"
    assert "ai_score" in data

@pytest.mark.asyncio
async def test_list_leads(client):
    response = await client.get("/leads", headers={"X-Tenant-ID": "demo-tenant-uuid"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)