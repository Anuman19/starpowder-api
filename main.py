from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

env = {
    "temperature": "0",
    "pressure": "0",
    "humidity": "0"}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return env


@app.post("/temperature")
async def post_temp(newTemp: str):
    env["temperature"] = newTemp


@app.get("/temperature")
async def get_temp():
    return env["temperature"]


@app.post("/humidity")
async def post_hum(newHum: str):
    env["humidity"] = newHum


@app.get("/humidity")
async def get_hum():
    return env["humidity"]


@app.post("/pressure")
async def post_pressure(newPressure: str):
    env["pressure"] = newPressure


@app.get("/pressure")
async def get_pressure():
    return env["pressure"]