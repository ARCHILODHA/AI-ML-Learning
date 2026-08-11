import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Data:")
print(data)

print("\nSum along rows:")
print(np.sum(data, axis=1))

print("\nSum along columns:")
print(np.sum(data, axis=0))

print("\nMean along rows:")
print(np.mean(data, axis=1))

print("\nMean along columns:")
print(np.mean(data, axis=0))
