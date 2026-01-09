from services.employee_rating_service import create_employee_rating_service

def create_employee_rating_controller(payload, db):
    return create_employee_rating_service(payload, db)
