# Weather api

## Installation and usage

To run this project:

- first clone the `.env.example` file and fill the required variables.
- Run `docker-compose up --build`
- Run migrations. See migrations section below
- Access the api through [localhost:8000](http://localhost:8000)

### Migrations

In order to run migrations:

Attach a terminal to the container and run alembic upgrade

```bash
docker container list
docker exec -it <container name> bash

alembic upgrade head
```

### Testing

To run test attach a terminal to the container:

```bash
docker container list
docker exec -it <container name> bash
```

then run:

```bash
pytest -vs

# coverage
coverage --branch -m pytest -vs
coverage html
```

### To run the api container

```bash
docker run -ti \
    --network weather_api_default \
    --net-alias api \
    -p 8000:8000 \
    -v /${PWD}/src:/usr/src \
    -e "environment=development" \
    weather_api_api
```
