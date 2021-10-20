from typing import Type
import datetime

from .abstract_repository import WeatherRepository
from .adapters import ModelToResponseAdapter


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
        lower_city = city.lower()
        lower_country = country.lower()

        model = self.local.get_by_city(lower_city, lower_country)

        if model is not None:
            is_cache_outdated = datetime.datetime.now() > \
                model.created_date + datetime.timedelta(seconds=self.cache)

            if is_cache_outdated:
                weather_data = self.online.get_by_city(
                    lower_city,
                    lower_country
                )

                self.update_weather(weather_data)
            else:
                # __dict__ is not the best option (includes some sqlalchemy
                # fields)
                weather_data = model.__dict__
        else:
            weather_data = self.online.get_by_city(lower_city, lower_country)

            self.update_weather(weather_data)

        return ModelToResponseAdapter(weather_data).adapt()

    def update_weather(self, data):
        return self.local.create(data)
