from api.models.base import BaseModel, db


class Stock(BaseModel):

    __tablename__ = "stocks"

    id = db.Column(db.Unicode(), primary_key=True)
    brand = db.Column(db.Unicode(), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False, default = 30)
    price = db.Column(db.Float, nullable=False, default = 100)

