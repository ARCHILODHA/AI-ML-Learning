import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "rainfall": [500, 600, 700, 800, 900, 1000, 1100, 750, 850, 950],
    "temperature": [30, 29, 28, 27, 26, 25, 24, 28, 27, 26],
    "fertilizer": [50, 60, 70, 80, 90, 100, 110, 75, 85, 95],
    "yield": [20, 24, 28, 32, 36, 40, 43, 30, 34, 38]
})

X = data[["rainfall", "temperature", "fertilizer"]]
y = data["yield"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(error, 2))

new_conditions = [[850, 27, 85]]

predicted_yield = model.predict(new_conditions)

print(
    "Predicted Crop Yield:",
    round(predicted_yield[0], 2)
)
