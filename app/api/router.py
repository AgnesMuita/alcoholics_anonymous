from fastapi.routing import APIRouter
from fastapi import FastAPI

# from api.auth.auth import router as login_router
from api.articles.articles import router as article_router
from api.chat import messages, rooms, sync, threads, members
# from api.chat.messages import router as message_router
from core.settings import settings

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



api_router = APIRouter()
app=FastAPI()

api_router.include_router(article_router, prefix="/articles", tags=["Articles"])
# api_router.include_router(chat_router, prefix="/chat", tags=["chat"])

api_router.include_router(messages.router, prefix=settings.API_V1_STR, tags=["messages"])  # include urls from message.py
api_router.include_router(rooms.router, prefix=settings.API_V1_STR, tags=["rooms"])  # include urls from rooms.py
api_router.include_router(threads.router, prefix=settings.API_V1_STR, tags=["threads"])  # include urls from threads.py
api_router.include_router(members.router, prefix=settings.API_V1_STR, tags=["members"])  # include urls from members.py
api_router.include_router(sync.router, prefix=settings.API_V1_STR, tags=["sync"])  # include urls from sync.py


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="../../templates")