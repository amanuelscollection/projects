from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentInfoBase(BaseModel):
    card_info: str
    payment_type: Optional[str] = None
    order_id: int
    total_price:float
    

class PaymentInfoCreate(PaymentInfoBase):
    pass

class PaymentInfoRead(PaymentInfoBase):
    id: int

    class Config:
        orm_mode = True

class PaymentInfoUpdate(PaymentInfoBase):
    card_info:str
    payment_type:str
    total_price: float

class PaymentInfo(PaymentInfoBase):
    id: int

    class Config:
        orm_mode = True