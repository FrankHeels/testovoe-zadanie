from typing import Optional
from models.task import Task

_tasks: list[Task] = []
_id_counter: int = 0

def get_all_tasks() -> list[Task]:
    return _tasks

def get_task_by_id(task_id: int) -> Optional[Task]:
    for task in _tasks:
        if task.id == task_id:
            return task
        
def save_task(task: Task) -> Task:
    global _id_counter
    _id_counter += 1
    task.id = _id_counter
    _tasks.append(task)
    return task

