from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
