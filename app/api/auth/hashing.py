from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
  #change simple password to a hashed value 
  def bcrypt(password:str):
    return pwd_cxt.hash(password)
  #verify password checks whether the inputted password matches the one in the DB
  def verify(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)