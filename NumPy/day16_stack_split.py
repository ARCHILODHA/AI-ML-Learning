import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical Stack:")
print(np.vstack((a, b)))

print("\nHorizontal Stack:")
print(np.hstack((a, b)))

arr = np.arange(8)

print("\nSplit:")
print(np.split(arr, 4))
