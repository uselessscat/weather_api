import pytest
from fastapi.testclient import TestClient

pytest_plugins = (
    'tests.fixtures.online_weather',
    'tests.fixtures.models',
    'tests.fixtures.fakers',
)


@pytest.fixture(scope='session')
def settings():
    from weather.settings import settings

    return settings


@pytest.fixture(scope='session')
def app(settings):
    from weather import create_app
    from weather.database.session import session_maker
    from weather.database import BaseModel

    app = create_app(settings)

    session = session_maker()
    BaseModel.metadata.create_all(session.get_bind())

    yield app

    BaseModel.metadata.drop_all(session.get_bind())


@pytest.fixture(scope='session')
def client(app):
    return TestClient(app)


@pytest.fixture()
def db_session():
    from weather.database.session import session_maker

    try:
        session = session_maker()

        yield session
    finally:
        session.close()


@pytest.fixture(scope='session')
def fake(app):
    from faker import Faker

    faker = Faker()
    faker.seed_instance(0)

    return faker
