import numpy as np

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


values = np.array([-5, -2, -1, 0, 1, 3, 5])

result = leaky_relu(values)

print("Input:")
print(values)

print("\nLeaky ReLU output:")
print(result)
