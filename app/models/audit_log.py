import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class AuditLog(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenant.id"), nullable=False, index=True)
    user_id = Column(String, ForeignKey("user.id"), nullable=True, index=True)
    action = Column(String, nullable=False)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    tenant = relationship("Tenant", backref="audit_logs")
    user = relationship("User")
