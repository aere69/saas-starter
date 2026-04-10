from fastapi import Depends, Request, HTTPException, status
from app.db.session import get_db_with_tenant
from app.core.tenants import TenantContext
from sqlalchemy.ext.asyncio import AsyncSession

def get_tenant(request: Request) -> TenantContext:
    tenant = getattr(request.state, "tenant", None)
    if tenant is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tenant context is required",
        )
    return tenant

async def get_db(request: Request) -> AsyncSession:
    async with get_db_with_tenant(request) as session:
        yield session

