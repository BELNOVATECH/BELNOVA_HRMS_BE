# from pydantic import BaseModel
# from datetime import date, datetime
# from typing import Optional, List

# from schemas.employee_family_schema import FamilyMemberCreate


# class EmployeeBase(BaseModel):
#     first_name: str
#     last_name: Optional[str] = None
#     email: Optional[str] = None
#     mobile: Optional[str] = None

#     present_address: Optional[str] = None
#     permanent_address: Optional[str] = None

#     father_name: Optional[str] = None
#     blood_group_id: Optional[int] = None
#     gender_id: Optional[int] = None
#     marital_status_id: Optional[int] = None
#     date_of_birth: Optional[date] = None
#     emergency_mobile: Optional[str] = None
#     reference_mobile: Optional[str] = None
#     aadhaar: Optional[str] = None

#     emp_code: Optional[str] = None
#     designation_id: Optional[int] = None
#     department_id: Optional[int] = None
#     employee_type_id: Optional[int] = None
#     manager_id: Optional[int] = None
#     role_id: Optional[int] = None
#     work_location_id: Optional[int] = None
#     shift_id: Optional[int] = None

#     hired_date: Optional[date] = None
#     join_date: Optional[date] = None
#     probation_end_date: Optional[date] = None

#     salary: Optional[float] = None
#     ctc: Optional[float] = None
#     pay_method_id: Optional[int] = None

#     bank_id: Optional[int] = None
#     bank_ac_no: Optional[str] = None
#     ifsc_code: Optional[str] = None

#     pan: Optional[str] = None
#     uan: Optional[str] = None
#     esic: Optional[str] = None

#     upload_doc: Optional[str] = None

#     user_id: Optional[int] = None
#     created_by: Optional[int] = None
#     modified_by: Optional[int] = None
#     is_active: Optional[bool] = True


# class EmployeeCreate(EmployeeBase):
#     family_member: Optional[List[FamilyMemberCreate]] = []


# class EmployeeRead(EmployeeBase):
#     id: int
#     created_date: Optional[datetime]
#     modified_date: Optional[datetime]

#     class Config:
#         from_attributes = True


# class EmployeeStatusUpdate(BaseModel):
#     is_active: bool


# class EmployeeStatusResponse(BaseModel):
#     emp_id: int
#     first_name: str
#     last_name: Optional[str] = None
#     is_active: bool


from pydantic import BaseModel
from datetime import date
from typing import Optional, List


# ---------- FAMILY ----------
class FamilyMemberCreate(BaseModel):
    relation_id: int
    first_name: str
    last_name: Optional[str] = None
    date_of_birth: date
    occupation_id: int

    phone: Optional[str] = None
    email: Optional[str] = None

    present_address: str
    permanent_address: str

    bank_account: Optional[str] = None
    ifsc_code: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None


class FamilyMemberRead(FamilyMemberCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


# ---------- EMPLOYEE ----------
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

    # ✅ mandatory
    family_member: FamilyMemberCreate

    class Config:
        extra = "forbid"


class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: Optional[str]
    mobile: Optional[str]
    is_active: bool

    family_members: List[FamilyMemberRead] = []

    class Config:
        from_attributes = True


class EmployeeStatusUpdate(BaseModel):
    is_active: bool


class EmployeeStatusResponse(BaseModel):
    emp_id: int
    first_name: str
    last_name: Optional[str]
    is_active: bool
