from fastapi import APIRouter

from app.api.api_v1.endpoints import algum, login, user

api_router = APIRouter()
api_router.include_router(algum.router, prefix="/algum", tags=["algum"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(login.router, prefix="/login", tags=["login"])