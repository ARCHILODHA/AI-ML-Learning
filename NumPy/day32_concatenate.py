import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print("Array A:")
print(a)

print("\nArray B:")
print(b)

print("\nConcatenated array:")
print(result)

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("\nVertical concatenation:")
print(np.concatenate((matrix_a, matrix_b), axis=0))

print("\nHorizontal concatenation:")
print(np.concatenate((matrix_a, matrix_b), axis=1))
