from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, Date

from .. import Base

__all__ = ['Base']


class Order_history(Base):

    __tablename__ = 'order_history'

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    order_id = Column(
        Integer,
        unique=False,
        nullable=False
    )
    date = Column(
        Date,
        unique=False,
        nullable=False
    )
    count = Column(
        Float(2),
        unique=False,
        nullable=True
    )
    status = Column(
        Unicode(225),
        unique=False,
        nullable=True
    )