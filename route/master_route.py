from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.master_schema import *
from controller.master_controller import *

router = APIRouter(prefix="/master", tags=["Access Management"])


@router.get("/modules", response_model=list[MasterModuleResponse])
def get_modules(db: Session = Depends(get_db)):
    return get_all_modules_controller(db)


@router.get("/screens", response_model=list[MasterScreenResponse])
def get_screens(db: Session = Depends(get_db)):
    return get_all_screens_controller(db)


@router.get("/permissions", response_model=list[MasterScreenPermissionResponse])
def get_permissions(db: Session = Depends(get_db)):
    return get_all_permissions_controller(db)


@router.post("/permissions", response_model=MasterScreenPermissionResponse)
def create_permission(
    data: MasterScreenPermissionCreate,
    db: Session = Depends(get_db)
):
    return create_permission_controller(data, db)


# ---------- PUT PERMISSION (NEW) ----------
@router.put(
    "/permissions/{permission_id}",
    response_model=MasterScreenPermissionResponse
)
def update_permission(
    permission_id: int,
    data: MasterScreenPermissionUpdate,
    db: Session = Depends(get_db)
):
    permission = update_permission_controller(permission_id, data, db)

    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    return permission
