from services.employee_count_service import get_active_employee_count_service

def get_active_employee_count_controller(db):
    return get_active_employee_count_service(db)
