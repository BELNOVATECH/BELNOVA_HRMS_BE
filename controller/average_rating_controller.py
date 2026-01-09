from services.average_rating_service import get_average_rating_service

def get_average_rating_controller(db):
    return get_average_rating_service(db)
