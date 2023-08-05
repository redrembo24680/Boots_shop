from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, ForeignKey
from sqlalchemy.orm import relationship


from .. import Base

__all__ = ['Base']


class Country(Base):
    __tablename__ = 'countries'
    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    tittle = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )


