from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from weather.database import session_dependency
from weather.settings import settings

from .repositories import LocalWeatherRepository, OnlineWeatherRepository
from .schemas import Weather
from .service import WeatherService

router = APIRouter(tags=['Weather'])


@router.get('/weather', response_model=Weather)
async def get_weather(
    city: str = Query(...),
    country: str = Query(...),
    session: Session = Depends(session_dependency),
):
    local = LocalWeatherRepository(session=session)
    online = OnlineWeatherRepository(
        base_url=settings.weather_url, api_key=settings.weather_api_key
    )

    service = WeatherService(local, online, cache=settings.weather_cache)

    weather = await service.get_weather(city, country)

    return Weather.model_validate(weather)


__all__ = ['router']
