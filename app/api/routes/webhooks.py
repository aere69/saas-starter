from fastapi import APIRouter, Request
from app.services.billing_service import BillingService

router = APIRouter()

@router.post("/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    return await BillingService.handle_webhook(payload, sig_header)
