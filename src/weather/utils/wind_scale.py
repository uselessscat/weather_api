class WindScale:
    WIND_SCALE_SPEED: int = 0
    WIND_SCALE_DESCRIPTION: int = 1

    WIND_SCALE_MAP: list[tuple[float, str]] = [
        # 0: speed, 1: description
        (32.7, 'Hurricane force'),
        (28.5, 'Violent storm'),
        (24.5, 'Storm'),
        (20.8, 'Strong/severe gale'),
        (17.2, 'Gale'),
        (13.9, 'High wind'),
        (10.8, 'Strong breeze'),
        (8.0, 'Fresh breeze'),
        (5.5, 'Moderate breeze'),
        (3.4, 'Gentle breeze'),
        (1.6, 'Light breeze'),
        (0.5, 'Light air'),
        (0.0, 'Calm'),
    ]

    @classmethod
    def get_description(cls, speed: float) -> str:
        return next(
            ws[cls.WIND_SCALE_DESCRIPTION]
            for ws in cls.WIND_SCALE_MAP
            if speed >= ws[cls.WIND_SCALE_SPEED]
        )
