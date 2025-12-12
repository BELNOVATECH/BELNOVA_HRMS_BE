from fastapi import APIRouter, Depends, Query, HTTPException
from core.database import get_db
from controller.attendance_controller import get_attendance_controller
from schemas.attendance_schema import AttendanceRead
from typing import Optional, List
from datetime import date

attendance_router = APIRouter()


@attendance_router.get("/", response_model=List[AttendanceRead])
def get_attendance(
    emp_id: Optional[int] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    export: bool = Query(False, description="Export to Excel"),
    db=Depends(get_db)
):

    if export:
        # REMOVE RESPONSE MODEL IN EXPORT MODE
        return get_attendance_controller(
            db, emp_id=emp_id, from_date=from_date, to_date=to_date, export=True
        )

    return get_attendance_controller(
        db, emp_id=emp_id, from_date=from_date, to_date=to_date, export=False
    )
