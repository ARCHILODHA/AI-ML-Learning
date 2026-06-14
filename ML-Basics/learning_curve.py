from sklearn.model_selection import learning_curve
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

train_sizes, train_scores, test_scores = learning_curve(
    DecisionTreeClassifier(),
    X,
    y
)

print(train_sizes)
