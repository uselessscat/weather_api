import urllib
import requests
from sqlalchemy import select, insert

from weather.weather.adapters import OnlineToLocalAdapter

from .abstract_repository import WeatherRepository
from .models import WeatherData


class LocalWeatherRepository(WeatherRepository):
    def __init__(self, *args, session, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = session

    def get_by_city(self, city: str, country: str):
        stmt = self.session.execute(
            select(WeatherData)
            .filter(WeatherData.city.ilike(city))
            .filter(WeatherData.country.ilike(country))
            .order_by(WeatherData.created_date.desc())
        )

        return stmt.scalars().first()

    def create(self, data):
        stmt = self.session.execute(
            insert(WeatherData).values(**data)
        )

        self.session.commit()

        return stmt


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
