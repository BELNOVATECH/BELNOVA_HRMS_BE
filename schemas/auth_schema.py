# schemas/auth_schema.py

from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    role_id: int
    mobile: str
    email: EmailStr
    password: str

    gender_id: Optional[int] = None
    dob: Optional[date] = None
    address: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    mobile: str

    class Config:
        from_attributes = True

# 🔥 THIS WAS MISSING
class LoginRequest(BaseModel):
    email: str
    password: str


class ScreenPermission(BaseModel):
    module_id: int
    module_name: str
    screen_id: int
    screen_name: str
    role_id: int
    role_name: str
    can_view: bool
    can_edit: bool
    can_delete: bool
    can_update: bool
    can_access: bool


class LoginResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    role_id: int
    role_name: str
    permissions: List[ScreenPermission]
    token: str
