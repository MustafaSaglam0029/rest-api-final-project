from fastapi import APIRouter
import logging

logger = logging.Logger("meter-logger")

meter_data_router = APIRouter()


@meter_data_router.get('/meter/')
async def get_meter_data():
    logger.info(f"Received GET request for meter_data")
    return {"body": {"message": "Showed successfully"}}

@meter_data_router.post('/meter/')
async def post_meter_data():
    logger.info(f"Received POST request for meter_data")
    return {"body": {"message": "Created successfully"}}

@meter_data_router.put('/meter/{business_partner_id}')
async def put_meter_data(business_partner_id:str):
    logger.info(f"Received PUT request for meter {business_partner_id}")
    return {"body": {"message": "Record is updated successfully"}}

@meter_data_router.delete('/meter/{business_partner_id}')
async def delete_meter_data(business_partner_id:str):
    logger.info(f"Received DELETE request for meter {business_partner_id}")
    return {"body": {"message": "Record is deleted successfully"}}