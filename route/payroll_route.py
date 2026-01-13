
# # from fastapi import APIRouter, Depends, HTTPException, Query
# # from sqlalchemy.orm import Session, joinedload

# # from core.database import get_db
# # from models.employee_model import Employee
# # from services.payroll_service import get_payroll_preview

# # router = APIRouter(
# #     prefix="/payroll",
# #     tags=["Payroll"]
# # )

# # @router.get("/calculate/{emp_id}")
# # def calculate_payroll_by_emp_id(
# #     emp_id: int,
# #     month: int | None = Query(None, ge=1, le=12),
# #     year: int | None = Query(None),
# #     db: Session = Depends(get_db)
# # ):
# #     try:
# #         return get_payroll_preview(emp_id, db, month, year)
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))


# # @router.get("/calculate-all")
# # def calculate_all_payrolls(
# #     month: int | None = Query(None, ge=1, le=12),
# #     year: int | None = Query(None),
# #     db: Session = Depends(get_db)
# # ):
# #     try:
# #         employees = db.query(Employee).filter(Employee.is_active == True).all()

# #         results = []
# #         for emp in employees:
# #             results.append(
# #                 get_payroll_preview(emp.id, db, month, year)  # ✅ FIX
# #             )

# #         return results

# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))




# from fastapi import APIRouter, Depends, HTTPException, Query
# from sqlalchemy.orm import Session
# from datetime import date
# from collections import defaultdict

# from core.database import get_db
# from models.employee_model import Employee
# from models.leave_model import LeaveRequest
# from models.master_perc_cal_id import MasterPercCalId
# from services.payroll_service import get_payroll_preview

# router = APIRouter(prefix="/payroll", tags=["Payroll"])

# APPROVED_STATUS_ID = 11


# # ==========================================================
# # CALCULATE PAYROLL BY EMPLOYEE ID
# # ==========================================================
# @router.get("/calculate/{emp_id}")
# def calculate_by_emp_id(
#     emp_id: int,
#     month: int | None = Query(None, ge=1, le=12),
#     year: int | None = Query(None),
#     db: Session = Depends(get_db)
# ):
#     today = date.today()
#     month = month or today.month
#     year = year or today.year

#     emp = (
#         db.query(Employee)
#         .filter(Employee.id == emp_id, Employee.is_active == True)
#         .first()
#     )

#     if not emp:
#         raise HTTPException(status_code=404, detail="Employee not found")

#     perc = (
#         db.query(MasterPercCalId)
#         .filter(MasterPercCalId.is_active == True)
#         .first()
#     )

#     leave_rows = (
#         db.query(LeaveRequest.total_days)
#         .filter(
#             LeaveRequest.emp_id == emp_id,
#             LeaveRequest.status_id == APPROVED_STATUS_ID,
#             LeaveRequest.is_active == True
#         )
#         .all()
#     )

#     leave_map = defaultdict(float)
#     leave_map[emp_id] = sum(float(r[0]) for r in leave_rows)

#     return get_payroll_preview(
#         emp,
#         perc,
#         leave_map,
#         month,
#         year
#     )


# # ==========================================================
# # CALCULATE PAYROLL FOR ALL EMPLOYEES
# # ==========================================================
# @router.get("/calculate-all")
# def calculate_all(
#     month: int | None = Query(None, ge=1, le=12),
#     year: int | None = Query(None),
#     db: Session = Depends(get_db)
# ):
#     today = date.today()
#     month = month or today.month
#     year = year or today.year

#     perc = (
#         db.query(MasterPercCalId)
#         .filter(MasterPercCalId.is_active == True)
#         .first()
#     )

#     employees = (
#         db.query(Employee)
#         .filter(Employee.is_active == True)
#         .all()
#     )

#     leave_rows = (
#         db.query(
#             LeaveRequest.emp_id,
#             LeaveRequest.total_days
#         )
#         .filter(
#             LeaveRequest.status_id == APPROVED_STATUS_ID,
#             LeaveRequest.is_active == True
#         )
#         .all()
#     )

#     leave_map = defaultdict(float)
#     for emp_id, days in leave_rows:
#         leave_map[emp_id] += float(days)

#     results = []
#     for emp in employees:
#         data = get_payroll_preview(
#             emp,
#             perc,
#             leave_map,
#             month,
#             year
#         )
#         if data:
#             results.append(data)

#     return results

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from collections import defaultdict

from core.database import get_db

from models.payroll_model import Payroll
from models.employee_model import Employee
from models.master_month import MasterMonth
from models.master_year import MasterYear
from models.master_perc_cal_id import MasterPercCalId
from models.leave_model import LeaveRequest

from services.payroll_service import get_payroll_preview

router = APIRouter(prefix="/payroll", tags=["Payroll"])

APPROVED_STATUS_ID = 2


# ==========================================================
# HELPERS
# ==========================================================
def is_future_month_year(month_id: int, year_id: int, db: Session) -> bool:
    month = db.query(MasterMonth).filter(MasterMonth.id == month_id).first()
    year = db.query(MasterYear).filter(MasterYear.id == year_id).first()

    if not month or not year:
        raise HTTPException(status_code=404, detail="Invalid month or year")

    today = date.today()
    year_value = int(year.year_name)
    month_value = month.id

    return (year_value > today.year) or (
        year_value == today.year and month_value > today.month
    )


