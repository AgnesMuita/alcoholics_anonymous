from pathlib import Path
from sys import modules
import secrets

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    """Application settings."""

    ENV: str = "dev"
    HOST: str = "localhost"
    PORT: int = 3000
    BASE_URL_: str = f"https://{HOST}:{PORT}"
    # quantity of workers for uvicorn
    WORKERS_COUNT: int = 1
    # Enable uvicorn reloading
    RELOAD: bool = False
    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "Wamwitha2020"
    DB_BASE: str = "postgres"
    DB_ECHO: bool = False

    SECRET_KEY: str = secrets.token_urlsafe(32)
    MESSAGE_COLLECTION = "messages"
    ROOM_COLLECTION = "rooms"
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "AA Chat"



    @property
    def BASE_URL(self) -> str:
        return self.BASE_URL_ if self.BASE_URL_.endswith("/") else f"{self.BASE_URL_}/"

    @property
    def DB_URL(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASE}"

    class Config:
        env_file = f"{BASE_DIR}/.env"
        env_file_encoding = "utf-8"
        fields = {
            "BASE_URL_": {
                "env": "BASE_URL",
            },
        }


class TestSettings(Settings):
    @property
    def DB_BASE(self):
        return f"{self.DB_BASE}_test"


if "pytest" in modules:
    settings = TestSettings()
else:
    settings = Settings()
