from abc import ABC, abstractmethod


class WeatherRepository(ABC):
    @abstractmethod
    def get_by_city(self, city: str, country: str):
        pass
