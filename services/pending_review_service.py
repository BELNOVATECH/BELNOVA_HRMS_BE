from sqlalchemy.orm import Session

from models.generated_models import (
    EmployeeRegistration,
    EmployeeRating
)


def get_pending_reviews_service(db: Session):

    rated_subquery = (
        db.query(EmployeeRating.emp_id)
        .distinct()
        .subquery()
    )

    pending = (
        db.query(
            EmployeeRegistration.id,
            EmployeeRegistration.first_name,
            EmployeeRegistration.last_name,
            EmployeeRegistration.designation_id
        )
        .filter(
            EmployeeRegistration.is_active == True
        )
        .filter(
            ~EmployeeRegistration.id.in_(rated_subquery)
        )
        .all()
    )

    employees = [
        {
            "employee_id": emp.id,
            "employee_name":
                f"{emp.first_name} {emp.last_name or ''}".strip(),
            "designation_id": emp.designation_id
        }
        for emp in pending
    ]

    return {
        "total_pending_reviews": len(employees),
        "employees": employees
    }