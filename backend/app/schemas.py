from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

class LeadCreate(BaseModel):
    name: str
    email: Optional[str]
    phone: Optional[str]
    source: str

class LeadResponse(BaseModel):
    id: UUID
    name: str
    ai_score: float
    status: str

class DealCreate(BaseModel):
    name: str
    amount: Optional[float]
    stage: str = "prospecting"
    contact_id: Optional[UUID]

class GenerateProposalRequest(BaseModel):
    deal_id: UUID
    style: str = "Professional"
    instructions: str = ""