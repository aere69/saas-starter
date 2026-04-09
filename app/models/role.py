import uuid
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class Role(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenant.id"), nullable=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False, default=list)

    tenant = relationship("Tenant", backref="roles")
