from sqlalchemy.orm import Session
from services.master_service import *

def get_all_modules_controller(db: Session):
    return get_all_modules_service(db)

def create_module_controller(data, db: Session):
    return create_module_service(data, db)

def get_all_screens_controller(db: Session):
    return get_all_screens_service(db)

def create_screen_controller(data, db: Session):
    return create_screen_service(data, db)

def get_all_permissions_controller(db: Session):
    return get_all_permissions_service(db)

def create_permission_controller(data, db: Session):
    return create_permission_service(data, db)

def delete_permission_controller(
    role_id: int,
    module_id: int,
    screen_id: Optional[int],
    db: Session
):
    return delete_permission_service(
        role_id, module_id, screen_id, db
    )


