from sqlalchemy.orm import Session
from models.master_module import MasterModule
from models.master_screen import MasterScreen
from models.master_screen_permission import MasterScreenPermission

# ---------- MODULE ----------
def get_all_modules_service(db: Session):
    return db.query(MasterModule).filter(
        MasterModule.is_active == True
    ).all()


# ---------- SCREEN ----------
def get_all_screens_service(db: Session):
    return db.query(MasterScreen).filter(
        MasterScreen.is_active == True
    ).all()


# ---------- PERMISSION ----------
def get_all_permissions_service(db: Session):
    return db.query(MasterScreenPermission).all()


# ---------- BULK CREATE ----------
def create_bulk_permission_service(data_list, db: Session):
    results = []

    for data in data_list:
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
            permission.can_view = data.can_view
            permission.can_edit = data.can_edit
            permission.can_delete = data.can_delete
            permission.can_access = data.can_access
            permission.can_update = data.can_update
            permission.is_active = data.is_active
        else:
            permission = MasterScreenPermission(**data.dict())
            db.add(permission)

        results.append(permission)

    db.commit()

    for p in results:
        db.refresh(p)

    return results


# ---------- BULK UPDATE (FIXED) ----------
def bulk_update_permission_service(data_list, db: Session):
    results = []

    for data in data_list:
        permission = (
            db.query(MasterScreenPermission)
            .filter(MasterScreenPermission.id == data.id)
            .first()
        )

        if not permission:
            continue

        permission.role_id = data.role_id
        permission.module_id = data.module_id
        permission.screen_id = data.screen_id

        permission.can_view = data.can_view
        permission.can_edit = data.can_edit
        permission.can_delete = data.can_delete
        permission.can_access = data.can_access
        permission.can_update = data.can_update
        permission.is_active = data.is_active

        results.append(permission)

    db.commit()

    for p in results:
        db.refresh(p)

    return results
