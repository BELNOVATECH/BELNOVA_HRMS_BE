from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.attendance_schema import (
    AttendanceLoginRequest,
    AttendanceResponse
)
from controller.attendance_controller import (
    login_controller,
    logout_controller,
    today_status_controller,
    get_attendance_by_emp_controller,
    delete_attendance_by_id_controller
)
from core.database import get_db

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/login", response_model=AttendanceResponse)
def attendance_login(
    req: AttendanceLoginRequest,
    db: Session = Depends(get_db)
):
    return login_controller(req, db)


@router.put("/logout/{emp_id}", response_model=AttendanceResponse)
def attendance_logout(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return logout_controller(emp_id, db)


@router.get("/status/{emp_id}", response_model=AttendanceResponse)
def today_login_status(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return today_status_controller(emp_id, db)




# ✅ DELETE ATTENDANCE BY ID
@router.delete("/delete/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    return delete_attendance_by_id_controller(attendance_id, db)
