import numpy as np

arr = np.array([1, np.nan, 3, np.inf])

print("Array:")
print(arr)

print("\nNaN Values:")
print(np.isnan(arr))

print("\nInfinite Values:")
print(np.isinf(arr))

print("\nReplace NaN with 0:")
clean = np.nan_to_num(arr)

print(clean)
