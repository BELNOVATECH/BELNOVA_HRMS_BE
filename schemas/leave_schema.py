from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List


# =================================================
# APPLY LEAVE
# =================================================
class ApplyLeaveRequest(BaseModel):
    emp_id: int
    leavetype_id: int
    start_date: date
    end_date: date
    total_days: Optional[float] = None
    reason: Optional[str] = None
    from_date_session: Optional[str] = None
    to_date_session: Optional[str] = None
    mobile: Optional[str] = None
    upload_file: Optional[str] = None
    reporting_manager_id: Optional[int] = None


class ApplyLeaveResponse(BaseModel):
    id: int
    approval_status_id: int
    created_date: datetime

    class Config:
        from_attributes = True


# =================================================
# APPROVE / REJECT
# =================================================
class LeaveApprovalRequest(BaseModel):
    leave_id: int
    action: str              # approve | reject
    approver_id: int
    remarks: Optional[str] = None


class LeaveApprovalResponse(BaseModel):
    leave_id: int
    approval_status_id: int
    approval_status: str
    approver_id: int
    remarks: Optional[str]
    modified_date: datetime


# =================================================
# LEAVE HISTORY (DB FUNCTION)
# =================================================
class LeaveHistoryResponse(BaseModel):
    leave_request_id: int
    emp_id: int
    leavetype_id: int
    leave_type: str
    start_date: date
    end_date: date
    total_days: float
    approval_status_id: int
    approval_status: str
    reason: Optional[str]
    # created_date: datetime


# =================================================
# MONTHLY SUMMARY
# =================================================
class MonthlyLeaveItem(BaseModel):
    leave_id: int
    start_date: date
    end_date: date
    total_days: float
    days_counted_in_month: float


class MonthlyLeaveSummaryResponse(BaseModel):
    emp_id: int
    month: int
    year: int
    total_leaves: float
    leaves: List[MonthlyLeaveItem]
