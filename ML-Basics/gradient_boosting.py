from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = GradientBoostingClassifier()
model.fit(X, y)

print(model.predict([X[0]]))
