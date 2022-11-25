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



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Wamwitha2020@localhost:5432/postgres'

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Base.metadata.create_all(engine)

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)
# Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()


database = databases.Database(SQLALCHEMY_DATABASE_URL)

