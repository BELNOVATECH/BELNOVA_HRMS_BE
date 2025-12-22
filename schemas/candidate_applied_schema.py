from pydantic import BaseModel, EmailStr, field_validator
from datetime import date, datetime
from typing import Optional
from utils.date_utils import convert_date
import re


# =================================================
# CREATE
# =================================================
class CandidateAppliedCreate(BaseModel):
    candidate_name: str
    designation_id: int
    dob: date
    email: EmailStr
    mobile: str
    address: str
    application_status_id: int
    upload_resume: Optional[str] = None

    @field_validator("mobile")
    def validate_mobile(cls, value):
        pattern = r"^[6-9]\d{9}$"
        if not re.fullmatch(pattern, value):
            raise ValueError("Invalid Indian mobile number")
        return value

    @field_validator("dob", mode="before")
    def validate_dob(cls, value):
        if isinstance(value, str):
            return convert_date(value)
        return value


# =================================================
# READ
# =================================================
class CandidateAppliedRead(BaseModel):
    id: int
    candidate_name: str
    designation_id: int
    dob: date
    email: EmailStr
    mobile: str
    address: str
    application_status_id: int
    upload_resume: Optional[str]
    is_active: bool
    created_date: Optional[datetime]

    class Config:
        from_attributes = True


# =================================================
# UPDATE
# =================================================
class CandidateAppliedUpdate(BaseModel):
    candidate_name: Optional[str] = None
    designation_id: Optional[int] = None
    dob: Optional[date] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    address: Optional[str] = None
    application_status_id: Optional[int] = None
    upload_resume: Optional[str] = None

    class Config:
        from_attributes = True
