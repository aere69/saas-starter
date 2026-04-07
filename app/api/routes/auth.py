from fastapi import APIRouter, Depends
from app.schemas.auth import RegisterRequest, LoginRequest, TokenPair, RefreshRequest, AccessToken
from app.schemas.user import User
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/register", response_model=User, status_code=201)
async def register(payload: RegisterRequest):
    return await AuthService.register(payload)

@router.post("/login", response_model=TokenPair)
async def login(payload: LoginRequest):
    return await AuthService.login(payload)

@router.post("/refresh", response_model=AccessToken)
async def refresh(payload: RefreshRequest):
    return await AuthService.refresh(payload)

@router.get("/me", response_model=User)
async def me(current_user=Depends(AuthService.get_current_user)):
    return current_user