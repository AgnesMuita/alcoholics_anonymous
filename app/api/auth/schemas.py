from pydantic import BaseModel as PydanticBaseModel

from db.models.common import TimestampModel, UUIDModel
from typing import Union, Optional


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class UserSchema(UUIDModel, BaseModel, table=True):

    id: UUIDModel
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    hashed_password: str
    disabled: Union[bool, None] = None
    username: str

    def __repr__(self):
        return f"<UserSchema (id: {self.id})>"


class TokenSchema(BaseModel):
    access_token:str    
    token_type:str

class TokenDataSchema(BaseModel):
    username:Optional[str]=None

