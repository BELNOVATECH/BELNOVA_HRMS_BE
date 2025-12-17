from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Boolean,
    Float,
    ForeignKey
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

    # 1 = Approved | 2 = Pending | 3 = Rejected
    approval_status_id = Column(Integer, default=2, nullable=False)
    approver_id = Column(Integer, nullable=True)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    remarks = Column(String(255), nullable=True)

    reporting_manager_id = Column(Integer, nullable=True)

    from_date_session = Column(String(20), nullable=True)
    to_date_session = Column(String(20), nullable=True)

    mobile = Column(String(20), nullable=True)
    upload_file = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True)

    employee = relationship("Employee", backref="leaves")
