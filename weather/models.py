from sqlalchemy.orm import Mapped
from core.database import Base
from weather.mixins import TimestampMixin


class WeatherData(TimestampMixin, Base):
    """Модель данных о погоде."""

    temperature: Mapped[float]
    wind_speed: Mapped[float]
    wind_direction: Mapped[str]
    pressure: Mapped[float]
    precipitation_type: Mapped[str]
    precipitation_amount: Mapped[float]