from pydantic import BaseModel
from typing import Optional


class JobTitleCreate(BaseModel):
    designation_id: int
    department_id: int
    status_id: int


class JobOpeningUpdate(BaseModel):
    designation_id: int
    department_id: int
    status_id: int
    is_active: Optional[bool] = None


class JobOpeningIsActiveUpdate(BaseModel):
    is_active: bool


class JobOpeningResponse(BaseModel):
    id: int
    designation_id: int
    department_id: int
    status_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }
