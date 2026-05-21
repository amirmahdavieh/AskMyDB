from database import connect
from agents import function_tool

@function_tool
def execute_sql(query: str)-> str:
    con, cur = connect()
    try:
        cur.execute(query)
        rows = cur.fetchall()

        result = [dict(row) for row in rows]

        return str(result)

    except Exception as e:
        return f"SQL_ERROR: {e}"

    finally:
        con.close()
