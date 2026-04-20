from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.task_exceptions import TaskNotFoundException

def task_not_found_handler(request: Request, exc: TaskNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Task not found",
            "detail": str(exc),
            "task_id": exc.task_id,
        }
    )