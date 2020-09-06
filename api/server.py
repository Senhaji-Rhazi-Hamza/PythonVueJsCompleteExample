from flask import Flask, jsonify, request
from flask_cors import CORS  # This is the magic
from models import Stock, User

import os


app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return "Api is up and running :)", 200

@app.route('/stocks', methods=["GET"])
def get_stocks():
    stocks = [
    {
        'id': stock.id,
        'brand': stock.brand,
        'price': stock.price

    } 
    for stock in  Stock.all()
    ]
    return jsonify(stocks), 200


@app.route('/buy', methods=["POST"])
def buy_stock():
    print("stock bought")
    user = User.get_by_id(request.json.get('user_id'))
    brand = request.json.get('brand').upper()
    quantity = int(request.json.get('quantity'))
    #print(request.json)
    #success= False
    success = user.buy_stock(brand=brand, quantity=quantity)
    
    return jsonify({'bought':success}), 200

@app.route('/sell', methods=["POST"])
def sell_stock():
    print("stock sold")
    return jsonify({'sold':True}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
