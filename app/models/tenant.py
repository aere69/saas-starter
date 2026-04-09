import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Enum
from app.db.base import Base
import enum

class TenantStatus(str, enum.Enum):
    active = "active"
    suspended = "suspended"

class Tenant(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    status = Column(Enum(TenantStatus), default=TenantStatus.active, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
