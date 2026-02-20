from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class AccountCreate(BaseModel):
    stdNum: int
    email: EmailStr
    password: str


class AccountResponse(BaseModel):
    id: int
    stdNum: int
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
