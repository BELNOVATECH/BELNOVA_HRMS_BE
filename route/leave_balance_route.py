from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.leave_balance_schema import (
    LeaveBalanceRequest,
    LeaveBalanceResponse
)
from services.leave_balance_service import leave_balance_controller

router = APIRouter(
    prefix="/leave",
    tags=["Leave Balance"]
)


@router.post(
    "/balance",
    response_model=LeaveBalanceResponse
)
def get_leave_balance(
    payload: LeaveBalanceRequest,
    db: Session = Depends(get_db)
):
    return leave_balance_controller(
        emp_id=payload.emp_id,
        year=payload.year,
        month=payload.month,
        offset=payload.offset,
        db=db
    )
