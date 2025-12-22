from pydantic import BaseModel
from typing import Optional

class DesignationCreate(BaseModel):
    designation_name: str
    dept_id: int
    is_active: Optional[bool] = True


class DesignationRead(BaseModel):
    id: int
    designation_name: str
    dept_id: Optional[int] = None
    is_active: bool

    model_config = {
        "from_attributes": True
    }
