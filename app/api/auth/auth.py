from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from db.models.profile import UserInDB, User
from typing import List




router = APIRouter()


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password:str):
  return "fakehashed" + password

@router.post("/token")
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
  user_dict=fake_users_db.get(form_data.username)
  if not user_dict:
    raise HTTPException(status_code=400,detail="Incorrect username or password")
  user = UserInDB(**user_dict)
  hashed_password=fake_hash_password(form_data.password)
  if not hashed_password == user.hashed_password:
    raise HTTPException(status_code=400, detail="Incorrect username or password")
  return {"access_token":user.username, "token_type":"bearer"}

@router.get('/', response_model=List[User])
async def index():
  return fake_users_db