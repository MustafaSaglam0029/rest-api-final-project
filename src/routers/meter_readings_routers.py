from fastapi import APIRouter
import logging

logger = logging.Logger("meter_readings-logger")

meter_readings_router = APIRouter()


@meter_readings_router.get('/meter_readings/')
async def get_meter_readings_data():
    logger.info(f"Received GET request for meter_readings_data")
    return {"body": {"message": "Showed successfully"}}

@meter_readings_router.post('/meter_readings/')
async def post_meter_readings_data():
    logger.info(f"Received POST request for meter_readings_data")
    return {"body": {"message": "Created successfully"}}

@meter_readings_router.put('/meter_readings/{account_id}')
async def put_meter_readings_data(account_id:str):
    logger.info(f"Received PUT request for meter_readings {account_id}")
    return {"body": {"message": "Record is updated successfully"}}

@meter_readings_router.delete('/meter_readings/{account_id}')
async def delete_meter_readings_data(account_id:str):
    logger.info(f"Received DELETE request for meter_readings {account_id}")
    return {"body": {"message": "Record is deleted successfully"}}