import numpy as np

def categorical_cross_entropy(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = -np.sum(y_true * np.log(y_pred), axis=1)

    return np.mean(loss)


y_true = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

y_pred = np.array([
    [0.8, 0.1, 0.1],
    [0.2, 0.7, 0.1],
    [0.1, 0.2, 0.7]
])

loss = categorical_cross_entropy(y_true, y_pred)

print("Categorical Cross Entropy Loss:", loss)
