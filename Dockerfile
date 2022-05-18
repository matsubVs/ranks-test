FROM python:3.10.4-bullseye
LABEL maintainer="matsubus@mail.ru"

RUN pip install poetry

WORKDIR /app/

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root
COPY . /app/

EXPOSE 8000
