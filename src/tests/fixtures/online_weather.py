import pytest


@pytest.fixture
def static_weather_response():
    def _static_weather_response():
        return {
            'coord': {
                'lon': -70.6483,
                'lat': -33.4569
            },
            'weather': [
                {
                    'id': 800,
                    'main': 'Clear',
                    'description': 'clear sky',
                    'icon': '01n'
                }
            ],
            'base': 'stations',
            'main': {
                'temp': 293.62,
                'feels_like': 292.45,
                'temp_min': 293.62,
                'temp_max': 293.62,
                'pressure': 1015,
                'humidity': 28,
                'sea_level': 1015,
                'grnd_level': 952
            },
            'visibility': 10000,
            'wind': {
                'speed': 3.6,
                'deg': 198,
                'gust': 1.01
            },
            'clouds': {
                'all': 0
            },
            'dt': 1634608847,
            'sys': {
                'type': 2,
                'id': 2039090,
                'country': 'CL',
                'sunrise': 1634551041,
                'sunset': 1634597862
            },
            'timezone': -10800,
            'id': 3871336,
            'name': 'Santiago',
            'cod': 200
        }

    return _static_weather_response
