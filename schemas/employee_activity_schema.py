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
    created_date: Optional[datetime] = None

    modified_by: Optional[int] = None
    modified_date: Optional[datetime] = None

    is_active: Optional[bool] = True


# ---------- RESPONSE ----------
from pydantic import BaseModel
from datetime import datetime
from typing import List


class EmployeeActivityResponse(BaseModel):
    id: int
    emp_id: int
    employee_first_name: str
    employee_last_name: str

    module_id: int
    module_name: str

    screen_id: int
    screen_name: str

    activity_description: str
    created_by: int
    created_date: datetime
    modified_by: int | None
    modified_date: datetime | None
    is_active: bool


class EmployeeActivityListResponse(BaseModel):
    total_records: int
    activities: List[EmployeeActivityResponse]
    message: str
