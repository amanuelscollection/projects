from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class CustomerRead(BaseModel):
    id: int
    name: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True
