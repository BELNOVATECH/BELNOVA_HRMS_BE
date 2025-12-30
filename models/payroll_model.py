from sqlalchemy import (
    Column, Integer, Float, DateTime, Boolean, ForeignKey
)
from core.database import Base
from datetime import datetime


class Payroll(Base):

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(
        Integer,
        ForeignKey("employee_registration.id", ondelete="CASCADE"),
        nullable=False
    )

    department_id = Column(Integer, nullable=False)

    # Earnings
    basic_salary = Column(Float, nullable=False)
    hra = Column(Float, nullable=False)
    bonus = Column(Float, default=0)

    # Deductions
    pf = Column(Float, default=0)
    esi = Column(Float, default=0)
    other_deductions = Column(Float, default=0)

    # Net
    net_salary = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)
