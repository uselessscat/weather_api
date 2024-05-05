import pytest


@pytest.fixture()
def add_model(db_session):
    async def _add_model(model, *args, **kwargs):
        async with db_session.begin():
            new = model(*args, **kwargs)

            db_session.add(new)

            return new

    return _add_model


@pytest.fixture()
def add_weather_data(add_model):
    def _add_weather_data(*args, **kwargs):
        from weather.weather.models import WeatherData

        return add_model(WeatherData, *args, **kwargs)

    return _add_weather_data
