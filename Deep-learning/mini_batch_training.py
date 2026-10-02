import numpy as np

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
], dtype=float)

y = np.array([
    [2],
    [4],
    [6],
    [8],
    [10],
    [12]
], dtype=float)

weight = np.array([[0.0]])
bias = 0.0

learning_rate = 0.01
epochs = 20
batch_size = 2

for epoch in range(epochs):
    indices = np.random.permutation(len(X))

    X_shuffled = X[indices]
    y_shuffled = y[indices]

    for i in range(0, len(X), batch_size):
        X_batch = X_shuffled[i:i + batch_size]
        y_batch = y_shuffled[i:i + batch_size]

        predictions = X_batch @ weight + bias

        error = predictions - y_batch

        dw = (2 / len(X_batch)) * X_batch.T @ error
        db = (2 / len(X_batch)) * np.sum(error)

        weight -= learning_rate * dw
        bias -= learning_rate * db

print("Learned weight:")
print(weight)

print("\nLearned bias:")
print(bias)

test_input = np.array([[7]])

prediction = test_input @ weight + bias

print("\nPrediction for 7:", prediction[0][0])
