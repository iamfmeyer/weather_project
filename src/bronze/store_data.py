import pandas as pd
from pathlib import Path
from datetime import datetime
import time


def weather_to_dataframe(weather_data: dict) -> pd.DataFrame:
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
        current_city_dict["_timestamp"] = datetime.now()
        current_city_dict["city"] = k
        current_city_dict["country"] = v["sys"]["country"]
        current_city_dict["weather_description"] = v["weather"][0]["description"]
        current_city_dict["temperature_celsius"] = v["main"]["temp"]
        current_city_dict["humidity"] = v["main"]["humidity"]
        current_city_dict["wind_speed"] = v["wind"]["speed"]
        current_city_dict["lat"] = v["coord"]["lat"]
        current_city_dict["long"] = v["coord"]["lon"]

        pdf_current_city = pd.DataFrame(current_city_dict, index=[0])
        print(pdf_current_city)
        pdf_current_weather = pd.concat(
            [pdf_current_weather, pdf_current_city], ignore_index=True
        )
    return pdf_current_weather


def weather_data_to_csv(
    pdf_current_weather_data: pd.DataFrame, storage_location: str
) -> None:
    csv_path = Path(storage_location) / "current_weather.csv"
    # Check if csv exists
    if Path(csv_path).is_file():
        print(
            """
                Appending new weather data to existing CSV file...
                """
        )
        pdf_current_weather_data.to_csv(csv_path, mode="a", header=False, index=False)

    else:
        print(
            """
            CSV file for storing weather does not exists yet.\n
            Creating it...
            """
        )
        # Create new csv file and store weather data
        pdf_current_weather_data.to_csv(csv_path, mode="w", header=True, index=False)
