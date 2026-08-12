import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50, 60, 70, 80],
    "Sales": [25, 32, 40, 48, 55, 63, 70, 78]
})

X = data[["Advertising"]]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Mean Absolute Error:",
      mean_absolute_error(y_test, predictions))

future_advertising = [[90]]
print("Predicted sales:", model.predict(future_advertising))
