import requests
import json

from config import TOKEN


def get_weather_data(data: str):
    response = requests.post(f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={data}")

    return response.json()