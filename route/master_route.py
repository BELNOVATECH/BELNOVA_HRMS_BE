from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from schemas.master_schema import (
    MasterModuleResponse,
    MasterScreenResponse,
    MasterScreenPermissionResponse,
    MasterScreenPermissionCreate,
    MasterScreenPermissionBulkUpdate,
)

from controller.master_controller import *

router = APIRouter(prefix="/master", tags=["Access Management"])

# ---------- MODULE ----------
@router.get("/modules/", response_model=List[MasterModuleResponse])
def get_modules(db: Session = Depends(get_db)):
    return get_all_modules_controller(db)

# ---------- SCREEN ----------
@router.get("/screens/", response_model=List[MasterScreenResponse])
def get_screens(db: Session = Depends(get_db)):
    return get_all_screens_controller(db)

# ---------- PERMISSION ----------
@router.get("/permissions/", response_model=List[MasterScreenPermissionResponse])
def get_permissions(db: Session = Depends(get_db)):
    return get_all_permissions_controller(db)

# ---------- BULK CREATE ----------
@router.post(
    "/permissions/bulk/",
    response_model=List[MasterScreenPermissionResponse]
)
def create_bulk_permissions(
    data: List[MasterScreenPermissionCreate],
    db: Session = Depends(get_db)
):
    return create_bulk_permission_controller(data, db)

# ---------- BULK UPDATE ----------
@router.put(
    "/permissions/bulk/",
    response_model=List[MasterScreenPermissionResponse]
)
def bulk_update_permissions(
    data: List[MasterScreenPermissionBulkUpdate],
    db: Session = Depends(get_db)
):
    return bulk_update_permission_controller(data, db)
