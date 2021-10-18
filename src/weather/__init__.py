from fastapi import FastAPI

from weather.status import status_router


def create_app(settings):
    app: FastAPI = FastAPI(
        title=settings.project_name,
        debug=settings.debug,
    )

    app.include_router(status_router)

    return app
