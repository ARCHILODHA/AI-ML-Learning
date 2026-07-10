import numpy as np

arr = np.array([1, 2, 3, 4])

copy_arr = arr.copy()
view_arr = arr.view()

arr[0] = 100

print("Original:", arr)
print("Copy:", copy_arr)
print("View:", view_arr)
