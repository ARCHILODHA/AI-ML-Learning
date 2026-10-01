import numpy as np

def binary_cross_entropy(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    epsilon = 1e-15

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )

    return loss


y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.2, 0.8, 0.7]

loss = binary_cross_entropy(y_true, y_pred)

print("Binary Cross Entropy Loss:", loss)
