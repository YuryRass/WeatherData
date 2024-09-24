import aiohttp
from typing import TYPE_CHECKING

from config import get_settings
from core.database import async_session
from weather.models import WeatherData
from weather.schema import FactWeatherInfo, WeatherInfo

settings = get_settings()

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def fetch_weather_data() -> FactWeatherInfo:
    """Возвращает данные о погоде в районе Сколтех."""

    headers = {"X-Yandex-Weather-Key": settings.API_WEATHER_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=settings.METEO_URL, headers=headers) as response:
            data = await response.json()
            return FactWeatherInfo(**data)

async def save_weather_data(data: WeatherInfo) -> None:
    """Функция для сохранения данных в БД."""
    session: "AsyncSession"
    async with async_session() as session:
        record = WeatherData(
            temperature=data.temp,
            wind_speed=data.wind_speed,
            wind_direction=data.wind_dir,
            pressure=data.pressure_mm,
            precipitation_type=data.prec_type,
            precipitation_amount=data.prec_strength
        )
        session.add(record)
        await session.commit()
