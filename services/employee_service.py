from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from models.employee_model import Employee
from schemas.employee_schema import EmployeeCreate


def create_employee_service(payload: EmployeeCreate, db: Session) -> Employee:
    """
    Create a new employee
    """

    # 🔁 Check duplicate emp_code (business rule)
    if payload.emp_code:
        exists = (
            db.query(Employee)
            .filter(Employee.emp_code == payload.emp_code)
            .first()
        )
        if exists:
            raise HTTPException(
                status_code=400,
                detail=f"Employee with emp_code '{payload.emp_code}' already exists"
            )

    try:
        new_employee = Employee(
            **payload.dict(exclude_none=True)
        )

        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)

        return new_employee

    except IntegrityError as e:
        db.rollback()

        # 🔥 Log REAL PostgreSQL error (for debugging)
        print("\n🔥 DATABASE ERROR:")
        print(str(e.orig))
        print("--------------------------------\n")

        raise HTTPException(
            status_code=400,
            detail="Employee creation failed due to database constraint"
        )


def get_employees_service(db: Session):
    """
    Fetch all employees
    """
    return db.query(Employee).all()
