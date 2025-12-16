from sqlalchemy.orm import Session
from datetime import date, timedelta
from fastapi import HTTPException
from sqlalchemy import func
from fastapi.responses import FileResponse
import pandas as pd

from models.attendance_tracker import AttendanceTracker
from services.attendance_service import get_attendance_service

# -----------------------------
# Time Utils
# -----------------------------
IST_OFFSET = timedelta(hours=5, minutes=30)

def format_time(dt):
    if not dt:
        return None
    return (dt + IST_OFFSET).strftime("%I:%M %p")

def format_working_hours(start, end):
    if not start or not end:
        return None
    seconds = (end - start).total_seconds()
    return f"{seconds / 3600:.2f} hrs"

def build_response(attendance: AttendanceTracker):
    return {
        "id": attendance.id,
        "emp_id": attendance.emp_id,
        "date": attendance.attendance_date,
        "login_time": format_time(attendance.check_in_time),
        "logout_time": format_time(attendance.check_out_time),
        "working_hours": format_working_hours(
            attendance.check_in_time, attendance.check_out_time
        ),
        "status": "LOGGED OUT" if attendance.check_out_time else "LOGGED IN",
        "remarks": attendance.remarks,
        "is_active": attendance.is_active
    }

# -----------------------------
# LOGIN
# -----------------------------
def login_controller(req, db: Session):
    today = date.today()

    existing = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == req.emp_id,
        AttendanceTracker.attendance_date == today,
        AttendanceTracker.check_in_time.isnot(None)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already logged in today")

    attendance = AttendanceTracker(
        emp_id=req.emp_id,
        attendance_date=today,
        check_in_time=func.now(),  # UTC
        working_status_id=req.working_status_id,
        remarks=req.remarks,
        created_by=1,
        created_date=func.now(),
        is_active=True
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return build_response(attendance)

# -----------------------------
# LOGOUT
# -----------------------------
def logout_controller(emp_id: int, db: Session):
    today = date.today()

    attendance = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == emp_id,
        AttendanceTracker.attendance_date == today,
        AttendanceTracker.check_out_time.is_(None)
    ).first()

    if not attendance:
        raise HTTPException(status_code=400, detail="Login required before logout")

    attendance.check_out_time = func.now()
    attendance.modified_by = 1
    attendance.modified_date = func.now()

    db.commit()
    db.refresh(attendance)

    return build_response(attendance)

# -----------------------------
# TODAY STATUS
# -----------------------------
def today_status_controller(emp_id: int, db: Session):
    today = date.today()

    attendance = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == emp_id,
        AttendanceTracker.attendance_date == today
    ).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="No attendance for today")

    return build_response(attendance)

# -----------------------------
# EMPLOYEE ATTENDANCE HISTORY
# -----------------------------
def get_attendance_by_emp_controller(emp_id: int, db: Session):
    records = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == emp_id
    ).order_by(AttendanceTracker.attendance_date.desc()).all()

    if not records:
        raise HTTPException(status_code=404, detail="No attendance records found")

    return [build_response(r) for r in records]

# -----------------------------
# DELETE ATTENDANCE
# -----------------------------
def delete_attendance_by_id_controller(attendance_id: int, db: Session):
    attendance = db.query(AttendanceTracker).filter(
        AttendanceTracker.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    db.delete(attendance)
    db.commit()

    return {
        "message": "Attendance record deleted successfully",
        "attendance_id": attendance_id
    }

# -----------------------------
# REPORT / EXPORT
# -----------------------------
def get_attendance_controller(
    db: Session,
    emp_id=None,
    from_date=None,
    to_date=None,
    export=False
):
    records = get_attendance_service(db, emp_id, from_date, to_date)

    formatted = []
    for r in records:
        formatted.append({
            "id": r.id,
            "emp_id": r.emp_id,
            "attendance_date": r.attendance_date.strftime("%Y-%m-%d"),
            "check_in_time": r.check_in_time.strftime("%Y-%m-%d %H:%M:%S") if r.check_in_time else None,
            "check_out_time": r.check_out_time.strftime("%Y-%m-%d %H:%M:%S") if r.check_out_time else None,
            "working_status_id": r.working_status_id,
            "working_hours": (
                r.working_hours.total_seconds() / 3600
                if r.working_hours else None
            ),
            "remarks": r.remarks,
            "created_by": r.created_by,
        })

    if export:
        filename = "attendance_export.xlsx"
        df = pd.DataFrame(formatted)
        df.to_excel(filename, index=False)

        return FileResponse(
            path=filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=filename
        )

    return formatted
