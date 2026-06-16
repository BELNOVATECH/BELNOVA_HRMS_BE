from sqlalchemy.orm import Session
from sqlalchemy import func

from models.generated_models import EmployeeRegistration


def get_active_employee_count_service(db: Session):

    total = (
        db.query(
            func.count(EmployeeRegistration.id)
        )
        .filter(
            EmployeeRegistration.is_active == True
        )
        .scalar()
    )

    return {
        "total_employees": total
    }