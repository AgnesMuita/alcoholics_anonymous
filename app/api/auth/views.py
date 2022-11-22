from api.auth.schemas import LoginSchema
from api.auth.services import AuthService
from db.db import db_session
from db.models.auth import LoginUser
from db.models.profile import UserInDB
from fastapi import APIRouter, Depends, Response, Header, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from typing import Optional
from fastapi_login import LoginManager #Loginmanager Class
from fastapi_login.exceptions import InvalidCredentialsException #Exception class
from fastapi.responses import RedirectResponse,HTMLResponse



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
  














DB = {"username":{"password":"qwertyuiop"}} # unhashed


SECRET = "secret-key"

# To obtain a suitable secret key you can run | import os; print(os.urandom(24).hex())
manager = LoginManager(SECRET,token_url="/",use_cookie=True)
manager.cookie_name = "some"

@manager.user_loader    
def load_user(username:str):
    user = DB.get(username)
    return user

@router.post("/")
async def login_user(data:OAuth2PasswordRequestForm=Depends()):
  username = data.username
  user = load_user(username)
  if not user:
    raise InvalidCredentialsException   
  access_token=manager.create_access_token(
    data ={"sub":username}
   )
  resp=RedirectResponse(url="/private", status_code=status.HTTP_302_FOUND)
  manager.set_cookie(resp,access_token)
  return resp

@router.get("/private")
def getPrivateendpoint(_=Depends(manager)):
    return "You are an authenticated user"





