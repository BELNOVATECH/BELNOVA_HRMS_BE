from typing import List
from schemas.payroll_schema import PayrollRequest, PayrollResponse

# 🔥 IN-MEMORY STORE
PAYROLL_STORE: List[PayrollResponse] = []


def add_payroll_service(payload: PayrollRequest) -> PayrollResponse:
    payroll = PayrollResponse(
        emp_id=payload.emp_id,
        department_id=payload.department_id,
        basic_salary=payload.basic_salary,
        hra=payload.hra,
        bonus=payload.bonus,
        pf=payload.pf,
        esi=payload.esi,
        other_deductions=payload.other_deductions,
        net_salary=payload.net_salary
    )

    PAYROLL_STORE.append(payroll)
    return payroll


def get_all_payrolls_service() -> List[PayrollResponse]:
    return PAYROLL_STORE
