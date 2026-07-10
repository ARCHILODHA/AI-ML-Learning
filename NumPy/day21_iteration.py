import numpy as np

arr = np.array([[1, 2], [3, 4]])

print("Elements:")

for x in np.nditer(arr):
    print(x)
