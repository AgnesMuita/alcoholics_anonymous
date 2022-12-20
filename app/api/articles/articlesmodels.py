from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    articles = relationship("Article", back_populates="owner")  

class Article(Base):
    __tablename__ = 'articles',
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    # author=Column(String, nullable=False)
    pages = Column(Integer,  nullable=False)
    published =Column(String,  nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))


    owner = relationship("User", back_populates="articles")
    def __repr__(self):
      return f"<Article title={self.title} pages={self.pages} published={self.published}>"