from sqlalchemy.orm import Session
from sqlalchemy import distinct

from models.employee_model import Employee
from models.attendance_tracker import AttendanceTracker
from models.leave_model import LeaveRequest


def get_dashboard_data_service(db: Session):
    # ---------------- TOTAL ----------------
    total_emps = db.query(Employee).all()
    total_list = [
        {"id": e.id, "name": f"{e.first_name} {e.last_name or ''}".strip()}
        for e in total_emps
    ]

    # ---------------- ACTIVE ----------------
    active_emps = db.query(Employee).filter(Employee.is_active == True).all()
    active_list = [
        {"id": e.id, "name": f"{e.first_name} {e.last_name or ''}".strip()}
        for e in active_emps
    ]

    # ---------------- INACTIVE ----------------
    inactive_emps = db.query(Employee).filter(Employee.is_active == False).all()
    inactive_list = [
        {"id": e.id, "name": f"{e.first_name} {e.last_name or ''}".strip()}
        for e in inactive_emps
    ]

    # ---------------- UNINFORMED LEAVES ----------------
    inactive_attendance_emp_ids = (
        db.query(distinct(AttendanceTracker.emp_id))
        .filter(AttendanceTracker.is_active == False)
        .subquery()
    )

    leave_emp_ids = (
        db.query(distinct(LeaveRequest.emp_id))
        .subquery()
    )

    uninformed_emps = (
        db.query(Employee)
        .filter(Employee.id.in_(inactive_attendance_emp_ids))
        .filter(~Employee.id.in_(leave_emp_ids))
        .all()
    )

    uninformed_list = [
        {
            "id": e.id,
            "name": f"{e.first_name} {e.last_name or ''}".strip(),
            "designation_id": e.designation_id
        }
        for e in uninformed_emps
    ]

    return {
        "total_employees": {
            "count": len(total_list),
            "employees": total_list
        },
        "active_employees": {
            "count": len(active_list),
            "employees": active_list
        },
        "inactive_employees": {
            "count": len(inactive_list),
            "employees": inactive_list
        },
        "uninformed_leaves": {
            "count": len(uninformed_list),
            "employees": uninformed_list
        }
    }
