from pydantic import BaseModel, EmailStr
from datetime import date
from decimal import Decimal
from typing import List, Optional


class FamilyMemberCreate(BaseModel):
    relation_id: int
    first_name: str
    last_name: str
    date_of_birth: date
    occupation_id: int
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    present_address: str
    permanent_address: str
    bank_account: Optional[str] = None
    ifsc_code: Optional[str] = None
    pan: Optional[str] = None
    aadhaar: str


class EmployeeCreate(BaseModel):

    first_name: str
    last_name: str
    email: EmailStr
    mobile: str

    present_address: Optional[str] = None
    permanent_address: Optional[str] = None
    father_name: Optional[str] = None

    blood_group_id: Optional[int] = None
    gender_id: int
    marital_status_id: int

    date_of_birth: Optional[date] = None

    emergency_mobile: Optional[str] = None
    reference_mobile: Optional[str] = None
    aadhaar: Optional[str] = None

    emp_code: Optional[str] = None

    designation_id: int
    department_id: int
    employee_type_id: int

    manager_id: Optional[int] = None
    role_id: int

    work_location_id: Optional[int] = None
    shift_id: Optional[int] = None

    hired_date: Optional[date] = None
    join_date: date
    probation_end_date: Optional[date] = None

    salary: Decimal
    ctc: Decimal

    bank_id: Optional[int] = None
    bank_ac_no: Optional[str] = None
    ifsc_code: Optional[str] = None

    pan: Optional[str] = None
    uan: Optional[str] = None
    esic: Optional[str] = None

    upload_doc: Optional[str] = None

    created_by: Optional[int] = None

    family_members: List[FamilyMemberCreate] = []