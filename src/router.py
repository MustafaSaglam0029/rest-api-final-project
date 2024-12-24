from fastapi import APIRouter

from src.routers.mandate_data_routers import mandate_data_router
from src.routers.meter_data_routers import meter_data_router
from src.routers.meter_readings_routers import meter_readings_router

api_router = APIRouter()

api_router.include_router(mandate_data_router)
api_router.include_router(meter_data_router)
api_router.include_router(meter_readings_router)