import urllib

import httpx
from sqlalchemy import insert, select

from weather.weather.adapters import OnlineToLocalAdapter

from .abstract_repository import WeatherRepository
from .models import WeatherData


class LocalWeatherRepository(WeatherRepository):
    def __init__(self, *args, session, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = session

    async def get_by_city(self, city: str, country: str):
        async with self.session.begin():
            stmt = await self.session.execute(
                select(WeatherData)
                .filter(WeatherData.city.ilike(city))
                .filter(WeatherData.country.ilike(country))
                .order_by(WeatherData.created_date.desc())
            )

            return stmt.scalars().first()

    async def create(self, data):
        async with self.session.begin():
            return await self.session.execute(
                insert(WeatherData).values(**data)
            )


class OnlineWeatherRepository(WeatherRepository):
    WEATHER_DATA: str = 'data/2.5/weather'

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    async def get_by_city(self, city: str, country: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                urllib.parse.urljoin(self.base_url, self.WEATHER_DATA),
                params={'q': f'{city},{country}', 'appid': self.api_key},
            )

            json = response.json()

        return OnlineToLocalAdapter(json).adapt()
