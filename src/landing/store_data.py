import pandas as pd
from pathlib import Path
from datetime import datetime


def weather_to_dataframe(weather_data: dict) -> pd.DataFrame:
    """This function converts the weather data into a pandas dataframe

    Args:
        weather_data (dict): A dictionary containing the weather data

    Returns:
        pd.DataFrame: A pandas dataframe containing the weather data
    """
    pdf_current_weather = pd.DataFrame(
        columns=[
            "_timestamp",
            "city",
            "country",
            "weather_description",
            "temperature_celsius",
            "humidity",
            "wind_speed",
            "lat",
            "long",
        ]
    )

    for k, v in weather_data.items():
        current_city_dict = dict()
        current_city_dict["_timestamp"] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        current_city_dict["city"] = k
        current_city_dict["country"] = v["sys"]["country"]
        current_city_dict["weather_description"] = v["weather"][0]["description"]
        current_city_dict["temperature_celsius"] = v["main"]["temp"]
        current_city_dict["humidity"] = v["main"]["humidity"]
        current_city_dict["wind_speed"] = v["wind"]["speed"]
        current_city_dict["lat"] = v["coord"]["lat"]
        current_city_dict["long"] = v["coord"]["lon"]

        pdf_current_city = pd.DataFrame(current_city_dict, index=[0])
        pdf_current_weather = pd.concat(
            [
                pdf_current_weather if not pdf_current_weather.empty else None,
                pdf_current_city,
            ],
            ignore_index=True,
        )
    return pdf_current_weather


def weather_data_to_parquet(
    pdf_current_weather_data: pd.DataFrame, storage_location: str
) -> None:
    """This function stores the current weather data in a parquet file

    Args:
        pdf_current_weather_data (pd.DataFrame): A pandas dataframe containing the weather data
        storage_location (str): A string containing the path to the directory where the parquet file should be stored
    """
    # Check if directory exists
    storage_location = Path(storage_location)
    if not storage_location.is_dir():
        storage_location.mkdir(parents=True)
        print(
            """
            Directory for storing weather data does not exist yet.\n
            Creating it...
            """
        )
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = Path(f"{storage_location}/{current_timestamp}.parquet")
    pdf_current_weather_data.to_parquet(file_path, engine="pyarrow")
