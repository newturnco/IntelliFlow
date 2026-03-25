import pytest
from app.database import SessionLocal, engine
from app.models import Base
from app.main import app
from httpx import ASGITransport, AsyncClient

@pytest.fixture(scope="function")
async def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
async def client(test_db):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac