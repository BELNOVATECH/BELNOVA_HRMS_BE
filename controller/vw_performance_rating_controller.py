from services.vw_performance_rating_service import (
    get_all_performance_ratings_service
)

def get_all_performance_ratings_controller(db):
    return get_all_performance_ratings_service(db)
