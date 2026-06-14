from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X = load_iris().data

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
