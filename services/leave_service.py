# services/leave_service.py
from sqlalchemy.orm import Session
from models.leave_model import LeaveRequest
from schemas.leave_schema import ApplyLeaveRequest
from fastapi import HTTPException
from datetime import datetime


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

        # ✔ Auto-default to pending = 1
        approval_status_id=1,

        # ✔ created_by = emp_id
        created_by=payload.emp_id,
        created_date=datetime.utcnow(),

        # ✔ safe fallback if frontend sends None
        reporting_manager_id=payload.reporting_manager_id or 1  
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


def leave_history(emp_id: int, db: Session):

    leaves = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.emp_id == emp_id)
        .order_by(LeaveRequest.id.desc())
        .all()
    )

    if not leaves:
        raise HTTPException(status_code=404, detail="No leave history found")

    return leaves
