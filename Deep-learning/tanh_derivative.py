import numpy as np

def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    output = tanh(x)
    return 1 - output ** 2


values = np.array([-2, -1, 0, 1, 2])

activation = tanh(values)
derivative = tanh_derivative(values)

print("Tanh output:")
print(activation)

print("\nTanh derivative:")
print(derivative)
