
from ..db import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Union, Optional
from db.models.common import TimestampModel, UUIDModel


class LoginUser(UUIDModel, table=True):
    __tablename__ = "loginusers"

    username: str
    hashed_password:str

    def __repr__(self):
        return f"<User (id: {self.id})>"

class User(UUIDModel, BaseModel, table=True):
    __tablename__ = "users"

    email: Union[str, None] = None
    full_name: Union[str, None] = None
    hashed_password: str
    disabled: Union[bool, None] = None
    username: str
    id:UUIDModel

    def __repr__(self):
        return f"<User (id: {self.id})>"

class UserInDB(User, table=True):
    hashed_passwords: str

class Token(BaseModel):
    access_token:str    
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None


