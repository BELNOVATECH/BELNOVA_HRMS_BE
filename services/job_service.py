from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.job_title import JobOpening


def get_all_job_openings_service(db: Session):
    return db.query(JobOpening).all()


def create_job_title_service(data, db: Session):
    job = JobOpening(
        designation_id=data.designation_id,
        department_id=data.department_id,
        status_id=data.status_id,
        is_active=True
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def update_job_opening_is_active_service(
    job_id: int,
    is_active: bool,
    db: Session
):
    job = db.query(JobOpening).filter(JobOpening.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job opening not found")

    job.is_active = is_active
    db.commit()
    db.refresh(job)
    return job


def update_job_opening_service(
    job_id: int,
    data,
    db: Session
):
    job = db.query(JobOpening).filter(JobOpening.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job opening not found")

    job.designation_id = data.designation_id
    job.department_id = data.department_id
    job.status_id = data.status_id

    if hasattr(data, "is_active") and data.is_active is not None:
        job.is_active = data.is_active

    db.commit()
    db.refresh(job)
    return job
