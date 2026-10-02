import numpy as np

def flatten_layer(data):
    data = np.array(data)
    return data.reshape(data.shape[0], -1)


data = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Original shape:")
print(data.shape)

result = flatten_layer(data)

print("\nFlattened data:")
print(result)

print("\nFlattened shape:")
print(result.shape)