def build_response(emp: Employee, payroll: Payroll, month: MasterMonth, year: MasterYear):
    return {
        "employee": {
            "id": emp.id,
            "name": emp.first_name,
            "emp_code": emp.emp_code,
            "designation_id": emp.designation_id,
            "designation_name": emp.designation_name,
            "join_date": emp.join_date,
            "bank_account_no": emp.bank_ac_no,
            "ifsc_code": emp.ifsc_code,
            "uan": emp.uan,
            "pan": emp.pan,
        },
        "period": f"{month.id}/{year.year_name}",
        "attendance": {
            "total_days": payroll.total_days,
            "paid_days": payroll.paid_days,
            "lop_days": payroll.lop_days,
        },
        "earnings": {
            "basic": float(payroll.basic),
            "hra": float(payroll.hra),
            "medical_allowance": float(payroll.medical_allowance),
            "special_allowance": float(payroll.special_allowance),
            "arrears": float(payroll.arrears),
            "gross_salary": float(payroll.total_earnings),
            "gross_after_lop": float(payroll.gross_earning),
        },
        "deductions": {
            "pf": float(payroll.pf),
            "esic": float(payroll.esic),
            "pt": float(payroll.pt),
            "tds": float(payroll.tds),
            "other_deductions": float(payroll.other_deductions),
            "total_deductions": float(payroll.total_deductions),
        },
        "net_salary": float(payroll.net_pay),
        "net_pay_in_words": payroll.net_pay_in_words,   # ✅ ADDED
    }


# ==========================================================
# CALCULATE / GET PAYSLIP BY EMPLOYEE
# ==========================================================
@router.get("/calculate/{emp_id}")
def get_payslip_by_employee(
    emp_id: int,
    month_id: int | None = Query(None),
    year_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    today = date.today()

    if month_id is None:
        month_id = today.month

    if year_id is None:
        year_obj = (
            db.query(MasterYear)
            .filter(MasterYear.year_name == str(today.year))
            .first()
        )
        if not year_obj:
            raise HTTPException(status_code=400, detail="Current year not found")
        year_id = year_obj.id

    if is_future_month_year(month_id, year_id, db):
        raise HTTPException(status_code=400, detail="Future month/year not allowed")

    emp = (
        db.query(Employee)
        .filter(Employee.id == emp_id, Employee.is_active == True)
        .first()
    )
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    month = db.query(MasterMonth).filter(MasterMonth.id == month_id).first()
    year = db.query(MasterYear).filter(MasterYear.id == year_id).first()

    if not month or not year:
        raise HTTPException(status_code=404, detail="Invalid month or year")

    existing = (
        db.query(Payroll)
        .filter(
            Payroll.emp_id == emp_id,
            Payroll.month_id == month_id,
            Payroll.year_id == year_id,
            Payroll.is_active == True,
        )
        .first()
    )

    if existing:
        return build_response(emp, existing, month, year)

    perc = (
        db.query(MasterPercCalId)
        .filter(MasterPercCalId.is_active == True)
        .first()
    )
    if not perc:
        raise HTTPException(status_code=400, detail="Percentage config not found")

    preview = get_payroll_preview(
        emp=emp,
        perc=perc,
        leave_map={},
        month=month.id,
        year=int(year.year_name),
    )

    if not preview:
        raise HTTPException(status_code=400, detail="Payroll calculation failed")

    payroll = Payroll(
        emp_id=emp.id,
        month_id=month_id,
        year_id=year_id,

        total_days=preview["attendance"]["total_days"],
        paid_days=preview["attendance"]["paid_days"],
        lop_days=preview["attendance"]["lop_days"],

        basic=preview["earnings"]["basic"],
        conveyance=0,
        hra=preview["earnings"]["hra"],
        medical_allowance=preview["earnings"]["medical_allowance"],
        special_allowance=preview["earnings"]["special_allowance"],
        arrears=preview["earnings"]["arrears"],

        total_earnings=preview["earnings"]["gross_salary"],

        pf=preview["deductions"]["pf"],
        esic=preview["deductions"]["esic"],
        pt=preview["deductions"]["pt"],
        tds=preview["deductions"]["tds"],
        other_deductions=preview["deductions"]["other_deductions"],

        total_deductions=preview["deductions"]["total_deductions"],
        gross_earning=preview["earnings"]["gross_after_lop"],
        deduction=preview["deductions"]["total_deductions"],

        net_pay=preview["net_salary"],
        net_pay_in_words=preview["net_pay_in_words"],  # ✅ FIX
        created_by=emp.id,
        perc_cal_id=perc.id,
    )

    db.add(payroll)
    db.commit()
    db.refresh(payroll)

    return build_response(emp, payroll, month, year)


# ==========================================================
# CALCULATE PAYROLL FOR ALL EMPLOYEES (PREVIEW ONLY)
# ==========================================================
@router.get("/calculate-all")
def calculate_all(
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None),
    db: Session = Depends(get_db),
):
    today = date.today()
    month = month or today.month
    year = year or today.year

    perc = (
        db.query(MasterPercCalId)
        .filter(MasterPercCalId.is_active == True)
        .first()
    )
    if not perc:
        raise HTTPException(status_code=400, detail="Percentage config not found")

    employees = db.query(Employee).filter(Employee.is_active == True).all()

    leave_rows = (
        db.query(LeaveRequest.emp_id, LeaveRequest.total_days)
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
        preview = get_payroll_preview(
            emp=emp,
            perc=perc,
            leave_map=leave_map,
            month=month,
            year=year
        )
        if preview:
            results.append(preview)

    return {
        "month": month,
        "year": year,
        "total_employees": len(results),
        "payroll": results
    }

