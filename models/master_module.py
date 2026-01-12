from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base

class MasterModule(Base):
    __tablename__ = "master_module"

    id = Column(Integer, primary_key=True, index=True)
    module_name = Column(String, nullable=False)
    # fa_fa_icon = Column(String, nullable=True)
    routes = Column(String, nullable=True)
    order_by = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
