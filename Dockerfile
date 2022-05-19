FROM --platform=linux/amd64 python:3.10.4-bullseye
LABEL maintainer="matsubus@mail.ru"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /ranks/
COPY poetry.lock pyproject.toml /ranks/
RUN poetry install --no-root
RUN poetry run python manage.py migrate
COPY . /ranks/

