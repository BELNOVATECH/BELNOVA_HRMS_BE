from models.employee_rating_model import EmployeeRating
from datetime import datetime

def create_employee_rating_service(payload, db):
    rating = EmployeeRating(
        emp_id=payload.emp_id,
        designation_id=payload.designation_id,
        rating=payload.rating,
        reviewer_id=payload.reviewer_id,
        created_by=payload.created_by,
        created_date=payload.created_date or datetime.utcnow(),
        is_active=payload.is_active
    )

    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating
