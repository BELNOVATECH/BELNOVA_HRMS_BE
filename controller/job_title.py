from fastapi import HTTPException
from services.job_service import create_job, get_job, get_all_jobs
from models.job_title import JobTitleCreateRequest, JobTitleResponse
from services.job_service import update_job_is_active
from models.job_title import IsActiveUpdate


def create_job_controller(request: JobTitleCreateRequest):
    job = create_job(request.position)

    return JobTitleResponse(
        id=job["id"],
        position=job["position"],
        is_active=job["is_active"]
    )


def get_job_controller(job_id: int):
    job = get_job(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job title not found")

    return JobTitleResponse(
        id=job["id"],
        position=job["position"],
        is_active=job["is_active"]
    )


def get_all_jobs_controller():
    jobs = get_all_jobs()

    return [
        JobTitleResponse(
            id=job["id"],
            position=job["position"],
            is_active=job["is_active"],
        )
        for job in jobs
    ]
def update_job_is_active_controller(job_id: int, request: IsActiveUpdate):
    job = update_job_is_active(job_id, request.is_active)

    if not job:
        raise HTTPException(status_code=404, detail="Job title not found")

    return JobTitleResponse(
        id=job["id"],
        position=job["position"],
        is_active=job["is_active"]
    )
