import numpy as np

arr = np.array([10, 20, 30, 40, 50])

np.save("numbers.npy", arr)

loaded = np.load("numbers.npy")

print("Saved Array:")
print(arr)

print("\nLoaded Array:")
print(loaded)
