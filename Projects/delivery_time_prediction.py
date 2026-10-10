import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

data = pd.DataFrame({
    "distance_km": [2, 5, 8, 10, 15, 20, 25, 30, 35, 40],
    "items": [1, 2, 3, 2, 4, 5, 6, 4, 7, 8],
    "traffic_level": [1, 2, 2, 3, 3, 4, 4, 5, 5, 5],
    "delivery_time": [15, 25, 32, 40, 48, 60, 72, 80, 95, 110]
})

X = data[["distance_km", "items", "traffic_level"]]
y = data["delivery_time"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("Mean Absolute Error:", round(mae, 2))
print("Root Mean Squared Error:", round(rmse, 2))

new_order = [[12, 3, 3]]

predicted_time = model.predict(new_order)

print(
    "\nPredicted Delivery Time:",
    round(predicted_time[0], 2),
    "minutes"
)
