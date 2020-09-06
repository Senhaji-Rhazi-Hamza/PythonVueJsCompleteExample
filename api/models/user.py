from api.models.base import BaseModel, db
from api.models.stock import Stock
from api.models.order import Order

class User(BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Unicode(), primary_key=True)
    name = db.Column(db.Unicode(), nullable=False)
    mail = db.Column(db.Unicode(), nullable=False)
    password = db.Column(db.Unicode(), nullable=False)
    funds = db.Column(db.Float, nullable= False, default= 100000)


    def buy_stock(self, quantity, brand):
        stock = Stock.query.filter(Stock.brand == brand).one_or_none()
        if not stock or quantity < 0 or (stock.quantity < quantity or stock.quantity * stock.price > self.funds):
            return False
        else:
            Order.create_buy_order(quantity=quantity, user_id=self.id, stock_id=stock.id)
            return True

    def sell_stock(self, quantity, brand):
        stock = Stock.query.filter(brand == brand).one_or_none()
        if not stock or (stock.quantity > quantity or stock.quantity * stock.price > self.funds):
            return False


        


   