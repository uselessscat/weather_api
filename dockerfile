FROM python:3.9

WORKDIR /usr/src

# if the poetry.lock does not exist, dont fail
COPY src/poetry.loc[k] src/pyproject.toml ./

# Install deps
RUN pip install 'poetry~=1.1.7' \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy source code
COPY ./src .

EXPOSE 8080

CMD hypercorn -w 4 -k uvloop -b 0.0.0.0:8000 weather.main:app
