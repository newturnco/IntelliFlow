from fastapi import APIRouter, Depends, HTTPException
from ..models import Deal, Tenant
from ..middleware.tenant import get_current_tenant
from ..services.ai_agent_studio import ProposalBuilderAgent
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

router = APIRouter(tags=["AI Drafting"])

class GenerateProposalRequest(BaseModel):
    deal_id: int
    style: str = "Professional"   # Professional, Modern, Casual
    instructions: str = ""

@router.post("/generate-proposal")
async def generate_proposal(req: GenerateProposalRequest, tenant: Tenant = Depends(get_current_tenant)):
    deal = ... # fetch from DB (omitted for brevity)
    agent = ProposalBuilderAgent(llm=ChatOpenAI(model="gpt-4o"), tenant=tenant)
    document = await agent.run(
        deal=deal,
        style=req.style,
        custom_instructions=req.instructions
    )
    # Save to Azure/Wasabi via storage service
    return {"url": document.url, "content": document.markdown}