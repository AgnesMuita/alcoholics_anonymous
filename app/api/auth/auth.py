from fastapi import APIRouter, Depends, HTTPException,status, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from hashing import Hash
from fastapi.middleware.cors import CORSMiddleware


from db.models.auth import UserInDB, User
from oauth import get_current_user
from jwttoken import create_access_token
from db.db import database



router = APIRouter()
app=FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(current_user:User = Depends(get_current_user)):
	return {"data":"Hello World"}

@router.post("/")
async def login(request:OAuth2PasswordRequestForm=Depends()):
  user_dict=database["users"].find_one({"username":request.username})
  if not user_dict:
    raise HTTPException(status_code=400,detail="Incorrect username")
  if not Hash.verify(user_dict["password"],request.password):
    raise HTTPException(status_code=400, detail="Incorrect password")
  access_token = create_access_token(data={"sub":user_dict["username"]})
  return {"access_token":access_token, "token_type":"bearer"}


@router.post("/register")
def create_user(request:User):
  #hash the inputted password
  hashed_pass=Hash.bcrypt(request.hashed_password)
  user_object=dict(request)
  user_object["hashed_password"] = hashed_pass
  user_id=database["users"].insert(user_object)
  return {"res":"created"}




# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True,
#     },
# }


# def fake_hash_password(password:str):
#   return "fakehashed" + password



