from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException
from datetime import datetime, date
import calendar

from models.leave_model import LeaveRequest
from schemas.leave_schema import (
    ApplyLeaveRequest,
    LeaveApprovalRequest,
    MonthlyLeaveItem,
    MonthlyLeaveSummaryResponse
)
from services.employee_validator import validate_employee


STATUS_APPROVED = 1
STATUS_PENDING = 2
STATUS_REJECTED = 3


# =================================================
# APPLY LEAVE
# =================================================
def apply_leave(payload: ApplyLeaveRequest, db: Session):

    employee = validate_employee(payload.emp_id, db)

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
        approval_status_id=STATUS_PENDING,
        created_by=employee.user_id,   # ✅ FK → users.id
        created_date=datetime.utcnow(),
        reporting_manager_id=payload.reporting_manager_id,
        is_active=True
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


# =================================================
# APPROVE / REJECT LEAVE
# =================================================
def approve_or_reject_leave(payload: LeaveApprovalRequest, db: Session):

    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == payload.leave_id,
        LeaveRequest.is_active == True
    ).first()

    if not leave:
        raise HTTPException(404, "Leave request not found")

    if leave.approval_status_id != STATUS_PENDING:
        raise HTTPException(
            400,
            "Only pending leaves can be approved or rejected"
        )

    action = payload.action.lower()

    if action == "approve":
        leave.approval_status_id = STATUS_APPROVED
        status_text = "Approved"
    elif action == "reject":
        leave.approval_status_id = STATUS_REJECTED
        status_text = "Rejected"
    else:
        raise HTTPException(400, "Action must be approve or reject")

    leave.approver_id = payload.approver_id
    leave.remarks = payload.remarks
    leave.modified_by = payload.approver_id
    leave.modified_date = datetime.utcnow()

    db.commit()
    db.refresh(leave)

    return {
        "leave_id": leave.id,
        "approval_status_id": leave.approval_status_id,
        "approval_status": status_text,
        "approver_id": leave.approver_id,
        "remarks": leave.remarks,
        "modified_date": leave.modified_date
    }


# =================================================
# LEAVE HISTORY (DB FUNCTION)
# =================================================
def leave_history(emp_id: int, limit: int, offset: int, db: Session):

    validate_employee(emp_id, db)

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

    if not rows:
        raise HTTPException(404, "No leave history found")

    return rows


# =================================================
# MONTHLY SUMMARY
# =================================================
def monthly_leave_summary_service(
    emp_id: int,
    year: int,
    month: int,
    db: Session
):

    validate_employee(emp_id, db)

    month_start = date(year, month, 1)
    month_end = date(year, month, calendar.monthrange(year, month)[1])

    leaves = (
        db.query(LeaveRequest)
        .filter(
            LeaveRequest.emp_id == emp_id,
            LeaveRequest.start_date <= month_end,
            LeaveRequest.end_date >= month_start
        )
        .all()
    )

    total_days = 0
    items = []

    for leave in leaves:
        effective_start = max(leave.start_date, month_start)
        effective_end = min(leave.end_date, month_end)
        days = (effective_end - effective_start).days + 1

        total_days += days

        items.append(
            MonthlyLeaveItem(
                leave_id=leave.id,
                start_date=leave.start_date,
                end_date=leave.end_date,
                total_days=leave.total_days or 0,
                days_counted_in_month=days
            )
        )

    return MonthlyLeaveSummaryResponse(
        emp_id=emp_id,
        month=month,
        year=year,
        total_leaves=total_days,
        leaves=items
    )
