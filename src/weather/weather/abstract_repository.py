from abc import ABC, abstractmethod


class WeatherRepository(ABC):
    @abstractmethod
    async def get_by_city(self, city: str, country: str):
        pass
