import requests


def get_weather_data(base_url: str, locations: list, unit: str, api_key: str) -> dict:
    """This function retrieves the weather data from the open weather api

    Args:
        base_url (str): A string containing the base url
        locations (list): A list containing the locations
        unit (str): A string containing the unit
        api_key (str): A string containing the api key

    Returns:
        dict: A dictionary containing the weather data
    """
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
