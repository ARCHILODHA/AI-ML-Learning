import numpy as np

# Polynomial:
# 2x^2 + 3x + 4

coefficients = np.array([2, 3, 4])

# Evaluate polynomial at x = 2
value = np.polyval(coefficients, 2)

# Calculate roots
roots = np.roots(coefficients)

# Differentiate polynomial
derivative = np.polyder(coefficients)

# Integrate polynomial
integral = np.polyint(coefficients)

print("Polynomial Coefficients:")
print(coefficients)

print("\nValue at x = 2:")
print(value)

print("\nRoots:")
print(roots)

print("\nDerivative Coefficients:")
print(derivative)

print("\nIntegral Coefficients:")
print(integral)
