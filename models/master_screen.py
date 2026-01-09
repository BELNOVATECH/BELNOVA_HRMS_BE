from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.database import Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.database import Base

class MasterScreen(Base):
    __tablename__ = "master_screen"

    id = Column(Integer, primary_key=True, index=True)
    screen_name = Column(String, nullable=False)
    screen_label = Column(String, nullable=True)
    fa_fa_icon = Column(String, nullable=True)
    routes = Column(String, nullable=True)
    module_id = Column(Integer, ForeignKey("master_module.id"))
    order_by = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)

