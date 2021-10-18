from typing import Type

from pydantic import BaseSettings
from fastapi.applications import FastAPI


class AppBuilder:
    def __init__(self, settings: Type[BaseSettings]):
        self.app: FastAPI = FastAPI(title=settings.project_name)

    def _include_routers(self):
        from weather.status import status_router

        # register app routes
        self.app.include_router(status_router)

    def build(self):
        self._include_routers()

        return self.app


__all__ = [
    AppBuilder
]
