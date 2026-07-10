import numpy as np

arr = np.array([10, 20, 30, 40, 50])

index = np.searchsorted(arr, 35)

print("Insert Position for 35:", index)

new_arr = np.insert(arr, index, 35)

print("Updated Array:")
print(new_arr)
