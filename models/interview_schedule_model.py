from sqlalchemy import Column, Integer, Date, String, Boolean, DateTime
from core.database import Base
from datetime import datetime


class InterviewSchedule(Base):
    __tablename__ = "interview_scheduled"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, nullable=False)

    designation_id = Column(Integer, nullable=False)   # ✅ changed
    status_id = Column(Integer, nullable=False)
    stage_id = Column(Integer, nullable=False)

    interview_date = Column(Date, nullable=False)
    feedback = Column(String)
    rating = Column(Integer)

    created_by = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer)
    modified_date = Column(DateTime)

    is_active = Column(Boolean, default=True)
