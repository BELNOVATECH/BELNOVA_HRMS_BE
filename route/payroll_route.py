from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from core.database import get_db
from models.employee_model import Employee
from services.payroll_service import get_payroll_preview

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.get("/calculate/{emp_id}")
def calculate_payroll(
    emp_id: int,
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None),
    db: Session = Depends(get_db)
):
    try:
        return get_payroll_preview(emp_id, db, month, year)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/calculate-all")
def calculate_all_payrolls(
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None),
    db: Session = Depends(get_db)
):
    try:
        employees = db.query(Employee).filter(Employee.is_active == True).all()

        results = []
        for emp in employees:
            results.append(
                get_payroll_preview(emp.id, db, month, year)
            )

        return results

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
