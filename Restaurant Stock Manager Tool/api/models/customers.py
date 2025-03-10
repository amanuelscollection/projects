import random
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .rewards import Rewards

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), index=True)
    phone_number = Column(String(50), unique=True, index=True)  # Reduced index length to match column length
    address = Column(String(100))  # Removed nullable=True

    orders = relationship("Order", back_populates="customer")
    rewards = relationship("Rewards", back_populates="customer")