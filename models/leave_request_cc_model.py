from sqlalchemy import (
    Column, Integer, DateTime, Boolean, ForeignKey
)
from core.database import Base
from datetime import datetime


class LeaveRequestCC(Base):
    __tablename__ = "leave_request_cc"

    id = Column(Integer, primary_key=True, index=True)

    leave_request_id = Column(
        Integer,
        ForeignKey("leave_request.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    cc_to_id = Column(
        Integer,
        ForeignKey("employee_registration.id"),
        nullable=False,
        index=True
    )

    created_by = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer)
    modified_date = Column(DateTime)

    is_active = Column(Boolean, default=True)
