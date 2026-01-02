from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from core.database import get_db

from services.leave_service import (
    apply_leave,
    approve_or_reject_leave,
    leave_history,
    monthly_leave_summary_service,
    pending_leaves
)

from schemas.leave_schema import (
    LeaveApprovalRequest,
    LeaveApprovalResponse,
    LeaveHistoryResponse,
    MonthlyLeaveSummaryResponse
)

router = APIRouter(prefix="/leave", tags=["Leave Management"])


# -------------------------------------------------
# APPLY LEAVE (FILE UPLOAD + FORM DATA)
# -------------------------------------------------
@router.post("/apply")
def apply_leave_api(
    emp_id: int = Form(...),
    leavetype_id: int = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    from_date_session_id: str = Form(...),
    to_date_session_id: str = Form(...),
    reason: str = Form(None),
    mobile: str = Form(None),
    reporting_manager_id: int = Form(None),
    cc: str = Form(None),              # "11,20"
    upload_file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    return apply_leave(
        emp_id,
        leavetype_id,
        start_date,
        end_date,
        from_date_session_id,
        to_date_session_id,
        reason,
        mobile,
        reporting_manager_id,
        cc,
        upload_file,
        db
    )


# -------------------------------------------------
# PENDING LEAVES
# -------------------------------------------------
@router.get("/pending/{emp_id}", response_model=list[LeaveHistoryResponse])
def get_pending_leaves(
    emp_id: int,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return pending_leaves(emp_id, limit, offset, db)


# -------------------------------------------------
# APPROVE / REJECT LEAVE
# -------------------------------------------------
@router.post("/approve-reject", response_model=LeaveApprovalResponse)
def approve_reject_leave_api(
    payload: LeaveApprovalRequest,
    db: Session = Depends(get_db)
):
    return approve_or_reject_leave(payload, db)


# -------------------------------------------------
# LEAVE HISTORY
# -------------------------------------------------
@router.get("/history/{emp_id}", response_model=list[LeaveHistoryResponse])
def get_leave_history(
    emp_id: int,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return leave_history(emp_id, limit, offset, db)


# -------------------------------------------------
# MONTHLY SUMMARY
# -------------------------------------------------
@router.get("/monthly-summary", response_model=MonthlyLeaveSummaryResponse)
def get_monthly_leave_summary(
    emp_id: int,
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return monthly_leave_summary_service(emp_id, year, month, db)
