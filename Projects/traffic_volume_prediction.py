import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "hour": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "temperature": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "rain": [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    "traffic": [500, 800, 1200, 1000, 700, 650, 900, 850, 750, 700]
})

X = data[["hour", "temperature", "rain"]]
y = data["traffic"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GradientBoostingRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(error, 2))

new_data = [[17, 30, 0]]

predicted_traffic = model.predict(new_data)

print(
    "Predicted Traffic Volume:",
    round(predicted_traffic[0])
)
