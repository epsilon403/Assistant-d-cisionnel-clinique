# ============================================================
# session.py - Configuration de la session SQLAlchemy
# ============================================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency: yield a DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
