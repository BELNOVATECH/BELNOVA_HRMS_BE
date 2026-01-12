from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from core.database import Base


class EmployeeActivity(Base):
    __tablename__ = "employee_activity"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(Integer, nullable=False)
    module_id = Column(Integer, nullable=False)
    screen_id = Column(Integer, nullable=False)

    activity_description = Column(String(255), nullable=False)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, server_default=func.now())

    modified_by = Column(Integer, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
