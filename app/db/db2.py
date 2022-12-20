from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import databases


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Wamwitha2020@localhost/postgres'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)
# Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()


database = databases.Database(SQLALCHEMY_DATABASE_URL)

