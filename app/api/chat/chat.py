
from collections import defaultdict


from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, WebSocket, Request, Depends, BackgroundTasks,  APIRouter
from fastapi.templating import Jinja2Templates

from starlette.websockets import WebSocketDisconnect
from starlette.middleware.cors import CORSMiddleware


from . import messages, rooms, sync, threads, members
from core.settings import settings


app = FastAPI()
router = APIRouter()  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(
    messages.router, prefix=settings.API_V1_STR, tags=["messages"]
)  # include urls from message.py
app.include_router(
    rooms.router, prefix=settings.API_V1_STR, tags=["rooms"]
)  # include urls from rooms.py
app.include_router(
    threads.router, prefix=settings.API_V1_STR, tags=["threads"]
)  # include urls from threads.py
app.include_router(
    members.router, prefix=settings.API_V1_STR, tags=["members"]
)  # include urls from members.py
app.include_router(
    sync.router, prefix=settings.API_V1_STR, tags=["sync"]
)  # include urls from sync.py


# app.mount(
#     "/",
#     StaticFiles(directory="../frontend/dist", html=True, check_dir=False),
#     name="static",
# )

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="../../templates")


    