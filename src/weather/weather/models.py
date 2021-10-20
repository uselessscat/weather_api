from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Integer, Float, DECIMAL

from weather.database import BaseModel


class WeatherData(BaseModel):
    __tablename__ = 'weather_data'
    # Im keeping this simple as possible as this is an example. Most of the
    # entities here can be normalized like cities, etc-

    # im not sure what are the longest city names.
    city = Column(String(50), nullable=True)
    country = Column(String(20), nullable=True)

    wind_speed = Column(DECIMAL(5, 1), nullable=True)
    wind_deg = Column(Integer, nullable=True)

    cloudiness = Column(Float, nullable=True)
    temperature = Column(DECIMAL(5, 2), nullable=True)
    pressure = Column(Integer, nullable=True)
    humidity = Column(Integer, nullable=True)

    sunrise = Column(DateTime, nullable=True)
    sunset = Column(DateTime, nullable=True)

    # Also can be Decimal
    lat = Column(DECIMAL(11, 7), nullable=True)
    lng = Column(DECIMAL(11, 7), nullable=True)

    requested_time = Column(DateTime, nullable=True)
