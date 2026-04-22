from settings import Settings


def test_settings_load_correctly():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "My App (Test)"
    assert settings.API_KEY == "test-api-key"
