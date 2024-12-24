from fastapi import FastAPI
from src.models.meter_data_model import IncomingMeterData
from src.utils.db_connection import conn
from src.utils.get_status import get_status

app = FastAPI()

@app.put('/meter/{business_partner_id}')
async def put_meter_data(business_partner_id:str, incoming_data:IncomingMeterData):

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
                "body": {"message": f"Request is commited successfully"}}

