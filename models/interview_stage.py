from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from core.database import Base


class InterviewStage(Base):
    __tablename__ = "interview_stage"

    id = Column(Integer, primary_key=True, index=True)
    stage_name = Column(String, nullable=False)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    modified_date = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


