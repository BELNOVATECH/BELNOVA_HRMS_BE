from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from controller.interview_schedule_controller import (
    schedule_interview_controller,
    get_interview_schedule_controller,
    update_interview_schedule_controller,
    delete_interview_schedule_controller
)

from schemas.interview_schedule_schema import (
    ScheduleInterviewRequest,
    ScheduleInterviewResponse,
    InterviewScheduleCreate,
    InterviewScheduleRead
)

interview_schedule_router = APIRouter(
    prefix="/interview-schedule",
    tags=["Interview Schedule"]
)


@interview_schedule_router.post(
    "/schedule",
    response_model=ScheduleInterviewResponse
)
def schedule_interview(
    payload: ScheduleInterviewRequest,
    db: Session = Depends(get_db)
):
    return schedule_interview_controller(payload, db)


@interview_schedule_router.get(
    "/",
    response_model=List[InterviewScheduleRead]
)
def get_interview_schedules(db: Session = Depends(get_db)):
    return get_interview_schedule_controller(db)


@interview_schedule_router.put(
    "/{interview_id}",
    response_model=InterviewScheduleRead
)
def update_interview_schedule(
    interview_id: int,
    payload: InterviewScheduleCreate,
    db: Session = Depends(get_db)
):
    return update_interview_schedule_controller(db, interview_id, payload)


# @interview_schedule_router.delete("/{interview_id}")
# def delete_interview_schedule(
#     interview_id: int,
#     db: Session = Depends(get_db)
# ):
#     return delete_interview_schedule_controller(db, interview_id)
