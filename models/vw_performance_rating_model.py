from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from core.database import Base

class VwPerformanceRating(Base):
    __tablename__ = "vw_performance_rating"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer)
    employee_name = Column(String)
    designation_id = Column(Integer)
    designation_name = Column(String)
    rating = Column(Numeric(2, 1))
    reviewer_id = Column(Integer)
    reviewer_name = Column(String)
    created_date = Column(TIMESTAMP)
