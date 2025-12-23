from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class Department(Base):
    __tablename__ = "master_department"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(100), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
