from fastapi import FastAPI, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
# from database import engine, Base
from typing import Annotated
from sqlalchemy.orm import Session
from app.database import session

app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def root():
    return {"Hello": "Relationship Family"} 

@app.post("/posts")
def create_post(payload: Post):
    print(payload.dict())
    return {"Hello": "Relationship Family"} 

@app.get("/posts")
def get_posts():
    return {"Hello": "Relationship Family"} 
