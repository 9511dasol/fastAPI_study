from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class ReserveCreate(BaseModel):
    room: str
    is_reserved: bool


class ReserveResponse(BaseModel):
    room: str
    # is_reserved: bool

    model_config = ConfigDict(from_attributes=True)
