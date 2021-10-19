from fastapi import APIRouter, Query

from weather.settings import settings

from .service import WeatherService
from .repositories import LocalWeatherRepository, OnlineWeatherRepository
from .schemas import Weather

router = APIRouter(
    tags=['Weather']
)


@router.get(
    '/weather',
    response_model=Weather
)
def get_weather(
    city: str = Query(...),
    country: str = Query(...),
):
    local = LocalWeatherRepository()
    online = OnlineWeatherRepository(
        base_url=settings.weather_url,
        api_key=settings.weather_api_key
    )

    service = WeatherService(
        local,
        online,
        cache=settings.weather_cache
    )

    weather = service.get_weather(city, country)

    return Weather.parse_obj(weather)


__all__ = [
    'router'
]
