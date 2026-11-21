import numpy as np

# Equations:
# 2x + 3y = 8
# 4x + 5y = 14

A = np.array([
    [2, 3],
    [4, 5]
])

B = np.array([8, 14])

# Solve linear equations
solution = np.linalg.solve(A, B)

print("Coefficient Matrix:")
print(A)

print("\nConstants:")
print(B)

print("\nSolution:")
print("x =", solution[0])
print("y =", solution[1])

# Verify solution
print("\nVerification:")
print(np.dot(A, solution))
