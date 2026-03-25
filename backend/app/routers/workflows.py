# blueprints.py
from fastapi import APIRouter, Depends
from ..services.temporal_worker import start_blueprint_workflow

router = APIRouter(tags=["Blueprints"])

@router.post("/execute/{blueprint_id}")
async def execute_blueprint(blueprint_id: str, tenant: Tenant = Depends(get_current_tenant)):
    workflow_id = await start_blueprint_workflow(blueprint_id, tenant.id)
    return {"workflow_id": workflow_id, "status": "started"}