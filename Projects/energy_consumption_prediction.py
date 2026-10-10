import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "temperature": [20, 22, 25, 28, 30, 32, 35, 27, 24, 21],
    "occupants": [2, 3, 4, 5, 5, 6, 7, 4, 3, 2],
    "appliances": [3, 4, 5, 6, 7, 8, 9, 5, 4, 3],
    "hours": [5, 6, 7, 8, 9, 10, 11, 7, 6, 5],
    "energy": [120, 150, 190, 240, 280, 330, 390, 210, 170, 130]
})

X = data[[
    "temperature",
    "occupants",
    "appliances",
    "hours"
]]

y = data["energy"]

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

new_house = [[29, 4, 6, 8]]

predicted_energy = model.predict(new_house)

print(
    "Predicted Energy Consumption:",
    round(predicted_energy[0], 2),
    "units"
)
