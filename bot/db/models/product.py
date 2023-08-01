from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval
from sqlalchemy.orm import relationship
from .orders import *

from .. import Base

__all__ = ['Base']


class Products(Base):
    __tablename__ = 'products'
    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    name = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    size = Column(
        Float(2),
        nullable=False
    )
    price = Column(
        Float(2),
        nullable=False
    )
    photo = Column(
        Unicode(225),
        nullable=False
    )
    gender = Column(
        Unicode(225),
        nullable=False
    )
    age_category = Column(
        Unicode(225),
        nullable=False
    )
    # user = relationship('orders', backref="products")
