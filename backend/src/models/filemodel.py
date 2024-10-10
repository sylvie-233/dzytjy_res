from sqlalchemy import Column, Integer, String

from .databases import DbModel

class FileModel(DbModel):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String)
    