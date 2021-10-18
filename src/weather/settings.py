from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    ''' App settings '''
    project_name: str = 'weather'
    environment: str = 'production'

    debug: bool = False

    database_uri: Optional[str]

    class Config:
        env_file: str = '.env'


__all__ = [
    Settings
]
