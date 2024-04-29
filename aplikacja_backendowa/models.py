from pydantic import BaseModel, ValidationError, validator
from datetime import datetime

class WeatherData(BaseModel):
    timestamp: datetime
    temperature: float
    pressure: int

    @validator("temperature")
    def validate_temperature(cls, value):
        if value < -50 or value > 50:
            raise ValueError("Temperature must be between -50°C and 50°C")
        return value

    @validator("pressure")
    def validate_pressure(cls, value):
        if value < 800 or value > 1200:
            raise ValueError("Pressure must be between 800 hPa and 1200 hPa")
        return value