from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, Date, ForeignKey
from sqlalchemy.orm import relationship
from .users import *
from .product import *
from .order_history import *

from .. import Base

__all__ = ['Base']


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        unique=True,
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        unique=True,
        nullable=True
    )
    count = Column(
        Float(2),
        unique=False,
        nullable=True
    )
    # order_history = relationship('order_history', backref="orders")
