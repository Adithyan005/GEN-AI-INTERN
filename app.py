from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and scaler
rf_model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Convert input values to floats
    try:
        input_data = np.array([
            float(data['OpenPrice']),
            float(data['HighPrice']),
            float(data['LowPrice']),
            float(data['Volume']),
            float(data['MovingAverage10']),
            float(data['MovingAverage50']),
            float(data['RSI']),
            float(data['MACD']),
            float(data['Volatility'])
        ]).reshape(1, -1)

        # Scale the input data
        input_scaled = scaler.transform(input_data)

        # Make prediction
        predicted_close_price = rf_model.predict(input_scaled)

        # Determine price movement
        open_price = float(data['OpenPrice'])  # Ensure OpenPrice is a float
        price_movement = 1 if predicted_close_price > open_price else 0

        return jsonify({
            'predicted_close_price': predicted_close_price[0],
            'price_movement': price_movement
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message if any exception occurs

if __name__ == '__main__':
    app.run(debug=True)
