import pytest
from httpx import ASGITransport, AsyncClient
from pytest_asyncio import is_async_test
from sqlalchemy.ext.asyncio import create_async_engine

pytest_plugins = (
    'tests.fixtures.online_weather',
    'tests.fixtures.models',
    'tests.fixtures.fakers',
)


def pytest_collection_modifyitems(items):
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(scope='session')

    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture(scope='session')
def settings():
    from weather.settings import settings

    return settings


@pytest.fixture(scope='session')
async def client(settings):  # noqa: ARG001
    from weather import create_app

    app = create_app(settings)

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://127.0.0.1',
    ) as client:
        yield client


@pytest.fixture(scope='session')
async def db_session(settings):
    from weather.database import BaseModel
    from weather.database.session import session_maker

    engine = create_async_engine(
        settings.database_uri,
        pool_pre_ping=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

    async with session_maker() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest.fixture(scope='session')
def fake():
    from faker import Faker

    faker = Faker()
    faker.seed_instance(0)

    return faker
