from fastapi import APIRouter, Depends

from services.task_service import TaskService
from dto.task import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks")


def get_task_service() -> TaskService:
    return TaskService()


@router.post("/", response_model=TaskResponse)
def create_task(
    task_create: TaskCreate, 
    task_service: TaskService = Depends(get_task_service)
    ):
    return task_service.create_task(task_create)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.get_all_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int, 
    task_service: TaskService = Depends(get_task_service)
    ):
    return task_service.get_task_by_id(task_id)