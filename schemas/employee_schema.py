from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class EmployeeBase(BaseModel):
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
    pay_method_id: Optional[int] = None

    bank_id: Optional[int] = None
    bank_ac_no: Optional[str] = None
    ifsc_code: Optional[str] = None

    pan: Optional[str] = None
    uan: Optional[str] = None
    esic: Optional[str] = None

    upload_doc: Optional[str] = None

    user_id: Optional[int] = None
    created_by: Optional[int] = None
    modified_by: Optional[int] = None
    is_active: Optional[bool] = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeRead(EmployeeBase):
    id: int
    created_date: Optional[datetime]
    modified_date: Optional[datetime]

    class Config:
        from_attributes = True
