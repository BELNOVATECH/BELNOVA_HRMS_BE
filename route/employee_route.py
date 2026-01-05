from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeRead,
    EmployeeStatusUpdate,
    EmployeeStatusResponse
)

from services.employee_service import (
    create_employee_service,
    get_employees_service,
    update_employee_status_service
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeRead)
def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee_service(payload, db)


@router.get("/", response_model=list[EmployeeRead])
def get_employees(db: Session = Depends(get_db)):
    return get_employees_service(db)


@router.put("/{emp_id}/status", response_model=EmployeeStatusResponse)
def update_employee_status(
    emp_id: int,
    payload: EmployeeStatusUpdate,
    db: Session = Depends(get_db)
):
    employee = update_employee_status_service(
        emp_id=emp_id,
        is_active=payload.is_active,
        db=db
    )

    return {
        "emp_id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "is_active": employee.is_active
    }
