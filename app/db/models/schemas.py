from pydantic import BaseModel

from db.models.common import TimestampModel, UUIDModel
from typing import Union, Optional




class User(UUIDModel, BaseModel, table=True):
    __tablename__ = "users"

    email: Union[str, None] = None
    full_name: Union[str, None] = None
    hashed_password: str
    disabled: Union[bool, None] = None
    username: str
    # id: UUIDModel, primary_key=True

    def __repr__(self):
        return f"<User (id: {self.id})>"


class Token(BaseModel):
    access_token:str    
    token_type:str

class TokenData(BaseModel):
  
    username:Optional[str]=None