from fastapi import APIRouter
from typing import List
from schemas.payroll_schema import PayrollRequest, PayrollResponse
from services.payroll_service import (
    add_payroll_service,
    get_all_payrolls_service
)

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.post("/payslip", response_model=PayrollResponse)
def create_payslip(payload: PayrollRequest):
    return add_payroll_service(payload)


@router.get("/payslips", response_model=List[PayrollResponse])
def get_all_payslips():
    return get_all_payrolls_service()
