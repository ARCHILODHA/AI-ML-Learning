import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../Datasets/housing.csv")

X = df[['area']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

print("Prediction:", model.predict([[1000]]))
