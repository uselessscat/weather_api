import responses


class TestWeatherRoutes:
    @responses.activate
    def test_get_weather_response_structure(
        self,
        settings,
        client,
        static_weather_response
    ):
        # prepare the response from online weather api
        url = settings.weather_url + '/data/2.5/weather'
        responses.add(responses.GET, url, json=static_weather_response())

        # do the call and assertions
        response = client.get(
            '/weather',
            params={
                'city': 'Santiago',
                'country': 'CL'
            }
        )

        assert response.status_code == 200
        json = response.json()

        assert json['location_name'] == 'Santiago, CL'
        assert json['temperature'] == '293.62 °K'
        assert json['wind'] == 'Gentle breeze, 3.6 m/s, 198°'
        assert json['cloudiness'] == 'Clear sky'
        assert json['pressure'] == '1015 hPa'
        assert json['humidity'] == '28%'
        assert json['sunrise'] == '09:57'
        assert json['sunset'] == '22:57'
        assert json['geo_coordinates'] == '[-33.4569, -70.6483]'
        assert json['requested_time'] == '2021-10-19T02:00:47'
