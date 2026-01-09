from services.role_service import (
    create_role_service,
    get_roles_service,
    update_role_service,
)


def create_role_controller(payload, db):
    return create_role_service(payload, db)


def get_roles_controller(db):
    return get_roles_service(db)


def update_role_controller(db, role_id, payload):
    return update_role_service(db, role_id, payload)



