import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("time_series_data.csv")

df["month"] = range(len(df))

X = df[["month"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)

print("Next month prediction:", model.predict([[len(df)]])[0])
