from fastapi import APIRouter

from app.api.api_v1.endpoints import algum, login, user, watson_message, action

api_router = APIRouter()
api_router.include_router(algum.router, prefix="/algum", tags=["algum"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(watson_message.router, prefix="/watson", tags=["watson"])
api_router.include_router(action.router, prefix="/action", tags=["action"])
