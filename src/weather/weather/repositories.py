import urllib
import requests

from weather.weather.adapters import OnlineToLocalAdapter

from .abstract_repository import WeatherRepository


class LocalWeatherRepository(WeatherRepository):
    def get_by_city(self, city: str, country: str):
        pass


class OnlineWeatherRepository(WeatherRepository):
    WEATHER_DATA: str = 'data/2.5/weather'

    def __init__(
        self,
        base_url,
        api_key
    ):
        self.base_url = base_url
        self.api_key = api_key

    def get_by_city(self, city: str, country: str):
        response = requests.get(
            urllib.parse.urljoin(self.base_url, self.WEATHER_DATA),
            params={
                'q': f'{city},{country}',
                'appid': self.api_key
            }
        )

        json = response.json()

        return OnlineToLocalAdapter(json).adapt()
