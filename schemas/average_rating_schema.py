from pydantic import BaseModel

class AverageRatingResponse(BaseModel):
    # calculation: str
    total_ratings: int
    sum_of_ratings: float
    average_rating: float
    message: str
