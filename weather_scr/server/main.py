from typing import Union

from fastapi import FastAPI

from scrap import get_weather_data

app = FastAPI()

@app.post("/weather/{data}") #If you need to accept get requests, change @app.post
def read_root(data: str):
    return get_weather_data(data=data)