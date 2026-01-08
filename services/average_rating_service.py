from sqlalchemy import func
from models.employee_rating_model import EmployeeRating

def get_average_rating_service(db):
    total_ratings = db.query(func.count(EmployeeRating.rating)).scalar() or 0
    sum_of_ratings = db.query(func.sum(EmployeeRating.rating)).scalar() or 0

    average_rating = (
        round(float(sum_of_ratings / total_ratings), 2)
        if total_ratings > 0
        else 0
    )

    return {
        # "calculation": "Average Rating = (Sum of all ratings) / (Total number of ratings)",
        "total_ratings": total_ratings,
        "sum_of_ratings": float(sum_of_ratings),
        "average_rating": average_rating,
        "message": f"The total average rating of all employees is {average_rating}"
    }
