
from fastapi import FastAPI, APIRouter
from db.models.books import Book


router = APIRouter()
@router.post("/")
def postInformation(info : Book):
    req_info = info.json()
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }
@router.get("/")
def getInformation():
    return {"key":"heey"}