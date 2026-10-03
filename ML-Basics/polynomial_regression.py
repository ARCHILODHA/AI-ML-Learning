import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([1, 4, 9, 16, 25])

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

model = LinearRegression()

model.fit(X_poly, y)

predictions = model.predict(X_poly)

print("Actual values:")
print(y)

print("\nPredicted values:")
print(predictions)

test_value = np.array([[6]])

test_poly = poly.transform(test_value)

prediction = model.predict(test_poly)

print("\nPrediction for 6:", prediction[0])
