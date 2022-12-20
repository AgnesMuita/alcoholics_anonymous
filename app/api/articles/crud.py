
from sqlalchemy.orm import Session

from . import articlesmodels
from . import schemas



def get_user(db: Session, user_id: int):
    return db.query(articlesmodels.User).filter(articlesmodels.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(articlesmodels.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = articlesmodels.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(articlesmodels.Article).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(articlesmodels.User).filter(articlesmodels.User.email == email).first()


def create_user_article(db: Session, item: schemas.ArticleCreate, user_id: int):
    db_item = articlesmodels.Article(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
