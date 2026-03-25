import pytest

@pytest.mark.asyncio
async def test_pipeline_forecast(client):
    response = await client.get("/deals/pipeline", headers={"X-Tenant-ID": "demo-tenant-uuid"})
    assert response.status_code == 200
    data = response.json()
    assert "forecast" in data
    assert "total_revenue" in data