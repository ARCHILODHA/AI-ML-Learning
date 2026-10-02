import numpy as np

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


values = np.array([-3, -1, 0, 1, 3])

result = elu(values)

print("Input:")
print(values)

print("\nELU output:")
print(result)
