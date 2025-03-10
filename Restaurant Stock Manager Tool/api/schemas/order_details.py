from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    ingredient_name: str
    ingredient_amount: int
    item_id: int
    price: Optional[float] = None

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailRead(OrderDetailBase):
    pass
    #id: int

    #class Config:
        #orm_mode = True

class OrderDetailUpdate(OrderDetailBase):
    pass