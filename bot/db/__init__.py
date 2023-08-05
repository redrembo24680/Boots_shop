from .base import Base, session, engine
from .base import Base
from .models import Users, Country, Products, Orders

__all__ = [
    "Base",
    "Users",
    "Country",
    "Products",
    "Orders"
]


# def migrate():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
#     # mss = [
#     #     Country(tittle='USA'),
#     #     Country(tittle='Ukraine'),
#     #     Country(tittle='Spain'),
#     # ]
#     #
#     # session.add_all(mss)
#     # session.commit()
#

# migrate()

