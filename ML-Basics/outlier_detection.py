import numpy as np

data = np.array([10, 12, 15, 18, 100])

mean = np.mean(data)
std = np.std(data)

z_scores = (data - mean) / std

print(z_scores)
