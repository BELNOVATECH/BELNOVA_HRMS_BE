# schemas/employee_schema.py

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class EmployeeBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    address: Optional[str] = None
    civil_status_id: Optional[int] = None
    gender_id: Optional[int] = None
    mobile: Optional[str] = None
    date_of_birth: Optional[date] = None
    emergency_mobile: Optional[str] = None
    position_id: Optional[int] = None
    hired_date: Optional[date] = None
    pay_method_id: Optional[int] = None
    department_id: Optional[int] = None
    work_status_id: Optional[int] = None
    is_active: Optional[bool] = True
    created_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    user_id: Optional[int] = None
    created_by: Optional[int] = None
    modified_by: Optional[int] = None
    manager_id: Optional[int] = None
    email: Optional[str] = None
    salary: Optional[float] = None
    join_date: Optional[date] = None
    upload_doc: Optional[str] = None
    bank_id: Optional[int] = None
    bank_ac_no: Optional[str] = None
    ifsc_code: Optional[str] = None
    esic: Optional[str] = None
    pan: Optional[str] = None
    emp_code: Optional[str] = None
    uan: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeRead(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
