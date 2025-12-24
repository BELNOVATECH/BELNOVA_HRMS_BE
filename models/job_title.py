from sqlalchemy import Column, Integer, Boolean
from core.database import Base


class JobOpening(Base):
    __tablename__ = "job_openings"

    id = Column(Integer, primary_key=True, index=True)
    designation_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
