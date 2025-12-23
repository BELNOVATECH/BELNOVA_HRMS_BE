from pydantic import BaseModel


class DepartmentCreateRequest(BaseModel):
    department: str


class IsActiveUpdate(BaseModel):
    is_active: bool


class DepartmentResponse(BaseModel):
    id: int
    department: str
    is_active: bool

    class Config:
        from_attributes = True
