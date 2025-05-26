# nl2sql_app/main.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/nl2sql")
async def convert_to_sql(request: Request):
    data = await request.json()
    nl_query = data.get("query")
    return {"sql": f"SELECT * FROM table WHERE field = '{nl_query}'"}