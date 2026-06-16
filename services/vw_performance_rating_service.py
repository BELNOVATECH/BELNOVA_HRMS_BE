from sqlalchemy import select
from sqlalchemy.orm import Session
from models.generated_models import t_vw_performance_rating

def get_performance_ratings_service(db: Session):

    data = db.execute(
        select(t_vw_performance_rating)
    ).mappings().all()

    return data