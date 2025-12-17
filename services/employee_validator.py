from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.employee_model import Employee


def validate_employee(emp_id: int, db: Session) -> Employee:
    """
    Validate employee exists and is active
    (Used by Leave Management & other services)
    """

    employee = (
        db.query(Employee)
        .filter(
            Employee.id == emp_id,
            Employee.is_active == True
        )
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=403,
            detail="Employee not registered or inactive"
        )

    return employee
