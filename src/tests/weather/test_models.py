from datetime import datetime
from decimal import Decimal

from sqlalchemy import select


class TestWeatherModel:
    async def test_create_weather_data_model(
        self,
        db_session,
        add_weather_data
    ):
        from weather.weather.models import WeatherData

        model = await add_weather_data(
            city='Arica',
            country='CL',
            wind_speed=1.0,
            wind_deg=100,
            cloudiness=25,
            temperature=270,
            pressure=123,
            humidity=90,
            sunrise=datetime.fromisoformat('2021-10-18T22:57:42'),
            sunset=datetime.fromisoformat('2021-10-18T22:57:42'),
            lat=Decimal('1.15'),
            lng=Decimal('2.15'),
            requested_time=datetime.fromisoformat('2021-10-19T02:00:47'),
        )

        assert isinstance(model.id, int)

        # force the orm to reload object instances
        db_session.expire_all()

        stmt = await db_session.execute(select(WeatherData).filter_by(id=model.id))

        db_model = stmt.scalar_one()

        assert db_model.city == 'Arica'
        assert db_model.country == 'CL'
        assert db_model.wind_speed == 1.0
        assert db_model.wind_deg == 100
        assert db_model.cloudiness == 25
        assert db_model.temperature == 270
        assert db_model.pressure == 123
        assert db_model.humidity == 90
        assert db_model.lat == Decimal('1.15')
        assert db_model.lng == Decimal('2.15')

        assert db_model.sunrise == datetime.fromisoformat(
            '2021-10-18T22:57:42')
        assert db_model.sunset == datetime.fromisoformat('2021-10-18T22:57:42')
        assert db_model.requested_time == datetime.fromisoformat(
            '2021-10-19T02:00:47'
        )

        await db_session.commit()
