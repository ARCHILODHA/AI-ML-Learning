import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.array_split(arr, 3)

print("Original array:")
print(arr)

print("\nSplit arrays:")

for i, part in enumerate(parts, start=1):
    print(f"Part {i}:", part)
