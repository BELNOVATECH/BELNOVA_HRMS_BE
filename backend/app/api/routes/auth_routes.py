from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from app.api.controllers.auth_controller import create_user, fetch_all_employees, login_user
from app.utils.date_utils import convert_date


router = APIRouter()


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    role_id: int
    gender_id: int
    mobile: str
    email: str
    password: str
    created_by: int
    civil_status_id: int
    position_id: int
    pay_method_id: int
    department_id: int
    work_status_id: int
    salary: float
    join_date: str
    emp_code: str | None = None
    dob: str | None = None
    emergency_mobile: str | None = None
    hired_date: str | None = None
    manager_id: int | None = None
    upload_doc: str | None = None
    bank_id: int | None = None
    bank_ac_no: str | None = None
    ifsc_code: str | None = None
    esic: str | None = None
    pan: str | None = None
    address: str | None = None

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/create/user")
def add_user(user: UserCreate):
    try:
        user.join_date = convert_date(user.join_date)
        user.dob = convert_date(user.dob)
        user.hired_date = convert_date(user.hired_date)

        result = create_user(user)

        print('result__________________')
        print(result)
        print('result__________________')

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/all-users")
def get_all_users():
    try:
        return fetch_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login(payload: LoginRequest):
    try:
        result = login_user(payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
