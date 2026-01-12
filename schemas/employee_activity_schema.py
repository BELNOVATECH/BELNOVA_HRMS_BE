from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# ---------- CREATE REQUEST ----------
class EmployeeActivityCreate(BaseModel):
    emp_id: int
    module_id: int
    screen_id: int
    activity_description: str

    created_by: int
    # created_date: Optional[datetime] = None

    modified_by: Optional[int] = None
    # modified_date: Optional[datetime] = None

    is_active: Optional[bool] = True


# ---------- RESPONSE ----------



class EmployeeActivityResponse(BaseModel):
    id: int

    emp_id: int
    employee_first_name: str
    employee_last_name: str

    created_by: int
    created_by_first_name: str
    created_by_last_name: str

    modified_by: Optional[int]
    modified_by_first_name: Optional[str]
    modified_by_last_name: Optional[str]

    module_id: int
    module_name: str

    screen_id: int
    screen_name: str

    activity_description: str
    created_date: datetime
    modified_date: Optional[datetime]
    is_active: bool


class EmployeeActivityListResponse(BaseModel):
    total_records: int
    activities: List[EmployeeActivityResponse]
    message: str