import random
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from sqlalchemy import Float

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tracking_number = Column(String(50), index=True)
    customer_phone_number = Column(String(50), ForeignKey('customers.phone_number'))
    takeout_delivery = Column(String(225))
    total_price = Column(Float(10, 2))
    discount_amount = Column(Float)
    item_id = Column(Integer)
    Amount = Column(Integer)

    menu_id = Column(Integer, ForeignKey("menu.id"))

    menu = relationship("Menu", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    rewards = relationship("Rewards", back_populates="order")
    resource_management = relationship("ResourceManagement", back_populates="order")
    payment_info = relationship("PaymentInfo", back_populates="order")