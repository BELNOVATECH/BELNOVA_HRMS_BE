from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TopPerformerResponse(BaseModel):
    emp_id: int
    designation_id: int
    rating: float
    created_date: Optional[datetime]

    class Config:
        from_attributes = True
