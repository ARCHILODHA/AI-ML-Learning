from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2], [1,4], [10,2], [10,4]])

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)
