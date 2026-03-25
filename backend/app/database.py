from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://intelliflow:SuperSecretPassword123!@postgres:5432/intelliflow")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
    # Enable Row Level Security for multitenancy
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE leads ENABLE ROW LEVEL SECURITY;"))
        # ... repeat for all tables (auto-applied in production migration)