from sqlalchemy.orm import Session

from services.pending_review_service import (
    get_pending_reviews_service
)


def get_pending_reviews_controller(
    db: Session
):
    return get_pending_reviews_service(db)