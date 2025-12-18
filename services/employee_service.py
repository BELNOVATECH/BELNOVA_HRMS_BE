from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from models.employee_model import Employee
from schemas.employee_schema import EmployeeCreate


def create_employee_service(payload: EmployeeCreate, db: Session):
    # Check duplicate emp_code
    if payload.emp_code:
        exists = db.query(Employee).filter(
            Employee.emp_code == payload.emp_code
        ).first()
        if exists:
            raise HTTPException(
                status_code=400,
                detail="Employee with this emp_code already exists"
            )

    try:
        employee = Employee(**payload.dict(exclude_none=True))
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    except IntegrityError as e:
        db.rollback()
        print("🔥 DB ERROR:", e.orig)
        raise HTTPException(
            status_code=400,
            detail="Employee creation failed"
        )


def get_employees_service(db: Session):
    """
    Fetch all employees
    """
    return db.query(Employee).order_by(Employee.id.desc()).all()
