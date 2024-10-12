from pydantic import BaseModel

class FileDto(BaseModel):
    filename: str
    subject: str
    grade: str
    tag: str
    
    filepath: str