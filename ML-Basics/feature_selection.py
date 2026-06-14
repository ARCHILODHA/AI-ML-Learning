from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

X, y = load_iris(return_X_y=True)

selector = SelectKBest(score_func=chi2, k=2)
X_new = selector.fit_transform(X, y)

print(X_new.shape)
