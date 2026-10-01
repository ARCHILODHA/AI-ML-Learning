import numpy as np

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return np.where(x > 0, 1, 0)


values = np.array([-3, -1, 0, 2, 4])

activated = relu(values)
derivative = relu_derivative(values)

print("Input:")
print(values)

print("\nReLU output:")
print(activated)

print("\nReLU derivative:")
print(derivative)
