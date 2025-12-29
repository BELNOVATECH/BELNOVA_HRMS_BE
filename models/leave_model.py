from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    Boolean, Float, ForeignKey
)
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime


class LeaveRequest(Base):
    __tablename__ = "leave_request"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(
        Integer,
        ForeignKey("employee_registration.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    leavetype_id = Column(Integer, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_days = Column(Float, nullable=True)

    reason = Column(String(255), nullable=True)

    # master_status
    # 10 = Approved | 11 = Pending | 3 = Rejected
    status_id = Column(Integer, default=11, nullable=False)

    approver_id = Column(Integer, nullable=True)
    approved_on = Column(DateTime, nullable=True)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    remarks = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True)

    reporting_manager_id = Column(Integer, nullable=True)

    from_date_session = Column(String(20), nullable=True)
    to_date_session = Column(String(20), nullable=True)

    mobile = Column(String(20), nullable=True)
    upload_file = Column(String(255), nullable=True)

    employee = relationship("Employee", backref="leaves")
