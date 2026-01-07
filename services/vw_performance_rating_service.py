from models.vw_performance_rating_model import VwPerformanceRating

def get_all_performance_ratings_service(db):
    return db.query(VwPerformanceRating).all()
