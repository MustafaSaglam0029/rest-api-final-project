import json
from src.models.mandate_data_model import MandateData
from fastapi import APIRouter
from src.routers.mandate_router import logger
from src.utils.db_connection import conn

mandate_post_router = APIRouter()


@mandate_post_router.post('/mandate/')
async def post_mandate_data(mandate_data:MandateData):

        logger.info(f"Received POST request for mandate_data")

        json_data = mandate_data.model_dump_json()
        data = json.loads(json_data)
        data = tuple(data.values())

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"INSERT INTO mandate VALUES{data}")
                con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Record for {mandate_data.business_partner_id} is created successfully"}}

