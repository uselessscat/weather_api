from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from weather.settings import settings
from weather.database import session_dependency

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
    session: Session = Depends(session_dependency),
):
    local = LocalWeatherRepository(session=session)
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

    return Weather.model_validate(weather)


__all__ = [
    'router'
]
