import numpy as np
import time

numbers = np.arange(1, 1000001)

# Traditional Python loop
start = time.time()

loop_result = []

for number in numbers:
    loop_result.append(number ** 2)

loop_time = time.time() - start

# NumPy vectorized operation
start = time.time()

numpy_result = numbers ** 2

numpy_time = time.time() - start

print("First 10 Loop Results:")
print(loop_result[:10])

print("\nFirst 10 NumPy Results:")
print(numpy_result[:10])

print("\nLoop Execution Time:")
print(loop_time)

print("\nNumPy Execution Time:")
print(numpy_time)
