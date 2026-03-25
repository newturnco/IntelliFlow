from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, Text, Boolean, UUID
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    domain = Column(String, unique=True)
    subscription_tier = Column(String, default="pro")
    storage_provider = Column(String, default="azure")  # azure | s3 | wasabi | r2
    storage_config = Column(JSON, nullable=True)  # encrypted credentials
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="sales")  # admin, sales, support
    tenant = relationship("Tenant")

class Lead(Base):
    __tablename__ = "leads"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    source = Column(String)  # web | linkedin | trade_show
    ai_score = Column(Float, default=0.0)
    status = Column(String, default="new")
    owner_id = Column(UUID(as_uuid=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tenant = relationship("Tenant")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    industry = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"))
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Deal(Base):
    __tablename__ = "deals"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    amount = Column(Float)
    stage = Column(String, default="prospecting")  # pipeline stages
    close_date = Column(DateTime)
    probability = Column(Float, default=0.3)
    contact_id = Column(UUID(as_uuid=True), ForeignKey("contacts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Activity(Base):
    __tablename__ = "activities"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    entity_type = Column(String)  # lead | deal | contact
    entity_id = Column(UUID(as_uuid=True))
    type = Column(String)  # call | email | meeting
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Blueprint(Base):
    __tablename__ = "blueprints"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    stages = Column(JSON)  # React Flow JSON for visual builder
    is_active = Column(Boolean, default=True)

class Proposal(Base):
    __tablename__ = "proposals"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    deal_id = Column(UUID(as_uuid=True), ForeignKey("deals.id"))
    title = Column(String)
    content_markdown = Column(Text)
    file_path = Column(String)  # stored in Azure/Wasabi
    generated_at = Column(DateTime(timezone=True), server_default=func.now())