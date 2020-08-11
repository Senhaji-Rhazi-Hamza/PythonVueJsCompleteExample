from api.models.base import BaseModel, db
from api.models.stock import Stock
from api.models.order import Order
from api.models.user_stock_quantity import UserStockQuantity

from sqlalchemy import func
class User(BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Unicode(), primary_key=True)
    name = db.Column(db.Unicode(), nullable=False)
    mail = db.Column(db.Unicode(), nullable=False)
    password = db.Column(db.Unicode(), nullable=False)
    funds = db.Column(db.Float, nullable= False, default= 100000)


    def buy_stock(self, quantity, brand):
        stock = Stock.query.filter(Stock.brand == brand).one_or_none()
        if not stock or quantity < 0 or (stock.quantity < quantity or quantity * stock.price > self.funds):
            return False
        else:
            Order.create_buy_order(quantity=quantity, user_id=self.id, stock_id=stock.id)
            self.funds -= stock.price * quantity 
            return True

    def get_stock_quantity(self, stock_id):
        user_stock_quantity = UserStockQuantity.get_or_create(user_id=self.id, stock_id=stock_id)
        return user_stock_quantity.quantity
    

    def sell_stock(self, quantity, brand):
        stock = Stock.query.filter(Stock.brand == brand).one_or_none()
        stock_infos = Stock.get_stock_infos_by_user_id(brand, self.id)
        if not stock_infos or (quantity > stock_infos.get('user_quantity')):
            return False
        else:
            Order.create_sell_order(quantity=quantity, user_id=self.id, stock_id=stock.id)
            self.funds += stock.price * quantity 
            return True
        



        


   