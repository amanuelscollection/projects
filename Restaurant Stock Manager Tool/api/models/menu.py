import random
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String(100))
    item_price = Column(Float)
    ingredient_name = Column(String(100))
    calories = Column(Integer)
    food_category = Column(String(50))
    

    orders = relationship("Order", back_populates="menu")
    resource_management = relationship("ResourceManagement", back_populates="menu")
    order_details = relationship("OrderDetail", back_populates="menu")
