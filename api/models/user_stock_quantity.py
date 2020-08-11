from api.models.base import BaseModel, db


class UserStockQuantity(BaseModel):

    __tablename__ = "user_stock_quantities"

    id = db.Column(db.Unicode(), primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    stock_id = db.Column(db.ForeignKey("stocks.id", ondelete="CASCADE"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default = 0)


    @classmethod
    def get_or_create(cls, uid=None, **kwargs):
        user_id, stock_id  = kwargs.get('user_id'), kwargs.get('stock_id')
        user_quantity_stock = cls.query.filter(cls.user_id == user_id, cls.stock_id == stock_id).one_or_none()
        if user_quantity_stock:
          return user_quantity_stock
        return super().get_or_create(uid=uid, **kwargs)
