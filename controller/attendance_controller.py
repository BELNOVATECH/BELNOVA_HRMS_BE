from sqlalchemy.orm import Session
from datetime import date, timedelta
from fastapi import HTTPException
from sqlalchemy import func
from models.attendance_tracker import AttendanceTracker

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
        check_in_time=func.now(),  # stored as UTC
        working_status_id=req.working_status_id,
        remarks=req.remarks,
        created_by=1,             # REQUIRED by DB
        created_date=func.now(),
        is_active=True
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return build_response(attendance)


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

def today_status_controller(emp_id: int, db: Session):
    today = date.today()

    attendance = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == emp_id,
        AttendanceTracker.attendance_date == today
    ).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="No attendance for today")

    return build_response(attendance)


def get_attendance_by_emp_controller(emp_id: int, db: Session):
    records = db.query(AttendanceTracker).filter(
        AttendanceTracker.emp_id == emp_id
    ).order_by(AttendanceTracker.attendance_date.desc()).all()

    if not records:
        raise HTTPException(status_code=404, detail="No attendance records found")

    return [build_response(r) for r in records]

def delete_attendance_by_id_controller(attendance_id: int, db: Session):
    attendance = db.query(AttendanceTracker).filter(
        AttendanceTracker.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    db.delete(attendance)
    db.commit()

    return {
        "message": "Attendance record deleted successfully",
        "attendance_id": attendance_id
    }
