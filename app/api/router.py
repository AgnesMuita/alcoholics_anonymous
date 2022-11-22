from fastapi.routing import APIRouter

from api.example.views import router as example_router
from api.system.views import router as system_router
from api.profile.views import router as login_router
from api.auth.views import router as auth_router
from api.auth.auth import router as user_router

api_router = APIRouter()
api_router.include_router(example_router, prefix="/example", tags=["example"])
# api_router.include_router(login_router, prefix="/profileaccount", tags=["profileaccount"])
# api_router.include_router(auth_router, prefix="/login", tags=["login"])
api_router.include_router(user_router, prefix="/userlogin", tags=["userlogin"])
