from src.routers.meter_router import logger
from fastapi import APIRouter
from src.utils.db_connection import conn

meter_del_router = APIRouter()


@meter_del_router.delete('/meter/{business_partner_id}')
async def delete_meter_data(business_partner_id:str):

        logger.info(f"Received DELETE request for meter {business_partner_id}")

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"DELETE FROM meter WHERE business_partner_id = '{business_partner_id}' ")
                con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Record for {business_partner_id} is deleted successfully"}}
