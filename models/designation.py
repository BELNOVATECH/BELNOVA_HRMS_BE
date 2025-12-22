from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.database import Base

class Designation(Base):
    __tablename__ = "master_designation"

    id = Column(Integer, primary_key=True, index=True)
    designation_name = Column(String, nullable=False)
    dept_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
