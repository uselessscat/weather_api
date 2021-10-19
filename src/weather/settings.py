from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    ''' App settings '''
    project_name: str = 'weather'
    environment: str = 'production'

    debug: bool = False

    database_uri: Optional[str]

    # how long the weather data should be considered valid
    weather_url: str = 'https://api.openweathermap.org'
    weather_api_key: Optional[str] = None
    weather_cache: int = 120

    class Config:
        env_file: str = '.env'


settings = Settings()

__all__ = [
    'settings',
    'Settings'
]
