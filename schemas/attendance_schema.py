from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime, timedelta

# =====================================
# REQUEST SCHEMA (LOGIN)
# =====================================
class AttendanceLoginRequest(BaseModel):
    emp_id: int
    working_status_id: int = 1
    remarks: Optional[str] = None


# =====================================
# RESPONSE SCHEMA (LOGIN / LOGOUT)
# =====================================
class AttendanceResponse(BaseModel):
    id: int
    emp_id: int
    date: date
    login_time: Optional[str]
    logout_time: Optional[str]
    working_hours: Optional[str]
    status: str
    remarks: Optional[str]
    is_active: bool


# =====================================
# READ / REPORT SCHEMA
# =====================================
class AttendanceRead(BaseModel):
    id: int
    emp_id: int
    attendance_date: date
    check_in_time: Optional[str]
    check_out_time: Optional[str]
    working_status_id: Optional[int]
    working_hours: Optional[float]
    remarks: Optional[str]
    created_by: Optional[int]

    class Config:
        from_attributes = True

    # -------- SERIALIZERS --------
    @staticmethod
    def serialize_time(value):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value

    @staticmethod
    def serialize_hours(value):
        if isinstance(value, timedelta):
            return value.total_seconds() / 3600
        return value

    @classmethod
    def model_validate(cls, obj):
        data = {
            "id": obj.id,
            "emp_id": obj.emp_id,
            "attendance_date": obj.attendance_date,
            "check_in_time": cls.serialize_time(obj.check_in_time),
            "check_out_time": cls.serialize_time(obj.check_out_time),
            "working_status_id": obj.working_status_id,
            "working_hours": cls.serialize_hours(obj.working_hours),
            "remarks": obj.remarks,
            "created_by": obj.created_by,
        }
        return super().model_validate(data)
