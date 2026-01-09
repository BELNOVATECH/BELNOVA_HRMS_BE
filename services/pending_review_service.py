from models.employee_model import Employee
from models.employee_rating_model import EmployeeRating

def get_pending_reviews_service(db):
    # Step 1: Get all ACTIVE employees
    active_employees = (
        db.query(
            Employee.id,
            Employee.first_name,
            Employee.last_name,
            Employee.designation_id
        )
        .filter(Employee.is_active == True)
        .all()
    )

    # Step 2: Get all employee IDs who already have ratings
    rated_employee_ids = {
        emp_id for (emp_id,) in db.query(EmployeeRating.emp_id).distinct().all()
    }

    # Step 3: Find employees NOT in employee_rating
    pending_employees = []

    for emp in active_employees:
        if emp.id not in rated_employee_ids:
            pending_employees.append({
                "employee_id": emp.id,
                "employee_name": f"{emp.first_name} {emp.last_name}",
                "designation_id": emp.designation_id
            })

    return {
        "total_pending_reviews": len(pending_employees),
        "employees": pending_employees
    }
