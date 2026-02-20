from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class ReserveCreate(BaseModel):
    room: str
    account: int
    date: datetime


class ReserveResponse(BaseModel):
    room: str
    account: int
    date: datetime

    model_config = ConfigDict(from_attributes=True)
