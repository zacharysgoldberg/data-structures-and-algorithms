from sqlalchemy import Column, String, Integer, Boolean, DateTime
from .database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    order_time = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)
    delivered = Column(Boolean, default=False, nullable=False)
