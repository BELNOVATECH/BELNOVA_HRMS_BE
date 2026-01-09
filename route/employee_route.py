from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from models.employee_model import Employee
from models.employee_family_member_model import EmployeeFamilyMember

from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeCreateResponse,
    EmployeeStatusUpdate,
    EmployeeStatusResponse
)

from services.employee_service import (
    create_employee_service,
    get_employees_service,
    update_employee_status_service
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/", response_model=list[EmployeeCreateResponse])
def get_employees(db: Session = Depends(get_db)):
    employees = get_employees_service(db)

    result = []
    for emp in employees:
        result.append({
            **emp.__dict__,
            "family_member": emp.family_members[0] if emp.family_members else None
        })

    return result


@router.post("/employee", response_model=EmployeeCreateResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    emp = create_employee_service(employee, db)

    return {
        **emp.__dict__,
        "family_member": emp.family_members[0]
    }


@router.put("/{emp_id}/status", response_model=EmployeeStatusResponse)
def update_employee_status(
    emp_id: int,
    payload: EmployeeStatusUpdate,
    db: Session = Depends(get_db)
):
    emp = update_employee_status_service(emp_id, payload.is_active, db)
    return {
        "emp_id": emp.id,
        "first_name": emp.first_name,
        "last_name": emp.last_name,
        "is_active": emp.is_active
    }
