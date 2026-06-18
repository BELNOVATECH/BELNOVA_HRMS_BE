from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import date
from decimal import Decimal


# =====================================================
# FAMILY MEMBER COMMON SCHEMA
# =====================================================

class FamilyMemberBase(BaseModel):
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


# =====================================================
# CREATE SCHEMAS
# =====================================================

class FamilyMemberCreate(FamilyMemberBase):
    pass


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


# =====================================================
# EMPLOYEE LIST RESPONSE
# =====================================================

class EmployeeListResponse(BaseModel):

    id: int

    emp_code: Optional[str] = None

    first_name: str
    last_name: Optional[str] = None

    email: Optional[str] = None
    mobile: Optional[str] = None

    department: Optional[str] = None
    designation_name: Optional[str] = None

    status_id: Optional[int] = None


# =====================================================
# FAMILY MEMBER RESPONSE
# =====================================================

class FamilyMemberResponse(FamilyMemberBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


# =====================================================
# DEPARTMENT RESPONSE
# =====================================================

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    department: str


# =====================================================
# DESIGNATION RESPONSE
# =====================================================

class DesignationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    designation_name: str


# =====================================================
# EMPLOYEE DETAILS RESPONSE
# =====================================================

class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    first_name: str
    last_name: Optional[str] = None

    email: Optional[EmailStr] = None
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

    salary: Optional[Decimal] = None
    ctc: Optional[Decimal] = None

    bank_id: Optional[int] = None
    bank_ac_no: Optional[str] = None
    ifsc_code: Optional[str] = None

    pan: Optional[str] = None
    uan: Optional[str] = None
    esic: Optional[str] = None

    upload_doc: Optional[str] = None

    status_id: Optional[int] = None

    department: Optional[DepartmentResponse] = None
    designation: Optional[DesignationResponse] = None

    employee_family_member: List[FamilyMemberResponse] = []



class MasterStatusResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    is_active: Optional[bool] = True