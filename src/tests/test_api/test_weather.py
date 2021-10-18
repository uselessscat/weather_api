
class TestWeather:
    def test_get_weather_response_structure(self, client):
        response = client.get(
            '/weather',
            params={
                'city': 'Santiago',
                'country': 'CL'
            }
        )

        assert response.status_code == 200

        json = response.json()

        assert isinstance(json.get('location_name'), str)
        assert isinstance(json.get('temperature'), str)
        assert isinstance(json.get('wind'), str)
        assert isinstance(json.get('cloudiness'), str)
        assert isinstance(json.get('pressure'), str)
        assert isinstance(json.get('humidity'), str)
        assert isinstance(json.get('sunrise'), str)
        assert isinstance(json.get('sunset'), str)
        assert isinstance(json.get('geo_coordinates'), str)
        assert isinstance(json.get('requested_time'), str)
        assert isinstance(json.get('forecast'), str)
