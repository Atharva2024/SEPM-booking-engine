from pydantic import BaseModel

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