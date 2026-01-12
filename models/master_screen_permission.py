from sqlalchemy import Column, Integer, Boolean, ForeignKey
from core.database import Base

class MasterScreenPermission(Base):
    __tablename__ = "master_screen_permission"

    id = Column(Integer, primary_key=True, index=True)

    role_id = Column(Integer, nullable=False)
    module_id = Column(Integer, ForeignKey("master_module.id"), nullable=False)
    screen_id = Column(Integer, ForeignKey("master_screen.id"), nullable=True)

    can_view = Column(Boolean, default=False)
    can_edit = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)
    can_access = Column(Boolean, default=False)
    can_update = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)
