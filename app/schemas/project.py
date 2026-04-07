from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: str
    tenant_id: str
    name: str
    description: str | None
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
