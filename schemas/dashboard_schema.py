from pydantic import BaseModel
from typing import List


class SimpleEmployee(BaseModel):
    id: int
    name: str


class UninformedEmployee(BaseModel):
    id: int
    name: str
    designation_id: int


class EmployeeBlock(BaseModel):
    count: int
    employees: List[SimpleEmployee]


class UninformedLeaveBlock(BaseModel):
    count: int
    employees: List[UninformedEmployee]


class DashboardResponse(BaseModel):
    total_employees: EmployeeBlock
    active_employees: EmployeeBlock
    inactive_employees: EmployeeBlock
    uninformed_leaves: UninformedLeaveBlock
