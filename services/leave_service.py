from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException
from datetime import datetime, date
import calendar

from models.leave_model import LeaveRequest
from schemas.leave_schema import (
    ApplyLeaveRequest,
    MonthlyLeaveItem,
    MonthlyLeaveSummaryResponse
)
from services.employee_validator import validate_employee


# ---------------------------------------------------
# 1. APPLY LEAVE
# ---------------------------------------------------
def apply_leave(payload: ApplyLeaveRequest, db: Session):

    # validate employee
    validate_employee(payload.emp_id, db)

    new_leave = LeaveRequest(
        emp_id=payload.emp_id,
        leavetype_id=payload.leavetype_id,
        start_date=payload.start_date,
        end_date=payload.end_date,
        total_days=payload.total_days,
        reason=payload.reason,
        from_date_session=payload.from_date_session,
        to_date_session=payload.to_date_session,
        mobile=payload.mobile,
        upload_file=payload.upload_file,
        approval_status_id=1,  # Pending
        created_by=payload.emp_id,
        created_date=datetime.utcnow(),
        reporting_manager_id=payload.reporting_manager_id
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


# ---------------------------------------------------
# 2. LEAVE HISTORY (DB FUNCTION)
# ---------------------------------------------------
def leave_history(emp_id: int, limit: int, offset: int, db: Session):

    validate_employee(emp_id, db)

    if limit <= 0 or offset < 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid pagination values"
        )

    try:
        result = db.execute(
            text("""
                SELECT *
                FROM fn_leave_request_get_list(
                    :emp_id, :limit, :offset
                )
            """),
            {
                "emp_id": emp_id,
                "limit": limit,
                "offset": offset
            }
        )

        rows = result.mappings().all()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    return rows


# ---------------------------------------------------
# 3. MONTHLY LEAVE SUMMARY
# ---------------------------------------------------
def monthly_leave_summary_service(
    emp_id: int,
    year: int,
    month: int,
    db: Session
):

    validate_employee(emp_id, db)

    month_start = date(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    month_end = date(year, month, last_day)

    leaves = (
        db.query(LeaveRequest)
        .filter(
            LeaveRequest.emp_id == emp_id,
            LeaveRequest.start_date <= month_end,
            LeaveRequest.end_date >= month_start
        )
        .all()
    )

    leave_items = []
    total_days_in_month = 0

    for leave in leaves:
        effective_start = max(leave.start_date, month_start)
        effective_end = min(leave.end_date, month_end)

        if effective_end < effective_start:
            continue

        days_counted = (effective_end - effective_start).days + 1
        total_days_in_month += days_counted

        leave_items.append(
            MonthlyLeaveItem(
                leave_id=leave.id,
                start_date=leave.start_date,
                end_date=leave.end_date,
                total_days=leave.total_days or 0,
                days_counted_in_month=days_counted
            )
        )

    return MonthlyLeaveSummaryResponse(
        emp_id=emp_id,
        month=month,
        year=year,
        total_leaves=total_days_in_month,
        leaves=leave_items
    )
