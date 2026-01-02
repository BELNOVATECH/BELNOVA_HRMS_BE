from sqlalchemy import (Column,Integer,Numeric,Boolean)
from core.database import Base


class MasterPercCalId(Base):
    __tablename__ = "master_perc_cal_id"

    id = Column(Integer, primary_key=True, index=True)

    basic_perc = Column(Numeric(10, 2), nullable=False)
    conveyance_perc = Column(Numeric(10, 2), nullable=False)
    hra_perc = Column(Numeric(10, 2), nullable=False)
    medical_allowance_perc = Column(Numeric(10, 2), nullable=False)
    special_allowance_perc = Column(Numeric(10, 2), nullable=False)
    arrears_perc = Column(Numeric(10, 2), nullable=False)

    total_earnings_perc = Column(Numeric(10, 2), nullable=False)
    gross_earning_perc = Column(Numeric(10, 2), nullable=False)

    pf_perc = Column(Numeric(10, 2), nullable=False)
    esic_perc = Column(Numeric(10, 2), nullable=False)
    pt_perc = Column(Numeric(10, 2), nullable=False)
    tds_perc = Column(Numeric(10, 2), nullable=False)
    other_deductions_perc = Column(Numeric(10, 2), nullable=False)

    total_deductions_perc = Column(Numeric(10, 2), nullable=False)
    deduction_perc = Column(Numeric(10, 2), nullable=False)

    net_pay_perc = Column(Numeric(10, 2), nullable=False)
    net_pay_in_words_perc = Column(Numeric(10, 2), nullable=False)

    is_active = Column(Boolean, default=True)
