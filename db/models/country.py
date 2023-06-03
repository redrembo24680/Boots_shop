from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval

from .. import Base

__all__ = ['Base']


class Country(Base):
    __tablename__ = 'Country'

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False
    )
    title = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )









