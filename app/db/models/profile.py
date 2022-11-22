
from ..db import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Union
from db.models.common import TimestampModel, UUIDModel




class User(UUIDModel, BaseModel, table=True):
    __tablename__ = "users"

    email: Union[str, None] = None
    full_name: Union[str, None] = None
    hashed_password: str
    disabled: Union[bool, None] = None
    username: str

    def __repr__(self):
        return f"<User (id: {self.id})>"

class UserInDB(User, table=True):
    hashed_passwords: str
