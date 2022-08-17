from fastapi import APIRouter
from .calculations import router as calculation_router

router = APIRouter()
router.include_router(calculation_router)
