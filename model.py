#importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib  # Import joblib for saving the model

# Load dataset
dataset = pd.read_csv('ml.csv')

# Creating a new column for Price Movement (if not already in the dataset)
# 1 = Price increased, 0 = Price decreased or stayed the same
dataset['PriceMovement'] = np.where(dataset['ClosePrice'] > dataset['OpenPrice'], 1, 0)

# Independent variables (exclude 'PriceMovement' since it's the target for evaluation)
x = dataset[['OpenPrice', 'HighPrice', 'LowPrice', 'Volume', 'MovingAverage10', 'MovingAverage50',
             'RSI', 'MACD', 'Volatility']]

# Dependent variable (Close Price for regression model)
y = dataset['ClosePrice']

# Standardization (feature scaling)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=0)

# Train RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(x_train, y_train)

# Predict the Close Price
y_pred_close_price = rf_regressor.predict(x_test)

# Convert the regression output (Close Price) into a binary classification for Price Movement
# If predicted Close Price > Open Price -> Price Movement = 1 (Increase)
# Else -> Price Movement = 0 (Decrease or No Change)
x_test_original = scaler.inverse_transform(x_test)  # Get the original scale for comparison
predicted_price_movement = np.where(y_pred_close_price > x_test_original[:, 0], 1, 0)  # Column 0 is Open Price

# Actual Price Movement (for comparison)
actual_price_movement = np.where(y_test > x_test_original[:, 0], 1, 0)

# Evaluate the classification accuracy of predicted price movement
accuracy = accuracy_score(actual_price_movement, predicted_price_movement)
conf_matrix = confusion_matrix(actual_price_movement, predicted_price_movement)

# Output accuracy and confusion matrix
print(f"Accuracy of Price Movement Prediction: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(conf_matrix)

# Save the model and scaler
joblib.dump(rf_regressor, 'rf_model.pkl')  # Save the model
joblib.dump(scaler, 'scaler.pkl')  # Save the scaler

# Check if model and scaler are saved successfully
try:
    rf_loaded = joblib.load('rf_model.pkl')  # Load the model to check if saved correctly
    scaler_loaded = joblib.load('scaler.pkl')  # Load the scaler to check if saved correctly
    print("Model and scaler saved successfully.")
except Exception as e:
    print("Error saving the model or scaler:", e)
