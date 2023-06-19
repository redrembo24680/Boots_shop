from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval

from .. import Base

__all__ = ['Base']


class Product(Base):
    __tablename__ = 'Products'

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
