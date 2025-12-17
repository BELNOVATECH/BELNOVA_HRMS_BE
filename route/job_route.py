from fastapi import APIRouter
from models.job_title import JobTitleCreateRequest
from models.job_title import IsActiveUpdate
from controller.job_title import update_job_is_active_controller

from controller.job_title import (
    create_job_controller,
    get_job_controller,
    get_all_jobs_controller
)

router = APIRouter(prefix="/job")

@router.post("/create")
def create_job(request: JobTitleCreateRequest):
    return create_job_controller(request)

@router.get("/all")
def get_all_jobs():
    return get_all_jobs_controller()

@router.put("/{job_id}/is-active")
def update_job_is_active(job_id: int, request: IsActiveUpdate):
    return update_job_is_active_controller(job_id, request)
