from typing import List
from fastapi import APIRouter, status, HTTPException
from schemas.task import STaskAdd, STask
from database import SessionDep
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Задачи"])

@router.get("", response_model=List[STask])
async def get_tasks(session: SessionDep):
    return await TaskRepository.get_all(session=session)


@router.get("/{task_id}", response_model=STask)
async def get_task(task_id: int, session: SessionDep):
    task = await TaskRepository.get_one(session=session, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена")
    return task

@router.post("", response_model=STask)
async def add_task(task: STaskAdd, session: SessionDep):
    return await TaskRepository.add_one(task=task, session=session)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def del_task(task_id: int, session: SessionDep):
    if await TaskRepository.del_one(task_id=task_id, session=session) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена")

