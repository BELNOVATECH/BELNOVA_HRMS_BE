from sqlalchemy import Column, Integer, String, Date, Time, Float, Text
from core.database import Base

class InterviewSchedule(Base):
    __tablename__ = "interview_scheduled"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, nullable=False)
    position_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)
    stage_id = Column(Integer, nullable=False)
    interview_date = Column(Date, nullable=False)
    rating = Column(Integer, nullable=True)
    feedback = Column(String, nullable=True)
    created_by = Column(Integer, nullable=False, default=1)
