from fastapi import FastAPI

from app.config import get_settings
from app.dependencies.db import ConnectionFactory
from app.api.v1 import router as v1_router

app = FastAPI()
app.include_router(v1_router, prefix='/api/v1')


@app.on_event('startup')
def startup():
    ConnectionFactory.initialize(get_settings().db_uri)
