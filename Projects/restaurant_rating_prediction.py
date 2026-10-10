import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "food_quality": [8, 7, 9, 6, 10, 8, 7, 9, 6, 10],
    "service": [9, 7, 8, 6, 10, 8, 6, 9, 7, 10],
    "ambience": [8, 6, 9, 7, 10, 8, 7, 9, 6, 9],
    "price_value": [7, 8, 8, 6, 9, 7, 8, 9, 6, 9],
    "rating": [8.2, 7.0, 8.5, 6.3, 9.7, 8.0, 7.0, 9.0, 6.4, 9.6]
})

X = data.drop("rating", axis=1)
y = data["rating"]

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

print("Mean Absolute Error:", round(error, 3))

new_restaurant = [[9, 8, 9, 8]]

predicted_rating = model.predict(new_restaurant)

print(
    "Predicted Restaurant Rating:",
    round(predicted_rating[0], 2)
)
