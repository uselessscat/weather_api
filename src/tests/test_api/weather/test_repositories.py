import responses
from responses import matchers

from weather.weather.repositories import OnlineWeatherRepository


class TestWeatherOnlineRepository:
    @responses.activate
    def test_repository_makes_requests(
        self,
        static_weather_response
    ):
        responses.add(
            responses.GET,
            'https://myweather.com/data/2.5/weather',
            json=static_weather_response(),
            match=[
                matchers.query_param_matcher({
                    'appid': 'an-api-key',
                    'q': 'santiago,cl'
                })
            ]
        )

        repository = OnlineWeatherRepository(
            'https://myweather.com',
            'an-api-key'
        )

        data = repository.get_by_city('santiago', 'cl')

        # for now just check first level
        assert data['location_name'] == 'Santiago, CL'
        assert data['temperature'] == '293.62 °K'
        assert data['wind'] == 'Gentle breeze, 3.6 m/s, 198°'
        assert data['cloudiness'] == 'Clear sky'
        assert data['pressure'] == '1015 hPa'
        assert data['humidity'] == '28%'
        assert data['sunrise'] == '09:57'
        assert data['sunset'] == '22:57'
        assert data['geo_coordinates'] == '[-33.4569, -70.6483]'
        assert data['requested_time'] == '2021-10-19T02:00:47'
