from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.master_role_model import MasterRole


def create_role_service(payload, db: Session):
    exists = db.query(MasterRole).filter(
        MasterRole.role_name == payload.role_name,
        MasterRole.is_active == True
    ).first()

    if exists:
        raise HTTPException(status_code=400, detail="Role already exists")

    role = MasterRole(
        role_name=payload.role_name,
        is_active=True
    )

    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_roles_service(db: Session):
    return db.query(MasterRole).filter(
        MasterRole.is_active == True
    ).order_by(
        MasterRole.id.desc()   # latest first
    ).all()


def update_role_service(db: Session, role_id: int, payload):
    role = db.query(MasterRole).filter(
        MasterRole.id == role_id
    ).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    if payload.is_active is not None:
        role.is_active = payload.is_active

    db.commit()
    db.refresh(role)
    return role


