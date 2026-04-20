from models.task import Task
from dto.task import TaskCreate, TaskResponse
import storage.memory as memory_storage
from exceptions.task_exceptions import TaskNotFoundException

class TaskService:
    def create_task(self, task_create: TaskCreate) -> TaskResponse:
        task = Task(
            id=0,
            title=task_create.title,
            description=task_create.description,    
            status=task_create.status
        )

        return memory_storage.save_task(task)
    
    def get_all_tasks(self) -> list[TaskResponse]:
        return memory_storage.get_all_tasks()
    
    def get_task_by_id(self, task_id: int) -> TaskResponse:
        task = memory_storage.get_task_by_id(task_id)
        if task is None:
            raise TaskNotFoundException(task_id)
        return task