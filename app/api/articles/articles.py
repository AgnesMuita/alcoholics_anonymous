
from sqlalchemy.orm import Session
import sqlalchemy
from typing import List
from fastapi import Depends, HTTPException, APIRouter

from . import crud, schemas
from .db import SessionLocal, engine

# booksmodel.Base.metadata.create_all(bind=engine)
metadata = sqlalchemy.MetaData()
metadata.create_all(engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/articles/", response_model=schemas.Article)
def create_item_for_user(
    user_id: int, item: schemas.ArticleCreate, db: Session = Depends(get_db)
):
    return crud.create_user_article(db=db, item=item, user_id=user_id)


@router.get("/articles/", response_model=List[schemas.Article])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_articles(db, skip=skip, limit=limit)
    return items




