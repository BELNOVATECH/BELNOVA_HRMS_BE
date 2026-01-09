from pydantic import BaseModel
from typing import List


class LoginRequest(BaseModel):
    email: str
    password: str


class ScreenPermission(BaseModel):
    module_id: int
    module_name: str
    screen_id: int
    screen_name: str
    can_view: bool
    can_edit: bool
    can_delete: bool
    can_update: bool
    can_access: bool


class LoginResponse(BaseModel):
    user_id: int
    role_id: int
    role_name: str
    permissions: List[ScreenPermission]
    token: str
