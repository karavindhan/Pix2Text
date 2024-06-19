# from model import model_pipeline
from pix2text import Pix2Text

from typing import Union

from fastapi import FastAPI, UploadFile
import io
from PIL import Image
import json
from flask import jsonify
from pix2text import PageJsonEncoder

app = FastAPI()

p2t = Pix2Text.from_config()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(image: UploadFile):
    # content = image.file.read()
    
    # image = Image.open(io.BytesIO(content))
    image = Image.open(image.file)
    doc = p2t.recognize_page(image)

    return json.loads(json.dumps(doc, cls=PageJsonEncoder, indent=4))

