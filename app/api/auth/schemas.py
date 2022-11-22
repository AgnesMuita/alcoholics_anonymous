from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class LoginSchema(BaseModel):
    id: Optional[UUID] = None
    username: str
    profile_picture: str

    class Config:
        orm_mode = True



