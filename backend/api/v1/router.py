from fastapi import APIRouter
from backend.api.v1.endpoints import query
from backend.api.v1.endpoints import auth

api_router = APIRouter()
api_router.include_router(query.router, prefix="/query", tags=["query"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])