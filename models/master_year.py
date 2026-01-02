# models/master_year.py
from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base

class MasterYear(Base):
    __tablename__ = "master_year"

    id = Column(Integer, primary_key=True, index=True)
    year_name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
