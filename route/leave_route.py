from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.leave_schema import (
    ApplyLeaveRequest,
    ApplyLeaveResponse,
    LeaveHistoryResponse,
    MonthlyLeaveSummaryResponse
)

from services.leave_service import (
    apply_leave,
    leave_history,
    monthly_leave_summary_service
)


router = APIRouter(prefix="/leave", tags=["Leave Management"])


# ---------------------------------------------------
# Apply Leave
# ---------------------------------------------------
@router.post("/apply", response_model=ApplyLeaveResponse)
def apply(payload: ApplyLeaveRequest, db: Session = Depends(get_db)):
    return apply_leave(payload, db)


# ---------------------------------------------------
# Leave History
# ---------------------------------------------------
@router.get("/history/{emp_id}", response_model=list[LeaveHistoryResponse])
def get_leave_history(emp_id: int, db: Session = Depends(get_db)):
    return leave_history(emp_id, db)


# ---------------------------------------------------
# Monthly Leave Summary (NEW)
# ---------------------------------------------------
@router.get("/monthly-summary", response_model=MonthlyLeaveSummaryResponse)
def get_monthly_leave_summary(emp_id: int, year: int, month: int, db: Session = Depends(get_db)):
    return monthly_leave_summary_service(emp_id, year, month, db)
