from src.utils.get_status import get_status
from src.models.mandate_data_model import IncomingMandateData
from fastapi import APIRouter
from src.routers.mandate_router import logger
from src.utils.db_connection import conn

mandate_put_router = APIRouter()


@mandate_put_router.put('/mandate/{business_partner_id}')
async def put_mandate_data(business_partner_id:str, incoming_data:IncomingMandateData):

        logger.info(f"Received PUT request for mandate {business_partner_id}")

        json_data = incoming_data.model_dump_json()
        status = get_status(json_data)

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"UPDATE mandate SET mandate_status = '{status}' WHERE business_partner_id = '{business_partner_id}' ")
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



