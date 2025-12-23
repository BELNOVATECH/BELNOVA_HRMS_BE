from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.department_schema import (
    DepartmentCreateRequest,
    DepartmentResponse,
    IsActiveUpdate
)
from services.department_service import (
    create_department,
    get_departments,
    update_department_status
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post("/", response_model=DepartmentResponse)
def create_department_api(
    payload: DepartmentCreateRequest,
    db: Session = Depends(get_db)
):
    return create_department(payload, db)


@router.get("/", response_model=list[DepartmentResponse])
def get_departments_api(
    db: Session = Depends(get_db)
):
    return get_departments(db)


@router.put("/{dept_id}/status", response_model=DepartmentResponse)
def update_department_status_api(
    dept_id: int,
    payload: IsActiveUpdate,
    db: Session = Depends(get_db)
):
    return update_department_status(dept_id, payload, db)
