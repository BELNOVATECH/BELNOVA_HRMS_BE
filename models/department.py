from pydantic import BaseModel

class DepartmentCreateRequest(BaseModel):
    department: str

class DepartmentResponse(BaseModel):
    id: int
    department: str
    is_active: bool = True


class IsActiveUpdate(BaseModel):
    is_active: bool