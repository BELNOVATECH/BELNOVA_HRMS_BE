from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from core.database import Base
from datetime import datetime


class CandidateApplied(Base):
    __tablename__ = "candidate_applied"

    id = Column(Integer, primary_key=True, index=True)

    candidate_name = Column(String, nullable=False)
    position_id = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)

    email = Column(String, unique=True, nullable=False)
    mobile = Column(String, unique=True, nullable=False)

    address = Column(String, nullable=False)

    application_status_id = Column(Integer, nullable=False)

    upload_resume = Column(String, nullable=True)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
