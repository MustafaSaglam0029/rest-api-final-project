from fastapi import APIRouter
from src.routers.mandate_router import logger
from src.utils.db_connection import conn

mandate_get_router = APIRouter()


@mandate_get_router.get("/mandate/")
async def get_mandate_data(business_partner_id: str | None = None, mandate_id: str | None = None ):

    logger.info(f"Received GET request for meter_data")

    try:
        con = conn()
        cur = con.cursor()

        if mandate_id is None:
            cur.execute(f"select * from mandate where business_partner_id = '{business_partner_id}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        elif business_partner_id is None:
            cur.execute(f"select * from mandate where mandate_id = '{mandate_id}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        else:
            cur.execute(f"select * from mandate where business_partner_id = '{business_partner_id}' and mandate_id = '{mandate_id}'")
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
            "body": {"message": f" Row is showed successfully"}}



