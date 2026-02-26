# ============================================================
# main.py - Point d'entrée FastAPI
# ============================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import get_settings
from backend.db.base import Base
from backend.db.session import engine
from backend.api.v1.router import api_router

# Import models so they register with Base.metadata
import backend.models.user  # noqa
import backend.models.query  # noqa

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
