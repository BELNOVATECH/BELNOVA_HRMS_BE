import os
import calendar
from datetime import datetime, date

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from models.leave_model import LeaveRequest
from models.leave_request_cc_model import LeaveRequestCC
from services.employee_validator import validate_employee
from schemas.leave_schema import (
    LeaveApprovalRequest,
    MonthlyLeaveItem,
    MonthlyLeaveSummaryResponse
)

UPLOAD_DIR = "uploads/leave_files"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

os.makedirs(UPLOAD_DIR, exist_ok=True)

STATUS_APPROVED = 10
STATUS_PENDING = 11
STATUS_REJECTED = 3


# -------------------------------------------------
# CALCULATE TOTAL DAYS
# -------------------------------------------------
def calculate_total_days(
    start_date: date,
    end_date: date,
    from_session_id: str,
    to_session_id: str
) -> float:
    from_sess = int(from_session_id)
    to_sess = int(to_session_id)

    if start_date == end_date:
        return 1.0 if from_sess == 1 and to_sess == 2 else 0.5

    days = (end_date - start_date).days + 1

    if from_sess == 2:
        days -= 0.5
    if to_sess == 1:
        days -= 0.5

    return float(days)


# -------------------------------------------------
# APPLY LEAVE (MULTIPART + FILE)
# -------------------------------------------------
def apply_leave(
    emp_id: int,
    leavetype_id: int,
    start_date: str,
    end_date: str,
    from_date_session_id: str,
    to_date_session_id: str,
    reason: str,
    mobile: str,
    reporting_manager_id: int,
    cc: str,
    upload_file: UploadFile,
    db: Session
):
    employee = validate_employee(emp_id, db)

    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)

    # 🔍 Overlapping leave check
    exists = db.query(LeaveRequest).filter(
        LeaveRequest.emp_id == emp_id,
        LeaveRequest.is_active == True,
        LeaveRequest.start_date <= end_date,
        LeaveRequest.end_date >= start_date
    ).first()

    if exists:
        raise HTTPException(400, "Leave already applied for selected dates")

    # 🔍 Validate leave type
    leave_type = db.execute(
        text("""
            SELECT leave_type
            FROM master_leavetype
            WHERE id = :id AND is_active = true
        """),
        {"id": leavetype_id}
    ).scalar()

    if not leave_type:
        raise HTTPException(400, "Invalid leave type")

    total_days = calculate_total_days(
        start_date,
        end_date,
        from_date_session_id,
        to_date_session_id
    )

    # -------------------------------------------------
    # SAVE FILE LOCALLY
    # -------------------------------------------------
    file_path = None
    if upload_file:
        file_bytes = upload_file.file.read()

        if len(file_bytes) > MAX_FILE_SIZE:
            raise HTTPException(400, "File size must be <= 10 MB")

        safe_filename = upload_file.filename.replace(" ", "_")
        filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_emp{emp_id}_{safe_filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as f:
            f.write(file_bytes)

    # -------------------------------------------------
    # CREATE LEAVE REQUEST
    # -------------------------------------------------
    leave = LeaveRequest(
        emp_id=emp_id,
        leavetype_id=leavetype_id,
        start_date=start_date,
        end_date=end_date,
        total_days=total_days,
        reason=reason,
        from_date_session_id=from_date_session_id,
        to_date_session_id=to_date_session_id,
        mobile=mobile,
        reporting_manager_id=reporting_manager_id,
        upload_file=file_path,          # ✅ PATH STORED
        status_id=STATUS_PENDING,
        created_by=employee.user_id,
        created_date=datetime.utcnow(),
        is_active=True
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    # -------------------------------------------------
    # CC EMPLOYEES
    # -------------------------------------------------
    if cc:
        for cc_id in map(int, cc.split(",")):
            db.add(
                LeaveRequestCC(
                    leave_request_id=leave.id,
                    cc_to_id=cc_id,
                    created_by=employee.user_id,
                    created_date=datetime.utcnow(),
                    is_active=True
                )
            )
        db.commit()

    return {
        "id": leave.id,
        "leavetype_id": leave.leavetype_id,
        "leave_type": leave_type,
        "status_id": leave.status_id,
        "created_date": leave.created_date,
        "upload_file": leave.upload_file
    }


# -------------------------------------------------
# APPROVE / REJECT
# -------------------------------------------------
def approve_or_reject_leave(payload: LeaveApprovalRequest, db: Session):
    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == payload.leave_id,
        LeaveRequest.is_active == True
    ).first()

    if not leave:
        raise HTTPException(404, "Leave not found")

    if leave.status_id != STATUS_PENDING:
        raise HTTPException(400, "Leave already processed")

    if payload.action.lower() == "approve":
        leave.status_id = STATUS_APPROVED
        status_text = "Approved"
    elif payload.action.lower() == "reject":
        leave.status_id = STATUS_REJECTED
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
        "status_id": leave.status_id,
        "approval_status": status_text,
        "approver_id": leave.approver_id,
        "remarks": leave.remarks,
        "modified_date": leave.modified_date
    }


# -------------------------------------------------
# HISTORY / PENDING / MONTHLY SUMMARY (UNCHANGED)
# -------------------------------------------------
def leave_history(emp_id: int, limit: int, offset: int, db: Session):
    validate_employee(emp_id, db)
    return db.execute(
        text("SELECT * FROM fn_leave_request_get_list(:emp_id, :limit, :offset)"),
        {"emp_id": emp_id, "limit": limit, "offset": offset}
    ).mappings().all()


def pending_leaves(emp_id: int, limit: int, offset: int, db: Session):
    validate_employee(emp_id, db)
    return db.execute(
        text("""
            SELECT *
            FROM fn_leave_request_get_list(:emp_id, :limit, :offset)
            WHERE status_id = :status
        """),
        {"emp_id": emp_id, "limit": limit, "offset": offset, "status": STATUS_PENDING}
    ).mappings().all()


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
