from decimal import Decimal

import pytest


@pytest.fixture()
def fake_weather_data(fake):
    def _fake_weather_data(**kwargs):
        return {
            **{
                'city': fake.city(),
                'country': fake.country_code(),
                'wind_speed': Decimal(fake.random_int(0, 350)) / 10,
                'wind_deg': Decimal(fake.random_int(0, 360)),
                'cloudiness': fake.random_int(0, 100),
                'temperature': Decimal(fake.random_int(2430, 3131)) / 10,
                'pressure': Decimal(fake.random_int(50, 200)),
                'humidity': fake.random_int(0, 100),
                'sunrise': fake.date_time(),
                'sunset': fake.date_time(),
                'lat': fake.latitude(),
                'lng': fake.longitude(),
                'requested_time': fake.date_time(),
            },
            **kwargs,
        }

    return _fake_weather_data
