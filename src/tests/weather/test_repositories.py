import respx
from httpx import Response

from weather.weather.repositories import (
    LocalWeatherRepository,
    OnlineWeatherRepository,
)


class TestWeatherRepository:
    async def test_repository_retrieve_response_from_database(
        self,
        db_session,
        add_weather_data,
        fake_weather_data,
    ):
        # Create fake data to run the test
        fake_data = fake_weather_data(
            city='La Serena',
            country='CL',
        )
        await add_weather_data(**fake_data)

        db_session.expire_all()

        repo = LocalWeatherRepository(session=db_session)

        weather_data = await repo.get_by_city('La Serena', 'CL')

        assert weather_data is not None
        assert weather_data.wind_speed == fake_data.get('wind_speed')
        assert weather_data.wind_deg == fake_data.get('wind_deg')
        assert weather_data.cloudiness == fake_data.get('cloudiness')
        assert weather_data.temperature == fake_data.get('temperature')
        assert weather_data.pressure == fake_data.get('pressure')
        assert weather_data.humidity == fake_data.get('humidity')
        assert weather_data.sunrise == fake_data.get('sunrise')
        assert weather_data.sunset == fake_data.get('sunset')
        assert weather_data.lat == fake_data.get('lat')
        assert weather_data.lng == fake_data.get('lng')
        assert weather_data.requested_time == fake_data.get('requested_time')


class TestWeatherOnlineRepository:
    @respx.mock
    async def test_repository_makes_requests(self, static_weather_response):
        response = static_weather_response()
        response['name'] = 'Cordoba'
        response['sys']['country'] = 'AR'

        respx.get('https://myweather.com/data/2.5/weather').mock(
            return_value=Response(200, json=response)
        )

        repository = OnlineWeatherRepository(
            'https://myweather.com', 'an-api-key'
        )

        data = await repository.get_by_city('Cordoba', 'AR')

        # for now just check first level
        assert data['city'] == 'cordoba'
        assert data['country'] == 'ar'
        assert data['wind_speed'] == 3.6
        assert data['wind_deg'] == 198
        assert data['cloudiness'] == 0
        assert data['temperature'] == 293.62
        assert data['pressure'] == 1015
        assert data['humidity'] == 28
        assert data['lat'] == -33.4569
        assert data['lng'] == -70.6483
        assert data['sunrise'].isoformat() == '2021-10-18T09:57:21'
        assert data['sunset'].isoformat() == '2021-10-18T22:57:42'
        assert data['requested_time'].isoformat() == '2021-10-19T02:00:47'
