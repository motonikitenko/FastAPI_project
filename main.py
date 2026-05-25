# main.py
from fastapi import FastAPI
from rousers.task import router as task_router
from models.tasks import TasksModel
from contextlib import asynccontextmanager
from database import engine
from models.tasks import TasksModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- КОД ПРИ СТАРТЕ ---
    # Мы обращаемся к движку и просим создать все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(TasksModel.metadata.create_all)

    print("База данных готова к работе")

    yield  # Разделяет старт и выключение

    # --- КОД ПРИ ВЫКЛЮЧЕНИИ ---
    print("Выключение сервера")



app = FastAPI(lifespan=lifespan)

app.include_router(task_router)

