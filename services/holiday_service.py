from sqlalchemy import select
from sqlalchemy.orm import Session

from models.generated_models import HolidayCalendar


def get_holidays_service(db: Session):
    result = db.execute(
        select(HolidayCalendar)
    )

    return result.scalars().all()