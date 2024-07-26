from typing import Optional
from utils import translates
from fastapi import FastAPI, UploadFile
import shutil

app = FastAPI()


@app.post("/")
def upload_file(file: UploadFile, ignore_list: Optional[str] = '', count_words: Optional[int] = None):
    path = f'media/{file.filename}'

    # save file
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
    translated_words = translates(path, ignore_list, count_words)
    return translated_words
