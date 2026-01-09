from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from fastapi import HTTPException

from models.employee_model import Employee
from models.employee_family_member_model import EmployeeFamilyMember
from schemas.employee_schema import EmployeeCreate


def create_employee_service(payload: EmployeeCreate, db: Session):
    emp = Employee(**payload.dict(exclude={"family_member"}))
    db.add(emp)
    db.commit()
    db.refresh(emp)

    family = EmployeeFamilyMember(
        emp_id=emp.id,
        **payload.family_member.dict()
    )
    db.add(family)
    db.commit()

    db.refresh(emp)
    return emp


def get_employees_service(db: Session):
    return (
        db.query(Employee)
        .options(joinedload(Employee.family_members))
        .all()
    )


# ✅ NEW: GET EMPLOYEE BY ID
def get_employee_by_id_service(emp_id: int, db: Session):
    emp = (
        db.query(Employee)
        .options(joinedload(Employee.family_members))
        .filter(Employee.id == emp_id)
        .first()
    )

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return emp


def update_employee_status_service(emp_id: int, is_active: bool, db: Session):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.is_active = is_active
    emp.modified_date = datetime.utcnow()
    db.commit()
    db.refresh(emp)
    return emp
