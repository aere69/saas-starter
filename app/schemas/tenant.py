from pydantic import BaseModel, EmailStr
from datetime import datetime

class Tenant(BaseModel):
    id: str
    name: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class TenantCreate(BaseModel):
    name: str

class TenantUpdate(BaseModel):
    name: str | None = None
    status: str | None = None

class TenantUser(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    role_id: str
    invited_at: datetime | None
    joined_at: datetime | None

    class Config:
        orm_mode = True

class TenantUserCreate(BaseModel):
    email: EmailStr
    role_id: str
