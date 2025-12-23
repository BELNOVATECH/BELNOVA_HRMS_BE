from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import text

from models.designation_model import Designation
from schemas.designation_schema import DesignationCreate


def create_designation_service(payload: DesignationCreate, db: Session):

    # ✅ Validate department WITHOUT touching department code
    dept_exists = db.execute(
        text("""
            SELECT 1
            FROM master_department
            WHERE id = :dept_id
              AND is_active = true
        """),
        {"dept_id": payload.dept_id}
    ).first()

    if not dept_exists:
        raise HTTPException(
            status_code=400,
            detail="Invalid or inactive department"
        )

    # ✅ Prevent duplicates
    exists = db.query(Designation).filter(
        Designation.designation_name == payload.designation_name,
        Designation.dept_id == payload.dept_id
    ).first()

    if exists:
        raise HTTPException(
            status_code=400,
            detail="Designation already exists for this department"
        )

    designation = Designation(
        designation_name=payload.designation_name,
        dept_id=payload.dept_id
    )

    db.add(designation)
    db.commit()
    db.refresh(designation)

    return designation


def get_designations_service(db: Session):
    return db.query(Designation).all()


def update_designation_status_service(
    designation_id: int,
    is_active: bool,
    db: Session
):
    designation = db.query(Designation).filter(
        Designation.id == designation_id
    ).first()

    if not designation:
        raise HTTPException(404, "Designation not found")

    designation.is_active = is_active
    db.commit()
    db.refresh(designation)

    return designation
