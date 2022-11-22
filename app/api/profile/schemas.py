from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    id: Optional[UUID] = None
    username: str
    profile_picture: str
    disabled: bool

    class Config:
        orm_mode = True

class UserInDBSchema(UserCreateSchema):
    hashed_password:str


class UserSchema(UserCreateSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


