from fastapi import APIRouter
import logging

logger = logging.Logger("mandate-logger")

mandate_data_router = APIRouter()


@mandate_data_router.get('/mandate/')
async def get_mandate_data():
    logger.info(f"Received GET request for mandate_data")
    return {"body": {"message": "Showed successfully"}}

@mandate_data_router.post('/mandate/')
async def post_mandate_data():
    logger.info(f"Received POST request for mandate_data")
    return {"body": {"message": "Created successfully"}}

@mandate_data_router.put('/mandate/{business_partner_id}')
async def put_mandate_data(business_partner_id:str):
    logger.info(f"Received PUT request for mandate {business_partner_id}")
    return {"body": {"message": "Record is updated successfully"}}

@mandate_data_router.delete('/mandate/{business_partner_id}')
async def delete_mandate_data(business_partner_id:str):
    logger.info(f"Received DELETE request for mandate {business_partner_id}")
    return {"body": {"message": "Record is deleted successfully"}}


