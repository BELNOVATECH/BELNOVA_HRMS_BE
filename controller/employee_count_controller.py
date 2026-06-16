from sqlalchemy.orm import Session

from services.employee_count_service import (
    get_active_employee_count_service
)


def get_active_employee_count_controller(
    db: Session
):
    return get_active_employee_count_service(db)