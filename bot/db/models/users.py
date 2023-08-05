from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, Date, ForeignKey
from sqlalchemy.orm import relationship

from .. import Base

__all__ = ['Base']


class Users(Base):
    __tablename__ = 'users'
    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    first_name = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    second_name = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    email = Column(
        Unicode(225),
        nullable=False
    )
    password = Column(
        Unicode(225),
        nullable=False
    )
    date = Column(
        Date,
        unique=False
    )
    country_id = Column(
        Integer,
        ForeignKey('countries.id'),
    )
    country = relationship(
        "Country",
        backref=__tablename__
    )

