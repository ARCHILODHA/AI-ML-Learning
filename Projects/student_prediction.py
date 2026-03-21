import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("../Datasets/sample.csv")

X = data[["Age"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

print("Prediction:", model.predict([[22]]))
