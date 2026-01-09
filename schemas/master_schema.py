from pydantic import BaseModel
from typing import Optional

# -------- MODULE --------
class MasterModuleCreate(BaseModel):
    module_name: str
    fa_fa_icon: Optional[str] = None
    routes: Optional[str] = None
    order_by: Optional[int] = None
    is_active: Optional[bool] = True

class MasterModuleResponse(MasterModuleCreate):
    id: int
    class Config:
        from_attributes = True


# -------- SCREEN --------
from pydantic import BaseModel
from typing import Optional

class MasterScreenResponse(BaseModel):
    id: int
    screen_name: str
    screen_label: Optional[str] = None
    fa_fa_icon: Optional[str] = None
    routes: Optional[str] = None
    module_id: int
    order_by: Optional[int] = None
    is_active: bool

    class Config:
        from_attributes = True



# -------- PERMISSION --------
class MasterScreenPermissionCreate(BaseModel):
    role_id: int
    module_id: int
    screen_id: Optional[int] = None   # ✅ FIX

    can_view: bool = False
    can_edit: bool = False
    can_delete: bool = False
    can_access: bool = False
    can_update: bool = False

    is_active: Optional[bool] = True


class MasterScreenPermissionResponse(MasterScreenPermissionCreate):
    id: int
    class Config:
        from_attributes = True
