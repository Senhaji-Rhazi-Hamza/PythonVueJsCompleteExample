from api.models.base import BaseModel, db
from sqlalchemy.orm import backref

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
      self.update_stock_and_user()


    @classmethod
    def create_buy_order(cls, **kwargs):
      cls.create({**kwargs, "is_buy":True})
    
    @classmethod
    def create_sell_order(cls, **kwargs):
      cls.create({**kwargs, "is_buy":False})

    def save(self):
      self.update_stock_and_user()
      self.stock.save()
      self.user.save()

      super().save()

    
    def update_stock_and_user(self):
      if self.is_buy:
        self.stock.quantity = self.stock.quantity - self.quantity
        self.user.funds -= self.quantity * self.stock.price
      else:
        self.stock.quantity = self.stock.quantity + self.quantity
        self.user.funds += self.quantity * self.stock.price








    
    


