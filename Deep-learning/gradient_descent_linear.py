import numpy as np

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

weight = 0.0
bias = 0.0

learning_rate = 0.01
epochs = 1000

n = len(X)

for epoch in range(epochs):
    predictions = weight * X + bias

    error = predictions - y

    dw = (2 / n) * np.sum(X * error)
    db = (2 / n) * np.sum(error)

    weight -= learning_rate * dw
    bias -= learning_rate * db

print("Learned weight:", weight)
print("Learned bias:", bias)

test_value = 6

prediction = weight * test_value + bias

print("Prediction for", test_value, ":", prediction)
