from flask import Blueprint, request, jsonify
from api.coingecko import fetch_crypto_data
from api.services.trend_analysis import analyze_trend  # Import trend analysis function

crypto_bp = Blueprint('crypto', __name__)

@crypto_bp.route('/crypto', methods=['GET'])
def get_crypto_price():
    """Endpoint to fetch historical cryptocurrency prices."""
    coin = request.args.get('coin', 'bitcoin')  # Default to Bitcoin
    days = request.args.get('days', 7, type=int)  # Default to 7 days

    data = fetch_crypto_data(coin, days)
    if data:
        return jsonify(data)
    return jsonify({'error': 'Invalid request or CoinGecko API issue'}), 400

@crypto_bp.route('/trend', methods=['GET'])
def get_crypto_trend():
    """Endpoint to analyze cryptocurrency price trend."""
    coin = request.args.get('coin', 'bitcoin')  # Default to Bitcoin
    days = request.args.get('days', 7, type=int)  # Default to 7 days

    data = fetch_crypto_data(coin, days)
    if not data or 'prices' not in data:
        return jsonify({'error': 'Invalid request or CoinGecko API issue'}), 400

    trend_data = analyze_trend(data['prices'])
    return jsonify(trend_data)
