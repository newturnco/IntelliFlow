import asyncio
from app.database import SessionLocal
from app.models import Tenant, User, Lead, Deal
from passlib.hash import bcrypt

async def seed():
    db = SessionLocal()
    # Default super tenant
    tenant = Tenant(name="Demo Company", domain="demo.intelliflowcrm.com")
    db.add(tenant)
    db.commit()

    # Super admin
    admin = User(
        tenant_id=tenant.id,
        email="admin@intelliflowcrm.com",
        hashed_password=bcrypt.hash("Admin123!"),
        role="super_admin"
    )
    db.add(admin)

    # Sample data
    lead1 = Lead(tenant_id=tenant.id, name="Acme Corp", email="ceo@acme.com", source="linkedin", ai_score=85.0)
    deal1 = Deal(tenant_id=tenant.id, name="Enterprise Deal", amount=45000, stage="negotiation", probability=70.0)
    db.add_all([lead1, deal1])
    db.commit()
    print("✅ Seed data applied - Admin: admin@intelliflowcrm.com / Admin123!")

if __name__ == "__main__":
    asyncio.run(seed())