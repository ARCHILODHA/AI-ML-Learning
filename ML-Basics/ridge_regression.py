import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

y = np.array([2, 4, 6, 8, 10, 12, 14, 16])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = Ridge(alpha=1.0)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Test values:")
print(y_test)

print("\nPredictions:")
print(predictions)

print("\nModel coefficient:")
print(model.coef_)

print("\nModel intercept:")
print(model.intercept_)
