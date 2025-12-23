from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.department import Department
from schemas.department_schema import (
    DepartmentCreateRequest,
    IsActiveUpdate
)


def create_department(payload: DepartmentCreateRequest, db: Session):
    # Duplicate check
    exists = db.query(Department).filter(
        Department.department.ilike(payload.department)
    ).first()

    if exists:
        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )

    dept = Department(
        department=payload.department,
        is_active=True
    )

    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept


def get_departments(db: Session):
    return db.query(Department).order_by(Department.id).all()


def update_department_status(
    dept_id: int,
    payload: IsActiveUpdate,
    db: Session
):
    dept = db.query(Department).filter(
        Department.id == dept_id
    ).first()

    if not dept:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    dept.is_active = payload.is_active
    db.commit()
    db.refresh(dept)
    return dept
