from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.attendance_request import AttendanceLoginRequest
from controller.attendance_controller import (
    login_controller,
    logout_controller,
     delete_attendance_by_id_controller 
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


# ✅ DELETE ATTENDANCE BY ID
@router.delete("/delete/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    return delete_attendance_by_id_controller(attendance_id, db)
