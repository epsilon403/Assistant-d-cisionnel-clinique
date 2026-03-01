# ============================================================
# config.py - Configuration centralisée (pydantic-settings)
# ============================================================
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "CliniQ - Assistant Décisionnel Clinique"
    DATABASE_URL: str = "postgresql://user:password@db:5432/cliniq"
    SECRET_KEY: str = "change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    VECTOR_STORE_PATH: str = "./data/vectorstore"
    GOOGLE_API_KEY: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
