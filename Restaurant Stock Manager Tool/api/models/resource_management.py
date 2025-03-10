import random
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class ResourceManagement(Base):
    __tablename__ = "resource_management"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey("menu.id"))
    ingredient_name = Column(String(100))
    ingredient_amount = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.id"))
    

    order = relationship("Order", back_populates="resource_management")
    menu = relationship("Menu", back_populates="resource_management")
    order_detail = relationship("OrderDetail", back_populates="resource_management")
    