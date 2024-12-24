import uvicorn
from fastapi import FastAPI
from src.models.mandate_data_model import IncomingMandateData
from src.utils.db_connection import conn
from src.utils.get_status import get_status

app = FastAPI()


@app.put('/mandate/{business_partner_id}')
async def put_mandate_data(business_partner_id:str, incoming_data:IncomingMandateData):

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
                "body": {"message": f"Request is commited successfully"}}



uvicorn.run(app, port=8080)