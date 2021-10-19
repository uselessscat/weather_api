# Weather api

## Installation and usage

To run the api container:

```bash
docker run -ti \
    --network weather_api_default \
    --net-alias api \
    -p 8000:8000 \
    -v /${PWD}/src:/usr/src \
    -e "environment=development" \
    weather_api_api
```
