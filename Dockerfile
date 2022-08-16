FROM python:3.10.6-bullseye

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.1.14

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR app

