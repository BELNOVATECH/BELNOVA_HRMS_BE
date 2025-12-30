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
    total_days = Column(Float, nullable=False)

    reason = Column(String(255))

    # master_status
    # 10 = Approved | 11 = Pending | 3 = Rejected
    status_id = Column(Integer, default=11, nullable=False)

    approver_id = Column(Integer)
    approved_on = Column(DateTime)

    created_by = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer)
    modified_date = Column(DateTime)

    remarks = Column(String(255))
    is_active = Column(Boolean, default=True)

    reporting_manager_id = Column(Integer)

    # 1 = Morning | 2 = Afternoon
    from_date_session_id = Column(String(1))
    to_date_session_id = Column(String(1))

    mobile = Column(String(20))
    upload_file = Column(String(255))

    employee = relationship("Employee", backref="leaves")
