from pydantic import BaseModel
from typing import Optional


class RoleCreate(BaseModel):
    role_name: str


class RoleUpdate(BaseModel):
    is_active: Optional[bool] = None


class RoleRead(BaseModel):
    id: int
    role_name: str
    is_active: bool

    class Config:
        from_attributes = True
