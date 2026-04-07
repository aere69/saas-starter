from fastapi import APIRouter, Depends
from app.schemas.tenant import TenantUser, TenantUserCreate
from app.services.tenant_service import TenantService
from app.services.auth_service import AuthService

router = APIRouter()

@router.get("", response_model=list[TenantUser])
async def list_tenant_users(tenant_id: str, user=Depends(AuthService.get_current_user)):
    return await TenantService.list_users(user, tenant_id)

@router.post("", response_model=TenantUser, status_code=201)
async def add_user_to_tenant(tenant_id: str, payload: TenantUserCreate, user=Depends(AuthService.get_current_user)):
    return await TenantService.add_user(user, tenant_id, payload)
