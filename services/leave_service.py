from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, date
import calendar

from models.leave_model import LeaveRequest
from schemas.leave_schema import (
    ApplyLeaveRequest,
    MonthlyLeaveSummaryResponse,
    MonthlyLeaveItem,
    LeaveHistoryResponse,
)


# ---------------------------------------------------
# STATUS MAPPER
# ---------------------------------------------------
def get_status_text(status_id: int):
    return {
        1: "Pending",
        2: "Approved",
        3: "Rejected"
    }.get(status_id, "Unknown")


# ---------------------------------------------------
# 1. APPLY LEAVE
# ---------------------------------------------------
def apply_leave(payload: ApplyLeaveRequest, db: Session):

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
        reporting_manager_id=payload.reporting_manager_id or 1
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


# ---------------------------------------------------
# 2. LEAVE HISTORY WITH STATUS NAME
# ---------------------------------------------------
def leave_history(emp_id: int, db: Session):
    leaves = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.emp_id == emp_id)
        .order_by(LeaveRequest.id.desc())
        .all()
    )

    if not leaves:
        raise HTTPException(status_code=404, detail="No leave history found")

    result = []
    for leave in leaves:
        result.append({
            "id": leave.id,
            "leavetype_id": leave.leavetype_id,
            "start_date": leave.start_date,
            "end_date": leave.end_date,
            "total_days": leave.total_days,
            "approval_status_id": leave.approval_status_id,
            "approval_status": get_status_text(leave.approval_status_id),
            "reason": leave.reason,
        })

    return result


# ---------------------------------------------------
# 3. FILTER LEAVES BY STATUS (Pending / Approved / Rejected)
# ---------------------------------------------------
def filter_leaves_by_status(emp_id: int, status: str, db: Session):

    status_map = {"pending": 1, "approved": 2, "rejected": 3}

    status_id = status_map.get(status.lower())
    if not status_id:
        raise HTTPException(400, "Invalid status. Use pending, approved, rejected")

    leaves = (
        db.query(LeaveRequest)
        .filter(
            LeaveRequest.emp_id == emp_id,
            LeaveRequest.approval_status_id == status_id
        )
        .all()
    )

    result = []
    for leave in leaves:
        result.append({
            "id": leave.id,
            "leavetype_id": leave.leavetype_id,
            "start_date": leave.start_date,
            "end_date": leave.end_date,
            "total_days": leave.total_days,
            "approval_status_id": leave.approval_status_id,
            "approval_status": get_status_text(leave.approval_status_id),
            "reason": leave.reason,
        })

    return result


# ---------------------------------------------------
# 4. MONTHLY LEAVE SUMMARY
# ---------------------------------------------------
def monthly_leave_summary_service(emp_id: int, year: int, month: int, db: Session):

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
                days_counted_in_month=days_counted,
            )
        )

    return MonthlyLeaveSummaryResponse(
        emp_id=emp_id,
        month=month,
        year=year,
        total_leaves=total_days_in_month,
        leaves=leave_items
    )
