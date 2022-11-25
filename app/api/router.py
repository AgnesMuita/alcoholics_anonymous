from fastapi.routing import APIRouter

from api.auth.auth import router as login_router
from api.books.books import router as book_router

api_router = APIRouter()

# api_router.include_router(login_router, prefix="/profileaccount", tags=["profileaccount"])
# api_router.include_router(auth_router, prefix="/login", tags=["login"])
# api_router.include_router(login_router, prefix="/accounts", tags=["accounts"])
api_router.include_router(book_router, prefix="/books", tags=["books"])
