from services.auth_service import login_service


def login_controller(payload, db):
    return login_service(payload, db)
