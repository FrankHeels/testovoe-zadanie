from dataclasses import dataclass
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    completed = "completed"

@dataclass
class Task:
    id: int
    title: str
    status: TaskStatus
    description: Optional[str] = None