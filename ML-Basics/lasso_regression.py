import numpy as np
from sklearn.linear_model import Lasso

X = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12],
    [5, 10, 15],
    [6, 12, 18]
])

y = np.array([6, 12, 18, 24, 30, 36])

model = Lasso(alpha=0.01)

model.fit(X, y)

predictions = model.predict(X)

print("Predictions:")
print(predictions)

print("\nCoefficients:")
print(model.coef_)

print("\nIntercept:")
print(model.intercept_)
