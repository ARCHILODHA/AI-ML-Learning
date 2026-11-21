import numpy as np

matrix = np.array([
    [4, 7],
    [2, 6]
])

# Calculate determinant
det = np.linalg.det(matrix)

# Calculate inverse
inverse = np.linalg.inv(matrix)

print("Original Matrix:")
print(matrix)

print("\nDeterminant:")
print(det)

print("\nInverse Matrix:")
print(inverse)

# Verify inverse
identity = np.dot(matrix, inverse)

print("\nIdentity Matrix:")
print(np.round(identity, 2))
