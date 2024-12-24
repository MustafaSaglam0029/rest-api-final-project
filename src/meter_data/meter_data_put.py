from src.utils.get_status import get_status
from src.models.meter_data_model import IncomingMeterData
from src.routers.meter_router import logger
from fastapi import APIRouter
from src.utils.db_connection import conn

meter_put_router = APIRouter()


@meter_put_router.put('/meter/{business_partner_id}')
async def put_meter_data(business_partner_id:str, incoming_data:IncomingMeterData):

        logger.info(f"Received PUT request for meter {business_partner_id}")

        json_data = incoming_data.model_dump_json()
        status = get_status(json_data)

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"UPDATE meter SET smart_collectable = '{status}' WHERE business_partner_id = '{business_partner_id}' ")
                con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Request for {business_partner_id} commited successfully"}}

