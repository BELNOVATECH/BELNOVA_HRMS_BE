from sqlalchemy.orm import Session
from typing import List

from services.master_service import (
    get_all_modules_service,
    get_all_screens_service,
    get_all_permissions_service,
    create_bulk_permission_service,
    bulk_update_permission_service,
)

from schemas.master_schema import (
    MasterScreenPermissionCreate,
    MasterScreenPermissionBulkUpdate,
)

def get_all_modules_controller(db: Session):
    return get_all_modules_service(db)

def get_all_screens_controller(db: Session):
    return get_all_screens_service(db)

def get_all_permissions_controller(db: Session):
    return get_all_permissions_service(db)

def create_bulk_permission_controller(
    data: List[MasterScreenPermissionCreate],
    db: Session
):
    return create_bulk_permission_service(data, db)

def bulk_update_permission_controller(
    data: List[MasterScreenPermissionBulkUpdate],
    db: Session
):
    return bulk_update_permission_service(data, db)
