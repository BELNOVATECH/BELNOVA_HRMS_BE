from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.department_schema import (
    DepartmentCreateRequest,
    DepartmentResponse,
    IsActiveUpdate
)

from controller.department import (
    create_department_controller,
    get_departments_controller,
    get_department_by_id_controller,
    update_department_status_controller
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post(
    "/",
    response_model=DepartmentResponse
)
def create_department(
    payload: DepartmentCreateRequest,
    db: Session = Depends(get_db)
):
    return create_department_controller(
        payload,
        db
    )


@router.get(
    "/",
    response_model=list[DepartmentResponse]
)
def get_departments(
    db: Session = Depends(get_db)
):
    return get_departments_controller(
        db
    )


@router.get(
    "/{dept_id}",
    response_model=DepartmentResponse
)
def get_department(
    dept_id: int,
    db: Session = Depends(get_db)
):
    return get_department_by_id_controller(
        dept_id,
        db
    )


@router.put(
    "/{dept_id}/status",
    response_model=DepartmentResponse
)
def update_department_status(
    dept_id: int,
    payload: IsActiveUpdate,
    db: Session = Depends(get_db)
):
    return update_department_status_controller(
        dept_id,
        payload,
        db
    )