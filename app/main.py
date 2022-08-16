from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.config import get_settings
from app.dependencies.db import ConnectionFactory
from app.domain.calculation import MathError
from app.api.v1 import router as v1_router

app = FastAPI()
app.include_router(v1_router, prefix='/api/v1')


@app.exception_handler(MathError)
def math_error_handler(_: Request, exc: MathError):
    return JSONResponse(
        status_code=422,
        content={
            'detail':    {
                "loc": [
                    "string",
                    0
                ],
                "msg": exc.detailed,
                "type": "math_error"
            }
        }
    )


@app.on_event('startup')
def startup():
    ConnectionFactory.initialize(get_settings().db_uri)
