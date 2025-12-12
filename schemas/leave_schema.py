from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


# ---------------------------------
# Apply Leave Request Schema
# ---------------------------------
class ApplyLeaveRequest(BaseModel):
    emp_id: int
    leavetype_id: int
    start_date: date
    end_date: date
    total_days: Optional[float]
    reason: Optional[str]
    from_date_session: Optional[str]
    to_date_session: Optional[str]
    mobile: Optional[str]
    upload_file: Optional[str]
    reporting_manager_id: Optional[int] = None  # optional


# ---------------------------------
# Apply Leave Response Schema
# ---------------------------------
class ApplyLeaveResponse(BaseModel):
    id: int
    approval_status_id: int
    approver_id: Optional[int]
    created_date: datetime

    class Config:
        from_attributes = True


# ---------------------------------
# Leave History Response
# ---------------------------------
class LeaveHistoryResponse(BaseModel):
    id: int
    leavetype_id: int
    start_date: date
    end_date: date
    total_days: float
    approval_status_id: int
    reason: Optional[str]

    class Config:
        from_attributes = True


# ---------------------------------
# Monthly Leave Summary Schemas
# ---------------------------------
class MonthlyLeaveItem(BaseModel):
    leave_id: int
    start_date: date
    end_date: date
    total_days: float
    days_counted_in_month: float

    class Config:
        from_attributes = True


class MonthlyLeaveSummaryResponse(BaseModel):
    emp_id: int
    month: int
    year: int
    total_leaves: float
    leaves: list[MonthlyLeaveItem]
