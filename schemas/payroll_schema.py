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
    id: int
    emp_id: int
    month_id: int
    year_id: int

    total_days: Optional[int] = 0
    paid_days: Optional[int] = 0
    lop_days: Optional[int] = 0

    basic: Optional[Decimal] = Decimal("0.00")
    hra: Optional[Decimal] = Decimal("0.00")
    special_allowance: Optional[Decimal] = Decimal("0.00")

    total_earnings: Optional[Decimal] = Decimal("0.00")

    pf: Optional[Decimal] = Decimal("0.00")
    esic: Optional[Decimal] = Decimal("0.00")
    pt: Optional[Decimal] = Decimal("0.00")

    total_deductions: Optional[Decimal] = Decimal("0.00")
    net_pay: Optional[Decimal] = Decimal("0.00")

    period: Optional[str] = ""

    class Config:
        from_attributes = True   # SQLAlchemy → Pydantic