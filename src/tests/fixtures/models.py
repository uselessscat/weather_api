import pytest


@pytest.fixture()
async def add_model(db_session):
    async def _add_model(model, *args, **kwargs):
        new = model(*args, **kwargs)

        db_session.add(new)
        await db_session.commit()

       # await db_session.refresh(new)
        #await db_session.commit()

        return new

    return _add_model


@pytest.fixture()
def add_weather_data(add_model):
    async def _add_weather_data(*args, **kwargs):
        from weather.weather.models import WeatherData

        return await add_model(WeatherData, *args, **kwargs)

    return _add_weather_data
