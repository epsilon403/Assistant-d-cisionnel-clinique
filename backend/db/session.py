from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Yield a database session for each request, then close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
