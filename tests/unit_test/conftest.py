# ============================================================
# conftest.py - Configuration partagée pour les tests unitaires
# ============================================================
# SQLite en mémoire + mocks MLflow → aucun Docker requis
# ============================================================
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.db.base import Base
from backend.db.session import get_db


# ─── In-memory SQLite database for tests ────────────────────────────────────────
SQLALCHEMY_TEST_DATABASE_URL = "sqlite://"

test_engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# ─── Patch heavy dependencies before importing the app ──────────────────────────
with patch("mlflow.set_tracking_uri"), \
     patch("mlflow.set_experiment"), \
     patch("mlflow.langchain.autolog"):
    from backend.main import app

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=test_engine)


@pytest.fixture()
def client():
    """Provide a TestClient with fresh tables for each test."""
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    yield TestClient(app)
