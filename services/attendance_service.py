from sqlalchemy import select, and_
from models.generated_models import AttendanceTracker


def get_attendance_service(db, emp_id=None, from_date=None, to_date=None):

    conditions = []

    if emp_id:
        conditions.append(AttendanceTracker.emp_id == emp_id)

    if from_date:
        conditions.append(AttendanceTracker.attendance_date >= from_date)

    if to_date:
        conditions.append(AttendanceTracker.attendance_date <= to_date)

    stmt = select(AttendanceTracker)

    if conditions:
        stmt = stmt.where(and_(*conditions))

    result = db.execute(stmt)
    return result.scalars().all()
