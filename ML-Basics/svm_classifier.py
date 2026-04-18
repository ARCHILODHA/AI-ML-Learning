from sklearn import svm
from sklearn.datasets import load_iris

data = load_iris()
model = svm.SVC()
model.fit(data.data, data.target)

print(model.predict([data.data[0]]))
