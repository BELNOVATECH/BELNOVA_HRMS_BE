from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List


# ================= APPLY LEAVE =================
class ApplyLeaveRequest(BaseModel):
    emp_id: int
    leavetype_id: int
    start_date: date
    end_date: date
    total_days: float
    reason: Optional[str]
    from_date_session: Optional[str]
    to_date_session: Optional[str]
    mobile: Optional[str]
    upload_file: Optional[str]
    reporting_manager_id: Optional[int]


class ApplyLeaveResponse(BaseModel):
    id: int
    leavetype_id: int
    leavetype_name: str
    status_id: int
    created_date: datetime




# ================= APPROVE / REJECT =================
class LeaveApprovalRequest(BaseModel):
    leave_id: int
    action: str       # approve | reject
    approver_id: int
    remarks: Optional[str]


class LeaveApprovalResponse(BaseModel):
    leave_id: int
    status_id: int
    approval_status: str
    approver_id: int
    remarks: Optional[str]
    modified_date: datetime


# ================= HISTORY =================
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


# ================= MONTHLY SUMMARY =================
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
