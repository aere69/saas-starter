from fastapi import APIRouter, Depends
from app.schemas.billing import BillingPlan, Subscription, SubscriptionCreate
from app.services.billing_service import BillingService
from app.services.auth_service import AuthService

router = APIRouter()

@router.get("/plans", response_model=list[BillingPlan])
async def list_plans():
    return await BillingService.list_plans()

@router.post("/tenants/{tenant_id}/subscriptions", response_model=Subscription)
async def create_subscription(tenant_id: str, payload: SubscriptionCreate, user=Depends(AuthService.get_current_user)):
    return await BillingService.create_or_update_subscription(user, tenant_id, payload)

@router.get("/tenants/{tenant_id}/subscriptions", response_model=Subscription)
async def get_subscription(tenant_id: str, user=Depends(AuthService.get_current_user)):
    return await BillingService.get_subscription(user, tenant_id)
