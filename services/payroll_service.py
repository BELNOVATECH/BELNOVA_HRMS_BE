# from sqlalchemy.orm import Session
# from datetime import date
# import calendar
# from decimal import Decimal

# from models.employee_model import Employee
# from models.leave_model import LeaveRequest
# from models.master_perc_cal_id import MasterPercCalId

# APPROVED_STATUS_ID = 11


# def get_payroll_preview(
#     emp_id: int,
#     db: Session,
#     month: int | None = None,
#     year: int | None = None
# ):
#     # =========================
#     # Month / Year handling
#     # =========================
#     today = date.today()
#     month = month or today.month
#     year = year or today.year

#     # =========================
#     # Employee
#     # =========================
#     emp = db.query(Employee).filter(Employee.id == emp_id).first()
#     if not emp:
#         raise Exception("Employee not found")

#     if not emp.ctc:
#         raise Exception("CTC not configured")

#     annual_ctc = Decimal(emp.ctc)
#     monthly_ctc = annual_ctc / Decimal("12")

#     # =========================
#     # Percentage Master
#     # =========================
#     perc = db.query(MasterPercCalId).filter(
#         MasterPercCalId.is_active == True
#     ).first()

#     if not perc:
#         raise Exception("Master percentage configuration missing")

#     # =========================
#     # Attendance (Leave only)
#     # =========================
#     total_days = calendar.monthrange(year, month)[1]

#     approved_leaves = (
#         db.query(LeaveRequest.total_days)
#         .filter(
#             LeaveRequest.emp_id == emp_id,
#             LeaveRequest.status_id == APPROVED_STATUS_ID,
#             LeaveRequest.is_active == True,
#             LeaveRequest.start_date.between(
#                 date(year, month, 1),
#                 date(year, month, total_days)
#             )
#         )
#         .all()
#     )

#     lop_days = sum(Decimal(str(l[0])) for l in approved_leaves)
#     paid_days = Decimal(total_days) - lop_days
#     if paid_days < 0:
#         paid_days = Decimal("0")

#     # =========================
#     # Earnings
#     # =========================
#     basic = monthly_ctc * Decimal(perc.basic_perc) / 100
#     hra = monthly_ctc * Decimal(perc.hra_perc) / 100
#     medical = monthly_ctc * Decimal(perc.medical_allowance_perc) / 100
#     special = monthly_ctc * Decimal(perc.special_allowance_perc) / 100
#     arrears = monthly_ctc * Decimal(perc.arrears_perc) / 100

#     gross_salary = basic + hra + medical + special + arrears

#     # =========================
#     # LOP calculation
#     # =========================
#     per_day_salary = gross_salary / Decimal(total_days)
#     lop_amount = per_day_salary * lop_days
#     gross_after_lop = gross_salary - lop_amount

#     # =========================
#     # Deductions
#     # =========================
#     basic_after_lop = basic / Decimal(total_days) * paid_days

#     pf = basic_after_lop * Decimal(perc.pf_perc) / 100
#     esic = gross_after_lop * Decimal(perc.esic_perc) / 100
#     pt = gross_after_lop * Decimal(perc.pt_perc) / 100
#     tds = gross_after_lop * Decimal(perc.tds_perc) / 100
#     other_deductions = gross_after_lop * Decimal(perc.other_deductions_perc) / 100

#     total_deductions = pf + esic + pt + tds + other_deductions

#     # =========================
#     # Net Salary
#     # =========================
#     net_salary = gross_after_lop - total_deductions
#     if net_salary < 0:
#         net_salary = Decimal("0.00")

#     # =========================
#     # Response
#     # =========================
#     return {
#         "employee": {
#             "id": emp.id,
#             "name": f"{emp.first_name} {emp.last_name}",
#             "emp_code": emp.emp_code,
#             "designation_id": emp.designation_id,

#             # ✅ FIXED — REAL DESIGNATION NAME
#             "designation_name": (
#                 emp.designation.designation_name
#                 if hasattr(emp, "designation") and emp.designation
#                 else None
#             ),

#             "join_date": emp.join_date,
#             "bank_account_no": emp.bank_ac_no,
#             "ifsc_code": emp.ifsc_code,
#             "uan": emp.uan,
#             "pan": emp.pan
#         },

#         "period": f"{month}/{year}",

#         "ctc": {
#             "annual": float(annual_ctc),
#             "monthly": round(float(monthly_ctc), 2)
#         },

#         "attendance": {
#             "total_days": total_days,
#             "paid_days": float(paid_days),
#             "lop_days": float(lop_days)
#         },

