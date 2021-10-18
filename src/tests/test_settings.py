class TestSettings:
    def test_override_settings(
        self,
        app
    ):
        from weather.settings import settings

        assert app.title == 'weather'
        assert settings.debug == True
        assert settings.environment == 'test'
