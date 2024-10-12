from os.path import join
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from config import get_upload_path
from dtos.apiresult import ApiResult
from models.databases import get_db
from models.filemodel import FileModel


fileRoute = APIRouter(prefix="/file")


@fileRoute.get("/allfile")
def get_all_file():
    return ApiResult(msg="allfile success")


@fileRoute.post("/upload_file", summary="文件上传")
async def upload_file_real(file: UploadFile):
    #打印文件名称
    print('file',file.filename)
    real_path, short_path = get_upload_path(file.filename)
    #将上传的文件保存到服务本地
    print(real_path, short_path)
    with open(real_path, 'wb') as f:
        #一次读取1024字节，循环读取写入
        for chunk in iter(lambda: file.file.read(1024), b''):
            f.write(chunk)

    return {"filename": file.filename, "filepath": short_path}


@fileRoute.get("/testdb")
def test_sqlitedb(db: Session = Depends(get_db)):
    file = FileModel(filename="abc.txt")
    db.add(file)
    db.commit()
    return "success"