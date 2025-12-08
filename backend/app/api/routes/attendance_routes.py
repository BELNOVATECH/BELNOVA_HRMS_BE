from fastapi import APIRouter, HTTPException
from typing import List
from app.api.controllers.attendance_controller import (
    create_attendance,
    get_attendance,
    AttendanceCreate,
    AttendanceResponse
)

router = APIRouter()


@router.get("/", response_model=List[AttendanceResponse])
def fetch_attendance(emp_id: int = -1):
    return get_attendance(emp_id)


@router.post("/", response_model=dict)
def add_attendance(attendance: AttendanceCreate):
    # No conversion needed here; controller handles it
    try:
        return create_attendance(attendance)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
