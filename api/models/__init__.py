from api.models.base import db, BaseModel
from api.models.user import User
from api.models.stock import Stock
from api.models.order import Order
from api.models.user_stock_quantity import UserStockQuantity

from api.utils.classes import all_subclasses


def open_new_session():
    db.session = db.gen_session()


def close_session(exc):
    if db.session.is_active:
        db.session.close()


def init_app(app):
    app.before_request(open_new_session)
    app.teardown_request(close_session)

# create the tables if not created


db.Base.metadata.create_all(db.engine)
db.session.commit()

all_BaseModel_subclasses = all_subclasses(BaseModel)

__all__ = [
  "db",
  "Stock",
  "User",
  "Order",
  "UserStockQuantity",
  "all_BaseModel_subclasses",
  ]
