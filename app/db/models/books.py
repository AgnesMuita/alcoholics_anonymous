from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from pydantic import BaseModel as PydanticBaseModel
from db.db import Base
from sqlalchemy.orm import relationship


from sqlalchemy import MetaData

metadata_obj = MetaData()



class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True
class Book(BaseModel):
    __tablename__ = 'books',
    metadata_obj,
    id : int
    title : str
    author : str
    pages:int
    published: str
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)

class Job(BaseModel):
    __tablename__ = 'jobs'

    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    company = Column(String,nullable=False)
    company_url = Column(String)
    location = Column(String,nullable = False)
    description = Column(String,nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(),default=True)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("books",back_populates="jobs")