from sqlalchemy.orm import Session
from models.master_module import MasterModule
from models.master_screen import MasterScreen
from models.master_screen_permission import MasterScreenPermission

# MODULE
def get_all_modules_service(db: Session):
    return db.query(MasterModule).filter(MasterModule.is_active == True).all()

def create_module_service(data, db: Session):
    module = MasterModule(**data.dict())
    db.add(module)
    db.commit()
    db.refresh(module)
    return module


# SCREEN
def get_all_screens_service(db: Session):
    return db.query(MasterScreen).filter(MasterScreen.is_active == True).all()

def create_screen_service(data, db: Session):
    screen = MasterScreen(**data.dict())
    db.add(screen)
    db.commit()
    db.refresh(screen)
    return screen



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

def delete_permission_service(
    role_id: int,
    module_id: int,
    screen_id: Optional[int],
    db: Session
):
    query = db.query(MasterScreenPermission).filter(
        MasterScreenPermission.role_id == role_id,
        MasterScreenPermission.module_id == module_id,
        MasterScreenPermission.is_active == True,
    )

    # 🔹 Screen-level delete
    if screen_id is not None:
        query = query.filter(
            MasterScreenPermission.screen_id == screen_id
        )
    # 🔹 Module-level delete
    else:
        query = query.filter(
            MasterScreenPermission.screen_id.is_(None)
        )

    permission = query.first()

    if permission:
        permission.is_active = False
        db.commit()

    return {"message": "Permission removed"}



