class TestSettings:
    def test_override_settings(
        self,
        app
    ):
        from weather.settings import settings

        assert app.title == 'weather'
        assert settings.debug is True
        assert settings.environment == 'test'
