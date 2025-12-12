from fastapi import APIRouter
from models.job_title import JobTitleCreateRequest
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

