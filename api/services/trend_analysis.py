import numpy as np

def analyze_trend(price_data):
    """Analyze price trend using percentage change and moving average."""
    prices = [price[1] for price in price_data]  # Extract price values
    initial_price = prices[0]
    final_price = prices[-1]

    # Fix variable name to ensure consistency
    percent_change = ((final_price - initial_price) / initial_price) * 100

    trend = "Uptrend" if percent_change > 1 else "Downtrend" if percent_change < -1 else "Neutral"
    moving_average = np.mean(prices)

    return {
        'percent_change': round(percent_change, 2),  # Ensure the name matches here
        'trend': trend,
        'moving_average': round(moving_average, 2)
    }
