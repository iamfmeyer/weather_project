import json
import requests
import time


def get_weather_data(base_url: str, locations: list, unit: str, api_key: str) -> dict:
    current_weather_dict = dict()

    for city in locations:
        url = f"{base_url}{city}&appid={api_key}&units={unit}"
        try:
            response = requests.get(url)
        except requests.HTTPError:
            break

        weather_data = response.json()
        current_weather_dict[city] = weather_data

    return current_weather_dict
