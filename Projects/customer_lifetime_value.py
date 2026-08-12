import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Purchases": [2, 4, 5, 8, 10, 12, 15, 20],
    "AvgOrderValue": [500, 600, 700, 800, 850, 900, 950, 1000],
    "LifetimeValue": [1200, 2800, 4000, 7200, 9500, 12000, 15000, 22000]
})

X = data[["Purchases", "AvgOrderValue"]]
y = data["LifetimeValue"]

model = LinearRegression()
model.fit(X, y)

customer = [[10, 850]]

print(
    "Predicted Customer Lifetime Value:",
    round(model.predict(customer)[0], 2)
)
