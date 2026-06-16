from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.interview_stage_schema import (
    InterviewStageCreate,
    InterviewStageUpdate,
    InterviewStageIsActiveUpdate,
    InterviewStageResponse,
    DeleteResponse
)

from controller.interview_stage_controller import (
    create_interview_stage_controller,
    get_all_interview_stages_controller,
    get_interview_stage_by_id_controller,
    update_interview_stage_controller,
    update_interview_stage_is_active_controller,
    delete_interview_stage_controller
)

router = APIRouter(
    prefix="/interview-stage",
    tags=["Interview Stage"]
)


@router.post(
    "/",
    response_model=InterviewStageResponse,
    summary="Create Interview Stage"
)
def create_stage(
    req: InterviewStageCreate,
    db: Session = Depends(get_db)
):
    return create_interview_stage_controller(
        req,
        db
    )


@router.get(
    "/",
    response_model=list[InterviewStageResponse],
    summary="Get All Interview Stages"
)
def get_all_stages(
    db: Session = Depends(get_db)
):
    return get_all_interview_stages_controller(
        db
    )


@router.get(
    "/{stage_id}",
    response_model=InterviewStageResponse,
    summary="Get Interview Stage By ID"
)
def get_stage(
    stage_id: int,
    db: Session = Depends(get_db)
):
    return get_interview_stage_by_id_controller(
        stage_id,
        db
    )


@router.put(
    "/{stage_id}",
    response_model=InterviewStageResponse,
    summary="Update Interview Stage"
)
def update_stage(
    stage_id: int,
    req: InterviewStageUpdate,
    db: Session = Depends(get_db)
):
    return update_interview_stage_controller(
        stage_id,
        req,
        db
    )


@router.put(
    "/{stage_id}/status",
    response_model=InterviewStageResponse,
    summary="Update Interview Stage Status"
)
def update_stage_status(
    stage_id: int,
    req: InterviewStageIsActiveUpdate,
    db: Session = Depends(get_db)
):
    return update_interview_stage_is_active_controller(
        stage_id,
        req,
        db
    )


@router.delete(
    "/{stage_id}",
    response_model=DeleteResponse,
    summary="Delete Interview Stage"
)
def delete_stage(
    stage_id: int,
    db: Session = Depends(get_db)
):
    return delete_interview_stage_controller(
        stage_id,
        db
    )