# main.py
import paho.mqtt.client as mqtt
import json
import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import requests

temp = {
    "celsius": "0",
    "pressure": "0",
    "humidity": "0"}

app = FastAPI()


@app.get("/")
async def root():
    return temp


@app.post("/temp")
async def post_temp(newTemp: str):
    temp["celsius"] = newTemp


@app.get("/temp")
async def get_temp():
    return temp


@app.post("/hum")
async def post_hum(newHum: str):
    temp["humidity"] = newHum


@app.get("/hum")
async def get_hum():
    return temp["humidity"]


@app.post("/pressure")
async def post_pressure(newPressure: str):
    temp["pressure"] = newPressure


@app.get("/pressure")
async def get_pressure():
    return temp["pressure"]
