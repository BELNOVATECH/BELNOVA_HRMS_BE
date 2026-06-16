from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmployeeRatingCreate(BaseModel):
    emp_id: int
    designation_id: int
    rating: float
    reviewer_id: int
    created_by: Optional[int] = None
    created_date: Optional[datetime] = None
    is_active: Optional[bool] = True


class EmployeeRatingResponse(BaseModel):
    id: int
    emp_id: int
    designation_id: int
    rating: float
    reviewer_id: int

    class Config:
        from_attributes = True