from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.task_schema import TaskCreate
from controller.task_controller import (
    create_task_controller,
    get_all_tasks_controller,
    get_task_by_id_controller
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/create")
def create_task(
    payload: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task_controller(payload, db)


@router.get("/")
def get_all_tasks(
    db: Session = Depends(get_db)
):
    return get_all_tasks_controller(db)


@router.get("/{task_id}")
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    return get_task_by_id_controller(task_id, db)