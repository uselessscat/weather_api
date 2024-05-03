class TestStatus:
    async def test_status(self, client):
        response = await client.get('/status')

        assert response.status_code == 200

        json = response.json()

        assert json['status'] == 'running'
