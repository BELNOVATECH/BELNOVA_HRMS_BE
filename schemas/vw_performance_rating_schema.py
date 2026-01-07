from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VwPerformanceRatingResponse(BaseModel):
    id: int
    emp_id: Optional[int]
    employee_name: Optional[str]
    designation_id: Optional[int]
    designation_name: Optional[str]   
    rating: Optional[float]
    reviewer_id: Optional[int]
    reviewer_name: Optional[str]
    created_date: Optional[datetime]

    class Config:
        from_attributes = True
