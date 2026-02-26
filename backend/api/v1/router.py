# ============================================================
# router.py - Routeur principal API v1
# ============================================================
from fastapi import APIRouter
from backend.api.v1.endpoints import query

api_router = APIRouter()
api_router.include_router(query.router, prefix="/query", tags=["query"])
