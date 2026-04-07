from pydantic import BaseModel
from typing import List

class Role(BaseModel):
    id: str
    tenant_id: str | None
    name: str
    permissions: List[str]

    class Config:
        orm_mode = True

class RoleCreate(BaseModel):
    name: str
    permissions: list[str] = []

class RoleAssignmentRequest(BaseModel):
    role_id: str
