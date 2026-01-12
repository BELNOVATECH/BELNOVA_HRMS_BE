from sqlalchemy.orm import Session
from sqlalchemy import func
from models.employee_model import Employee

def get_monthly_payroll_cost(db: Session):
    total_ctc = (
        db.query(func.sum(Employee.ctc))
        .filter(Employee.is_active == True)  
        .scalar()
    )

    if not total_ctc:
        return 0

    monthly_cost = total_ctc / 12
    return round(monthly_cost, 2)
