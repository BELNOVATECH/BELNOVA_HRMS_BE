from fastapi import HTTPException

from services.task_service import (
    create_task_service,
    get_all_tasks_service,
    get_task_by_id_service
)


def create_task_controller(payload, db):
    return create_task_service(payload, db)


def get_all_tasks_controller(db):
    return get_all_tasks_service(db)


def get_task_by_id_controller(task_id, db):

    task = get_task_by_id_service(task_id, db)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task