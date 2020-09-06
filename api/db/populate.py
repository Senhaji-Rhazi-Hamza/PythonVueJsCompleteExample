#import ipdb; ipdb.set_trace()
from api.models import Stock, User


def populate_stocks():
    print("populating stocks")
    Stock.delete_all()
    for stock in STOCKS:
        Stock.get_or_create(**stock)

def populate_users():
    print("populating users")
    User.delete_all()
    for user_args in USERS:
        User.get_or_create(**user_args)

STOCKS = [
    {"uid": "1", "brand": "BMW", "quantity": 1000, "price": 100},
    {"uid": "2", "brand": "Mercedes", "quantity": 1000, "price": 100},
    {"uid": "3", "brand": "Google", "quantity": 10000, "price": 200},
    {"uid": "4", "brand": "Twitter", "quantity": 10000, "price": 200},
]




USERS = [
    {"uid": "Hamza", "mail": "hamza@gmail.com", "name": "hamza", "password":"oviouspassword"}
]

if __name__ == "__main__":
    populate_stocks()
    populate_users()

