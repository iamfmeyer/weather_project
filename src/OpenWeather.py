import yaml
from pathlib import Path


class OpenWeather:
    _api_key: str

    def __init__(self):
        self.secrets_path = Path("../secrets/API.yaml")
        self.config_path = Path("../config.yaml")
        self.load_api_key()
        self.config_args = self.get_api_args()

        self.current_weather_url: str = self.config_args["current_weather_url"]
        self.locations: list = self.config_args["locations"]
        self.unit: str = self.config_args["unit"]
        self.storage_location: str = self.config_args["storage_location"]

    def load_api_key(self) -> None:
        try:
            with self.secrets_path.open(mode="r", encoding="utf-8") as f:
                secrets: dict = yaml.safe_load(f)
                api_key: str = secrets["open_weather_api"]["API_KEY"]
                self._api_key = api_key

        except FileNotFoundError as e:
            print("File could not be found.\n" + str(e))

    def get_api_key(self) -> str:
        return self._api_key

    def get_api_args(self) -> dict:
        try:
            with self.config_path.open(mode="r", encoding="utf-8") as f:
                config: dict = yaml.safe_load(f)

                current_weather_url: str = config["open_weather_api"]["current_weather"]
                locations: list = config["open_weather_api"]["locations"]
                unit: str = config["open_weather_api"]["unit"]
                storage_location: str = config["storage_location"]
                config_args_dict = {
                    "current_weather_url": current_weather_url,
                    "locations": locations,
                    "unit": unit,
                    "storage_location": storage_location,
                }

                return config_args_dict

        except FileNotFoundError as e:
            print("File could not be found.\n" + str(e))
