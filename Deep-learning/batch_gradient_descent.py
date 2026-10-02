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

    errors = predictions - y

    dw = (2 / n) * np.sum(X * errors)
    db = (2 / n) * np.sum(errors)

    weight -= learning_rate * dw
    bias -= learning_rate * db

    if (epoch + 1) % 100 == 0:
        loss = np.mean(errors ** 2)
        print(f"Epoch {epoch + 1}, Loss: {loss:.6f}")

print("\nFinal weight:", weight)
print("Final bias:", bias)
