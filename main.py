from fastapi import FastAPI
import uvicorn
from exceptions.handlers import task_not_found_handler
from exceptions.task_exceptions import TaskNotFoundException
from routers.tasks_router import router

app = FastAPI()
app.include_router(router)
app.add_exception_handler(TaskNotFoundException, task_not_found_handler)

@app.get("/")
def health_check():
    return {"message": "Hello, Health Check!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)