
from ..db import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Union
from db.models.common import TimestampModel, UUIDModel


class LoginUser(UUIDModel, table=True):
    __tablename__ = "loginusers"

    username: str

    def __repr__(self):
        return f"<User (id: {self.id})>"



