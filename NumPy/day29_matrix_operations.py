import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition:")
print(A + B)

print("\nMatrix Subtraction:")
print(A - B)

print("\nMatrix Multiplication:")
print(A @ B)

print("\nElement-wise Multiplication:")
print(A * B)
