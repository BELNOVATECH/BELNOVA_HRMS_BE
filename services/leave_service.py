from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException
from datetime import datetime, date
import calendar

from models.leave_model import LeaveRequest
from services.employee_validator import validate_employee
from schemas.leave_schema import (
    ApplyLeaveRequest,
    LeaveApprovalRequest,
    MonthlyLeaveItem,
    MonthlyLeaveSummaryResponse
)

STATUS_APPROVED = 1
STATUS_PENDING = 2
STATUS_REJECTED = 3


# =================================================
# APPLY LEAVE (WITH LEAVE TYPE NAME USING DB FUNCTION)
# =================================================
def apply_leave(payload: ApplyLeaveRequest, db: Session):

    # ✅ Validate employee
    employee = validate_employee(payload.emp_id, db)

    # ✅ Prevent duplicate leave
    exists = db.query(LeaveRequest).filter(
        LeaveRequest.emp_id == payload.emp_id,
        LeaveRequest.leavetype_id == payload.leavetype_id,
        LeaveRequest.start_date == payload.start_date,
        LeaveRequest.end_date == payload.end_date,
        LeaveRequest.is_active == True
    ).first()

    if exists:
        raise HTTPException(status_code=400, detail="Leave already applied")

    # ✅ Insert leave
    leave = LeaveRequest(
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
        reporting_manager_id=payload.reporting_manager_id,
        approval_status_id=STATUS_PENDING,
        created_by=employee.user_id,
        created_date=datetime.utcnow(),
        is_active=True
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    # =================================================
    # 🔥 FETCH LEAVE TYPE NAME USING EXISTING DB FUNCTION
    # =================================================
    result = db.execute(
        text("""
            SELECT *
            FROM fn_leave_request_get_list(
                :emp_id, :limit, :offset
            )
        """),
        {
            "emp_id": payload.emp_id,
            "limit": 1,
            "offset": 0
        }
    )

    row = result.mappings().first()

    if not row:
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch leave type after apply"
        )

    # ✅ Final response
    return {
        "id": leave.id,
        "leavetype_id": leave.leavetype_id,
        "leavetype_name": row["leave_type"],
        "approval_status_id": leave.approval_status_id,
        "created_date": leave.created_date
    }


# =================================================
# APPROVE / REJECT LEAVE
# =================================================
def approve_or_reject_leave(payload: LeaveApprovalRequest, db: Session):

    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == payload.leave_id,
        LeaveRequest.is_active == True
    ).first()

    if not leave:
        raise HTTPException(404, "Leave not found")

    if leave.approval_status_id != STATUS_PENDING:
        raise HTTPException(400, "Leave already processed")

    action = payload.action.lower()

    if action == "approve":
        leave.approval_status_id = STATUS_APPROVED
        status_text = "Approved"
    elif action == "reject":
        leave.approval_status_id = STATUS_REJECTED
        status_text = "Rejected"
    else:
        raise HTTPException(400, "Invalid action")

    leave.approver_id = payload.approver_id
    leave.approved_on = datetime.utcnow()
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
            FROM fn_leave_request_get_list(:emp_id, :limit, :offset)
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
def monthly_leave_summary_service(emp_id: int, year: int, month: int, db: Session):

    validate_employee(emp_id, db)

    start = date(year, month, 1)
    end = date(year, month, calendar.monthrange(year, month)[1])

    leaves = db.query(LeaveRequest).filter(
        LeaveRequest.emp_id == emp_id,
        LeaveRequest.start_date <= end,
        LeaveRequest.end_date >= start
    ).all()

    total = 0
    items = []

    for leave in leaves:
        eff_start = max(leave.start_date, start)
        eff_end = min(leave.end_date, end)
        days = (eff_end - eff_start).days + 1

        total += days

        items.append(
            MonthlyLeaveItem(
                leave_id=leave.id,
                start_date=leave.start_date,
                end_date=leave.end_date,
                total_days=leave.total_days,
                days_counted_in_month=days
            )
        )

    return MonthlyLeaveSummaryResponse(
        emp_id=emp_id,
        month=month,
        year=year,
        total_leaves=total,
        leaves=items
    )
