import json
from psycopg2.extras import Json
from src.models.meter_readings_model import MeterReadings
from fastapi import APIRouter
from src.utils.db_connection import conn
from src.routers.meter_readings_router import logger

readings_post_router = APIRouter()


@readings_post_router.post('/meter_readings/')
async def post_meter_readings_data(meter_readings_data:MeterReadings):

        logger.info(f"Received POST request for meter_readings_data")

        json_data = meter_readings_data.model_dump_json()
        data = json.loads(json_data)
        data = [dict(data)]

        insert_sgl = """
        INSERT INTO meter_readings (account_id, brand, connection_ean_code, energy_type, meter_number,
                           reading_date, reading_electricity, reading_gas, rejection,
                           validation_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        for record in data:

            reading_electricity = Json(record['reading_electricity']) if isinstance(record['reading_electricity'],dict) else record['reading_electricity']
            reading_gas = Json(record['reading_gas']) if isinstance(record['reading_gas'], dict) else record['reading_gas']
            rejection = Json(record['rejection']) if isinstance(record['rejection'], dict) else record['rejection']


        try:
            con = conn()
            cur = con.cursor()

            cur.execute(insert_sgl, (
                record['account_id'], record['brand'],
                record['connection_ean_code'], record['energy_type'], record['meter_number'],
                record['reading_date'], reading_electricity,
                reading_gas, rejection, record['validation_status']
            ))

            con.commit()

        except Exception as e:
                print(f"Error: {e}")

        finally:
                if cur:
                        cur.close()

                if con:
                        con.close()

        return {"status_code": 200,
                "body": {"message": f"Request {meter_readings_data.account_id} created successfully"}}



