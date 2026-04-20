from pydantic import BaseModel, Field
from pydantic import ConfigDict
from typing import Optional


class TaskCreate(BaseModel):
    """Валидация входящих данных от клиента"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1024)
    status: str = Field(default="new")

class TaskResponse(BaseModel):
    """Схема для ответа клиенту"""
    id: int
    title: str
    description: Optional[str] = None
    status: str

    model_config = ConfigDict(from_attributes=True)