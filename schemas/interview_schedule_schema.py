from pydantic import BaseModel
from datetime import date
from utils.date_utils import convert_date



class InterviewScheduleCreate(BaseModel):
    candidate_id: int
    position_id: int
    status_id: int
    stage_id: int
    interview_date: date
    rating: int | None = None
    feedback: str | None = None
    created_by: int
    
    # @field_validator("interview_date", mode="before")
    # def validate_dob(cls, value):
    #     if isinstance(value, str):
    #         return convert_date(value)
    #     return value 


class InterviewScheduleRead(BaseModel):
    id: int
    candidate_id: int
    position_id: int
    status_id: int
    stage_id: int
    interview_date: date
    rating: int | None
    feedback: str | None
    created_by: int 

    model_config = {"from_attributes": True}
