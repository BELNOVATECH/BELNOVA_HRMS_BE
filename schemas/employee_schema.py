from pydantic import BaseModel
from datetime import date
from typing import Optional, List

from schemas.employee_family_schema import (
    FamilyMemberCreate,
    FamilyMemberResponse
)

# ---------- CREATE ----------
class EmployeeCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None

    present_address: Optional[str] = None
    permanent_address: Optional[str] = None

    father_name: Optional[str] = None
    blood_group_id: Optional[int] = None
    gender_id: Optional[int] = None
    marital_status_id: Optional[int] = None
    date_of_birth: Optional[date] = None

    emergency_mobile: Optional[str] = None
    reference_mobile: Optional[str] = None
    aadhaar: Optional[str] = None

    emp_code: Optional[str] = None
    designation_id: Optional[int] = None
    department_id: Optional[int] = None
    employee_type_id: Optional[int] = None
    manager_id: Optional[int] = None
    role_id: Optional[int] = None
    work_location_id: Optional[int] = None
    shift_id: Optional[int] = None

    hired_date: Optional[date] = None
    join_date: Optional[date] = None
    probation_end_date: Optional[date] = None

    salary: Optional[float] = None
    ctc: Optional[float] = None

    bank_id: Optional[int] = None
    bank_ac_no: Optional[str] = None
    ifsc_code: Optional[str] = None

    pan: Optional[str] = None
    uan: Optional[str] = None
    esic: Optional[str] = None

    upload_doc: Optional[str] = None
    created_by: Optional[int] = None
    user_id: Optional[int] = None

    # 🔥 SINGLE FAMILY INPUT
    family_member: FamilyMemberCreate

    class Config:
        extra = "forbid"


class EmployeeCreateResponse(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: Optional[str]
    mobile: Optional[str]

    present_address: Optional[str]
    permanent_address: Optional[str]

    father_name: Optional[str]
    blood_group_id: Optional[int]
    gender_id: Optional[int]
    marital_status_id: Optional[int]
    date_of_birth: Optional[date]

    emergency_mobile: Optional[str]
    reference_mobile: Optional[str]
    aadhaar: Optional[str]

    emp_code: Optional[str]
    designation_id: Optional[int]
    department_id: Optional[int]
    employee_type_id: Optional[int]
    manager_id: Optional[int]
    role_id: Optional[int]
    work_location_id: Optional[int]
    shift_id: Optional[int]

    hired_date: Optional[date]
    join_date: Optional[date]
    probation_end_date: Optional[date]

    salary: Optional[float]
    ctc: Optional[float]

    bank_id: Optional[int]
    bank_ac_no: Optional[str]
    ifsc_code: Optional[str]

    pan: Optional[str]
    uan: Optional[str]
    esic: Optional[str]

    upload_doc: Optional[str]
    created_by: Optional[int]
    user_id: Optional[int]

    is_active: bool

    # ✅ OPTIONAL
    family_member: Optional[FamilyMemberResponse] = None

    class Config:
        from_attributes = True


class EmployeeStatusUpdate(BaseModel):
    is_active: bool


class EmployeeStatusResponse(BaseModel):
    emp_id: int
    first_name: str
    last_name: Optional[str]
    is_active: bool
