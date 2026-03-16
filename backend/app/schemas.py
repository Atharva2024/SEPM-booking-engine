from pydantic import BaseModel
from datetime import datetime
from typing import List

class ResourceBase(BaseModel):
    name: str
    category: str
    price_per_hour: float
    total_inventory: int


class ResourceCreate(ResourceBase):
    pass


class ResourceResponse(ResourceBase):
    id: int

    class Config:
        orm_mode = True

# Booking Schemas
class BookingItemCreate(BaseModel):
    resource_id: int
    quantity: int


class BookingCreate(BaseModel):
    user_email: str
    start_time: datetime
    end_time: datetime
    items: List[BookingItemCreate]