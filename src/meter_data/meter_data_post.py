import json
from src.models.meter_data_model import MeterData
from src.routers.meter_router import logger
from fastapi import APIRouter
from src.utils.db_connection import conn

meter_post_router = APIRouter()


@meter_post_router.post('/meter/')
async def post_meter_data(meter_data:MeterData):

        logger.info(f"Received POST request for meter_data")

        json_data = meter_data.model_dump_json()
        data = json.loads(json_data)
        data = tuple(data.values())

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"INSERT INTO meter VALUES{data}")
                con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Request {meter_data.business_partner_id} created successfully"}}

