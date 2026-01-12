
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.payroll_services_cost import get_monthly_payroll_cost



router = APIRouter(prefix="/payroll", tags=["Payroll"])

@router.get("/cost")
def get_payroll_cost(db: Session = Depends(get_db)):
    payroll_cost = get_monthly_payroll_cost(db)
    return {
        "status": "success",
        "payroll_cost": payroll_cost
    }