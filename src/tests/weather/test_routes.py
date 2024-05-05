import respx
from httpx import Response
from sqlalchemy import update


class TestWeatherRoutes:
    @respx.mock
    async def test_get_weather_response_structure(
        self, settings, client, static_weather_response
    ):
        # prepare the response from online weather api
        url = settings.weather_url + '/data/2.5/weather'
        respx.get(url).mock(
            return_value=Response(200, json=static_weather_response())
        )

        # do the call and assertions
        response = await client.get(
            '/weather', params={'city': 'Santiago', 'country': 'CL'}
        )

        assert response.status_code == 200
        json = response.json()

        assert json['location_name'] == 'santiago, cl'
        assert json['temperature'] == '293.62 °K'
        assert json['wind'] == 'Gentle breeze, 3.6 m/s, 198°'
        assert json['cloudiness'] == 'Clear sky'
        assert json['pressure'] == '1015 hPa'
        assert json['humidity'] == '28%'
        assert json['sunrise'] == '09:57'
        assert json['sunset'] == '22:57'
        assert json['geo_coordinates'] == '[-33.4569, -70.6483]'
        assert json['requested_time'] == '2021-10-19T02:00:47'

    @respx.mock
    async def test_get_weather_use_cache(
        self, settings, client, db_session, static_weather_response
    ):
        from weather.weather.models import WeatherData

        # prepare the response from online weather api
        response = static_weather_response()
        response['name'] = 'Valdivia'

        url = settings.weather_url + '/data/2.5/weather'
        respx.get(url).mock(return_value=Response(200, json=response))

        # do the call and assertions
        response = await client.get(
            '/weather', params={'city': 'Valdivia', 'country': 'CL'}
        )

        assert response.status_code == 200
        json = response.json()

        assert json['location_name'] == 'valdivia, cl'
        assert json['temperature'] == '293.62 °K'

        # we will update the row to check that the api retrieves from database
        async with db_session.begin():
            await db_session.execute(
                update(WeatherData)
                .filter(WeatherData.city.ilike('Valdivia'))
                .filter(WeatherData.country.ilike('CL'))
                .values(temperature=100.1)
            )

        # do the call and assertions
        response = await client.get(
            '/weather', params={'city': 'Valdivia', 'country': 'CL'}
        )

        assert response.status_code == 200

        json = response.json()
        assert json['temperature'] == '100.10 °K'
