from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval

from .. import Base

__all__ = ['Base']


class Product(Base):
    __tablename__ = 'Product'

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False
    )
    name = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )
    size = Column(
        Float(2),
        nullable=False
    )
    prize = Column(
        Float(2),
        nullable=False
    )