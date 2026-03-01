from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import get_settings
from backend.db.base import Base
from backend.db.session import engine
from backend.api.v1.router import api_router
import mlflow
import os

# Register models so SQLAlchemy picks them up
import backend.models.user  # noqa
import backend.models.query  # noqa


tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
os.environ["MLFLOW_TRACKING_URI"] = tracking_uri

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("medical_rag_experiment")
mlflow.langchain.autolog(log_traces=True)


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
