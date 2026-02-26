# ============================================================
# query.py - Schémas Pydantic pour les requêtes RAG
# ============================================================
from pydantic import BaseModel
from datetime import datetime


class QueryCreate(BaseModel):
    query: str


class QueryResponse(BaseModel):
    id: int
    query: str
    reponse: str
    created_at: datetime

    model_config = {"from_attributes": True}