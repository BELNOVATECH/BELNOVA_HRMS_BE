from sqlalchemy import Column, Integer, String, Date
from core.database import Base

class HolidayCalendar(Base):
    __tablename__ = "holiday_calendar"

    id = Column(Integer, primary_key=True, index=True)
    holiday_name = Column(String, nullable=False)
    holiday_date = Column(Date, nullable=False)
