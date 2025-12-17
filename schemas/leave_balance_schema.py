from pydantic import BaseModel
from typing import List


class LeaveBalanceRequest(BaseModel):
    emp_id: int
    year: int
    month: int
    offset: int = 0


class LeaveBalanceItem(BaseModel):
    leave_type_id: int
    leave_type: str
    granted: float
    consumed: float
    balance: float


class LeaveBalanceResponse(BaseModel):
    emp_id: int
    year: int
    month: int
    leaves: List[LeaveBalanceItem]
