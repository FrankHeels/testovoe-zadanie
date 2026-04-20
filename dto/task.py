from pydantic import BaseModel, Field
from pydantic import ConfigDict
from typing import Optional

from models.task import TaskStatus


class TaskCreate(BaseModel):
    """Валидация входящих данных от клиента"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1024)
    status: TaskStatus = Field(default=TaskStatus.new)

class TaskResponse(BaseModel):
    """Схема для ответа клиенту"""
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus

    model_config = ConfigDict(from_attributes=True)