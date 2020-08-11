from random import random
from api.models.base import BaseModel, db
from api.models.user_stock_quantity import UserStockQuantity

class Stock(BaseModel):

    __tablename__ = "stocks"

    id = db.Column(db.Unicode(), primary_key=True)
    brand = db.Column(db.Unicode(), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False, default = 30)
    price = db.Column(db.Float, nullable=False, default = 100)

    
    @classmethod
    def get_stock_by_brand(cls, brand):
        return cls.query.filter(cls.brand == brand).one_or_none()


    @classmethod
    def get_stocks_infos_by_user_id(cls, user_id):
        stocks_infos = cls.session.query(Stock, UserStockQuantity)\
        .join(UserStockQuantity, cls.id == UserStockQuantity.stock_id)\
        .filter(UserStockQuantity.user_id == user_id).all()         
        return [
            {
                'brand':stock.brand,
                'user_id': user_id,
                'user_quantity': ust_quantity.quantity,
                'stock_id': stock.id
            } 
            for stock, ust_quantity in stocks_infos
        ]
    
    @classmethod
    def get_stock_infos_by_user_id(cls, brand, user_id):
        stock = Stock.get_stock_by_brand(brand)
        stock_infos, ust_quantity = cls.session.query(Stock, UserStockQuantity)\
        .join(UserStockQuantity, cls.id == UserStockQuantity.stock_id)\
        .filter(UserStockQuantity.user_id == user_id, UserStockQuantity.stock_id == stock.id ).one_or_none()   
        if stock_infos:     
            return {
                    'brand':stock_infos.brand,
                    'user_id': user_id,
                    'user_quantity': ust_quantity.quantity,
                    'stock_id': stock_infos.id
                } 
                

    @classmethod
    def add_stock_quantity(cls, stock_id, quantity):
        stock = cls.get_by_id(stock_id)
        stock.quantity += quantity
        stock.save()

    @classmethod 
    def update_stock_prices(cls):
        for stock in cls.all():
            t = (random() - 0.5) / 4
            stock.price = round(stock.price * (1 + t), 2)
            stock.save()
            

