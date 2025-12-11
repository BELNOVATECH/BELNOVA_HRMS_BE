# route/leave_route.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.leave_schema import ApplyLeaveRequest, ApplyLeaveResponse, LeaveHistoryResponse
from services.leave_service import apply_leave, leave_history

router = APIRouter(prefix="/leave", tags=["Leave Management"])


@router.post("/apply", response_model=ApplyLeaveResponse)
def apply(payload: ApplyLeaveRequest, db: Session = Depends(get_db)):
    return apply_leave(payload, db)


@router.get("/history/{emp_id}", response_model=list[LeaveHistoryResponse])
def get_leave_history(emp_id: int, db: Session = Depends(get_db)):
    return leave_history(emp_id, db)
