from sqlalchemy import Column, Integer, String, Date, Time, Float, Text
from core.database import Base
from sqlalchemy import Interval

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
