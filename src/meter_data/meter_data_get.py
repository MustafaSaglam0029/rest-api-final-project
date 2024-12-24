from fastapi import FastAPI
from src.utils.db_connection import conn


app = FastAPI()

@app.get("/meter/")
async def get_meter_data(business_partner_id: str | None = None, connection_ean_code: str | None = None ):
    try:
        con = conn()
        cur = con.cursor()

        if connection_ean_code is None:
            cur.execute(f"select * from meter where business_partner_id = '{business_partner_id}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        elif business_partner_id is None:
            cur.execute(f"select * from meter where connection_ean_code = '{connection_ean_code}'")
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            rows = [dict(zip(column_names, row)) for row in rows]
            return rows

        else:
            cur.execute(f"select * from meter where business_partner_id = '{business_partner_id}' and connection_ean_code = '{connection_ean_code}'")
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