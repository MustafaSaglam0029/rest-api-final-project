from fastapi import APIRouter
from src.utils.db_connection import conn
from src.routers.meter_readings_router import logger

readings_del_router = APIRouter()


@readings_del_router.delete('/meter_readings/{account_id}')
async def delete_meter_readings_data(account_id:str):

        logger.info(f"Received DELETE request for meter_readings {account_id}")

        try:
                con = conn()
                cur = con.cursor()
                cur.execute(f"DELETE FROM meter_readings WHERE business_partner_id = '{account_id}' ")
                con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Record for {account_id} is deleted successfully"}}

