from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import date

from core.database import get_db
from schemas.attendance_request import AttendanceLoginRequest
from schemas.attendance_schema import AttendanceRead
from controller.attendance_controller import (
    login_controller,
    logout_controller,
    delete_attendance_by_id_controller,
    get_attendance_controller
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/login")
def login_route(
    req: AttendanceLoginRequest,
    db: Session = Depends(get_db)
):
    return login_controller(req, db)


@router.post("/logout/{emp_id}")
def logout_route(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return logout_controller(emp_id, db)


@router.get("/", response_model=List[AttendanceRead])
def get_attendance(
    emp_id: Optional[int] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    export: bool = Query(False, description="Export attendance to Excel"),
    db: Session = Depends(get_db)
):
    if export:
        # IMPORTANT: no response_model when exporting
        return get_attendance_controller(
            db,
            emp_id=emp_id,
            from_date=from_date,
            to_date=to_date,
            export=True
        )

    return get_attendance_controller(
        db,
        emp_id=emp_id,
        from_date=from_date,
        to_date=to_date,
        export=False
    )


@router.delete("/delete/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    return delete_attendance_by_id_controller(attendance_id, db)
