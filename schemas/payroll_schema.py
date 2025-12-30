from pydantic import BaseModel


class PayrollRequest(BaseModel):
    emp_id: int
    department_id: int
    basic_salary: float
    hra: float
    bonus: float
    pf: float
    esi: float
    other_deductions: float = 0.0
    net_salary: float


# SAME FIELDS FOR GET RESPONSE
class PayrollResponse(BaseModel):
    emp_id: int
    department_id: int
    basic_salary: float
    hra: float
    bonus: float
    pf: float
    esi: float
    other_deductions: float
    net_salary: float
