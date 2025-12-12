from services.holiday_service import get_holidays_service

def get_holidays_controller(db):
    return get_holidays_service(db)
