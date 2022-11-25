
from sqlalchemy import Integer, String, Boolean, Column
from pydantic import BaseModel as PydanticBaseModel

from db.models.common import TimestampModel, UUIDModel
from db.db import Base


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    full_name =Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<User (id: {self.id})>"

class Token(BaseModel):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    access_token = Column(String, nullable=False)
    token_type = Column(String, nullable=False)

class TokenData(BaseModel):
    __tablename__ = "token data"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)





