from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db

from controller.interview_schedule_controller import (
    schedule_interview_controller,
    get_interview_schedule_controller,
    get_interview_schedule_by_id_controller,
    update_interview_schedule_controller,
    delete_interview_schedule_controller
)

from schemas.interview_schedule_schema import (
    ScheduleInterviewRequest,
    ScheduleInterviewResponse,
    InterviewScheduleUpdate,
    InterviewScheduleRead,
    DeleteResponse
)

router = APIRouter(
    prefix="/interview-schedule",
    tags=["Interview Schedule"]
)


@router.post(
    "/schedule",
    response_model=ScheduleInterviewResponse
)
def schedule_interview(
    payload: ScheduleInterviewRequest,
    db: Session = Depends(get_db)
):
    return schedule_interview_controller(
        payload,
        db
    )


@router.get(
    "/",
    response_model=List[InterviewScheduleRead]
)
def get_interview_schedules(
    db: Session = Depends(get_db)
):
    return get_interview_schedule_controller(
        db
    )


@router.get(
    "/{interview_id}",
    response_model=InterviewScheduleRead
)
def get_interview_schedule(
    interview_id: int,
    db: Session = Depends(get_db)
):
    return get_interview_schedule_by_id_controller(
        interview_id,
        db
    )


@router.put(
    "/{interview_id}",
    response_model=InterviewScheduleRead
)
def update_interview_schedule(
    interview_id: int,
    payload: InterviewScheduleUpdate,
    db: Session = Depends(get_db)
):
    return update_interview_schedule_controller(
        interview_id,
        payload,
        db
    )


@router.delete(
    "/{interview_id}",
    response_model=DeleteResponse
)
def delete_interview_schedule(
    interview_id: int,
    db: Session = Depends(get_db)
):
    return delete_interview_schedule_controller(
        interview_id,
        db
    )