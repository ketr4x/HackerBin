from fastapi import FastAPI
from sqlmodel import Session, select
from database import create_db, get_session

app = FastAPI()
create_db()


@app.post("/test")
async def test():
    return {"message": "Server is up"}


