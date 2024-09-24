from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройка приложения"""

    # данные для базы данных PostgreSQL
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # Сколтех координаты
    LATITUDE: float
    LONGITUDE: float

    API_WEATHER_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        """URL адрес базы данных postgresql"""

        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def METEO_URL(self) -> str:
        """URL адрес для получения данных о погоде в районе Сколтех."""

        return (
            f"https://api.weather.yandex.ru/v2/forecast?lat={self.LATITUDE}&lon={self.LONGITUDE}"
        )

    model_config = SettingsConfigDict(env_file=".env")


def get_settings(**kwargs: Any) -> Settings:
    return Settings(**kwargs)
