# main.py
import uuid

from fastapi import FastAPI, Request
from app.schemas import STaskAdd, STask

tasks = []

app = FastAPI()


@app.post("/tasks", response_model=STask)
async def add_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict