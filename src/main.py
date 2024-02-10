from OpenWeather import OpenWeather
from landing.read_data import get_weather_data
from landing.store_data import weather_to_dataframe, weather_data_to_parquet


def main():
    open_weather = OpenWeather()

    current_weather_dict: dict = get_weather_data(
        base_url=open_weather.current_weather_url,
        api_key=open_weather.get_api_key(),
        locations=open_weather.locations,
        unit=open_weather.unit,
    )

    pdf_current_weather = weather_to_dataframe(current_weather_dict)
    weather_data_to_parquet(pdf_current_weather, open_weather.storage_location_landing)


if __name__ == "__main__":
    main()
