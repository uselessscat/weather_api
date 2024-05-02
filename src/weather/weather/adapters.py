from datetime import datetime, timezone

from weather.utils.wind_scale import WindScale


class ModelToResponseAdapter:
    CLOUDINESS_PERCENT: int = 0
    CLOUDINESS_DESCRIPTION: int = 1
    CLOUDINESS_MAP: list[tuple[float, str]] = [
        # 0: percent, 1: description
        (85.0, 'Overcast clouds'),
        (51.0, 'Broken clouds'),
        (25.0, 'Scattered clouds'),
        (11.0, 'Few clouds'),
        (0.0, 'Clear sky'),
    ]

    def __init__(self, model):
        self.model = model

    @classmethod
    def _get_cloudiness(cls, percent):
        # These values are only valid to this specific api
        return next(
            cloud[cls.CLOUDINESS_DESCRIPTION]
            for cloud in cls.CLOUDINESS_MAP
            if percent >= cloud[cls.CLOUDINESS_PERCENT]
        )

    def adapt(self):
        model = self.model

        city = model.get('city')
        country = model.get('country')

        wind_speed = model.get('wind_speed')
        wind_deg = model.get('wind_deg')
        wind_desc = WindScale.get_description(wind_speed)

        cloud_percent = model.get('cloudiness')
        cloudiness = self._get_cloudiness(cloud_percent)

        temperature = model.get('temperature')
        pressure = model.get('pressure')
        humidity = model.get('humidity')

        sunrise = model.get('sunrise').time().strftime('%H:%M')
        sunset = model.get('sunset').time().strftime('%H:%M')

        lat = model.get('lat')
        lon = model.get('lng')

        time = model.get('requested_time').isoformat()

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


class OnlineToLocalAdapter:
    def __init__(self, data):
        self.data = data

    def adapt(self):
        data = self.data
        city = data.get('name').lower()

        sys = data.get('sys')
        country = sys.get('country').lower()

        main = data.get('main')
        temperature = main.get('temp')
        pressure = main.get('pressure')
        humidity = main.get('humidity')

        wind = data.get('wind')
        wind_speed = wind.get('speed')
        wind_deg = wind.get('deg')

        cloud_percent = data.get('clouds').get('all')

        lat = data.get('coord').get('lat')
        lng = data.get('coord').get('lon')

        sunrise = datetime.fromtimestamp(sys.get('sunrise'), timezone.utc)
        sunset = datetime.fromtimestamp(sys.get('sunset'), timezone.utc)
        time = datetime.fromtimestamp(data.get('dt'), timezone.utc)

        return {
            'city': city,
            'country': country,
            'wind_speed': wind_speed,
            'wind_deg': wind_deg,
            'cloudiness': cloud_percent,
            'temperature': temperature,
            'pressure': pressure,
            'humidity': humidity,
            'sunrise': sunrise,
            'sunset': sunset,
            'lat': lat,
            'lng': lng,
            'requested_time': time,
        }
