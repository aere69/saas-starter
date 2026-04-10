from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.core.tenants import TenantContext
from fastapi import Request

engine = create_async_engine(settings.database_url, echo=False, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@asynccontextmanager
async def get_db_with_tenant(request: Request):
    async with AsyncSessionLocal() as session:
        tenant: TenantContext | None = getattr(request.state, "tenant", None)
        if tenant:
            await session.execute(
                "SET app.current_tenant = :tenant.id",
                {"tenant_id": tenant.id},
            )
        try:
            yield session
        finally:
            if tenant:
                await session.execute("RESET app.current_tenant")

