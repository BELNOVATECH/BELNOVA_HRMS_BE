from pydantic import BaseModel
from typing import List

class PendingReviewEmployee(BaseModel):
    employee_id: int
    employee_name: str
    designation_id: int

class PendingReviewResponse(BaseModel):
    total_pending_reviews: int
    employees: List[PendingReviewEmployee]
