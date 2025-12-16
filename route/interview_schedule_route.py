from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from controller.interview_schedule_controller import (
    create_interview_schedule_controller,
    get_interview_schedule_controller,
)
from schemas.interview_schedule_schema import (
    InterviewScheduleCreate,
    InterviewScheduleRead,
)
from typing import List

interview_schedule_router = APIRouter()

@interview_schedule_router.post("/", response_model=InterviewScheduleRead)
def create_interview_schedule(data: InterviewScheduleCreate, db: Session = Depends(get_db)):
    return create_interview_schedule_controller(data, db)

@interview_schedule_router.get("/", response_model=List[InterviewScheduleRead])
def get_interview_schedules(db: Session = Depends(get_db)):
    return get_interview_schedule_controller(db)
