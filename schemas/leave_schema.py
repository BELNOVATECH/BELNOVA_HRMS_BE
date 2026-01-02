from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List



class ApplyLeaveRequest(BaseModel):
    emp_id: int
    leavetype_id: int
    start_date: date
    end_date: date
    reason: Optional[str]
    from_date_session_id: str  # "1" or "2"
    to_date_session_id: str    # "1" or "2"
    mobile: Optional[str]
    upload_file: Optional[str]
    reporting_manager_id: Optional[int]


class ApplyLeaveResponse(BaseModel):
    id: int
    leavetype_id: int
    leave_type: str
    status_id: int
    created_date: datetime


class LeaveApprovalRequest(BaseModel):
    leave_id: int
    action: str        # approve | reject
    approver_id: int
    remarks: Optional[str]


class LeaveApprovalResponse(BaseModel):
    leave_id: int
    status_id: int
    approval_status: str
    approver_id: int
    remarks: Optional[str]
    modified_date: datetime


class LeaveHistoryResponse(BaseModel):
    leave_request_id: int
    emp_id: int
    leavetype_id: int
    leave_type: str
    start_date: date
    end_date: date
    total_days: float
    status_id: int
    status_name: str
    reason: Optional[str]


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
