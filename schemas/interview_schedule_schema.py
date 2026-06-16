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

    model_config = {
        "from_attributes": True
    }


class InterviewScheduleUpdate(BaseModel):
    candidate_id: Optional[int] = None
    designation_id: Optional[int] = None
    status_id: Optional[int] = None
    stage_id: Optional[int] = None
    interview_date: Optional[date] = None

    rating: Optional[int] = Field(None, ge=1, le=5)
    feedback: Optional[str] = None


class InterviewScheduleRead(BaseModel):
    id: int
    candidate_id: int
    designation_id: int
    status_id: int
    stage_id: int
    interview_date: date

    rating: Optional[int]
    feedback: Optional[str]

    is_active: bool
    created_date: Optional[datetime]
    modified_date: Optional[datetime]

    model_config = {
        "from_attributes": True
    }


class DeleteResponse(BaseModel):
    message: str