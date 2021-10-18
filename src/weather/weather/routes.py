from fastapi import APIRouter, Query

router = APIRouter(
    tags=['Weather']
)


@router.get('/weather')
def get_weather(
    city: str = Query(...),
    country: str = Query(...),
):
    return {
        'location_name': f'{city}, {country}',
        'temperature': '',
        'wind': '',
        'cloudiness': '',
        'pressure': '',
        'humidity': '',
        'sunrise': '',
        'sunset': '',
        'geo_coordinates': '',
        'requested_time': '',
        'forecast': '',
    }


__all__ = [
    'router'
]
