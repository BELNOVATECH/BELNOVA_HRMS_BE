from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.leave_balance_schema import LeaveBalanceResponse
from services.leave_balance_service import leave_balance_controller

router = APIRouter(
    prefix="/leave",
    tags=["Leave Balance"]
)


@router.get("/balance", response_model=LeaveBalanceResponse)
def get_leave_balance(
    emp_id: int = Query(..., description="Employee ID"),
    year: int = Query(..., description="Year (e.g. 2025)"),
    limit: int = Query(10, description="Pagination limit"),
    offset: int = Query(0, description="Pagination offset"),
    db: Session = Depends(get_db)
):
    return leave_balance_controller(
        emp_id=emp_id,
        year=year,
        limit=limit,
        offset=offset,
        db=db
    )
