import random
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Rewards(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    phone_number = Column(String(250), ForeignKey('customers.phone_number'))
    orders_amount = Column(Integer)
    discount_amount = Column(Integer)

    order = relationship("Order", back_populates="rewards")
    customer = relationship("Customer", back_populates="rewards")
