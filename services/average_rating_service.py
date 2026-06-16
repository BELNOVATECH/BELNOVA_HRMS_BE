from sqlalchemy import func
from sqlalchemy.orm import Session
from models.generated_models import EmployeeRating

def get_average_rating_service(db: Session):
    result = db.query(
        func.count(EmployeeRating.id).label("total_ratings"),
        func.sum(EmployeeRating.rating).label("sum_of_ratings"),
        func.avg(EmployeeRating.rating).label("average_rating")
    ).first()

    return {
        "total_ratings": result.total_ratings or 0,
        "sum_of_ratings": float(result.sum_of_ratings or 0),
        "average_rating": round(float(result.average_rating or 0), 2),
        "message": f"Average rating is {round(float(result.average_rating or 0), 2) if result.average_rating else 0}"
    }

    