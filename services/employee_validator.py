from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.generated_models import EmployeeRegistration


def validate_employee(emp_id: int, db: Session) -> EmployeeRegistration:
    """
    Validate employee exists and is active
    (Used by Leave Management & other services)
    """

    employee = (
        db.query(EmployeeRegistration)
        .filter(
            EmployeeRegistration.id == emp_id,
            EmployeeRegistration.is_active == True
        )
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=403,
            detail="Employee not registered or inactive"
        )

    return employee