from pydantic import BaseModel

class LeaveBalanceRequest(BaseModel):
    emp_id: int
