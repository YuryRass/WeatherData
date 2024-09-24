from pydantic import BaseModel, Field, field_validator

from weather.utils import PRECIPITATION_TYPE_MAP, WIND_DIRECTION_MAP, WindDirection


class WeatherInfo(BaseModel):
    """Схема информации о погоде."""

    temp: float = Field(..., description='Temperature in degrees Celsius')
    wind_speed: float = Field(..., description='Wind speed in meters per second')
    wind_dir: str = Field(..., description='Wind direction as a string')
    pressure_mm: float = Field(..., description='Pressure in mm of mercury')
    prec_type: int = Field(..., description='Type of precipitation', ge=0, le=4)
    prec_strength: float = Field(..., description='Amount of precipitation')

    @field_validator("wind_dir")
    def change_wind_dir(cls, value: str) -> str:
        """Меняет значение wind_dir."""
        if value not in WindDirection._value2member_map_:
            raise ValueError("Ошибка в валидации значения направления ветра")
        return WIND_DIRECTION_MAP[value]

    @field_validator("prec_type")
    def change_precipitation_type(cls, value: int) -> str:
        """Меняет значение prec_type."""
        return PRECIPITATION_TYPE_MAP[value]

class FactWeatherInfo(BaseModel):
    """Информация о погоде на данный момент."""

    fact: WeatherInfo
