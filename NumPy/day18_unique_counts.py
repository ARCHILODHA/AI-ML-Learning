import numpy as np

arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])

unique = np.unique(arr)
values, counts = np.unique(arr, return_counts=True)

print("Unique Values:")
print(unique)

print("\nValue Counts:")
for v, c in zip(values, counts):
    print(v, ":", c)
