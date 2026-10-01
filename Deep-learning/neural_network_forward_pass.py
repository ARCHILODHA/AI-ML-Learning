import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([
    [0.5, 0.2],
    [0.8, 0.4],
    [0.1, 0.9]
])

weights_input_hidden = np.array([
    [0.4, 0.3, 0.2],
    [0.5, 0.6, 0.1]
])

bias_hidden = np.array([0.1, 0.1, 0.1])

weights_hidden_output = np.array([
    [0.5],
    [0.7],
    [0.2]
])

bias_output = 0.1

hidden_layer = np.dot(X, weights_input_hidden) + bias_hidden
hidden_activation = sigmoid(hidden_layer)

output_layer = np.dot(
    hidden_activation,
    weights_hidden_output
) + bias_output

output = sigmoid(output_layer)

print("Hidden layer output:")
print(hidden_activation)

print("\nFinal network output:")
print(output)
