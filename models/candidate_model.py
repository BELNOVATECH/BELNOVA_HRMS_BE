from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
import re

class CandidateCreate(BaseModel):
    name: str
    role: str
    dob: date
    email: EmailStr
    address: str
    mobile_number: str

    @field_validator("mobile_number")
    def validate_mobile(cls, value):
        pattern = r"^[6-9]\d{9}$"
        if not re.fullmatch(pattern, value):
            raise ValueError("Invalid Indian mobile number.")
        return f"+91 {value[:5]} {value[5:]}"


class CandidateRead(BaseModel):
    id: int
    name: str
    role: str
    dob: date
    email: EmailStr
    address: str
    mobile_number: str

    model_config = {"from_attributes": True}
