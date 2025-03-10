from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .order_details import OrderDetailCreate 

class OrderBase(BaseModel):
    customer_phone_number: str
    takeout_delivery:Optional[str] = None
    item_id: int
    Amount: int


class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int

    class Config:
        orm_mode = True

class OrderUpdate(OrderBase):
    pass

class Order(OrderBase):
    pass