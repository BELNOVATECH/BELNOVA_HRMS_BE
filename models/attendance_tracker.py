from sqlalchemy import (
    Column, BigInteger, Integer, Date, TIMESTAMP,
    Interval, Boolean, VARCHAR
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AttendanceTracker(Base):
    __tablename__ = "attendance_tracker"

    id = Column(BigInteger, primary_key=True, index=True)
    emp_id = Column(BigInteger, nullable=False)

    attendance_date = Column(Date, nullable=False)
    check_in_time = Column(TIMESTAMP)
    check_out_time = Column(TIMESTAMP)

    working_status_id = Column(Integer)
    working_hours = Column(Interval)

    remarks = Column(VARCHAR(100))

    created_by = Column(BigInteger)
    created_date = Column(TIMESTAMP)

    modified_by = Column(BigInteger)
    modified_date = Column(TIMESTAMP)

    is_active = Column(Boolean, default=True)
