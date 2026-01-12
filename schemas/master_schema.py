from pydantic import BaseModel
from typing import Optional

# -------- MODULE --------
class MasterModuleResponse(BaseModel):
    id: int
    module_name: str
    is_active: bool

    class Config:
        from_attributes = True


# -------- SCREEN --------
class MasterScreenResponse(BaseModel):
    id: int
    screen_name: str
    module_id: int
    is_active: bool

    class Config:
        from_attributes = True


# -------- PERMISSION CREATE --------
class MasterScreenPermissionCreate(BaseModel):
    role_id: int
    module_id: int
    screen_id: Optional[int] = None

    can_view: bool = False
    can_edit: bool = False
    can_delete: bool = False
    can_access: bool = False
    can_update: bool = False

    is_active: bool = True


# -------- PERMISSION UPDATE (FIXED) --------
class MasterScreenPermissionBulkUpdate(BaseModel):
    id: int
    role_id: int
    module_id: int
    screen_id: Optional[int] = None

    can_view: bool
    can_edit: bool
    can_delete: bool
    can_access: bool
    can_update: bool
    is_active: bool


# -------- RESPONSE --------
class MasterScreenPermissionResponse(MasterScreenPermissionCreate):
    id: int

    class Config:
        from_attributes = True
