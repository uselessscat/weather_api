from pydantic.utils import path_type
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope='session')
def override_settings():
    ''' Replace the global settings object with a better one for testing '''
    from weather.settings import Settings

    # use the whole module to override the global variable, not very clean
    # TODO: use environment variables
    import weather.settings as settings

    settings.settings = Settings(
        environment='test',
        debug=True,
        database_uri='postgresql://postgres:postgres@db/weather_test',
    )

    return settings.settings


@pytest.fixture(scope='session')
def app(override_settings):
    from weather import create_app

    app = create_app(override_settings)

    return app


@pytest.fixture(scope='session')
def client(app):
    return TestClient(app)
