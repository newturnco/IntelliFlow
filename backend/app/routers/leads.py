from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Lead, Tenant
from ..middleware.tenant import get_current_tenant
from ..schemas import LeadCreate, LeadResponse
from ..services.ai import predict_lead_score

router = APIRouter(tags=["Leads"])

@router.post("/")
async def create_lead(lead: LeadCreate, db: Session = Depends(get_db), tenant: Tenant = Depends(get_current_tenant)):
    new_lead = Lead(**lead.model_dump(), tenant_id=tenant.id)
    db.add(new_lead)
    db.commit()
    # Auto-assign round-robin + AI scoring
    new_lead.ai_score = predict_lead_score(new_lead)
    db.commit()
    return new_lead

@router.get("/")
async def list_leads(db: Session = Depends(get_db), tenant: Tenant = Depends(get_current_tenant)):
    return db.query(Lead).filter(Lead.tenant_id == tenant.id).all()