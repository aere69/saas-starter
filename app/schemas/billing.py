from pydantic import BaseModel
from datetime import datetime

class BillingPlan(BaseModel):
    id: str
    name: str
    price_monthly: float
    currency: str
    features: list[str]

class Subscription(BaseModel):
    id: str
    tenant_id: str
    plan: str
    status: str
    current_period_end: datetime

    class Config:
        orm_mode = True

class SubscriptionCreate(BaseModel):
    plan_id: str
    payment_method_id: str | None = None
