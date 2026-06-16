from sqlalchemy.orm import Session

from services.department_service import (
    create_department_service,
    get_departments_service,
    get_department_by_id_service,
    update_department_status_service
)


def create_department_controller(
    payload,
    db: Session
):
    return create_department_service(
        payload,
        db
    )


def get_departments_controller(
    db: Session
):
    return get_departments_service(
        db
    )


def get_department_by_id_controller(
    dept_id: int,
    db: Session
):
    return get_department_by_id_service(
        dept_id,
        db
    )


def update_department_status_controller(
    dept_id: int,
    payload,
    db: Session
):
    return update_department_status_service(
        dept_id,
        payload,
        db
    )