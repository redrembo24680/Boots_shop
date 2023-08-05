from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, Date, ForeignKey
from .users import *


from .. import Base

__all__ = ['Base']


class Orders(Base):
    __tablename__ = 'orders'
    contact = Column(
        Unicode(225),
        primary_key=True,
        nullable=False
    )

