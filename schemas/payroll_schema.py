# from pydantic import BaseModel


# class PayrollRequest(BaseModel):
#     emp_id: int
#     department_id: int
#     basic_salary: float
#     hra: float
#     bonus: float
#     pf: float
#     esi: float
#     other_deductions: float = 0.0
#     net_salary: float


# # SAME FIELDS FOR GET RESPONSE
# class PayrollResponse(BaseModel):
#     emp_id: int
#     department_id: int
#     basic_salary: float
#     hra: float
#     bonus: float
#     pf: float
#     esi: float
#     other_deductions: float
#     net_salary: float


from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

# ---------- REQUEST ----------
class PayrollRequest(BaseModel):
    employee_id: int
    month: int
    year: int

class PayrollResponse(BaseModel):
    emp_id: int
    month_id: int
    year_id: int

    total_days: int
    paid_days: int
    lop_days: int

    basic: Decimal
    hra: Decimal
    medical_allowance: Decimal
    special_allowance: Decimal
    arrears: Decimal

    total_earnings: Decimal

    pf: Decimal
    esic: Decimal
    pt: Decimal
    tds: Decimal
    other_deductions: Decimal

    total_deductions: Decimal
    net_pay: Decimal
    net_pay_in_words: Optional[str]   # ✅ IMPORTANT

    class Config:
        from_attributes = True