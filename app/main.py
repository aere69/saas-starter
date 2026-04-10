from fastapi import FastAPI
from app.api.routes import auth, tenants, tenant_users, roles, billing, projects, webhooks
from app.core.middleware import TenantResolutionMiddleware

app = FastAPI(title='SaaS Multi-Tenant Platform')

# add middleware
app.add_middleware(TenantResolutionMiddleware)

# include routers...
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
app.include_router(tenant_users.router, prefix="/tenants/{tenant_id}/users", tags=["Tenant Users"])
app.include_router(roles.router, tags=["Roles"])
app.include_router(billing.router, prefix="/billing", tags=["Billing"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])
