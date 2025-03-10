import random
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    card_info = Column(String(100))
    total_price = Column(Float(10, 2))
    payment_type = Column(String(50))
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship("Order", back_populates="payment_info")