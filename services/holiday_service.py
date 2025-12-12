from sqlalchemy import select
from models.holiday_model import HolidayCalendar

def get_holidays_service(db):
    result = db.execute(select(HolidayCalendar))
    return result.scalars().all()
