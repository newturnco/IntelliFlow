from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Deal, Tenant
from ..middleware.tenant import get_current_tenant
from ..schemas import DealCreate, DealResponse
from ..services.forecasting import calculate_pipeline_forecast

router = APIRouter(tags=["Deals"])

@router.post("/")
async def create_deal(deal: DealCreate, db: Session = Depends(get_db), tenant: Tenant = Depends(get_current_tenant)):
    new_deal = Deal(**deal.model_dump(), tenant_id=tenant.id)
    db.add(new_deal)
    db.commit()
    return new_deal

@router.get("/pipeline")
async def get_pipeline(db: Session = Depends(get_db), tenant: Tenant = Depends(get_current_tenant)):
    deals = db.query(Deal).filter(Deal.tenant_id == tenant.id).all()
    return {
        "deals": deals,
        "forecast": calculate_pipeline_forecast(deals),
        "total_revenue": sum(d.amount for d in deals if d.stage == "Closed Won")
    }