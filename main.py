# main.py
import paho.mqtt.client as mqtt
import json
import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import requests

class Temp(BaseModel):
    type: str
    data: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/temp/")
async def post_temp(temp: Temp):
    return temp



