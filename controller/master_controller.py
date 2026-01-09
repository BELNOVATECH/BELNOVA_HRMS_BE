from sqlalchemy.orm import Session
from services.master_service import *
from schemas.master_schema import MasterScreenPermissionUpdate


def get_all_modules_controller(db: Session):
    return get_all_modules_service(db)


def get_all_screens_controller(db: Session):
    return get_all_screens_service(db)


def get_all_permissions_controller(db: Session):
    return get_all_permissions_service(db)


def create_permission_controller(data, db: Session):
    return create_permission_service(data, db)


# ---------- UPDATE PERMISSION ----------
def update_permission_controller(
    permission_id: int,
    data: MasterScreenPermissionUpdate,
    db: Session
):
    return update_permission_service(permission_id, data, db)
