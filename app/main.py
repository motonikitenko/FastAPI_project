# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
class User(BaseModel):
    username: str
    message: str

@app.post("/")
async def root(user :User):
    return user