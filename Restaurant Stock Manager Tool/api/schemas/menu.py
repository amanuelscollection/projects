from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Menu(BaseModel):
    id: int

    class Config:
        orm_mode = True

class MenuItem(BaseModel):
    item_name: str
    item_price: float
    ingredient_name: str
    calories: int
    food_category: str

class MenuItemCreate(BaseModel):
    id: int
    item_name: str
    item_price: float
    ingredient_name: str
    calories: int
    food_category: str

class MenuItemUpdate(BaseModel):
    item_name: Optional[str]
    item_price: Optional[float]
    ingredient_name: Optional[str]
    calories: Optional[int]
    food_category: Optional[str]

class MenuItemRead(BaseModel):
    id: int
    item_name: str
    item_price: float
    ingredient_name: str
    calories: int
    food_category: str

    class Config:
        orm_mode = True