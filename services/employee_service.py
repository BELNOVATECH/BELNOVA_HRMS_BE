# services/employee_service.py

from sqlalchemy.orm import Session
from models.employee_model import Employee
from schemas.employee_schema import EmployeeCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def create_employee_service(payload: EmployeeCreate, db: Session) -> Employee:
    """
    Create a new employee and log real PostgreSQL errors if insertion fails.
    """

    # Check duplicate emp_code
    if payload.emp_code:
        exists = db.query(Employee).filter(Employee.emp_code == payload.emp_code).first()
        if exists:
            raise HTTPException(
                status_code=400,
                detail=f"Employee with emp_code {payload.emp_code} already exists"
            )

    try:
        new_emp = Employee(**payload.dict(exclude_none=True))
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        return new_emp

    except IntegrityError as e:
        db.rollback()

        # 🔥 PRINT REAL DB ERROR
        print("\n\n🔥 REAL DATABASE ERROR (POSTGRES SAYS):")
        print(str(e.orig))
        print("--------------------------------------------------\n\n")

        raise HTTPException(status_code=400, detail="Database integrity error")


def get_employees_service(db: Session):
    """
    Fetch all employees
    """
    return db.query(Employee).all()
