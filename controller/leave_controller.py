from pydantic import BaseModel
from typing import Optional

class ApplyLeaveRequest(BaseModel):
    emp_id: int
    from_date: str
    to_date: str
    no_of_days: float
    session_start: str
    session_end: str
    type_of_leave: str
    reason: str
    upload_files: Optional[str] = None
    approved_by: Optional[str] = None
    approved_on: Optional[str] = None


class ApplyLeaveResponse(BaseModel):
    leave_id: int
    leave_status: str
    approved_by: Optional[str]
    approved_on: Optional[str]
