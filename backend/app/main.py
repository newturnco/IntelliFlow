from fastapi import FastAPI
from .core.storage import get_storage_service
from .routers import leads, deals, ai_drafting, auth  # all modules
from .middleware.tenant import TenantMiddleware
from .database import init_db
from .models import Base

app = FastAPI(title="IntelliFlow CRM API", version="1.0")

app.add_middleware(TenantMiddleware)   # enforces tenant_id everywhere

# All your modules mounted here
app.include_router(auth.router, prefix="/auth")
app.include_router(leads.router, prefix="/leads")
app.include_router(deals.router, prefix="/deals")
app.include_router(ai_drafting.router, prefix="/ai")   # Proposal Builder, Ask AI, etc.

@app.get("/health")
async def health():
    return {"status": "healthy", "storage": "ready"}

@app.on_event("startup")
async def startup():
    init_db()