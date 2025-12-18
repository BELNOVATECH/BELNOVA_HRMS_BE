from sqlalchemy.orm import Session
from services.job_title_service import (
    get_all_job_openings_service,
    create_job_title_service,
    update_job_opening_is_active_service
)


def get_all_job_openings_controller(db: Session):
    return get_all_job_openings_service(db)


def create_job_title_controller(data, db: Session):
    return create_job_title_service(data, db)

def update_job_opening_is_active_controller(
    job_id: int,
    is_active: bool,
    db: Session
):
    return update_job_opening_is_active_service(job_id, is_active, db)
