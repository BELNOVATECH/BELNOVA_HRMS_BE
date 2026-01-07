
# from fastapi import APIRouter, Depends, HTTPException, Query
# from sqlalchemy.orm import Session, joinedload

# from core.database import get_db
# from models.employee_model import Employee
# from services.payroll_service import get_payroll_preview

# router = APIRouter(
#     prefix="/payroll",
#     tags=["Payroll"]
# )

# @router.get("/calculate/{emp_id}")
# def calculate_payroll_by_emp_id(
#     emp_id: int,
#     month: int | None = Query(None, ge=1, le=12),
#     year: int | None = Query(None),
#     db: Session = Depends(get_db)
# ):
#     try:
#         return get_payroll_preview(emp_id, db, month, year)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# @router.get("/calculate-all")
# def calculate_all_payrolls(
#     month: int | None = Query(None, ge=1, le=12),
#     year: int | None = Query(None),
#     db: Session = Depends(get_db)
# ):
#     try:
#         employees = db.query(Employee).filter(Employee.is_active == True).all()

#         results = []
#         for emp in employees:
#             results.append(
#                 get_payroll_preview(emp.id, db, month, year)  # ✅ FIX
#             )

#         return results

#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))




from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from collections import defaultdict

from core.database import get_db
from models.employee_model import Employee
from models.leave_model import LeaveRequest
from models.master_perc_cal_id import MasterPercCalId
from services.payroll_service import get_payroll_preview

router = APIRouter(prefix="/payroll", tags=["Payroll"])

APPROVED_STATUS_ID = 11


# ==========================================================
# CALCULATE PAYROLL BY EMPLOYEE ID
# ==========================================================
@router.get("/calculate/{emp_id}")
def calculate_by_emp_id(
    emp_id: int,
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None),
    db: Session = Depends(get_db)
):
    today = date.today()
    month = month or today.month
    year = year or today.year

    emp = (
        db.query(Employee)
        .filter(Employee.id == emp_id, Employee.is_active == True)
        .first()
    )

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    perc = (
        db.query(MasterPercCalId)
        .filter(MasterPercCalId.is_active == True)
        .first()
    )

    leave_rows = (
        db.query(LeaveRequest.total_days)
        .filter(
            LeaveRequest.emp_id == emp_id,
            LeaveRequest.status_id == APPROVED_STATUS_ID,
            LeaveRequest.is_active == True
        )
        .all()
    )

    leave_map = defaultdict(float)
    leave_map[emp_id] = sum(float(r[0]) for r in leave_rows)

    return get_payroll_preview(
        emp,
        perc,
        leave_map,
        month,
        year
    )


# ==========================================================
# CALCULATE PAYROLL FOR ALL EMPLOYEES
# ==========================================================
@router.get("/calculate-all")
def calculate_all(
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None),
    db: Session = Depends(get_db)
):
    today = date.today()
    month = month or today.month
    year = year or today.year

    perc = (
        db.query(MasterPercCalId)
        .filter(MasterPercCalId.is_active == True)
        .first()
    )

    employees = (
        db.query(Employee)
        .filter(Employee.is_active == True)
        .all()
    )

    leave_rows = (
        db.query(
            LeaveRequest.emp_id,
            LeaveRequest.total_days
        )
        .filter(
            LeaveRequest.status_id == APPROVED_STATUS_ID,
            LeaveRequest.is_active == True
        )
        .all()
    )

    leave_map = defaultdict(float)
    for emp_id, days in leave_rows:
        leave_map[emp_id] += float(days)

    results = []
    for emp in employees:
        data = get_payroll_preview(
            emp,
            perc,
            leave_map,
            month,
            year
        )
        if data:
            results.append(data)

    return results
