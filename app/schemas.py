from pydantic import BaseModel, Field

class STaskBase(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Название задачи")
    description: str | None = Field(None, max_length=300)
    priority: int = Field(1, le=5)
class STaskAdd(STaskBase):
    pass
class STask(STaskBase):
    id: int