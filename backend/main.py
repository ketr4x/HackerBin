from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import create_db, get_session

app = FastAPI()
create_db()


@app.post("/test")
async def test():
    return {"message": "Server is up"}


@app.post("/api/user/create")
async def create_user(session: Session = Depends(get_session)):
