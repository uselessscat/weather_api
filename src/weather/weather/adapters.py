from typing import List, Tuple
from datetime import datetime

from weather.utils.wind_scale import WindScale


class OnlineToLocalAdapter:
    CLOUDINESS_PERCENT: int = 0
    CLOUDINESS_DESCRIPTION: int = 1
    CLOUDINESS_MAP: List[Tuple[float, str]] = [
        # 0: percent, 1: description
        (85.0, 'Overcast clouds'),
        (51.0, 'Broken clouds'),
        (25.0, 'Scattered clouds'),
        (11.0, 'Few clouds'),
        (0.0, 'Clear sky'),
    ]

    def __init__(self, data):
        self.data = data

    @classmethod
    def _get_cloudiness(cls, percent):
        # These values are only valid to this specific api
        return next(
            cloud[cls.CLOUDINESS_DESCRIPTION]
            for cloud in cls.CLOUDINESS_MAP
            if percent >= cloud[cls.CLOUDINESS_PERCENT]
        )

    def adapt(self):
        parse = datetime.utcfromtimestamp
        data = self.data
        sys = data.get('sys')
        main = data.get('main')

        city = data.get('name')
        time = parse(data.get('dt')).isoformat()
        country = sys.get('country')

        sunrise = parse(sys.get('sunrise')).time().strftime('%H:%M')
        sunset = parse(sys.get('sunset')).time().strftime('%H:%M')

        temperature = main.get('temp')
        pressure = main.get('pressure')
        humidity = main.get('humidity')

        wind_speed = data.get('wind').get('speed')
        wind_deg = data.get('wind').get('deg')  # TODO: use description
        wind_desc = WindScale.get_description(wind_speed)

        cloud_percent = data.get('clouds').get('all')
        cloudiness = self._get_cloudiness(cloud_percent)

        lat = data.get('coord').get('lat')
        lon = data.get('coord').get('lon')

        return {
            'location_name':  f'{city}, {country}',
            'temperature': f'{temperature} °K',
            'wind': f'{wind_desc}, {wind_speed} m/s, {wind_deg}°',
            'cloudiness': cloudiness,
            'pressure': f'{pressure} hPa',
            'humidity': f'{humidity}%',
            'sunrise': sunrise,
            'sunset': sunset,
            'geo_coordinates': f'[{lat}, {lon}]',
            'requested_time': time,
            # 'forecast': {}
        }
