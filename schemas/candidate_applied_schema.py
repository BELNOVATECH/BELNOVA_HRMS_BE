from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from utils.date_utils import convert_date

import re

class CandidateAppliedCreate(BaseModel):
    candidate_name: str
    position_id: int
    dob: date
    email: EmailStr
    mobile: str
    address: str
    application_status_id: int
    upload_resume: str | None = None

    @field_validator("mobile")
    def validate_mobile(cls, value):
        pattern = r"^[6-9]\d{9}$"
        if not re.fullmatch(pattern, value):
            raise ValueError("Invalid Indian mobile number.")
        return value
    
    @field_validator("dob", mode="before")
    def validate_dob(cls, value):
        if isinstance(value, str):
            return convert_date(value)
        return value   
    
    

class CandidateAppliedRead(BaseModel):
    id: int
    candidate_name: str
    position_id: int
    dob: date
    email: EmailStr
    mobile: str
    address: str
    application_status_id: int
    upload_resume: str | None

    model_config = {"from_attributes": True}
