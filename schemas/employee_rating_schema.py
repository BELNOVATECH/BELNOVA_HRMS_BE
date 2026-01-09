from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EmployeeRatingCreate(BaseModel):
    emp_id: int
    designation_id: int
    rating: float = Field(..., ge=1, le=5)
    reviewer_id: int
    created_by: Optional[int] = None
    created_date: Optional[datetime] = None
    is_active: Optional[bool] = True
