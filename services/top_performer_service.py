from models.employee_rating_model import EmployeeRating

def get_top_performers_service(db):
    return (
        db.query(EmployeeRating)
        .filter(EmployeeRating.rating >= 4.5)   # ✅ rating >= 4.5
        .order_by(EmployeeRating.rating.desc())
        .all()
    )
