from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


# =================================================
# NEW – Schedule interview (from candidate_applied)
# =================================================
class ScheduleInterviewRequest(BaseModel):
    candidate_applied_id: int
    stage_id: int
    interview_date: date
    created_by: int


class ScheduleInterviewResponse(BaseModel):
    id: int
    candidate_id: int
    stage_id: int
    interview_date: date
    is_active: bool

    class Config:
        from_attributes = True


# =================================================
# CRUD – interview_schedule table
# =================================================
class InterviewScheduleCreate(BaseModel):
    candidate_id: int
    position_id: Optional[int] = None
    status_id: Optional[int] = None
    stage_id: int
    interview_date: date
    created_by: Optional[int] = None


class InterviewScheduleRead(BaseModel):
    id: int
    candidate_id: int
    position_id: Optional[int]
    status_id: Optional[int]
    stage_id: int
    interview_date: date
    is_active: bool
    created_date: Optional[datetime]

    class Config:
        from_attributes = True
