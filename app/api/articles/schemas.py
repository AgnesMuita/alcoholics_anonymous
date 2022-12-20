from pydantic import BaseModel as PydanticBaseModel
from typing import List


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class ArticleBase(BaseModel):
    # __tablename__ = 'books',
    id : int
    title : str
    author : str
    pages:int
    published: str
    
    def __repr__(self):
        return "<Article(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Article] = []

    class Config:
        orm_mode = True