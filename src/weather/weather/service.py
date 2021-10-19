from typing import Type

from .abstract_repository import WeatherRepository


class WeatherService:
    def __init__(
        self,
        local_repository: Type[WeatherRepository],
        online_repository: Type[WeatherRepository] = None,
        cache: int = 120
    ):
        self.cache = cache
        self.local = local_repository
        self.online = online_repository

    def get_weather(self, city: str, country: str):
        return self.online.get_by_city(city, country)

    def update_weather(self, city: str, country: str, data):
        return None
