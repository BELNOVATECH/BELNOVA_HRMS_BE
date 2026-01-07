from sqlalchemy import Column, BigInteger, Integer, Numeric, Boolean, TIMESTAMP
from core.database import Base

class EmployeeRating(Base):
    __tablename__ = "employee_rating"

    id = Column(BigInteger, primary_key=True, index=True)
    emp_id = Column(Integer, nullable=False)
    designation_id = Column(Integer, nullable=False)
    rating = Column(Numeric(2, 1), nullable=False)
    reviewer_id = Column(Integer, nullable=False)
    created_by = Column(BigInteger)
    created_date = Column(TIMESTAMP)
    modified_by = Column(BigInteger)
    modified_date = Column(TIMESTAMP)
    is_active = Column(Boolean)
