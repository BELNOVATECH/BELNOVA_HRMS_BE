from sqlalchemy import func
from models.employee_model import Employee  # ✅ EXISTING MODEL

def get_active_employee_count_service(db):
    total = (
        db.query(func.count(Employee.id))
        .filter(Employee.is_active == True)
        .scalar()
    )

    return {"total_employees": total}
