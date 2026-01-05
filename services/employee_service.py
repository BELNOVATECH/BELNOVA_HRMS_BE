from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

from models.employee_model import Employee
from models.employee_family_member_model import EmployeeFamilyMember
from schemas.employee_schema import EmployeeCreate


def create_employee_service(payload: EmployeeCreate, db: Session) -> Employee:
    """
    Creates an employee and related family members in a single transaction
    """

    # -------------------------------------------------
    # CHECK DUPLICATE EMP CODE
    # -------------------------------------------------
    if payload.emp_code:
        exists = (
            db.query(Employee)
            .filter(Employee.emp_code == payload.emp_code)
            .first()
        )
        if exists:
            raise HTTPException(
                status_code=400,
                detail="Employee with this emp_code already exists"
            )

    try:
        # -------------------------------------------------
        # CREATE EMPLOYEE
        # -------------------------------------------------
        employee_data = payload.dict(
            exclude={"family_member"},   # ✅ CORRECT KEY
            exclude_none=True
        )

        employee = Employee(**employee_data)
        db.add(employee)
        db.commit()
        db.refresh(employee)

        # -------------------------------------------------
        # CREATE FAMILY MEMBERS
        # -------------------------------------------------
        for member in payload.family_member or []:
            family = EmployeeFamilyMember(
                emp_id=employee.id,
                created_by=payload.created_by,
                created_date=datetime.utcnow(),
                is_active=True,
                **member.dict()
            )
            db.add(family)

        db.commit()
        return employee

    except IntegrityError as e:
        db.rollback()
        print("🔥 DB ERROR:", e.orig)
        raise HTTPException(
            status_code=400,
            detail="Employee creation failed"
        )


def get_employees_service(db: Session):
    return (
        db.query(Employee)
        .order_by(Employee.id.desc())
        .all()
    )


def update_employee_status_service(
    emp_id: int,
    is_active: bool,
    db: Session
) -> Employee:

    employee = (
        db.query(Employee)
        .filter(Employee.id == emp_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.is_active = is_active
    employee.modified_date = datetime.utcnow()

    db.commit()
    db.refresh(employee)
    return employee