#         "earnings": {
#             "basic": round(float(basic), 2),
#             "hra": round(float(hra), 2),
#             "medical_allowance": round(float(medical), 2),
#             "special_allowance": round(float(special), 2),
#             "arrears": round(float(arrears), 2),
#             "gross_salary": round(float(gross_salary), 2),
#             "lop_amount": round(float(lop_amount), 2),
#             "gross_after_lop": round(float(gross_after_lop), 2)
#         },

#         "deductions": {
#             "pf": round(float(pf), 2),
#             "esic": round(float(esic), 2),
#             "pt": round(float(pt), 2),
#             "tds": round(float(tds), 2),
#             "other_deductions": round(float(other_deductions), 2),
#             "total_deductions": round(float(total_deductions), 2)
#         },

#         "net_salary": round(float(net_salary), 2)
#     }




from datetime import date
import calendar
from decimal import Decimal
from collections import defaultdict

from models.employee_model import Employee
from models.leave_model import LeaveRequest
from models.master_perc_cal_id import MasterPercCalId

APPROVED_STATUS_ID = 11


def get_payroll_preview(
    emp: Employee,                      
    perc: MasterPercCalId,              
    leave_map: dict,                   
    month: int,
    year: int
):
    if not emp.ctc:
        return None

    annual_ctc = Decimal(emp.ctc)
    monthly_ctc = annual_ctc / Decimal("12")

    total_days = calendar.monthrange(year, month)[1]

    lop_days = Decimal(leave_map.get(emp.id, 0))
    paid_days = Decimal(total_days) - lop_days
    if paid_days < 0:
        paid_days = Decimal("0")

    # =========================
    # Earnings
    # =========================
    basic = monthly_ctc * Decimal(perc.basic_perc) / 100
    hra = monthly_ctc * Decimal(perc.hra_perc) / 100
    medical = monthly_ctc * Decimal(perc.medical_allowance_perc) / 100
    special = monthly_ctc * Decimal(perc.special_allowance_perc) / 100
    arrears = monthly_ctc * Decimal(perc.arrears_perc) / 100

    gross_salary = basic + hra + medical + special + arrears

    # =========================
    # LOP
    # =========================
    per_day_salary = gross_salary / Decimal(total_days)
    lop_amount = per_day_salary * lop_days
    gross_after_lop = gross_salary - lop_amount

    # =========================
    # Deductions
    # =========================
    basic_after_lop = basic / Decimal(total_days) * paid_days

    pf = basic_after_lop * Decimal(perc.pf_perc) / 100
    esic = gross_after_lop * Decimal(perc.esic_perc) / 100
    pt = gross_after_lop * Decimal(perc.pt_perc) / 100
    tds = gross_after_lop * Decimal(perc.tds_perc) / 100
    other_deductions = gross_after_lop * Decimal(perc.other_deductions_perc) / 100

    total_deductions = pf + esic + pt + tds + other_deductions
    net_salary = gross_after_lop - total_deductions
    if net_salary < 0:
        net_salary = Decimal("0.00")

    # =========================
    # RESPONSE (UNCHANGED)
    # =========================
    return {
        "employee": {
            "id": emp.id,
            "name": f"{emp.first_name} {emp.last_name}",
            "emp_code": emp.emp_code,
            "designation_id": emp.designation_id,
            "designation_name": (
                emp.designation.designation_name
                if hasattr(emp, "designation") and emp.designation
                else None
            ),
            "join_date": emp.join_date,
            "bank_account_no": emp.bank_ac_no,
            "ifsc_code": emp.ifsc_code,
            "uan": emp.uan,
            "pan": emp.pan
        },
        "period": f"{month}/{year}",
        "ctc": {
            "annual": float(annual_ctc),
            "monthly": round(float(monthly_ctc), 2)
        },
        "attendance": {
            "total_days": total_days,
            "paid_days": float(paid_days),
            "lop_days": float(lop_days)
        },
        "earnings": {
            "basic": round(float(basic), 2),
            "hra": round(float(hra), 2),
            "medical_allowance": round(float(medical), 2),
            "special_allowance": round(float(special), 2),
            "arrears": round(float(arrears), 2),
            "gross_salary": round(float(gross_salary), 2),
            "lop_amount": round(float(lop_amount), 2),
            "gross_after_lop": round(float(gross_after_lop), 2)
        },
        "deductions": {
            "pf": round(float(pf), 2),
            "esic": round(float(esic), 2),
            "pt": round(float(pt), 2),
            "tds": round(float(tds), 2),
            "other_deductions": round(float(other_deductions), 2),
            "total_deductions": round(float(total_deductions), 2)
        },
        "net_salary": round(float(net_salary), 2)
    }
