from typing import Callable
from urllib.parse import urlparse

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send

from app.core.config import settings
from app.core.tenants import TenantContext
from app.services.tenant_service import TenantService  # you already have this

class TenantResolutionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable):
        tenant_id = await self._resolve_tenant_id(request)
        if tenant_id:
            # Attach tenant context to request.state
            request.state.tenant = TenantContext(id=tenant_id, subdomain=self._get_subdomain(request))
        else:
            request.state.tenant = None

        response = await call_next(request)
        return response

    async def _resolve_tenant_id(self, request: Request) -> str | None:
        # 1) Header-based
        header_name = settings.tenant_header
        tenant_id = request.headers.get(header_name)
        if tenant_id:
            # Optionally validate tenant exists/active
            if await TenantService.is_active_tenant(tenant_id):
                return tenant_id
            return None

        # 2) Subdomain-based
        subdomain = self._get_subdomain(request)
        if subdomain and subdomain not in ("www", ""):
            tenant = await TenantService.get_tenant_by_subdomain(subdomain)
            if tenant:
                return tenant.id

        return None

    def _get_subdomain(self, request: Request) -> str | None:
        host = request.headers.get("host", "")
        # e.g. tenant.example.com
        if not host.endswith(settings.base_domain):
            return None
        parts = host.split(".")
        if len(parts) < 3:
            return None
        return parts[0]
