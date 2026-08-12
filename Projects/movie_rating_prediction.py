import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Popularity": [20, 40, 60, 80, 90, 70, 50, 30],
    "Budget": [10, 20, 30, 50, 60, 40, 25, 15],
    "Rating": [5.2, 5.8, 6.5, 7.2, 8.1, 7.0, 6.2, 5.5]
})

X = data[["Popularity", "Budget"]]
y = data["Rating"]

model = LinearRegression()
model.fit(X, y)

movie = [[85, 55]]

prediction = model.predict(movie)

print("Predicted movie rating:", round(prediction[0], 2))
