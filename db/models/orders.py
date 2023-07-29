from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval,Date, ForeignKey

from .. import Base

__all__ = ['Base']


class Users(Base):

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
    