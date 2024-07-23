from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from translate import Translator
import shutil

app = FastAPI()


@app.post("/file/")
def upload_file(file: UploadFile, count_words: int):
    path = f'media/{file.filename}'

    # save file
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return index(path, count_words)


def index(path, count):
    translator = Translator(from_lang='English', to_lang='Russian')
    temp = {}
    results = []

    with open(path, 'r') as f:
        ignore = ['and', 'you', 'the', 'for', 'can', 'app', 'url', 'code', 'web']

        for line in f:
            for word in line.split():
                word = word.lower().strip(',').strip('.').strip('!').strip('"').strip('?')
                if len(word) > 2 and word not in ignore and word.isalpha():
                    if word not in temp:
                        temp[word.strip(',').strip('.').strip('(').strip(')').lower()] = 1
                    else:
                        temp[word] += 1

    temp = sorted(temp.items(), key=lambda x: x[1])
    res = [i for i in temp if i[1] >= count]

    for i in res:
        result = translator.translate(i[0]).lower()
        results.append(f'{i[0]} - {result} ({i[1]} раз)')

    return results
