from pydantic import BaseModel
from typing import List


class LeaveBalanceItem(BaseModel):
    leave_type_id: int
    leave_type: str
    granted: float
    consumed: float
    balance: float


class LeaveBalanceResponse(BaseModel):
    emp_id: int
    year: int
    leaves: List[LeaveBalanceItem]
