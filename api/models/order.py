from api.models.base import BaseModel, db
from sqlalchemy.orm import backref
from api.models.user_stock_quantity import UserStockQuantity
from api.models.stock import Stock
class Order(BaseModel):

    __tablename__ = "orders"

    id = db.Column(db.Unicode(), primary_key=True)
    user_id =  db.Column(
        db.Unicode(),
        db.ForeignKey("users.id", ondelete="CASCADE"),
    )
    stock_id =  db.Column(
        db.Unicode(),
        db.ForeignKey("stocks.id", ondelete="CASCADE"),
    )
    quantity = db.Column(db.Integer(), nullable=False)
    is_buy = db.Column(db.Boolean, default=False)
    stock = db.relationship("Stock", backref="orders")
    user = db.relationship("User", backref="orders")

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)


    @classmethod
    def create_buy_order(cls, **kwargs):
      user_stock_quantity = UserStockQuantity.get_or_create(user_id=kwargs.get('user_id'), stock_id=kwargs.get('stock_id'))
      user_stock_quantity.quantity += kwargs.get("quantity") 
      instance = cls.create(**{**kwargs, "is_buy":True})
      Stock.add_stock_quantity(kwargs.get('stock_id'), -kwargs.get("quantity"))
      user_stock_quantity.save()
      return instance
    
    @classmethod
    def create_sell_order(cls, **kwargs):
      user_stock_quantity = UserStockQuantity.get_or_create(user_id=kwargs.get('user_id'), stock_id=kwargs.get('stock_id'))
      user_stock_quantity.quantity -= kwargs.get("quantity") 
      instance = cls.create(**{**kwargs, "is_buy":False})
      Stock.add_stock_quantity(kwargs.get('stock_id'), kwargs.get("quantity"))
      user_stock_quantity.save()
      return instance









    
    


