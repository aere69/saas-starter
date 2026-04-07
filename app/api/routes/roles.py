from fastapi import APIRouter, Depends
from app.schemas.role import Role, RoleCreate, RoleAssignmentRequest
from app.services.tenant_service import TenantService
from app.services.auth_service import AuthService

router = APIRouter()

@router.get("/roles", response_model=list[Role])
async def list_global_roles():
    return await TenantService.list_global_roles()

@router.get("/tenants/{tenant_id}/roles", response_model=list[Role])
async def list_tenant_roles(tenant_id: str, user=Depends(AuthService.get_current_user)):
    return await TenantService.list_roles(user, tenant_id)

@router.post("/tenants/{tenant_id}/roles", response_model=Role, status_code=201)
async def create_role(tenant_id: str, payload: RoleCreate, user=Depends(AuthService.get_current_user)):
    return await TenantService.create_role(user, tenant_id, payload)

@router.post("/tenants/{tenant_id}/users/{user_id}/roles", status_code=204)
async def assign_role(tenant_id: str, user_id: str, payload: RoleAssignmentRequest, user=Depends(AuthService.get_current_user)):
    return await TenantService.assign_role(user, tenant_id, user_id, payload)
