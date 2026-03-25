import pytest
from unittest.mock import patch

@pytest.mark.asyncio
@patch("app.services.ai_agent_studio.ProposalBuilderAgent.run")
async def test_generate_proposal(mock_run, client):
    mock_run.return_value = {"url": "https://storage.../proposal.pdf", "content": "# Proposal"}
    response = await client.post("/ai/generate-proposal", 
                                 json={"deal_id": "123e4567-e89b-12d3-a456-426614174000", "style": "Modern"},
                                 headers={"X-Tenant-ID": "demo-tenant-uuid"})
    assert response.status_code == 200
    assert "url" in response.json()