from pydantic import BaseModel
from typing import Optional
from datetime import date


class AttendanceLoginRequest(BaseModel):
    emp_id: int
    working_status_id: int = 1
    remarks: Optional[str] = None


class AttendanceResponse(BaseModel):
    id: int
    emp_id: int
    date: date
    login_time: Optional[str]
    logout_time: Optional[str]
    working_hours: Optional[str]
    status: str
    remarks: Optional[str]
    is_active: bool
