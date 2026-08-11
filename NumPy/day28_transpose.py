import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original matrix:")
print(matrix)

print("\nTransposed matrix:")
print(matrix.T)

print("\nUsing transpose():")
print(np.transpose(matrix))
