from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1],[2],[3]])

scaler = StandardScaler()
print(scaler.fit_transform(data))
