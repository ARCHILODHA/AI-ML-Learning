import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    output = sigmoid(x)
    return output * (1 - output)


values = np.array([-3, -1, 0, 1, 3])

activation = sigmoid(values)
derivative = sigmoid_derivative(values)

print("Sigmoid output:")
print(activation)

print("\nSigmoid derivative:")
print(derivative)
