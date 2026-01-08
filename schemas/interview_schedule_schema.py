from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime


class ScheduleInterviewRequest(BaseModel):
    candidate_id: int
    designation_id: int
    status_id: int
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


# 🔑 USED IN PUT /interview-schedule/{id}
class InterviewScheduleCreate(BaseModel):
    candidate_id: Optional[int] = None
    designation_id: Optional[int] = None
    status_id: Optional[int] = None
    stage_id: Optional[int] = None
    interview_date: Optional[date] = None
    created_by: Optional[int] = None

    # ⭐⭐ ADDED FOR YOUR REQUIREMENT
    rating: Optional[int] = Field(None, ge=1, le=5)
    feedback: Optional[str] = None


class InterviewScheduleRead(BaseModel):
    id: int
    candidate_id: int
    designation_id: int
    status_id: int
    stage_id: int
    interview_date: date

    # ⭐⭐ RETURN TO FRONTEND
    rating: Optional[int]
    feedback: Optional[str]

    is_active: bool
    created_date: Optional[datetime]

    class Config:
        from_attributes = True
