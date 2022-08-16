from fastapi import FastAPI

from app.config import get_settings
from app.dependencies.db import ConnectionFactory

app = FastAPI()


@app.on_event('startup')
def startup():
    ConnectionFactory.initialize(get_settings().db_uri)
