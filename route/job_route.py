from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.job_title_schema import (
    JobOpeningResponse,
    JobTitleCreate,
    JobOpeningIsActiveUpdate,
    JobOpeningUpdate
)

from controller.job_title import (
    get_all_job_openings_controller,
    create_job_title_controller,
    update_job_opening_is_active_controller,
    update_job_opening_controller
)

router = APIRouter(
    prefix="/job-openings",
    tags=["Job Openings"]
)


@router.get("/", response_model=list[JobOpeningResponse])
def get_all_job_openings(db: Session = Depends(get_db)):
    return get_all_job_openings_controller(db)


@router.post("/", response_model=JobOpeningResponse)
def create_job_opening(
    data: JobTitleCreate,
    db: Session = Depends(get_db)
):
    return create_job_title_controller(data, db)


@router.put("/{job_id}/status", response_model=JobOpeningResponse)
def update_job_opening_status(
    job_id: int,
    req: JobOpeningIsActiveUpdate,
    db: Session = Depends(get_db)
):
    return update_job_opening_is_active_controller(
        job_id,
        req.is_active,
        db
    )


@router.put("/{job_id}/update", response_model=JobOpeningResponse)
def update_job_opening(
    job_id: int,
    data: JobOpeningUpdate,
    db: Session = Depends(get_db)
):
    return update_job_opening_controller(job_id, data, db)
