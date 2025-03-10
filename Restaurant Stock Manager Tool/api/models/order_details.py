import random
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient_name = Column(String(100))
    ingredient_amount = Column(Integer)
    item_id = Column(Integer, ForeignKey('menu.id'))
    r_id = Column(Integer, ForeignKey('resource_management.id'))
    date_time = Column(DATETIME, nullable=False, server_default=func.now())
    order_id = Column(Integer, ForeignKey('orders.id'))
    price = Column(Float(10 ,2))

    order = relationship("Order", back_populates="order_details")
    menu = relationship("Menu", back_populates="order_details")
    resource_management = relationship("ResourceManagement", back_populates="order_detail")
    