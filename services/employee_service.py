from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

from models.employee_model import Employee
from models.employee_family_member_model import EmployeeFamilyMember
from schemas.employee_schema import EmployeeCreate


def create_employee_service(payload: EmployeeCreate, db: Session) -> Employee:
    """
    Create employee and (optional) single family member
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
            exclude={"family_member"},
            exclude_none=True
        )

        employee = Employee(**employee_data)
        db.add(employee)
        db.commit()
        db.refresh(employee)

        # -------------------------------------------------
        # CREATE FAMILY MEMBER (ONLY ONE)
        # -------------------------------------------------
        if payload.family_member:
            family = EmployeeFamilyMember(
                emp_id=employee.id,
                relation_id=payload.family_member.relation_id,
                first_name=payload.family_member.first_name,
                last_name=payload.family_member.last_name,
                date_of_birth=payload.family_member.date_of_birth,
                occupation_id=payload.family_member.occupation_id,
                phone=payload.family_member.phone,
                email=payload.family_member.email,
                present_address=payload.family_member.present_address,
                permanent_address=payload.family_member.permanent_address,
                bank_account=payload.family_member.bank_account,
                ifsc_code=payload.family_member.ifsc_code,
                pan=payload.family_member.pan,
                aadhar=payload.family_member.aadhar,
                created_by=payload.created_by,
                created_date=datetime.utcnow(),
                is_active=True
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
    return db.query(Employee).order_by(Employee.id.desc()).all()


def update_employee_status_service(
    emp_id: int,
    is_active: bool,
    db: Session
) -> Employee:

    employee = db.query(Employee).filter(Employee.id == emp_id).first()

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
