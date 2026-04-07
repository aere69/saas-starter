from fastapi import APIRouter, Depends
from app.schemas.tenant import Tenant, TenantCreate, TenantUpdate
from app.services.tenant_service import TenantService
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("", response_model=Tenant, status_code=201)
async def create_tenant(payload: TenantCreate, user=Depends(AuthService.get_current_user)):
    return await TenantService.create_tenant(user, payload)

@router.get("", response_model=list[Tenant])
async def list_tenants(user=Depends(AuthService.get_current_user)):
    return await TenantService.list_tenants(user)

@router.get("/{tenant_id}", response_model=Tenant)
async def get_tenant(tenant_id: str, user=Depends(AuthService.get_current_user)):
    return await TenantService.get_tenant(user, tenant_id)

@router.patch("/{tenant_id}", response_model=Tenant)
async def update_tenant(tenant_id: str, payload: TenantUpdate, user=Depends(AuthService.get_current_user)):
    return await TenantService.update_tenant(user, tenant_id, payload)
