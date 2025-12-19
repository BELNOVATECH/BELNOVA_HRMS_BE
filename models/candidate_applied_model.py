from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from core.database import Base


class CandidateApplied(Base):
    __tablename__ = "candidate_applied"

    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String)
    designation_id = Column(Integer)
    email = Column(String)
    application_status_id = Column(Integer)
    upload_resume = Column(String)
    created_by = Column(Integer)
    created_date = Column(DateTime)
    modified_by = Column(Integer)
    modified_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    mobile = Column(String)
    address = Column(String)
    dob = Column(Date)
