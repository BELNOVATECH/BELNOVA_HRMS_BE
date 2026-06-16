from pydantic import BaseModel
from typing import Optional


class EmployeeActivityCreate(BaseModel):
    emp_id: int
    module_id: int
    screen_id: int
    activity_description: str

    created_by: int

    modified_by: Optional[int] = None

    is_active: bool = True