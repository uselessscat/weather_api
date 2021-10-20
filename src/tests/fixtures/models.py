import pytest


@pytest.fixture
def add_model(db_session):
    def _add_model(model, *args, **kwargs):
        new = model(*args, **kwargs)

        db_session.add(new)
        db_session.commit()

        return new

    return _add_model


@pytest.fixture
def add_weather_data(add_model):
    def _add_weather_data(*args, **kwargs):
        from weather.weather.models import WeatherData

        return add_model(
            WeatherData,
            *args,
            **kwargs
        )

    return _add_weather_data
