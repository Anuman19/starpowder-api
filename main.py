# main.py
from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "temperature"}


class Temp(BaseModel):
    type: str
    data: str


@app.post("/temp/")
async def post_temp(temp: Temp):
    return temp
