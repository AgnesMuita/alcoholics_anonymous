from api.router import api_router
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core.settings import settings
from api.chat import messages, rooms, sync, threads, members
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates



def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="Alcoholics Anonymous",
        description="AA by Aggie",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=JSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    # app = FastAPI(
    #     title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    # )


    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )


    # app.include_router(
    #     messages.router, prefix=settings.API_V1_STR, tags=["messages"]
    # )  # include urls from message.py
    # app.include_router(
    #     rooms.router, prefix=settings.API_V1_STR, tags=["rooms"]
    # )  # include urls from rooms.py
    # app.include_router(
    #     threads.router, prefix=settings.API_V1_STR, tags=["threads"]
    # )  # include urls from threads.py
    # app.include_router(
    #     members.router, prefix=settings.API_V1_STR, tags=["members"]
    # )  # include urls from members.py
    # app.include_router(
    #     sync.router, prefix=settings.API_V1_STR, tags=["sync"]
    # )  # include urls from sync.py


    # app.mount("/static", StaticFiles(directory="static"), name="static")

    # templates = Jinja2Templates(directory="../../templates")




    return app
