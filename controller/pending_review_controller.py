from services.pending_review_service import get_pending_reviews_service

def get_pending_reviews_controller(db):
    return get_pending_reviews_service(db)
