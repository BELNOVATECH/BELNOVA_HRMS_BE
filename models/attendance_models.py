from sqlalchemy import Column, Integer, String, Date, Time, Float, Text
from core.database import Base
from sqlalchemy import Interval

class Attendance(Base):
    __tablename__ = "attendance_tracker"   # <-- set to your real table name

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, nullable=False)
    attendance_date = Column(Date, nullable=False)
    check_in_time = Column(String, nullable=True)   # adjust type if your DB uses time/datetime
    check_out_time = Column(String, nullable=True)
    working_status_id = Column(Integer, nullable=True)
    working_hours = Column(Interval, nullable=True)
    remarks = Column(String, nullable=True)
    created_by = Column(Integer, nullable=True)