class TestStatus:
    def test_status(
        self,
        client
    ):
        response = client.get('/status')

        assert response.status_code == 200

        json_response = response.json()

        assert json_response['status'] == 'running'
