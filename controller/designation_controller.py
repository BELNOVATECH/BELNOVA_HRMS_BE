from sqlalchemy.orm import Session

from schemas.designation_schema import (
    DesignationCreate,
    DesignationStatusUpdate
)
from services.designation_service import (
    create_designation_service,
    get_designations_service,
    get_designation_by_id_service,
    update_designation_status_service
)


def create_designation_controller(
    payload: DesignationCreate,
    db: Session
):
    return create_designation_service(payload, db)


def get_designations_controller(db: Session):
    return get_designations_service(db)


def get_designation_by_id_controller(
    designation_id: int,
    db: Session
):
    return get_designation_by_id_service(designation_id, db)


def update_designation_status_controller(
    designation_id: int,
    payload: DesignationStatusUpdate,
    db: Session
):
    return update_designation_status_service(
        designation_id,
        payload,
        db
    )
