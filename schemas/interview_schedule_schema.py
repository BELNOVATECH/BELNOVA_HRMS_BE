from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


# ===============================
# Schedule interview (POST)
# ===============================
class ScheduleInterviewRequest(BaseModel):
    candidate_applied_id: int
    designation_id: int        # ✅ added
    status_id: int             # ✅ added
    stage_id: int
    interview_date: date
    created_by: int


class ScheduleInterviewResponse(BaseModel):
    id: int
    candidate_id: int
    designation_id: int
    status_id: int
    stage_id: int
    interview_date: date
    is_active: bool

    class Config:
        from_attributes = True


# ===============================
# CRUD schemas
# ===============================
class InterviewScheduleCreate(BaseModel):
    candidate_id: int
    designation_id: int        # ✅ changed
    status_id: int
    stage_id: int
    interview_date: date
    created_by: Optional[int] = None


class InterviewScheduleRead(BaseModel):
    id: int
    candidate_id: int
    designation_id: int
    status_id: int
    stage_id: int
    interview_date: date
    is_active: bool
    created_date: Optional[datetime]

    class Config:
        from_attributes = True
