import numpy as np

arr = np.arange(1, 13)

print("Original:")
print(arr)

matrix = arr.reshape(3, 4)
print("\nReshaped (3x4):")
print(matrix)

print("\nFlatten:")
print(matrix.flatten())

print("\nRavel:")
print(matrix.ravel())
