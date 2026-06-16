from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.employee_schema import EmployeeCreate

from services.employee_service import (
    create_employee_service,
    get_all_employees_service,
    get_employee_by_id_service
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("")
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee_service(
        payload,
        db
    )


@router.get("")
def get_employees(
    db: Session = Depends(get_db)
):
    return get_all_employees_service(db)


@router.get("/{emp_id}")
def get_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return get_employee_by_id_service(
        emp_id,
        db
    )