from os.path import dirname, join
from typing import Tuple


UPLOAD_FILE_PATH = join(dirname(dirname(__file__)), "static", "files")
# print(UPLOAD_FILE_PATH)


def get_upload_path(filename: str) -> Tuple[str, str]:
    file_suf = filename.split(".")[-1].lower()
    real_path = ""
    short_path = "/static"
    if file_suf == "doc" or file_suf == "docx":
        real_path = join(UPLOAD_FILE_PATH, "docx")
        short_path += "/docx"
    elif file_suf == "pdf":
        real_path = join(UPLOAD_FILE_PATH, "pdf")
        short_path += "/pdf"
    elif file_suf == "jpg" or file_suf == "jpeg" or file_suf == "png":
        real_path = join(UPLOAD_FILE_PATH, "img")
        short_path += "/img"
    elif file_suf == "mp3":
        real_path = join(UPLOAD_FILE_PATH, "audio")
        short_path += "/audio"
    else:
        real_path = join(UPLOAD_FILE_PATH, "default")
        short_path += "/default"

    return (join(real_path, filename), join(short_path, filename))
        
    