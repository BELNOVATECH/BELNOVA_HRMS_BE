from sqlalchemy import (
    Column, BigInteger, Integer, Numeric, String,
    Boolean, DateTime, ForeignKey
)
from datetime import datetime
from core.database import Base

class Payroll(Base):
    __tablename__ = "payslips"

    id = Column(BigInteger, primary_key=True, index=True)

    emp_id = Column(BigInteger, ForeignKey("employee_registration.id"))
    month_id = Column(Integer, nullable=False)
    year_id = Column(Integer, ForeignKey("master_year.id"), nullable=False)

    total_days = Column(Integer, nullable=False)
    paid_days = Column(Integer, nullable=False)
    lop_days = Column(Integer, nullable=False)

    basic = Column(Numeric(10, 2), nullable=False)
    conveyance = Column(Numeric(10, 2), nullable=False, default=0)
    hra = Column(Numeric(10, 2), nullable=False)
    medical_allowance = Column(Numeric(10, 2), nullable=False, default=0)
    special_allowance = Column(Numeric(10, 2), nullable=False)
    arrears = Column(Numeric(10, 2), nullable=False, default=0)

    total_earnings = Column(Numeric(10, 2), nullable=False)

    pf = Column(Numeric(10, 2), nullable=False)
    esic = Column(Numeric(10, 2), nullable=False, default=0)
    pt = Column(Numeric(10, 2), nullable=False, default=0)
    tds = Column(Numeric(10, 2), nullable=False, default=0)
    other_deductions = Column(Numeric(10, 2), nullable=False, default=0)

    total_deductions = Column(Numeric(10, 2), nullable=False)
    gross_earning = Column(Numeric(10, 2), nullable=False)
    deduction = Column(Numeric(10, 2), nullable=False)

    net_pay = Column(Numeric(10, 2), nullable=False)
    net_pay_in_words = Column(String(500))

    created_by = Column(BigInteger)
    created_date = Column(DateTime, default=datetime.utcnow)
    modified_by = Column(BigInteger)
    modified_date = Column(DateTime)

    is_active = Column(Boolean, default=True)
    perc_cal_id = Column(Integer)
