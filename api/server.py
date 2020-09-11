from flask import Flask, jsonify, request
from flask_cors import CORS  # This is the magic
from models import Stock, User

import os


DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
}


app = Flask(__name__)
CORS(app, origins= "*")

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
    return jsonify(stocks), 200, DEFAULT_HEADERS


@app.route('/user', methods=["GET"])
def get_user_info():
    user_id = request.args.get('user_id', None)
    user = User.get_by_id(user_id)
    user_infos = {
        "funds" : user.funds,
        "user_stock_infos" : Stock.get_stocks_infos_by_user_id(user_id=user.id),
        "user_id":user_id
    }
    return jsonify(user_infos), 200, DEFAULT_HEADERS

@app.route('/buy', methods=["POST"])
def buy_stock():
    #import ipdb; ipdb.set_trace()
    user = User.get_by_id(request.json.get('user_id'))
    brand = request.json.get('brand')
    quantity = int(request.json.get('quantity'))
    #print(request.json)
    #success= False
    success = user.buy_stock(brand=brand, quantity=quantity)
    
    return jsonify({'success':success}), 200, DEFAULT_HEADERS

@app.route('/sell', methods=["POST"])
def sell_stock():
    user = User.get_by_id(request.json.get('user_id'))
    brand = request.json.get('brand')
    quantity = int(request.json.get('quantity'))
    success = user.sell_stock(brand=brand, quantity=quantity)
    return jsonify({'success':success}), 200, DEFAULT_HEADERS

@app.route('/update_stocks', methods=["POST"])
def update_stocks():
    Stock.update_stock_prices()
    return jsonify({'success':True}), 200, DEFAULT_HEADERS




if __name__ == "__main__":
    app.run(debug=True, threaded=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
