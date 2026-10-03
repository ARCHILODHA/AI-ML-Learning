import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([
    2,
    4,
    6,
    8,
    10
])

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "linear_model.pkl")

print("Model saved successfully.")

loaded_model = joblib.load("linear_model.pkl")

test_data = np.array([
    [6],
    [7],
    [8]
])

predictions = loaded_model.predict(test_data)

print("\nPredictions from loaded model:")
print(predictions)
