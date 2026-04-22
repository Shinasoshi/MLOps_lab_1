from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed_values = {"dev", "test", "prod"}
        if value not in allowed_values:
            raise ValueError("ENVIRONMENT must be one of: dev, test, prod")
        return value
