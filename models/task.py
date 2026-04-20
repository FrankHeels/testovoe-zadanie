from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    status: str
    description: Optional[str] = None