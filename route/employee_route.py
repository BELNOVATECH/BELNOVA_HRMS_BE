from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeCreateResponse,
    EmployeeStatusUpdate,
    EmployeeStatusResponse
)
from services.employee_service import (
    create_employee_service,
    get_employees_service,
    get_employee_by_id_service,
    update_employee_status_service
)

router = APIRouter(prefix="/employees", tags=["Employees"])


# ============================================================
# CREATE EMPLOYEE (User + Employee + Family Members)
# ============================================================
@router.post("/employee", response_model=EmployeeCreateResponse)
def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    emp = create_employee_service(payload, db)

    return {
        **emp.__dict__,
        "family_member": emp.family_members   # 🔥 now returns list
    }


# ============================================================
# GET ALL EMPLOYEES
# ============================================================
@router.get("/", response_model=list[EmployeeCreateResponse])
def get_employees(db: Session = Depends(get_db)):
    employees = get_employees_service(db)

    return [
        {
            **emp.__dict__,
            "family_member": emp.family_members
        }
        for emp in employees
    ]


# ============================================================
# GET EMPLOYEE BY ID
# ============================================================
@router.get("/{emp_id}", response_model=EmployeeCreateResponse)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    emp = get_employee_by_id_service(emp_id, db)

    return {
        **emp.__dict__,
        "family_member": emp.family_members
    }


# ============================================================
# ACTIVATE / DEACTIVATE EMPLOYEE
# ============================================================
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
