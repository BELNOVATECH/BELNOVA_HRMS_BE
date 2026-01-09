from fastapi import APIRouter, Depends
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


# ✅ DELETE ACCESS
@router.delete("/permissions")
def delete_permission(
    role_id: int,
    module_id: int,
    screen_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return delete_permission_controller(
        role_id, module_id, screen_id, db
    )
