from flask import Flask, jsonify, request
from models import Stock
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
