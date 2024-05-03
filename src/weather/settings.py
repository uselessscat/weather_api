from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings"""

    model_config = SettingsConfigDict(env_file='.env')

    project_name: str = 'weather'
    environment: str = 'production'

    debug: bool = False

    database_uri: Optional[str]

    # how long the weather data should be considered valid
    weather_url: str = 'https://api.openweathermap.org'
    weather_api_key: Optional[str] = None
    weather_cache: int = 120


settings = Settings()

__all__ = ['settings', 'Settings']
