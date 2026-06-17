from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.generated_models import (
    JobOpenings,
    MasterDesignation,
    MasterDepartment,
    MasterStatus
)


def get_all_job_openings_service(db: Session):
    return db.query(JobOpenings).all()


def create_job_title_service(data, db: Session):

    designation = db.query(MasterDesignation).filter(
        MasterDesignation.id == data.designation_id
    ).first()

    if not designation:
        raise HTTPException(
            status_code=404,
            detail="Designation not found"
        )

    department = db.query(MasterDepartment).filter(
        MasterDepartment.id == data.department_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    status = db.query(MasterStatus).filter(
        MasterStatus.id == data.status_id
    ).first()

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Status not found"
        )

    job = JobOpenings(
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
    job = db.query(JobOpenings).filter(
        JobOpenings.id == job_id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job opening not found"
        )

    job.is_active = is_active

    db.commit()
    db.refresh(job)

    return job


def update_job_opening_service(
    job_id: int,
    data,
    db: Session
):
    job = db.query(JobOpenings).filter(
        JobOpenings.id == job_id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job opening not found"
        )

    designation = db.query(MasterDesignation).filter(
        MasterDesignation.id == data.designation_id
    ).first()

    if not designation:
        raise HTTPException(
            status_code=404,
            detail="Designation not found"
        )

    department = db.query(MasterDepartment).filter(
        MasterDepartment.id == data.department_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    status = db.query(MasterStatus).filter(
        MasterStatus.id == data.status_id
    ).first()

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Status not found"
        )

    job.designation_id = data.designation_id
    job.department_id = data.department_id
    job.status_id = data.status_id

    if data.is_active is not None:
        job.is_active = data.is_active

    db.commit()
    db.refresh(job)

    return job