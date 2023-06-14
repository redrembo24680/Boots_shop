from .base import Base, session, engine
from .models import Country, Product

__all__ = [
    "Base",
    "Country",
    "Product"
]


# def migrate():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
#
# migrate()
