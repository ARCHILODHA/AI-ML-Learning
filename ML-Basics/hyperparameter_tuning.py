from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

params = {'n_estimators': [10, 50]}

model = GridSearchCV(RandomForestClassifier(), params)
model.fit(X, y)

print(model.best_params_)
