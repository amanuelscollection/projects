from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ResourceManagementBase(BaseModel):
    item_id: Optional[int] = None
    ingredient_name: str
    ingredient_amount: int

class ResourceManagementCreate(BaseModel):
    item_id: int
    ingredient_name: str
    ingredient_amount: int

class ResourceManagementRead(ResourceManagementBase):
    id: int

    class Config:
        orm_mode = True

class ResourceManagementUpdate(BaseModel):
    ingredient_amount: Optional[int]