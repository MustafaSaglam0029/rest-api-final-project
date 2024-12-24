from fastapi import APIRouter
from src.routers.meter_readings_router import logger
from src.utils.db_connection import conn

readings_get_router = APIRouter()


@readings_get_router.get("/meter_readings/")
async def get_meter_readings_data(account_id: str | None = None, connection_ean_code: str | None = None ):

    logger.info(f"Received GET request for meter_readings_data")

    try:
        con = conn()
        cur = con.cursor()

        if connection_ean_code is None:
            cur.execute(f"select * from meter_readings where account_id = '{account_id}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        elif account_id is None:
            cur.execute(f"select * from meter_readings where connection_ean_code = '{connection_ean_code}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        else:
            cur.execute(f"select * from meter_readings where account_id = '{account_id}' and connection_ean_code = '{connection_ean_code}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()

    return {"status_code": 200,
            "body": {"message": f"Row is showed successfully"}}

