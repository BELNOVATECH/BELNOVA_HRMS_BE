from sqlalchemy.orm import Session
from models.master_module import MasterModule
from models.master_screen import MasterScreen
from models.master_screen_permission import MasterScreenPermission
from schemas.master_schema import MasterScreenPermissionUpdate


# ---------- MODULE ----------
def get_all_modules_service(db: Session):
    return db.query(MasterModule).filter(MasterModule.is_active == True).all()


# ---------- SCREEN ----------
def get_all_screens_service(db: Session):
    return db.query(MasterScreen).filter(MasterScreen.is_active == True).all()


# ---------- PERMISSION ----------
def get_all_permissions_service(db: Session):
    return (
        db.query(MasterScreenPermission)
        .filter(MasterScreenPermission.is_active == True)
        .all()
    )


def create_permission_service(data, db: Session):
    permission = (
        db.query(MasterScreenPermission)
        .filter(
            MasterScreenPermission.role_id == data.role_id,
            MasterScreenPermission.module_id == data.module_id,
            MasterScreenPermission.screen_id == data.screen_id,
        )
        .first()
    )

    if permission:
        permission.is_active = True
        permission.can_access = data.can_access
        permission.can_view = data.can_view
        permission.can_edit = data.can_edit
        permission.can_delete = data.can_delete
        permission.can_update = data.can_update
    else:
        permission = MasterScreenPermission(**data.dict())
        db.add(permission)

    db.commit()
    db.refresh(permission)
    return permission


# ---------- UPDATE PERMISSION (NEW) ----------
def update_permission_service(
    permission_id: int,
    data: MasterScreenPermissionUpdate,
    db: Session
):
    permission = (
        db.query(MasterScreenPermission)
        .filter(MasterScreenPermission.id == permission_id)
        .first()
    )

    if not permission:
        return None

    permission.can_view = data.can_view
    permission.can_edit = data.can_edit
    permission.can_delete = data.can_delete
    permission.can_access = data.can_access
    permission.can_update = data.can_update
    permission.is_active = data.is_active

    db.commit()
    db.refresh(permission)
    return permission
