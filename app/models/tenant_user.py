import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class TenantUser(Base):
    __tablename__ = "tenant_user"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenant.id"), nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)
    role_id = Column(String, ForeignKey("role.id"), nullable=True)
    invited_at = Column(DateTime, nullable=True)
    joined_at = Column(DateTime, nullable=True)

    __table_args__ = (
        UniqueConstraint("tenant_id", "user_id", name="uq_tenant_user_membership"),
    )

    tenant = relationship("Tenant", backref="tenant_users")
    user = relationship("User", backref="tenant_memberships")
    role = relationship("Role")
