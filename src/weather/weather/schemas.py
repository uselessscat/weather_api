from pydantic import BaseModel, Field


class Weather(BaseModel):
    location_name: str = Field(...)
    temperature: str = Field(...)
    wind: str = Field(...)
    cloudiness: str = Field(...)
    pressure: str = Field(...)
    humidity: str = Field(...)
    sunrise: str = Field(...)
    sunset: str = Field(...)
    geo_coordinates: str = Field(...)
    requested_time: str = Field(...)

    # forecast: Optional[str] = Field(None)
