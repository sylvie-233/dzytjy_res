from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dtos.apiresult import ApiResult
from models.databases import get_db
from models.filemodel import FileModel


fileRoute = APIRouter(prefix="/file")


@fileRoute.get("/allfile")
def get_all_file():
    return ApiResult(msg="allfile success")


@fileRoute.get("/testdb")
def test_sqlitedb(db: Session = Depends(get_db)):
    file = FileModel(filename="abc.txt")
    db.add(file)
    db.commit()
    return "success"