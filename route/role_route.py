from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from controller.role_controller import (
    create_role_controller,
    get_roles_controller,
    update_role_controller,
)

from schemas.role_schema import (
    RoleCreate,
    RoleUpdate,
    RoleRead
)


role_router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@role_router.post("/", response_model=RoleRead)
def create_role(payload: RoleCreate, db: Session = Depends(get_db)):
    return create_role_controller(payload, db)


@role_router.get("/", response_model=List[RoleRead])
def get_roles(db: Session = Depends(get_db)):
    return get_roles_controller(db)


@role_router.put("/{role_id}", response_model=RoleRead)
def update_role(
    role_id: int,
    payload: RoleUpdate,
    db: Session = Depends(get_db)
):
    return update_role_controller(db, role_id, payload)



