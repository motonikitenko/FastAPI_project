from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.tasks import TasksModel
from schemas.task import STaskAdd

class TaskRepository:
    @classmethod
    async def get_one(cls, session: AsyncSession, task_id: int):
        query = select(TasksModel).where(TasksModel.id == task_id)
        res = await session.execute(query)
        return res.scalar_one_or_none()

    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(TasksModel)
        res = await session.execute(query)
        return res.scalars().all()

    @classmethod
    async def add_one(cls, session: AsyncSession, task: STaskAdd):
        new_task = TasksModel(**task.model_dump())
        session.add(new_task)
        await session.commit()
        await session.refresh(new_task)
        return new_task

    @classmethod
    async def del_one(cls, session: AsyncSession, task_id: int):
        task = await cls.get_one(session, task_id)
        if task is not None:
            await session.delete(task)
            await session.commit()
            return task_id
        return None