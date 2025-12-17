from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.leave_schema import (
    ApplyLeaveRequest,
    ApplyLeaveResponse,
    LeaveApprovalRequest,
    LeaveApprovalResponse,
    LeaveHistoryResponse,
    MonthlyLeaveSummaryResponse
)

from services.leave_service import (
    apply_leave,
    approve_or_reject_leave,
    leave_history,
    monthly_leave_summary_service
)

router = APIRouter(
    prefix="/leave",
    tags=["Leave Management"]
)


# =================================================
# APPLY LEAVE
# =================================================
@router.post("/apply", response_model=ApplyLeaveResponse)
def apply_leave_api(
    payload: ApplyLeaveRequest,
    db: Session = Depends(get_db)
):
    return apply_leave(payload, db)


# =================================================
# APPROVE / REJECT
# =================================================
@router.post(
    "/approve-reject",
    response_model=LeaveApprovalResponse
)
def approve_reject_leave_api(
    payload: LeaveApprovalRequest,
    db: Session = Depends(get_db)
):
    return approve_or_reject_leave(payload, db)


# =================================================
# LEAVE HISTORY
# =================================================
@router.get(
    "/history/{emp_id}",
    response_model=list[LeaveHistoryResponse]
)
def get_leave_history(
    emp_id: int,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return leave_history(emp_id, limit, offset, db)


# =================================================
# MONTHLY SUMMARY
# =================================================
@router.get(
    "/monthly-summary",
    response_model=MonthlyLeaveSummaryResponse
)
def get_monthly_leave_summary(
    emp_id: int,
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return monthly_leave_summary_service(emp_id, year, month, db)
