# from sqlalchemy.orm import Session
# from sqlalchemy import func, distinct

# from models.generated_models import (
#     EmployeeRegistration,
#     AttendanceTracker,
#     LeaveRequest
# )


# def get_dashboard_data_service(db: Session):

#     # ==========================
#     # TOTAL EMPLOYEES
#     # ==========================

#     total_count = (
#         db.query(func.count(EmployeeRegistration.id))
#         .scalar()
#     )

#     total_employees = (
#         db.query(EmployeeRegistration)
#         .all()
#     )

#     total_list = [
#         {
#             "id": emp.id,
#             "name": f"{emp.first_name} {emp.last_name or ''}".strip()
#         }
#         for emp in total_employees
#     ]

#     # ==========================
#     # ACTIVE EMPLOYEES
#     # ==========================

#     active_count = (
#         db.query(func.count(EmployeeRegistration.id))
#         .filter(EmployeeRegistration.is_active == True)
#         .scalar()
#     )

#     active_employees = (
#         db.query(EmployeeRegistration)
#         .filter(EmployeeRegistration.is_active == True)
#         .all()
#     )

#     active_list = [
#         {
#             "id": emp.id,
#             "name": f"{emp.first_name} {emp.last_name or ''}".strip()
#         }
#         for emp in active_employees
#     ]

#     # ==========================
#     # INACTIVE EMPLOYEES
#     # ==========================

#     inactive_count = (
#         db.query(func.count(EmployeeRegistration.id))
#         .filter(EmployeeRegistration.is_active == False)
#         .scalar()
#     )

#     inactive_employees = (
#         db.query(EmployeeRegistration)
#         .filter(EmployeeRegistration.is_active == False)
#         .all()
#     )

#     inactive_list = [
#         {
#             "id": emp.id,
#             "name": f"{emp.first_name} {emp.last_name or ''}".strip()
#         }
#         for emp in inactive_employees
#     ]

#     # ==========================
#     # UNINFORMED LEAVES
#     # ==========================

#     attendance_emp_ids = (
#         db.query(distinct(AttendanceTracker.emp_id))
#         .filter(AttendanceTracker.is_active == False)
#         .subquery()
#     )

#     leave_emp_ids = (
#         db.query(distinct(LeaveRequest.emp_id))
#         .subquery()
#     )

#     uninformed_employees = (
#         db.query(EmployeeRegistration)
#         .filter(EmployeeRegistration.id.in_(attendance_emp_ids))
#         .filter(~EmployeeRegistration.id.in_(leave_emp_ids))
#         .all()
#     )

#     uninformed_list = [
#         {
#             "id": emp.id,
#             "name": f"{emp.first_name} {emp.last_name or ''}".strip(),
#             "designation_id": emp.designation_id
#         }
#         for emp in uninformed_employees
#     ]

#     # ==========================
#     # RESPONSE
#     # ==========================

#     return {

#         "total_employees": {
#             "count": total_count,
#             "employees": total_list
#         },

#         "active_employees": {
#             "count": active_count,
#             "employees": active_list
#         },

#         "inactive_employees": {
#             "count": inactive_count,
#             "employees": inactive_list
#         },

#         "uninformed_leaves": {
#             "count": len(uninformed_list),
#             "employees": uninformed_list
#         }
#     }




from sqlalchemy.orm import Session
from sqlalchemy import func, distinct

from models.generated_models import (
    EmployeeRegistration,
    AttendanceTracker,
    LeaveRequest
)


def get_dashboard_data_service(db: Session):

    # ==========================
    # FETCH EMPLOYEES ONCE
    # ==========================

    employees = db.query(
        EmployeeRegistration.id,
        EmployeeRegistration.first_name,
        EmployeeRegistration.last_name,
        EmployeeRegistration.designation_id,
        EmployeeRegistration.is_active
    ).all()

    total_list = []
    active_list = []
    inactive_list = []

    for emp in employees:

        employee_data = {
            "id": emp.id,
            "name": f"{emp.first_name} {emp.last_name or ''}".strip()
        }

        total_list.append(employee_data)

        if emp.is_active:
            active_list.append(employee_data)
        else:
            inactive_list.append(employee_data)

    # ==========================
    # UNINFORMED LEAVES
    # ==========================

    attendance_emp_ids = (
        db.query(distinct(AttendanceTracker.emp_id))
        .filter(AttendanceTracker.is_active == False)
        .subquery()
    )

    leave_emp_ids = (
        db.query(distinct(LeaveRequest.emp_id))
        .subquery()
    )

    uninformed_employees = (
        db.query(
            EmployeeRegistration.id,
            EmployeeRegistration.first_name,
            EmployeeRegistration.last_name,
            EmployeeRegistration.designation_id
        )
        .filter(EmployeeRegistration.id.in_(attendance_emp_ids))
        .filter(~EmployeeRegistration.id.in_(leave_emp_ids))
        .all()
    )

    uninformed_list = [
        {
            "id": emp.id,
            "name": f"{emp.first_name} {emp.last_name or ''}".strip(),
            "designation_id": emp.designation_id
        }
        for emp in uninformed_employees
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