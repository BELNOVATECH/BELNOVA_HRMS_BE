from pydantic import BaseModel
from typing import Optional


class AttendanceLoginRequest(BaseModel):
    emp_id: int
    working_status_id: int
    remarks: Optional[str] = None
