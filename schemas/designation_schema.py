from pydantic import BaseModel

class DesignationCreate(BaseModel):
    designation_name: str
    dept_id: int


class DesignationResponse(BaseModel):
    id: int
    designation_name: str
    dept_id: int
    is_active: bool

    class Config:
        from_attributes = True


class DesignationStatusUpdate(BaseModel):
    is_active: bool
