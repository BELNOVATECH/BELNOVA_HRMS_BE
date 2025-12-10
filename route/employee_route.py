# route/employee_route.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.employee_schema import EmployeeCreate, EmployeeRead
from services.employee_service import create_employee_service, get_employees_service

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeRead)
def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee_service(payload, db)

@router.get("/", response_model=list[EmployeeRead])
def get_employees(db: Session = Depends(get_db)):
    return get_employees_service(db)
