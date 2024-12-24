from fastapi import FastAPI
from src.utils.db_connection import conn

app = FastAPI()


@app.delete('/meter_readings/{account_id}')
async def delete_meter_readings_data(account_id:str):

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

