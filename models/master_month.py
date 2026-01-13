from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class MasterMonth(Base):
    __tablename__ = "master_month"

    id = Column(Integer, primary_key=True, index=True)
    month_name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<MasterMonth(id={self.id}, month_name='{self.month_name}')>"
