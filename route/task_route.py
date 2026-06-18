from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.task_schema import TaskCreate, MasterTaskTypeResponse, MasterProjectResponse
from controller.task_controller import (
    create_task_controller,
    get_all_tasks_controller,
    get_task_by_id_controller,
    get_all_task_types_service,
    get_task_type_by_id_service,
    get_all_projects_service,
    get_project_by_id_service
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

@router.get(
    "/task-types",
    response_model=list[MasterTaskTypeResponse]
)
def get_task_types(db: Session = Depends(get_db)):
    return get_all_task_types_service(db)


@router.get(
    "/task-types/{task_type_id}",
    response_model=MasterTaskTypeResponse
)
def get_task_type(task_type_id: int, db: Session = Depends(get_db)):
    task_type = get_task_type_by_id_service(db)

    if not task_type:
        raise HTTPException(
            status_code=404,
            detail="Task Type not found"
        )

    return task_type


# ---------------- Projects ----------------

@router.get(
    "/projects",
    response_model=list[MasterProjectResponse]
)
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects_service(db)


@router.get(
    "/projects/{project_id}",
    response_model=MasterProjectResponse
)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id_service(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

@router.get("/{task_id}")
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    return get_task_by_id_controller(task_id, db)


@router.get(
    "/task-types",
    response_model=list[MasterTaskTypeResponse]
)
def get_task_types(db: Session = Depends(get_db)):
    return get_all_task_types_service(db)


@router.get(
    "/task-types/{task_type_id}",
    response_model=MasterTaskTypeResponse
)
def get_task_type(task_type_id: int, db: Session = Depends(get_db)):
    task_type = get_task_type_by_id_service(db)

    if not task_type:
        raise HTTPException(
            status_code=404,
            detail="Task Type not found"
        )

    return task_type


# ---------------- Projects ----------------

@router.get(
    "/projects",
    response_model=list[MasterProjectResponse]
)
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects_service(db)


@router.get(
    "/projects/{project_id}",
    response_model=MasterProjectResponse
)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id_service(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project