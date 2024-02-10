import yaml
from omegaconf import OmegaConf
from pathlib import Path


class OpenWeather:
    _api_key: str

    def __init__(self):
        self.config_path = Path("/home/fmeyer/code/repos/weather_project/config.yaml")
        self.config_args = self.get_config_parameters()

        self.secrets_path = Path(self.config_args["secrets_path"])
        self._load_api_key()

        self.current_weather_url: str = self.config_args["current_weather_url"]
        self.locations: list = self.config_args["locations"]
        self.unit: str = self.config_args["unit"]
        self.storage_location_landing: str = self.config_args[
            "storage_location_landing"
        ]
        self.storage_location_silver: str = self.config_args["storage_location_silver"]

    def _load_api_key(self) -> None:
        """
        This function loads the api key from the secrets file
        """
        try:
            with self.secrets_path.open(mode="r", encoding="utf-8") as f:
                secrets: dict = yaml.safe_load(f)
                api_key: str = secrets["open_weather_api"]["API_KEY"]
                self._api_key = api_key

        except FileNotFoundError as e:
            print("File could not be found.\n" + str(e))

    def get_api_key(self) -> str:
        """This function returns the api key

        Returns:
            str: A string containing the api key
        """
        return self._api_key

    def get_config_parameters(self) -> dict:
        """This function returns the config parameters

        Returns:
            dict: A dictionary containing the config parameters
        """
        try:
            with self.config_path.open(mode="r", encoding="utf-8") as f:
                config = OmegaConf.load(f)

                secrets_path: str = config.secrets
                current_weather_url: str = config.open_weather_api.current_weather
                locations: list = config.open_weather_api.locations
                unit: str = config.open_weather_api.unit
                storage_location_landing: str = config.data_storage_location.landing
                storage_location_silver: str = config.data_storage_location.silver
                config_args_dict = {
                    "secrets_path": secrets_path,
                    "current_weather_url": current_weather_url,
                    "locations": locations,
                    "unit": unit,
                    "storage_location_landing": storage_location_landing,
                    "storage_location_silver": storage_location_silver,
                }

                return config_args_dict

        except FileNotFoundError as e:
            print("File could not be found.\n" + str(e))
