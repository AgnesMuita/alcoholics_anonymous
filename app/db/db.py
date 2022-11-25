from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY, Boolean)
from core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import databases

from sqlmodel.ext.asyncio.session import AsyncSession



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Wamwitha2020@localhost:5432/postgres"

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# metadata = sqlalchemy.MetaData()
# metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()




# async_engine = create_async_engine(settings.DB_URL, echo=settings.DB_ECHO, future=True)


# async def db_session() -> AsyncGenerator:
#     async_session = sessionmaker(
#         bind=async_engine,
#         class_=AsyncSession,
#         expire_on_commit=False,
#     )
#     async with async_session() as session:
#         yield session
# metadata = sqlalchemy.MetaData()

# AATable = sqlalchemy.Table(
#     'users',metadata,
#     sqlalchemy.Column("id", Integer, primary_key=True),
#     sqlalchemy.Column("username", String),
#     sqlalchemy.Column("hashed_password", String),
#     sqlalchemy.Column("disabled", Boolean)
# )

# # metadata.create_all(engine)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

