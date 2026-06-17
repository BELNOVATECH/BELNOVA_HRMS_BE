from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.generated_models import MasterDepartment


def create_department_service(payload, db: Session):

    exists = db.query(MasterDepartment).filter(
        MasterDepartment.department.ilike(payload.department)
    ).first()

    if exists:
        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )

    department = MasterDepartment(
        department=payload.department,
        is_active=True
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department


def get_departments_service(db: Session):
    return db.query(
        MasterDepartment
    ).order_by(
        MasterDepartment.id
    ).all()


def get_department_by_id_service(
    dept_id: int,
    db: Session
):
    department = db.query(
        MasterDepartment
    ).filter(
        MasterDepartment.id == dept_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


def update_department_status_service(
    dept_id: int,
    payload,
    db: Session
):
    department = get_department_by_id_service(
        dept_id,
        db
    )

    department.is_active = payload.is_active

    db.commit()
    db.refresh(department)

    return department